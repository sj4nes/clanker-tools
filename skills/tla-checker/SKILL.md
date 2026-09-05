---
name: tla-checker
description: >-
  Use `tla-checker` / `tla-rs` (a lightweight Rust TLA+ checker for a supported
  TLA+ subset) to model bounded concurrent, distributed, transactional, or
  protocol-like systems, exhaustively explore reachable states, check safety
  invariants and deadlocks, run bounded liveness analysis, and inspect
  counterexample traces. Use to find design flaws before or alongside
  implementation — not as proof of an unbounded production system.
version: 1.0.0
author: Simon Janes
tags: [formal-methods, tla-plus, model-checking, concurrency, distributed-systems, verification]
---

# Formal Model Checking with `tla-checker`

You are an autonomous engineering agent that uses `tla-checker` / `tla-rs` to model and check safety properties, deadlocks, bounded liveness properties, and failure scenarios in stateful, concurrent, distributed, transactional, or protocol-like systems.

Use `tla-checker` to find design flaws **before** or alongside implementation and tests. Treat it as a formal exploration tool for a bounded model — not as proof that an arbitrary production system is correct under every possible input, scale, runtime, or implementation detail.

Your priorities are:

1. Model the relevant state and transitions faithfully enough for the decision at hand.
2. State invariants precisely and check them exhaustively within explicit bounds.
3. Treat counterexamples as concrete debugging evidence.
4. Make exploration bounds, constants, assumptions, and unsupported features explicit.
5. Keep the model separate from implementation code while maintaining traceability to the system being modeled.

Workflow:

    define system boundary → model state → model actions → state properties
    → run bounded exploration → analyze trace → refine model or design → recheck

`tla-checker` explores reachable states, checks invariants, reports counterexample traces, supports an interactive terminal UI, and provides controls for constants, state/depth limits, deadlocks, liveness/fairness checks, scenarios, analytics, JSON output, and state-graph export.

## Purpose and fit

Use `tla-checker` for systems whose correctness depends on **state transitions and ordering**: concurrent tasks sharing a queue/lock/lease/token/cache/resource; distributed protocols and message-passing workflows; retry/timeout/cancellation/backoff/idempotency logic; leader election, ownership handoff, failover; transaction workflows and commit/rollback; deployment, rollback, migration, expand-contract release sequences; configuration rollout and feature-flag transitions; job schedulers, worker pools, queue consumers; resource allocation, admission control, rate limits, capacity constraints; multi-step authz/authn flows; state machines, parsers, workflow engines, coordination protocols; replication, cache invalidation, eventual-consistency assumptions; API behavior where multiple actors interleave; bug reports of the form "this only fails under a particular order of events."

Do **not** use `tla-checker` as the sole tool for: parsing/type-checking/compiling/formatting/testing Rust source; proving memory safety, ownership, type safety, or absence of UB in a Rust implementation; validating cryptography; measuring performance/latency/throughput/capacity; validating a system at unbounded scale; replacing integration/load/fuzz/property/security/e2e tests; proving production correctness when the model contains arbitrary finite bounds; modeling a feature that depends on unsupported TLA+ syntax or semantics without first confirming compatibility.

It is a lightweight alternative to TLC for specs that fit its supported subset (standard modules including Naturals, Integers, Sequences, FiniteSets, TLC, Bags, Bits) but has real boundedness and temporal-logic limitations.

## Core model

A TLA+ model describes `State --Action--> Next State`, via: **Constants** (fixed model parameters), **Variables** (mutable state), **`Init`** (allowed initial states), **`Next`** (allowed transitions), **Invariants** (hold in every reachable state), **Properties** (temporal/liveness, when supported and explicitly enabled), **Configuration** (values for constants and entry points).

```tla
---- MODULE Counter ----
EXTENDS Naturals

CONSTANT Limit
VARIABLE x

Init == x = 0
Next == x < Limit /\ x' = x + 1
TypeOK == x \in 0..Limit
InvNeverExceedsLimit == x <= Limit
====
```

```sh
tla Counter.tla --validate -c 'Limit=5'    # parse + check; no exploration
tla Counter.tla --list-invariants -c 'Limit=5'
tla Counter.tla -c 'Limit=5' --allow-deadlock
```

Definitions beginning with `Inv`, `TypeOK`, or `NotSolved` are automatically checked (`--list-invariants` prints exactly what was detected — run it whenever a check passes suspiciously fast, to confirm your invariants were actually picked up). This `Counter` **reaches a deadlock** at `x = Limit`: once `x` equals `Limit` no `Next` disjunct is enabled, so a plain `tla Counter.tla -c 'Limit=5'` exits non-zero with a deadlock trace. Here that terminal state is intended, so `--allow-deadlock` is correct; alternatively add a `x = Limit /\ x' = x` stutter disjunct. Treat every deadlock this deliberately — see the deadlock policy below.

## Required operating principles

- Model the **smallest system** that can reveal the suspected correctness issue. Bound all finite domains intentionally and document every bound.
- Use symbolic names rather than fragile numeric encodings when names improve trace readability.
- Represent all state relevant to the property; omitted state creates false confidence. Keep environment behavior explicit — model message loss, duplication, crash, timeout, external failure, or stale reads if those matter.
- Prefer one action per meaningful transition or protocol event. Write invariants before or alongside actions, not only after a failure appears. Use a type invariant for every variable.
- State whether deadlock is a bug, expected terminal behavior, or intentionally allowed.
- Treat passing results as evidence about the modeled finite state space only. Treat failing results as high-value evidence — investigate the trace before modifying the model.
- Do not "fix" a counterexample by weakening an invariant unless the original invariant was genuinely not a requirement. Do not suppress deadlocks with `--allow-deadlock` until you have classified the deadlock as intentional. Do not claim liveness was checked unless `--check-liveness` was enabled and the property is supported.
- Do not use unbounded domains merely because they match a conceptual requirement; create an explicit finite model.
- Keep model edits reviewable through version control. Keep formal-model outputs separate from production code and build artifacts.

## Installation and capability verification

Build from source (`cargo build --release`); the executable is `target/release/tla`; the CLI is invoked as `tla`.

```sh
command -v tla
tla --help
tla --version   # or record the git revision / crate version used
```

Do not assume a globally installed `tla` binary is this tool — confirm its help output contains the expected options: `--max-states`, `--max-depth`, `--config`, `--allow-deadlock`, `--check-liveness`, `--scenario`, `--export-dot`, `--json`, `--validate`, `--list-invariants`. (Verified against `tla 0.6.11`.)

## Supported subset and constraints

Read the project's current `SYNTAX_STATUS.md` if available. The checker supports logic, comparisons, arithmetic, sets, functions, quantifiers, records, tuples/sequences, `IF-THEN-ELSE`, `CASE`, `LET-IN`, primed variables, `UNCHANGED`, transitive closure, and module instances.

Documented limitations:

- `Nat` and `Int` are **bounded** (stated default range −100 to 100).
- Temporal operators `[]`, `<>`, `~>` are parsed but not evaluated in ordinary exploration. Use `--check-liveness` for supported liveness/fairness analysis via strongly connected components.
- Unbounded quantifiers such as `\E x : P` without a finite domain are unsupported.
- `Seq(S)` enumeration is unsupported.
- Recursive operators must be declared with `RECURSIVE`.

Therefore: use finite process sets (`Procs = {"p1","p2","p3"}`); bounded numeric ranges (`0..MaxRetries`); quantify over known finite sets (`\A p \in Procs: ...`); avoid unconstrained integers/naturals; avoid designs requiring enumeration of arbitrary-length sequences; declare recursion where required; confirm exact supported operator semantics before using advanced features. A model that runs is not necessarily faithful.

## Required workflow

### 1. Define the model question

Start with a concrete correctness question ("Can two workers simultaneously own the same job after retries and stale messages?", "Can a request be charged twice if a client retries after a timeout?"), not "model the service" or "prove the system correct". Define: system boundary; actors; state to model; operations/events; environmental failures and nondeterminism to include; the safety/liveness/deadlock properties; expected terminal states; explicit finite bounds; connection to production implementation or design docs. Do not begin from an implementation dump — a useful model is a smaller abstraction centered on the failure mode under investigation.

### 2. Identify actors and constants

Represent fixed, finite populations as constants (`CONSTANT Procs, Jobs, MaxRetries`). Accepted constant forms: integer, Boolean, string, set. Use explicit CLI constants when experimenting:

```sh
tla formal/job_claim.tla -c 'Procs={"worker_a","worker_b"}' -c 'Jobs={"job_1","job_2"}' -c 'MaxRetries=2'
```

Start with the **smallest nontrivial** configuration (e.g. 2–3 processes, 1–2 shared resources for mutual exclusion; 2 clients / 1 request / 1–3 retries for retry correctness), then widen bounds after the model behaves as expected. Do not start with large values.

### 3. Define variables and a type invariant

Declare every mutable piece of state explicitly, then constrain every variable:

```tla
None == "none"
TypeOK ==
    /\ owner  \in [Jobs -> (Procs \cup {None})]
    /\ status \in [Jobs -> {"ready", "claimed", "done", "failed"}]
    /\ retries \in [Jobs -> 0..MaxRetries]
```

The type invariant is not boilerplate — it detects state-update mistakes, incomplete `EXCEPT` expressions, wrong record values, accidental domain expansion, and transitions that fail to preserve state representation. Names beginning `TypeOK` are auto-checked.

### 4. Write `Init`

Every variable must receive an initial value; do not leave state implicit because an implementation initializes it elsewhere.

```tla
Init ==
    /\ owner = [j \in Jobs |-> None]
    /\ status = [j \in Jobs |-> "ready"]
    /\ retries = [j \in Jobs |-> 0]
```

Iterate on syntax with `--validate` (parse and check, no exploration), then on early behavior with `--quick` (caps exploration at 10,000 states — not a complete pass if the reachable space is larger).

### 5. Model actions with primed state

Every transition relates current to next-state variables using primes; use finite-domain quantifiers only.

```tla
Claim(p, j) ==
    /\ p \in Procs /\ j \in Jobs
    /\ status[j] = "ready" /\ owner[j] = None
    /\ owner'  = [owner  EXCEPT ![j] = p]
    /\ status' = [status EXCEPT ![j] = "claimed"]
    /\ UNCHANGED retries

Next ==
    \/ \E p \in Procs, j \in Jobs: Claim(p, j)
    \/ \E p \in Procs, j \in Jobs: Complete(p, j)
    \/ \E p \in Procs, j \in Jobs: FailAndRetry(p, j)
```

### 6. Preserve unchanged variables

Every action must assign or explicitly preserve every state variable — `UNCHANGED var` or `UNCHANGED <<var_a, var_b>>`. Do not omit variables because "they should stay the same"; an incomplete next-state relation produces invalid states, parser errors, false counterexamples, or an unintended model. After adding any action, check `TypeOK` still holds under exploration.

### 7. State safety invariants

An invariant must be true in every reachable state. Name them `Inv...` for auto-checking.

```tla
InvOwnerMatchesStatus ==
    \A j \in Jobs: (status[j] = "claimed") => (owner[j] \in Procs)

InvTerminalJobsUnowned ==
    \A j \in Jobs: (status[j] \in {"done", "failed"}) => (owner[j] = None)
```

If the system can track multiple claims or leases, represent that state directly. Do not "prove" mutual exclusion using a model that cannot represent simultaneous ownership.

### 8. Define configuration

`tla-checker` supports TLC-style `.cfg` files and auto-discovers `Spec.cfg` beside `Spec.tla`; `--config PATH` sets one explicitly. Directives: `INIT`, `NEXT`, `SPECIFICATION`, `CONSTANT(S)`, `INVARIANT(S)`, `PROPERTY`/`PROPERTIES`, `SYMMETRY`, `CHECK_DEADLOCK`. **CLI flags override configuration values.**

```text
CONSTANT Procs = {"worker_a", "worker_b"}
CONSTANT Jobs = {"job_1", "job_2"}
CONSTANT MaxRetries = 2
INIT Init
NEXT Next
INVARIANT TypeOK
INVARIANT InvOwnerMatchesStatus
CHECK_DEADLOCK TRUE
```

Check `.cfg` into version control when it represents an intended, repeatable model instance. Record every CLI override in the completion report — a passing run with temporary constants is not a passing canonical configuration.

## State-space limits

Documented defaults: max states 1,000,000; max trace depth 100; quick mode 10,000 states. Control explicitly with `--max-states` / `--max-depth`.

Distinguish three separate things: **model constants** (what system sizes/inputs exist in the model), **`--max-states`** (how many discovered states the checker may explore), **`--max-depth`** (greatest trace depth followed). A state cap or depth cap can prevent complete exploration — **do not describe a run as exhaustive if the checker stopped at a configured limit.** Every report must separate "bounded model parameters" from "exploration limits", and state plainly when a result is limited.

## Deadlock policy

A state with no valid `Next` action may indicate a missing recovery path, contradictory guard, unavailable transition, or incomplete model. **Do not suppress deadlocks automatically.** Detect them with `CHECK_DEADLOCK TRUE`.

Use `--allow-deadlock` only when deadlock corresponds to an intended terminal state (all jobs complete; a one-shot protocol terminates; a finite workflow reaches a valid completed state). When allowing deadlocks, add a terminal-state predicate that proves every allowed deadlock is valid:

```tla
Done == \A j \in Jobs: status[j] \in {"done", "failed"}
```

If `--allow-deadlock` eliminates a failure without a corresponding terminal-state argument, treat the model as unresolved.

## Counterexample analysis

When an invariant fails, the checker reports a trace with state differences and changed variables. Treat it as one of four cases:

| Type | Meaning | Response |
|---|---|---|
| Real design flaw | Model represents an invalid but reachable system behavior | Change design/implementation plan; add a regression model |
| Missing precondition | Action permits a transition production code should reject | Add and justify a guard/validation condition |
| Missing state/model behavior | Model omits a relevant condition or transition | Correct model, then re-run all checks |
| Incorrect invariant | Property is stronger/different than the actual requirement | Restate requirement and revise only with evidence |

Workflow: save the command + exact model/config; identify the first violating state; list preceding actions and changed values; translate each abstract transition into the real-system event; confirm whether the execution is possible under intended production semantics; determine whether the issue is design, model, or requirement; add a narrowly scoped fix or guard; re-run the smallest reproducing configuration; expand bounds again; keep the counterexample as a regression artifact. Do not add an invariant that merely excludes the failing state unless it corresponds to a genuine protocol condition the system enforces.

Capture the trace with `--trace-json FILE` (state-by-state JSON) or `--save-counterexample FILE` (trace plus metadata for replay); re-run it later with `--replay FILE` to confirm a fix removed it. The failing-run JSON (`--json`) embeds the trace as a `trace` array of `{index, action, state}` and `stats` as `{states_explored, transitions, max_depth, elapsed_secs}`; with `--count-satisfying` it adds a `properties` array of `{name, satisfied, violated, errors, total, ratio, depth_breakdown}`.

## References

- [`references/analytics-and-modes.md`](references/analytics-and-modes.md) — symmetry reduction, scenario-driven exploration, `--continue` / `--count-satisfying` / `--sweep` / `--json` / `--verbose`, liveness and fairness (`--check-liveness`), interactive TUI (`-i`), DOT state-graph export and modes, and the full command-pattern catalog.
- [`references/modeling-and-examples.md`](references/modeling-and-examples.md) — model quality rules (model the environment, avoid implementation mirroring, model atomicity intentionally, avoid accidental under-modeling), the model review checklist, two worked examples (duplicate processing after retry; lease ownership), the phased iterative-refinement strategy, state-explosion management, and failure handling (parse errors, undefined identifiers, invariant violations, deadlock, limit reached).

## Required completion report

```text
Model goal:            - [the concrete engineering question]
Model scope:           - [actors, bounds; what is included; what is excluded]
Model artifacts:       - formal/<spec>.tla, formal/<spec>.cfg
Properties checked:    - TypeOK, Inv...; deadlock policy
Command:               - [exact tla command with --max-states / --max-depth]
Result:                - Passed for the declared bounded model / Failed: <Inv> violated
[Counterexample:       - numbered real-system events]
[Interpretation:       - what the trace means for the system]
Next action:           - [model change, rerun, sweep]
Limitations:           - bounded abstract model, not a proof of the implementation;
                         [unmodeled faults]; result applies only to stated constants,
                         assumptions, supported subset, and exploration limits
```

For a pass, report states/transitions explored and max depth reached, and never say "the system is formally proven correct" — say **"No violation was found in the declared bounded model."**

## Completion requirements

Before declaring a `tla-checker` task complete, confirm that:

- The concrete engineering question was stated.
- The system boundary, actors, environmental assumptions, and excluded behaviors were documented.
- All domains are finite and all bounds are explicit.
- Every variable has an initial value and type constraint.
- Every action updates or preserves every variable.
- Every safety property is represented by a clear invariant.
- Deadlock behavior is deliberate and documented.
- The installed checker's supported subset and relevant option behavior were verified.
- The exact configuration, CLI arguments, state limit, and depth limit were recorded.
- A successful result is described only as a result for the declared bounded model.
- A failed invariant or deadlock was investigated using its trace rather than suppressed.
- Any scenario, sweep, JSON result, or graph artifact is clearly identified as derived output.
- No model-check result is misrepresented as a substitute for implementation tests, code review, runtime validation, or production safeguards.
