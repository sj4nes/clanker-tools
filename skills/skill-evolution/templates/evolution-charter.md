# Evolution charter

Fill this in before running the loop. If there is no evaluator, stop here — this
is an authoring task, not an evolution task.

## The document

- **Path / identifier:**
- **Role:** agent skill | system prompt | runbook | tool description | policy | other
- **Where it runs (model, harness, context):**
- **Current version / hash:**

## The evaluator

- **How a task is scored:** (command, service, judge model, rubric)
- **Per-case output:** metric vector + diagnostic? (a diagnostic is strongly preferred)
- **Deterministic?** if not, how many evaluations are averaged per case:

## Metrics

| Metric | Type | Threshold / boundary | Notes |
|---|---|---|---|
| e.g. task success | target (primary) | improve by ≥ 1.0 pt | |
| e.g. constraint-satisfaction rate | target (auxiliary) | improve by ≥ 2.0 pt | can carry a flat primary |
| e.g. cost per task | protected | regress by ≤ 0 | |
| e.g. previously-passing subset | protected | regress by ≤ 0 | |

## Task pool

- **Total tasks:**
- **Optimization pool:** (ids or rule)
- **Held-out test set:** (ids or rule — never used for rollouts or acceptance)
- **Trace set for `S_0`:** (may overlap the optimization pool; disjoint from held-out)
- **Split method:** (odd/even id, random with seed, benchmark-native)

## Loop parameters

- **Edit-budget unit:** lines | bullets | sections
- `b_base` (budget at zero volatility):
- `b_min` (floor):
- `V_max` (volatility saturation — calibrate after a few rounds):
- `beta2` (volatility EMA decay): 0.9
- **Batch size `|B_t|`:** (≥ 2 required; 5–10 typical)
- **Sampling seed:**

## Stop conditions

- **Round cap `T_max`:**
- **No-improvement streak `k`:**
- **Other:**

## Transfer

- **Will `S_final` run on other models / contexts?** yes / no
- **If yes, list them:**
- **Retention target:**

## Non-goals

- (What this run is explicitly not trying to improve.)
