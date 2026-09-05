# `tla-checker` modeling quality, examples, and failure handling

## Project layout

```text
formal/
  README.md                 # real system modeled; corresponding impl files/tests;
                            # actors and state; environmental assumptions; constants;
                            # invariants and meaning; deadlock policy; liveness;
                            # exact commands; known model limitations
  protocol.tla
  protocol.cfg
  scenarios/
    duplicate-claim.txt
  artifacts/
    .gitkeep                # ignored output directory
```

Do not place generated graph files, large trace exports, or temporary checker output in `src/`.

## Model quality rules

### Model the environment

Do not model only ideal execution if the requirement concerns faults or concurrency. Explicitly consider whether the model needs: message loss, duplication, reordering, delayed delivery; crash before/after persistence; retry after unknown outcome; network partition; stale cache reads; clock skew or lease expiration; partial deployment; repeated invocation; external service failure; concurrent actor actions; cancellation at any intermediate state. For each omitted behavior, state why it is outside the model boundary:

```text
Out of scope: network partition and persistent node crash.
In scope: delayed/duplicated client retries after an unknown response outcome.
```

A model that excludes the failure mechanism cannot establish safety against that mechanism.

### Avoid implementation mirroring

Do not transcribe production Rust line by line into TLA+. Model: relevant state; allowed transitions; preconditions; atomicity boundaries; effects; fault/interleaving behavior; required properties. A useful model may be 50 lines even when the implementation is thousands.

### Model atomicity intentionally

A major source of concurrency errors is the wrong atomic action boundary. If a workflow reads ownership, checks whether unowned, writes ownership, and emits an event as separate operations visible to other actors, do not model them as one atomic `Claim` action unless the storage system guarantees atomic compare-and-set. Model separate transitions or an explicit compare-and-swap condition. The model should reflect the strongest guarantee actually provided by the implementation, database, transaction, lock, or external API — not an assumed one.

### Avoid accidental under-modeling

A passing invariant is meaningless if the model never permits the dangerous transition. Check action reachability via state counts, verbose depth breakdowns, interactive exploration, `--count-satisfying` predicates, targeted scenarios, and explicit "can reach" predicates:

```tla
CanBeClaimed == \E j \in Jobs: status[j] = "claimed"
```

```sh
tla formal/job_claim.tla --config formal/job_claim.cfg --count-satisfying CanBeClaimed --verbose
```

If a core state never appears, inspect whether a transition guard is impossible or an initialization constraint is too strong.

## Model review checklist

Before running a substantive check, confirm: every real actor is represented or intentionally abstracted; every relevant shared resource is represented; every variable has an initial value; every action defines or preserves every variable; each action has a real-world counterpart; action guards match actual preconditions; relevant faults and nondeterminism are represented; numeric and collection domains are finite; type constraints cover every variable; safety invariants express actual requirements; deadlock semantics are deliberate; constants and exploration limits are explicit; any symmetry reduction is justified; unsupported syntax/semantics are avoided or verified; the model can reach the nontrivial states it is supposed to investigate.

## Example: duplicate processing after retry

```tla
---- MODULE RetryCharge ----
EXTENDS Naturals

CONSTANT Clients, MaxRetries
None == "none"
VARIABLES request_state, charge_count, retries

TypeOK ==
    /\ request_state \in [Clients -> {"new", "sent", "processing", "done"}]
    /\ charge_count  \in [Clients -> 0..2]
    /\ retries       \in [Clients -> 0..MaxRetries]

Init ==
    /\ request_state = [c \in Clients |-> "new"]
    /\ charge_count  = [c \in Clients |-> 0]
    /\ retries       = [c \in Clients |-> 0]

Send(c) ==
    /\ c \in Clients /\ request_state[c] = "new"
    /\ request_state' = [request_state EXCEPT ![c] = "sent"]
    /\ UNCHANGED <<charge_count, retries>>

Process(c) ==
    /\ c \in Clients /\ request_state[c] = "sent"
    /\ request_state' = [request_state EXCEPT ![c] = "processing"]
    /\ charge_count'  = [charge_count EXCEPT ![c] = @ + 1]
    /\ UNCHANGED retries

Retry(c) ==
    /\ c \in Clients
    /\ request_state[c] \in {"sent", "processing"}
    /\ retries[c] < MaxRetries
    /\ request_state' = [request_state EXCEPT ![c] = "sent"]
    /\ retries'       = [retries EXCEPT ![c] = @ + 1]
    /\ UNCHANGED charge_count

Finish(c) ==
    /\ c \in Clients /\ request_state[c] = "processing"
    /\ request_state' = [request_state EXCEPT ![c] = "done"]
    /\ UNCHANGED <<charge_count, retries>>

Next ==
    \/ \E c \in Clients: Send(c)
    \/ \E c \in Clients: Process(c)
    \/ \E c \in Clients: Retry(c)
    \/ \E c \in Clients: Finish(c)

InvNoDuplicateCharge == \A c \in Clients: charge_count[c] <= 1
====
```

```text
CONSTANT Clients = {"client_a", "client_b"}
CONSTANT MaxRetries = 1
INIT Init
NEXT Next
INVARIANT TypeOK
INVARIANT InvNoDuplicateCharge
CHECK_DEADLOCK TRUE
```

```sh
tla formal/retry_charge.tla --config formal/retry_charge.cfg --max-states 100000 --max-depth 30
```

The model intentionally permits a retry while the request is already `"processing"`, so `Process(c)` can run again and push `charge_count[c]` past one — a counterexample. The correct response is not to remove `Retry`; it is to determine the production guarantee needed (idempotency key, atomic deduplication record, durable processing status, conditional state transition). This model proves nothing about a specific payment processor or Rust implementation until its transitions and atomicity assumptions are connected to actual code and storage behavior.

## Example: lease ownership

```tla
---- MODULE Lease ----
EXTENDS Naturals, FiniteSets

CONSTANT Nodes, MaxEpoch
None == "none"
VARIABLES owner, epoch, active

TypeOK ==
    /\ owner \in Nodes \cup {None}
    /\ epoch \in 0..MaxEpoch
    /\ active \subseteq Nodes

Init == owner = None /\ epoch = 0 /\ active = {}

Acquire(n) ==
    /\ n \in Nodes /\ owner = None
    /\ epoch < MaxEpoch                 \* bound epoch so it stays within TypeOK
    /\ owner' = n /\ epoch' = epoch + 1 /\ active' = {n}

Release(n) ==
    /\ n \in Nodes /\ owner = n
    /\ owner' = None /\ UNCHANGED epoch /\ active' = {}

Next == \/ \E n \in Nodes: Acquire(n)
        \/ \E n \in Nodes: Release(n)

InvSingleActiveOwner == Cardinality(active) <= 1
InvOwnerMatchesActive ==
    /\ owner = None => active = {}
    /\ owner \in Nodes => active = {owner}
====
```

```text
CONSTANT Nodes = {"n1", "n2", "n3"}
CONSTANT MaxEpoch = 3
INIT Init
NEXT Next
INVARIANT TypeOK
INVARIANT InvSingleActiveOwner
INVARIANT InvOwnerMatchesActive
```

```sh
tla Lease.tla --config Lease.cfg --allow-deadlock   # 13 reachable states, no violations
```

Two things this small model illustrates. **`Cardinality` needs `FiniteSets`** — `tla-checker` happens to resolve it without the `EXTENDS`, but TLC and the wider ecosystem do not, so declare it. **The `epoch < MaxEpoch` guard is not cosmetic**: without it `Acquire` keeps incrementing `epoch` past `MaxEpoch`, immediately violating `TypeOK` (`epoch \in 0..MaxEpoch`). And the model deadlocks once no lease is held and every epoch is spent — that terminal state is legitimate here, hence `--allow-deadlock`. To model a real distributed lease, add separate local views, clock/epoch behavior, delayed observations, expiration, persistence, and retry behavior — increase fidelity only where it affects the property.

## Iterative refinement strategy

1. **Happy path** — basic actors, initial state, normal transitions, type invariant, basic safety invariant. Goal: validate notation and state evolution.
2. **Competing actors** — ≥2 interchangeable actors, shared resource contention, nondeterministic choice of actor/action. Goal: expose races and mutual-exclusion failures.
3. **Faults and retries** — only faults relevant to the question (retry, timeout, message duplication, lost response, delayed ack, partial persistence, crash/restart). Goal: expose failure-path violations.
4. **Compatibility and deployment** — old/new versions, schema/config versions, rollout steps, rollback conditions, mixed fleet states. Goal: expose migration and rollout hazards.
5. **Wider finite bounds** — increase one parameter at a time (`--sweep 'N=2;3;4;5'`), then investigate the smallest failing value.

Do not scale every dimension simultaneously — it makes state explosion harder to diagnose and counterexamples less interpretable.

## State-explosion management

Manage growth through model design, not by simply raising limits: reduce actors to the smallest number that can exhibit the failure; reduce resource identifiers to one or two representative elements; bound retry and message counts; abstract payload values into a small finite set; collapse irrelevant implementation state; model a representative request rather than every request type; use symmetry reduction only when justified; split separate concerns into separate models; use scenarios to investigate a known path; use parameter sweeps to locate the threshold where behavior changes; export graphs only for small state spaces; record state and depth limits explicitly. Do not hide state explosion by using `--quick` as the only validation or by silently reducing the model until it passes.

## Failure handling

**Parse/syntax error:** read the cited source location; check module delimiters, operator spelling, backslashes, primes, parentheses/brackets/braces; confirm the feature is in the supported subset; reduce to a minimal reproducing construct; re-run the smallest configuration after correction.

**Undefined identifier:** check spelling and case; confirm it is declared before use; confirm an `INSTANCE` module is in the expected directory and uses supported syntax; check scoped names within parameterized definitions; do not silently replace an undefined variable with a similarly named one. (The tool reports source locations for parse errors and suggests similar undefined-variable names.)

**Invariant violation:** preserve the trace and command; identify the first violating state; classify (real design flaw / missing guard / missing model behavior / invalid requirement); fix design or model based on evidence; add a regression scenario or invariant; re-run the original bound, then expanded bounds.

**Deadlock:** determine whether the state is a valid terminal state; if not, identify which transition should be available and why its guard fails; check for a missing recovery action, invalid guard, or overconstrained model; add `--allow-deadlock` only if a terminal-state predicate justifies it; re-run without suppressing unrelated deadlocks.

**State/depth limit reached:** do not call the check exhaustive; record the limit reached; reduce irrelevant state, add symmetry if valid, or split concerns; run parameter sweeps and targeted scenarios; increase limits only when hardware/time budget and expected state growth justify it; preserve prior findings — do not overwrite a complete small-model result with an incomplete large-model run.
