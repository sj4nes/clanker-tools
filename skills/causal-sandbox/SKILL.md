---
name: causal-sandbox
description: >-
  Build a small, executable, authored-rule state-transition sandbox that an
  agent DRIVES to observe cause and effect — run the rules forward from initial
  conditions to a traced outcome, or search backward from an unwanted outcome
  for the minimal earlier change that avoids it — instead of predicting
  consequences in its head. Use when an agent (or a person) needs to answer
  "if I do X from here, what happens and why", "outcome Z occurred and should
  not have — what caused it", "what is the smallest change that prevents Z", or
  "compare these two policies' downstream effects", for a domain whose
  transition rules can be WRITTEN DOWN AND DEFENDED: planning and scheduling,
  configuration and feature-flag rollout, permission and role systems,
  approval and workflow engines, resource allocation, protocol and retry
  logic, game-like or logistics worlds. Enforces a typed state schema, a rule
  register where every transition declares its guard, read-set, and write-set,
  a confluence check (the causal story is only valid where rule order does not
  change the result), branching-time traces, deterministic replay, a bounded
  world with every bound stated, and a materialized trace + causal graph handed
  to the agent rather than raw state. A META skill: orchestrates
  `agent-automation` (how the agent calls the sandbox as a pure what-if tool),
  `temporal-data-modeling` (the branching-time trace and the gluing / confluence
  check), `tla-checker` and `lean` (formal cores), and `simulation` (the
  boundary: when rules cannot be authored, use a surrogate instead). NOT for
  domains where you have only input–output behavior and no defensible rules,
  NOT a reachability checker for "can the system ever reach a bad state", and
  NOT a licence to call a traced run proof about the real system.
version: 0.1.0
author: Simon Janes
tags: [causal-sandbox, agent-tooling, state-transition, rule-engine, causality, counterfactual, confluence, what-if, branching-time, simulation]
---

# Causal Sandbox

You are a causal-sandbox engineer. Your job is not "write a simulator" — it is
to **give an agent a small executable world it can run, so it observes cause and
effect from a trace instead of predicting consequences from priors**. The
deliverable is a package: a state schema, a rule register in which every
transition declares what it reads and what it writes, a confluence verdict, an
engine that produces a deterministic branching trace and a causal graph, and a
driver contract by which the agent poses scenarios and navigates the result —
forward from causes, backward from effects.

**Experiment instead of predict.** If the transition rules can be written down,
the agent must *run* them. A consequence the agent reasoned out with no run
behind it is a guess, and this skill exists to replace the guess with a traced,
replayable, inspectable run.

Keep five layers independently inspectable:

1. **Target domain** — the real or proposed system whose dynamics are being encoded.
2. **State schema** — a typed relational store: entity types, relations, the fields that vary, and the resolution each is visible at.
3. **Rule register** — guarded transitions. Each rule declares a **guard** (the precondition predicate), typed **parameters**, a **read-set** (the state it inspects), a **write-set** (the state it changes), whether it is **nondeterministic**, a **justification**, and a **source**.
4. **Engine run** — rules applied to an initial state, producing a **trace** (a tree of states, one branch per intervention or nondeterministic choice) and a **causal graph** (event → event edges, derived from read/write overlap).
5. **Driver contract** — how the agent submits a scenario, reads the materialized trace and causal graph, walks forward and backward, and diffs two branches.

`authored rules ≠ a run ≠ proof about the real system`. A rule set that looks
right is not a run; a single traced run shows what happened *under these rules
in this scenario*, not what the real system must do.

## The failure mode this skill exists to prevent

An agent asked "what happens if I revoke this role while a job holds a lease on
it?" will, by default, **narrate a plausible answer**. It may be right. It has no
way to know it is right, and neither do you. The narration is not replayable, not
diffable, and carries no causal chain — so when it is wrong, the error is silent
and propagates into the next step.

CityPlanner (Zhang et al., *CityPlanner: A Sandbox Agent for Executable Urban
Planning*, 2026) is the empirical case: giving a frozen model an executable
sandbox with an evaluator raised plan feasibility from 15–28% to 95–100% across
three planning tasks, with no parameter changes — the model went from *asserting*
plans were valid to *checking* them. This skill takes the next step: not just an
evaluator on the end state, but the **causal chain** that produced it, navigable
in both directions.

## The two semantics of a query

| | **Forward** (what does this cause) | **Backward** (what caused this / what prevents this) |
|---|---|---|
| Input | initial state + rules + an intervention | initial state + rules + a target predicate that became true/false and should not have |
| Output | the trace, plus a causal graph: for each event, which earlier events fed its read-set | the minimal set of initial-fact or intervention changes that make the target event not fire — bounded abduction over the rule guards on the path to it |
| Agent navigation | "what did this event enable" — walk causal-graph edges outward | "why did this happen" — walk edges backward to the root causes; then "what is the smallest fix" |
| Failure if skipped | the agent asserts a consequence with no chain | the agent blames the most recent visible event (a recency heuristic), not the actual cause |

Backward queries are **not** "delete the bad event." Deleting an event that a
guard later depends on produces an invalid or incoherent trace. Minimal
intervention means the *fewest changed initial facts or interventions* such that
the target event's guard is never satisfied on any branch, and the trace stays
valid. See [`references/forward-and-backward.md`](references/forward-and-backward.md).

## Confluence: the correctness gate for every causal claim

A causal graph read off a trace is only meaningful where **rule order does not
change the result**. If two enabled rules can fire in either order and reach
*different* states — a genuine conflict, not mere interleaving — then "A caused
B" on that slice is an artifact of the scheduler, and the agent must not read
cause and effect off it.

This is one property under three names, and the skill uses the convergence
deliberately:

| Field | Name | Statement |
|---|---|---|
| Term rewriting | **confluence** / Church–Rosser | different reduction orders reach a common form |
| Wolfram Physics | **causal invariance** | different update orders yield the same causal graph |
| `temporal-data-modeling` | **the gluing check** | overlapping intervals agree; the result does not depend on gluing order |

Procedure, per scenario slice:

1. **Find conflicting rule pairs.** Rules `r1`, `r2` conflict if both can be
   enabled in some reachable state and `writeset(r1) ∩ (writeset(r2) ∪
   readset(r2)) ≠ ∅` (or symmetrically), *and* firing them in the two orders
   reaches different states.
2. **Resolve each conflict** one of three ways: make the rules **commute**
   (rewrite so order does not matter), add an explicit **arbitration** rule
   (priority, a tie-break predicate, a queue), or **accept non-confluence** on
   that slice.
3. **On an accepted non-confluent slice, report the branch set, not a single
   causal graph.** The agent gets "under order ⟨r1, r2⟩: …; under ⟨r2, r1⟩: …"
   and must not be handed a single "A caused B".

Full treatment, including why interleaving that reconverges is fine:
[`references/rules-and-causality.md`](references/rules-and-causality.md).

## Principles

- **Experiment, not predict.** If the rules are authorable, run them. A predicted
  consequence with no trace is a guess; replace it. The agent's job is to pose
  the scenario and read the trace, not to compute the outcome.
- **No cause/effect question, no sandbox.** Refuse or escalate until there is: a
  specific forward or backward question, an observable predicate to read off the
  trace, the initial state it runs from, and the intervention(s) to compare.
  "Model the permission system" is not a task; "does revoking role R from user U
  while job J holds a lease on R leave J able to write after the lease renews,
  starting from config C" is.
- **The rules are an authored claim.** Every rule carries a justification and a
  source. They are written by a person who can defend them — not learned, not
  inferred from a few traces, not vibes. If you can only observe input→output
  behavior and cannot write the transition down and defend it, this is the wrong
  tool: use [`simulation`](../simulation/SKILL.md) to build a surrogate.
- **Every transition declares its read-set and write-set, and the engine enforces
  it.** No rule may inspect state it did not declare reading or mutate state it
  did not declare writing. This is not documentation — it is the mechanism that
  makes the causal graph cheap and trustworthy: event B causally depends on
  event A iff A precedes B on a path and `writeset(A) ∩ readset(B) ≠ ∅`. An
  undeclared read or write means a causal graph you cannot trust.
- **Confluence is checked before any causal claim.** Run the confluence pass.
  Report the verdict per slice. Never hand the agent a single causal graph for a
  non-confluent slice.
- **The trace is a tree, not a line.** Comparing interventions, and any
  nondeterministic rule, branches the trace. Model it as branching time and
  carry, on each branch, the intervention or choice that created it. The
  branching-time representation and its gluing check are
  [`temporal-data-modeling`](../temporal-data-modeling/SKILL.md)'s job — use it,
  do not re-derive it.
- **Deterministic replay.** Same initial state + same rules + same scheduler seed
  → the same trace, exactly. The trace is an artifact you can diff, store, and
  re-run. Non-reproducible traces are not evidence.
- **The world is bounded and every bound is a claim.** Finite entities, finite
  steps, finite value domains. State each bound. A consequence that appears only
  past the step budget is **unobserved**, not absent — say so, exactly as
  [`tla-checker`](../tla-checker/SKILL.md) does for its state bound.
- **Hand the agent the materialized trace and causal graph, not raw state.** A
  model will not reconstruct the causal chain from a pile of state dumps in
  context — materialize it (this is
  [`temporal-data-modeling`](../temporal-data-modeling/SKILL.md)'s
  "when a language model is the downstream reader" note applied directly). Give
  it the event list, the causal edges, the per-branch intervention, and a query
  interface — forward deps, backward deps, branch diff.
- **The sandbox is pure what-if.** It reads the real system's state to seed
  initial conditions; it changes nothing. Any action that alters a real system
  of record goes through [`agent-automation`](../agent-automation/SKILL.md)'s
  typed-action → policy → approval → verify path. The sandbox informs that
  decision; it is not part of its execution.
- **Verify the engine before trusting a trace.** Degenerate cases (no enabled
  rule → state frozen; empty write-set → state unchanged; a rule then its inverse
  → original state); read/write-set enforcement fires on a violation; replay is
  byte-identical; the confluence checker flags a known conflicting pair and
  passes a known-commuting pair.
- **Calibrated language.** "Under the authored rules", "within the step bound",
  "for the modeled entities", "confluent on this slice — the causal claim holds",
  "non-confluent slice — branch set reported", "minimal intervention within a
  2-change budget". Never "the sandbox proves X causes Y" — it shows that under
  these rules, in this run, A's write fed B's read.

## Workflow

1. **Frame the cause/effect question.** Restate: forward or backward; the
   observable predicate and how it is read off a state; the initial state; the
   interventions to compare; the bounds (entities, steps, value domains); what a
   wrong answer would cost. Skeleton in
   [`templates/sandbox-charter.md`](templates/sandbox-charter.md).
2. **Define the state schema.** Entity types, relations, varying fields. Classify
   each varying field **persistent** or **cumulative** and declare its resolution
   — delegate that discipline to
   [`temporal-data-modeling`](../temporal-data-modeling/SKILL.md); do not restate
   it here.
3. **Write the rule register.** One row per transition: name, guard, typed
   parameters, read-set, write-set, nondeterministic?, justification, source.
   Skeleton in [`templates/rule-register.md`](templates/rule-register.md); the
   formalism in
   [`references/rules-and-causality.md`](references/rules-and-causality.md).
4. **Run the confluence pass.** Enumerate conflicting rule pairs; for each,
   commute / arbitrate / accept-non-confluent. Record the verdict. A non-confluent
   slice with a pending causal question is a blocking issue — resolve it or
   switch the deliverable to a branch set.
5. **Build the engine** (or configure an existing rule engine). It must: enforce
   read/write-set declarations, apply rules deterministically under a seed, emit
   a branching trace and a causal graph, and support replay. Keep engine / rules
   / scenario / analysis in separate files.
6. **Verify the engine.** The degenerate cases, read/write enforcement, replay
   determinism, and the confluence-checker self-test (Principles). Do this before
   any scenario run.
7. **Run the scenario.** Forward: emit the trace + causal graph for each
   intervention branch. Backward: bounded minimal-intervention search from the
   target event — see
   [`references/forward-and-backward.md`](references/forward-and-backward.md).
8. **Materialize for the agent.** The event list, causal edges, per-branch
   intervention, and the navigation contract (forward deps, backward deps, branch
   diff). Not raw state.
   [`references/driving-the-sandbox.md`](references/driving-the-sandbox.md).
9. **Report with limits.** The rules and their sources; every bound; the
   confluence verdict per slice; the trace and causal graph; the interventions
   compared and the causal path between them; explicit non-claims — above all,
   never that the trace is proof about the real system, and never a causal claim
   on a non-confluent slice.

## Method selection

| Situation | Primary move | What it must produce |
|---|---|---|
| "Will action X break invariant Y, starting from config C?" | Forward run from C with X as the intervention | The trace; Y read off each state; if Y breaks, the causal path from X to the break |
| "Outcome Z happened and should not have — why?" | Backward causal-dependency walk from the Z event | The chain of events whose write-sets fed the guard of the Z event, back to root causes in the initial state |
| "What is the smallest change that prevents Z?" | Bounded minimal-intervention (abduction) search | The fewest initial-fact / intervention changes that keep the Z-event guard unsatisfied on every branch, with the trace still valid; and a note on why a naive "remove the last event" is invalid or not minimal |
| "Compare policy A vs policy B downstream" | Two branches from a shared root | The causal-graph diff: which events exist under one and not the other, and the first state where the observable diverges |
| "These rules interact unpredictably" | Confluence pass first | The conflicting rule pairs; for each, a commute rewrite, an arbitration rule, or a non-confluent verdict with the branch set |
| "Can the system *ever* reach a bad state, under any interleaving?" | Not this skill | Use [`tla-checker`](../tla-checker/SKILL.md) — exhaustive bounded reachability, not a scenario trace |
| "Prove invariant Y holds in every reachable state" | Not this skill | Use [`lean`](../lean/SKILL.md) — a machine-checked proof, not a checked trace |
| "I have input–output data but cannot write the rules down" | Not this skill | Use [`simulation`](../simulation/SKILL.md) — a validated surrogate model |
| The agent must then *act* on a real system based on the trace | Hand off | [`agent-automation`](../agent-automation/SKILL.md) — the sandbox result is an input to the typed-action → policy → approval path, not part of it |

## Guardrails — refuse or escalate when

- There is no specific forward or backward question, no observable predicate, or
  no initial state.
- The transition rules cannot be authored and defended — only observed
  input–output behavior exists. Route to [`simulation`](../simulation/SKILL.md).
- A causal claim is being made on a slice the confluence pass flagged
  non-confluent, without reporting the branch set.
- A rule in the register reads or writes state it did not declare — the causal
  graph derived from it is not trustworthy until the declaration is fixed.
- A consequence that appears only past the step or entity bound is being reported
  as "will not happen" rather than "not observed within the bound".
- A single traced run is being presented as proof about the real system rather
  than as behavior under the authored rules in one scenario.
- The sandbox is wired to cause real side effects. It must be pure what-if; state
  changes go through [`agent-automation`](../agent-automation/SKILL.md).
- The agent is reasoning out a consequence it could have obtained by running the
  rules. That is the failure this skill exists to prevent.
- A backward query is being "answered" by deleting the unwanted event instead of
  finding the minimal initial-condition change.

## Templates

- [`templates/sandbox-charter.md`](templates/sandbox-charter.md) — the
  cause/effect question, observable, initial state, interventions, forward or
  backward, bounds, cost of a wrong answer.
- [`templates/rule-register.md`](templates/rule-register.md) — one row per rule:
  name, guard, parameters, read-set, write-set, nondeterministic?, justification,
  source.
- [`templates/trace-report.md`](templates/trace-report.md) — the run report:
  rules and sources, bounds, per-slice confluence verdict, the trace and causal
  graph, interventions compared, the causal path, non-claims.

## References

- [`references/rules-and-causality.md`](references/rules-and-causality.md) — the
  rule formalism (guard / parameters / read-set / write-set / nondeterminism);
  how the causal graph is derived from read/write overlap along a path; the
  confluence = causal-invariance = gluing-check convergence, conflicting-pair
  detection, and the commute / arbitrate / branch-set resolutions; why
  reconverging interleaving is not a conflict.
- [`references/forward-and-backward.md`](references/forward-and-backward.md) —
  forward trace and causal-graph construction; the backward causal-dependency
  walk; the bounded minimal-intervention (abduction) search — its budget, what
  "minimal" means, why "delete the bad event" fails, and how it reports "no fix
  within budget".
- [`references/driving-the-sandbox.md`](references/driving-the-sandbox.md) — the
  agent interface: scenario submission, the materialized trace + causal-graph
  format, the navigation queries (forward deps, backward deps, branch diff), and
  using the sandbox as a pure what-if tool inside an
  [`agent-automation`](../agent-automation/SKILL.md) loop.

[`verification/`](verification/) (`sh verification/run.sh`) builds a small
authored-rule sandbox — an inventory world with `consume`, `restock`, and a
guarded `reorder` rule, plus a role system with conflicting `grant` / `revoke` —
and asserts each prescribed mechanism: a forward run shows `reorder` fired
*because* a prior `consume` dropped stock below threshold (the causal edge is
present) (`bc` + `py`); a backward query on "stock hit zero on day 5" returns
"raise the reorder threshold" as a 1-change fix and rejects "skip the day-4
consume" as invalid (`py`); the confluence checker flags `grant`/`revoke` on the
same role as conflicting and passes two independent `grant`s as commuting
(`py`); a causal claim read off the non-confluent `grant`/`revoke` slice flips
when the scheduler order flips (`py`); and the degenerate cases hold — no enabled
rule freezes the state, an empty-write rule leaves it unchanged, and replay under
a fixed seed is byte-identical (`py`).

## Completion report

Report: the cause/effect question as you understood it (forward or backward, the
observable, the initial state); the state schema; the rule register with every
rule's read-set and write-set and its source; every bound and what it excludes;
the confluence verdict per scenario slice and how each conflict was resolved; the
trace and causal graph, materialized; the interventions compared and the causal
path between them; the minimal intervention found (or "no fix within the N-change
budget"); and explicit non-claims — above all, never that a traced run is proof
about the real system, and never a causal claim on a non-confluent slice.
