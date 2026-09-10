# Verifying `temporal-data-modeling`

`sh run.sh` — seconds, no network, stdlib + `bc` only.

## The case

A 7-day active-membership + login log (`checks.bc` and `tdm.py` share it):
members `m1..m5`; a persistent field (who is active *on* each day), an additive
cumulative field (login counts) and a set-valued cumulative field (who was
active *during* a window); one team merge on d4; one coverage gap on d6
(`ACTIVE["d6"] = None`, explicitly not `{}`).

Every number has a closed form computable by hand, so each check compares the
skill's prescribed operator against both the naive method it replaces and the
ground truth.

## What each check asserts

| # | Prescribed step (SKILL.md) | Negative contrast that must fail |
|---|---|---|
| 1 | classify a field persistent vs cumulative before aggregating | summing a persistent field ("member-days") matches neither valid view |
| 2a | round-trip class: inclusion-only ⇒ left-rigid | — (positive: `F → P K F` is exact) |
| 2b | round-trip class: churning field ⇒ loose ⇒ store both | deriving one view from the other loses a state |
| 3 | gluing check: cumulative overlap counted once | naive sum of half-intervals double-counts the boundary day |
| 3b | reconstruction is cut-point independent | — (positive) |
| 4 | set-valued cumulative field glues by dedup union | a count-additive pipeline over-counts (8 vs 5) |
| 5 | coverage gap ⇒ `unobserved`, excluded from churn | `disappear` policy invents 3 phantom departures + 3 arrivals |
| 6 | evaluate a coarse property by restrict-then-check | per-day evaluation of a week-resolution flag gives 3, truth is 5 |

## Limits

These gates catch mechanical defects — an unclassified field, a summed
persistent field, a diffed identity transition, a gap read as an event. They do
**not** catch bad judgement: a field mis-classified persistent-vs-cumulative
passes every gate and is caught only if a test cover happens to exercise it.
When applying the skill for real, choose a gluing-check cover that spans an
identity transition *and* a coverage gap, as this case does.
