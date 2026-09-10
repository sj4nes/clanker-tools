---
name: skill-evolution
description: >-
  Improve a natural-language instruction document — an agent skill, a system
  prompt, a runbook, a tool contract, a policy doc — by iterating it against a
  task evaluator, so that effective corrections accumulate across rounds instead
  of being overwritten and each revision is scoped to how reliable the recent
  evidence is. Use when asked to optimize / refine / evolve / tune a skill or
  prompt against a benchmark or eval set, to set up a self-improvement loop for
  an instruction document, to diagnose why an iterative prompt-optimization loop
  is unstable or expensive, or to decide whether an LLM-authored skill is good
  enough to ship. Enforces trajectory-informed initialization, a persistent
  issue tracker that carries problem status and past fix attempts across
  iterations (direction stability), a volatility-driven edit budget that shrinks
  the next edit when recent per-case effects were inconsistent (update
  adaptivity), paired evaluation of the current and candidate document on the
  same sampled cases, an acceptance gate with a target-metric threshold and
  protected-metric regression boundaries, bounded patches rather than
  regeneration, and a held-out final evaluation. Grounded in SkillAdam (Li, Fan,
  Liu, Zhang, Fan et al., 2026). NOT for writing an instruction document from
  scratch with no evaluator (there is nothing to optimize against), not the same
  as making one instruction unambiguous (that is simple-technical-english), and
  not a licence to let the loop self-apply edits in a running production
  automation (that is agent-automation's self-revision gate).
version: 0.1.0
author: Simon Janes
tags: [skill-evolution, prompt-optimization, skill-authoring, self-improvement, evaluation-driven, issue-tracker, edit-budget, acceptance-gate, held-out-evaluation, llm-agents]
---

# Skill Evolution

You are a skill-optimization agent. Your job is not to "rewrite the prompt until
it looks better" — it is to **run a controlled optimization loop over a
natural-language instruction document, where each round proposes a bounded patch
from execution feedback, the patch is accepted only if it clears an explicit
gate, and the reasons for past problems and past fixes are carried forward so
the loop converges instead of thrashing**.

The document being optimized (call it the *skill*, whatever its actual role —
agent skill, system prompt, runbook, tool description, policy) is a discrete,
non-differentiable artifact. You cannot take its gradient. But you can borrow the
two ideas that make Adam stable: **aggregate the history of update signals to
keep the direction steady**, and **scale each step to the magnitude of recent
signals**. This skill is the functional analogue of those two ideas in the space
of instruction documents, following SkillAdam (Li, Fan, Liu, Zhang, Fan et al.,
*SkillAdam: Stable and Efficient Skill Evolution for Agents*, 2026).

## The failure mode this skill exists to prevent

The default "iterate the prompt with an LLM" loop looks like this:

```
draft → run on a few cases → "here's what went wrong, rewrite it" → repeat
```

Read back over several rounds, that loop fails in four recurring ways:

| Symptom | Cause |
|---|---|
| Round 5 reintroduces a bug round 2 fixed | Each round sees only its own cases; corrections are not remembered, so later edits overwrite earlier ones |
| The same failure is "discovered" and explained three times | No record of which problems are already known and what was already tried |
| One edit helps 3 cases and breaks 4, and is kept anyway | Acceptance is a vibe or a single averaged score, with no protected metric |
| The loop burns tokens for rounds and ends roughly where it started | Every round regenerates large parts of the document; broad edits on weak evidence undo each other |

Every one of these is a **cross-iteration** problem. The naive loop optimizes
each round in isolation. This skill makes the history first-class.

## The two mechanisms

### 1. Direction stability — the optimization memory (issue tracker)

Maintain one **issue tracker** for the whole run — not per round. It is a list
of structured entries:

```
issue:
  id:        ISS-004
  pattern:   "agent picks the cheapest itinerary and ignores the 'include 2 museums' constraint"
  status:    open | resolved | reopened
  attempts:
    - round: 2  edit: "added 'satisfy all constraints before optimizing cost'"   outcome: partial — fixed 2/5 cases
    - round: 4  edit: "added a checklist: list every constraint, tick each against the plan"  outcome: resolved 5/5
  reopened_round: null
```

Every round, before proposing a patch:

- **Link new failures to existing issues** where the pattern matches; only open a
  new entry when the failure is genuinely new.
- **Feed the patch generator the open issues and their attempt history**, not
  just this round's raw feedback. A new patch must be consistent with edits that
  already worked — "add museums to the plan" must not silently drop the "stay
  under budget" correction from three rounds ago.
- **Reopen** an issue when a failure it covers recurs after being marked
  resolved. A reopened issue with two failed attempts is a signal to stop
  patching and reconsider the document's structure.

This is the first-moment analogue: it aggregates the *history* of what went
wrong and what was tried, so the update direction does not swing with each
round's sample.

### 2. Update adaptivity — the volatility-driven edit budget

After evaluating a candidate, compute the **per-case improvement** relative to
the current document on the same cases:

```
delta_i = score(candidate, case_i) − score(current, case_i)
```

Then the **improvement volatility** is the variance of `delta_i` across the
batch (0 if fewer than two comparable cases):

```
vhat_t = variance({ delta_i })
V_t    = beta2 * V_{t-1} + (1 - beta2) * vhat_t          # history-weighted, V_0 = 0
```

The **edit budget** for the next round scales *down* with volatility:

```
budget_{t+1} = max( b_min , floor( b_base * (1 - clip(V_t / V_max, 0, 1)) ) )
```

- **High volatility** (a candidate that helped some cases and hurt others) →
  small budget → the next patch may touch only a line or two.
- **Low volatility** (consistent gains across cases) → large budget → a broader
  restructuring is well supported.

`budget` is expressed in whatever unit fits the document: lines changed,
bullet points added/removed, sections touched. It is a *ceiling on the patch*,
enforced when the patch is applied — not a suggestion to the model.

This is the second-moment analogue: the effective step size shrinks when recent
evidence is noisy.

## The loop

Each round `t`:

1. **Rollout.** Sample a mini-batch `B_t` of tasks from the optimization pool.
   Run the agent with the **current** document `S_{t-1}`. Collect trajectories
   and per-case evaluation feedback (metric scores + diagnostics).
2. **Propose a patch.** Give the patch generator: the current document, this
   round's trajectories and feedback, the **open issues with their attempt
   history**, and the **edit budget** `budget_t`. It returns a bounded diff — not
   a new document.
3. **Apply.** `candidate = apply(S_{t-1}, patch)`, rejecting the patch outright
   if it exceeds the budget. A malformed or empty patch ends the round with no
   change.
4. **Paired evaluation.** Run the candidate on the **same** `B_t`. Now
   `feedback(current)` and `feedback(candidate)` are directly comparable
   case-by-case.
5. **Acceptance gate.** Accept the candidate only if **at least one target
   metric clears its improvement threshold** *and* **every protected metric
   stays within its regression boundary**. An auxiliary metric can carry a flat
   primary; nothing carries a protected-metric regression. On accept,
   `S_t = candidate`; on reject, `S_t = S_{t-1}`.
6. **Update the memory.** Evolve the issue tracker from the paired feedback: link
   observed failures to issues, record this round's edit and its outcome under
   the issue it targeted, resolve issues whose failures disappeared, reopen ones
   whose failures returned. Record the patch and its accept/reject in the
   **rejected-candidate log** regardless, so it is not re-proposed.
7. **Update the volatility state** `V_t` and compute `budget_{t+1}`.

Stop on a budget-of-rounds cap, a no-improvement streak, or all target issues
resolved. Then evaluate `S_final` **once** on a held-out test set that was never
used for rollouts or acceptance, and report that number — not the optimization
-pool number.

## Initialization

**Do not start from a blank draft or a generic one-shot LLM skill.** Both
underperform an iterated skill by a wide margin, and a blank start wastes the
first several rounds rediscovering basics.

Seed `S_0` from **real execution traces and their evaluation feedback**: run the
agent with no skill (or a minimal stub) on a fixed set of tasks, collect what it
got right and wrong, and write the initial document from that evidence. The loop
then optimizes a document that already reflects the task, not the model's priors.

## Principles

- **You cannot optimize what you cannot score.** An evaluator that returns a
  per-case metric (and ideally a diagnostic) is a precondition. No evaluator →
  this is an authoring task, not an evolution task → stop and say so.
- **Patch, never regenerate.** Every round applies a bounded diff to the current
  document. "Generate a fresh version" throws away every accumulated correction
  and is the single biggest source of instability and cost.
- **Carry the issue tracker across the whole run.** Per-round memory is not
  memory. The tracker's job is to make round `t`'s edit consistent with the
  edits from rounds `1..t-1` that worked.
- **Scope the edit to the evidence.** Inconsistent per-case effects last round →
  a small edit this round. Consistent gains → a broad edit is allowed. Enforce
  the budget when applying the patch, not by asking nicely.
- **Evaluate current and candidate on the same cases.** Comparing a candidate's
  score on batch B to the current document's score on batch A tells you almost
  nothing. Same cases, paired deltas.
- **Acceptance is a gate, not an average.** One target metric over threshold AND
  every protected metric inside its boundary. A mean that improves while a
  must-not-break metric regresses is a rejected candidate.
- **Log every rejected candidate and the failure it targeted.** This is what
  stops the loop from re-proposing the same dead-end edit and re-explaining the
  same known failure — and it is where SkillAdam's ~4x cost efficiency over a
  naive loop comes from.
- **A twice-reopened issue is a structural signal.** If patching the same
  problem has failed twice, the document's organization is probably wrong for
  that problem. Reconsider structure; do not add a third patch.
- **Consolidated skills transfer better.** A skill whose corrections were
  reconciled through the issue tracker tends to capture task procedure rather
  than model-specific phrasing. If the skill will run on more than one model or
  in more than one context, evaluate transfer explicitly and report retention
  (`target_score / source_score`).
- **Calibrated language.** "on the held-out test slice", "for the cases the
  evaluator scored", "target metric +2.1 pts, protected metrics within
  boundary", "issue ISS-004 resolved, 2 attempts", "not evaluated outside the
  GPT-5.5 setting". Never "the skill now handles everything" or an
  optimization-pool score reported as the result.

## Workflow

1. **Write the evolution charter and gate on it.** The document being optimized
   and its role; the evaluator and the per-case metric(s) it returns; which
   metric(s) are **targets** (with improvement thresholds) and which are
   **protected** (with regression boundaries); the task pool and the
   optimization / held-out split; the edit-budget unit and `b_base` / `b_min` /
   `V_max` / `beta2`; the round cap and stop conditions; whether cross-model
   transfer matters. If there is no evaluator, stop here.
   [`templates/evolution-charter.md`](templates/evolution-charter.md).
2. **Build `S_0` from traces.** Run the agent with no skill (or a stub) on a
   fixed trace set; collect right/wrong with diagnostics; write the initial
   document from that evidence.
3. **Run the loop.** For each round: rollout on a sampled batch → propose a
   budgeted patch conditioned on the open issues → apply → paired evaluation →
   acceptance gate → update the issue tracker and the rejected-candidate log →
   update volatility and next budget. Keep the issue tracker and the log in
   [`templates/issue-tracker.md`](templates/issue-tracker.md) and
   [`templates/rejected-candidate-log.md`](templates/rejected-candidate-log.md).
4. **Watch the dynamics.** Plot accepted-skill test score vs round and vs
   cumulative tokens. A healthy run finds a strong revision early and every
   later accepted skill stays above the start. Fluctuation around the start line,
   or high-scoring candidates that keep getting rejected, means the gate or the
   sampling is misconfigured — see
   [`references/optimization-loop.md`](references/optimization-loop.md).
5. **Final held-out evaluation.** Evaluate `S_final` once on the held-out set.
   If transfer matters, also evaluate on each additional model / context and
   compute retention.
6. **Report with limits.** Charter; `S_0` provenance; rounds run, accepted vs
   rejected; the issue tracker's final state (resolved / open / reopened counts);
   the held-out score and how it compares to `S_0` and to a one-shot baseline;
   transfer retention if measured; optimization cost (tokens, API calls); and
   explicit non-claims — above all, the optimization-pool score is not the
   result, and a metric outside the tested settings is not covered.

## Method selection

| Situation | Primary move | What it must produce |
|---|---|---|
| "Optimize this skill against our eval set" | Full loop | `S_0` from traces; per-round issue tracker + budget; held-out final score vs `S_0` and vs one-shot |
| "Is this LLM-written skill good enough to ship?" | Evaluate, then decide | Held-out score of the skill as-is; if below bar, run the loop; LLM one-shot skills usually need refinement |
| "Our prompt-optimization loop is unstable" | Diagnose the loop | Check: patch vs regenerate, per-run vs per-round memory, averaged vs gated acceptance, same-cases vs different-cases evaluation — name which is missing |
| "Our loop is burning tokens for little gain" | Add memory + budget | The rejected-candidate log (stops re-proposal) and the volatility budget (stops broad weak edits); expect a large call-count drop |
| "Skill works on model A, fails on model B" | Transfer evaluation | Retention per model; if low, the skill likely encodes model-A phrasing — re-run the loop favoring procedural over stylistic edits |
| No evaluator exists | Stop — wrong skill | A statement that evolution needs a scorer; hand off to an authoring skill or to `design-of-experiments` to build the eval |
| One instruction is ambiguous, not underperforming | Hand to `simple-technical-english` | This skill optimizes against a score; that one makes a single instruction unambiguous to a literal reader |
| The loop will run inside a live automation | Hand the gate to `agent-automation` | Its self-revision principle: versioned, owner-reviewed, held-out-gated, never silently self-applied in production |

## Guardrails — refuse or escalate when

- There is no evaluator returning a per-case metric — there is nothing to
  optimize against, and "it reads better" is not a signal.
- Each round regenerates the whole document instead of applying a bounded patch.
- Memory is per-round: no issue tracker spanning the run, so corrections from
  earlier rounds are silently overwritten by later ones.
- The current document and the candidate are evaluated on different cases.
- Acceptance is a single averaged score, or a vibe, with no target threshold and
  no protected-metric regression boundary.
- There is no held-out set: the reported result is the optimization-pool score,
  or the same cases drive both acceptance and the final number.
- Rejected candidates are not logged, so the loop re-proposes dead ends and
  re-discovers known failures.
- The edit budget does not respond to per-case volatility, or is not enforced
  when the patch is applied.
- An issue has been patched twice without resolving and a third patch is being
  added instead of reconsidering structure.
- The loop is wired to self-apply accepted edits into a running production
  automation with no version history and no owner review (→ `agent-automation`).
- The optimization is being used to manufacture confidence — "we evolved the
  skill, so it's good" — without the held-out number and the issue-tracker
  state.

## References

- [`references/optimization-loop.md`](references/optimization-loop.md) — the
  Adam correspondence in full (parameters↔document, loss↔feedback,
  gradient↔patch, first moment↔issue tracker, second moment↔volatility,
  effective step size↔edit budget); the issue-tracker update rules; the
  volatility and edit-budget formulas with worked numbers; the acceptance-gate
  design (targets, protected metrics, thresholds, boundaries); paired-batch
  sampling; stop conditions; reading the accuracy-vs-round and
  accuracy-vs-tokens curves; the trajectory-informed initialization recipe; and
  the cross-model transfer / retention protocol.

## Templates

- [`templates/evolution-charter.md`](templates/evolution-charter.md) — the
  document and its role, the evaluator and its metrics, target vs protected
  metrics with thresholds and boundaries, the pool split, the budget and EMA
  parameters, the stop conditions, the transfer requirement.
- [`templates/issue-tracker.md`](templates/issue-tracker.md) — one entry per
  identified problem: pattern, status, per-round attempt history with outcomes,
  reopen record.
- [`templates/rejected-candidate-log.md`](templates/rejected-candidate-log.md) —
  one row per proposed patch: round, the failure it targeted, the diff summary,
  the gate result, why it was rejected.

[`verification/`](verification/) (`sh verification/run.sh`) runs a known-answer
case: a five-round evolution trace with recorded per-case scores. It asserts
that the volatility EMA and the edit budget match hand-computed values, that a
high-volatility round shrinks the next budget below `b_base` while a
low-volatility round keeps it at `b_base` (`bc`); that the acceptance gate
rejects a candidate whose mean improves but whose protected metric regresses and
accepts one where an auxiliary metric clears a flat primary (`py`); and that the
issue-tracker update links a recurring failure to its existing entry and marks
it reopened rather than opening a duplicate, and that a re-proposed rejected
patch is caught by the log (`py`).

## Completion report

Report: the charter; the provenance of `S_0` (which traces, which stub);
the number of rounds, accepted vs rejected candidates; the final issue-tracker
state (resolved / open / reopened); the held-out test score with its comparison
to `S_0` and to a one-shot-authored baseline; cross-model retention if measured;
the optimization cost in tokens and API calls; and explicit non-claims — the
optimization-pool score is not the deliverable number, a metric outside the
evaluated model/context settings is not covered, and "evolved" is not "correct".
