# `tla-checker` analytics, modes, and command patterns

## Symmetry reduction

For interchangeable actors, `-s CONST` / `--symmetry CONST` reduces redundant state exploration.

```sh
tla formal/lock_protocol.tla -c 'Procs={"p1","p2","p3"}' --symmetry Procs
```

Use symmetry only when members of the set are truly interchangeable under initial state, actions, invariants, configuration, and external assumptions. Valid: `Procs = {"p1","p2","p3"}` when every process has identical behavior. Invalid: `Nodes = {"leader","follower_1","follower_2"}` when one node has special permissions or behavior. Before relying on it, run a small model both with and without symmetry and confirm failure/no-failure behavior agrees. Treat symmetry as an optimization, not a semantic shortcut.

## Scenario-driven exploration

`--scenario` investigates a suspected execution sequence while retaining the model's state semantics. Syntax: one or more `step:` lines containing TLA+ predicates over current and next state variables. Prefer a scenario file (shell quoting of primed variables is awkward):

```text
# formal/scenarios/retry-duplicate.txt
step: status'["job_1"] = "claimed"
step: retries'["job_1"] = retries["job_1"] + 1
step: status'["job_1"] = "ready"
```

```sh
tla formal/job_claim.tla --config formal/job_claim.cfg --scenario @formal/scenarios/retry-duplicate.txt
```

Use scenarios to reproduce a reported failure sequence, force a suspected race ordering, demonstrate the conditions required for a violation, compare expected vs actual transitions, or create a focused regression artifact after a fix. Do **not** use scenarios to hide unrestricted checker failures — first run ordinary exhaustive bounded exploration, then use scenarios to understand, minimize, or document a particular trace.

## Analytics and exploration modes

### `--continue`

By default the checker stops at the first invariant violation. `--continue` explores beyond violations and counts them across the state space.

```sh
tla formal/protocol.tla --config formal/protocol.cfg --continue --allow-deadlock
```

Use when assessing how common a failure is, when multiple invariants may fail, when comparing alternative designs, or when you need depth information about when violations first emerge. Do not use it as a substitute for fixing a known safety failure.

### `--count-satisfying NAME`

Measures how many reachable states satisfy a definition/predicate. Repeatable; emits per-property info in JSON.

```sh
tla formal/protocol.tla --config formal/protocol.cfg --allow-deadlock --continue \
  --count-satisfying InvSafe --count-satisfying AllJobsDone --verbose
```

Use for: what fraction of reachable states is healthy; at what depth failures first appear; how much of the state space is terminal; whether a mitigation increases the proportion of valid states. Do **not** confuse "most states satisfy an invariant" with correctness — for a safety invariant, a single reachable violating state fails the requirement.

### `--sweep`

Compares behavior across small values of one model constant, producing a comparison table.

```sh
tla formal/retry_protocol.tla --sweep 'MaxRetries=0;1;2;3' \
  --count-satisfying InvNoDuplicateCharge --allow-deadlock --continue
```

Use to find when an invariant begins to fail as a count grows, whether retries increase unsafe states, whether capacity constraints create deadlocks, whether an algorithm works only for trivial values. Rules: small interpretable values; keep all other constants fixed and documented; report every value tested; re-run a failing value **without** `--continue` to capture the first minimal trace; do not extrapolate small-bounded trends to production scale without qualification.

### `--json`

```sh
tla formal/protocol.tla --config formal/protocol.cfg --json > formal/artifacts/protocol-result.json
```

Output includes a `properties` array and can include `depth_breakdown` per property. Store JSON in a generated-artifacts directory; do not overwrite evidence from distinct runs unless the workflow uses versioned results.

### `--verbose`

Depth breakdowns and extra exploration info — useful for the first depth at which a violation appears, whether state-space growth accelerates, whether an expected transition is never reached, whether a liveness condition fails only after certain interleavings.

## Liveness and fairness

Safety asks "does something bad ever happen?" (two workers own the same job; a counter goes negative; a completed transaction is charged twice). Liveness asks "does something good eventually happen?" (a queued job eventually completes; a leader is eventually elected; a retrying client eventually succeeds).

Temporal operators are parsed but not evaluated in ordinary checking. Run liveness explicitly:

```sh
tla formal/protocol.tla --config formal/protocol.cfg --check-liveness
```

Before claiming a liveness result, document: the liveness formula; the fairness assumptions; the finite model bounds; whether terminal deadlocks are allowed; whether the tool reports complete exploration within its state/depth limits; any unsupported temporal semantics avoided. Do not model "eventually" by choosing an arbitrary maximum number of steps unless that bounded guarantee is the actual requirement — a bounded response-time property and an eventual-progress property are different claims.

## Interactive exploration

```sh
tla formal/protocol.tla --config formal/protocol.cfg -i
```

The TUI can step through transitions, backtrack, evaluate expressions in a REPL, trace variable changes, test hypotheses against visited states, toggle guard display, perform random walks, step until a condition holds, save/load traces, reset, and quit. Use for understanding an unfamiliar model, demonstrating a protocol, walking a counterexample manually, testing a hypothesis before encoding it as an invariant, or exploring why a guard is/isn't enabled. Do **not** use interactive exploration as the only validation — a manually selected path cannot establish that all bounded reachable states satisfy an invariant. Convert any important interactive finding into a formal invariant, a scenario file, a noninteractive command, a regression test, or a model comment linked to source/issue.

## State graph export

```sh
mkdir -p formal/artifacts
tla formal/protocol.tla --config formal/protocol.cfg \
  --export-dot formal/artifacts/protocol.dot --dot-mode clean
dot -Tsvg formal/artifacts/protocol.dot -o formal/artifacts/protocol.svg   # confirm Graphviz first
```

| Mode | Use |
|---|---|
| `clean` | Default overview: all nodes, no self-loops, merged parallel edges |
| `full` | Low-level: all nodes and edges, including self-loops |
| `trace` | Counterexample-focused graph, falls back to full if no trace exists |
| `choices` | Counterexample trace plus alternative transitions at trace states |

Error states are highlighted red; trace edges are red and emphasized. Use DOT graphs only when the state space is small enough to stay legible, or to explain a counterexample/deadlock, competing action choices, or a correct vs incorrect protocol variant. Do not interpret a giant state graph visually — use bounds, scenarios, analytic counts, and trace output.

## Command patterns

```sh
# Fast syntax / model iteration
tla formal/protocol.tla --config formal/protocol.cfg --quick

# Full bounded safety check
tla formal/protocol.tla --config formal/protocol.cfg --max-states 1000000 --max-depth 100

# Explicit constants
tla formal/protocol.tla -c 'Procs={"p1","p2","p3"}' -c 'N=3' --max-states 500000 --max-depth 80

# Check and continue gathering violations
tla formal/protocol.tla --config formal/protocol.cfg --allow-deadlock --continue --verbose

# Parameter sweep
tla formal/protocol.tla --config formal/protocol.cfg --sweep 'N=2;3;4;5' \
  --count-satisfying InvSafety --allow-deadlock --continue --verbose

# Liveness check
tla formal/protocol.tla --config formal/protocol.cfg --check-liveness

# JSON result artifact
mkdir -p formal/artifacts
tla formal/protocol.tla --config formal/protocol.cfg --json > formal/artifacts/protocol-result.json

# Counterexample-focused graph
mkdir -p formal/artifacts
tla formal/protocol.tla --config formal/protocol.cfg \
  --export-dot formal/artifacts/protocol-trace.dot --dot-mode trace
```
