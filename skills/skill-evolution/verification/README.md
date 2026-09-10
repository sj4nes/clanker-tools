# Verifying `skill-evolution`

`sh run.sh` — seconds, no network, stdlib + `bc` only.

## The case

The 4-round worked example from
[`../references/optimization-loop.md`](../references/optimization-loop.md):
`b_base = 8`, `b_min = 1`, `V_max = 2.0`, `beta2 = 0.9`, batches of four cases
with recorded per-case improvement vectors. Every number has a closed form
computable by hand.

## What each check asserts

| # | Prescribed mechanism (SKILL.md) | Negative contrast that must hold |
|---|---|---|
| 1 | volatility EMA + edit budget: `budget = max(b_min, floor(b_base·(1 − clip(V/V_max))))` | a volatile round (big wins *and* big losses) drops the next budget from 8 to 4; the EMA keeps it at 4 through the following calm round; it recovers to 5 only afterward |
| 2 | acceptance gate: a target must clear its threshold **and** every protected metric must stay within its boundary | a candidate whose mean improves but whose `cost` (or `safety_pass`) regresses is **rejected**; a flat primary carried by an auxiliary target is accepted |
| 3 | issue-tracker update: link a recurrence to its existing entry, mark it `reopened` | a recurring failure does **not** open a duplicate issue; a genuinely new failure does open one |
| 4 | rejected-candidate log: check before re-proposing | a patch signature already logged as `rejected` is flagged as a dead end; a fresh signature is not |

## Limits

These gates catch mechanical defects — an edit budget that ignores volatility, a
gate that averages instead of protecting, a tracker that duplicates issues, a
loop with no dead-end memory. They do **not** catch bad judgement: a
mis-scoped issue pattern, a `V_max` calibrated to the wrong scale, or a target
threshold set so low that noise clears it will pass every check here and is
caught only by watching the accuracy-vs-round curve on a real run.
