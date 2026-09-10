# Checks and evaluation

## The gluing check (procedure)

The narrative model's central consistency requirement: data on an interval must
agree with data on any cover of it. Run this on real or realistic data, not on
paper.

**Setup.** Pick an interval `I = [a,b]` and an interior point `p`, giving the
cover `([a,p], [p,b])` meeting at the instant `[p,p]`.

**For each persistent field `F`:**

1. Compute `F([a,p])`, `F([p,b])`, `F([p,p])`, and the stored/derived `F([a,b])`.
2. Compute the agreement: `A = { x in F([a,p]) restricted to p } ∩ { x in F([p,b]) restricted to p }`,
   then pull that back to the full interval.
3. **Assert** `F([a,b]) == A`. If `F([a,b])` is larger, the model is asserting
   validity that the halves do not support. If smaller, it is dropping valid
   data.

**For each cumulative field `F̂`:**

1. Compute `F̂([a,p])`, `F̂([p,b])`, `F̂([p,p])`, and the stored/derived `F̂([a,b])`.
2. Compute the combination: `U = F̂([a,p]) ∪ F̂([p,b])` de-duplicated along
   `F̂([p,p])` (the overlap instant is contributed once, not twice).
3. **Assert** `F̂([a,b]) == U`. The common bug: the overlap instant `p` is
   summed into both halves, so `F̂([a,b])` over-counts by `F̂([p,p])`.

**Order independence.** Repeat with a different split point `p'`. The
reconstruction must not depend on where you cut. If it does, the field's
semantics are mis-stated (often: a field treated as cumulative that is really
persistent-with-a-max, or vice versa).

## Multi-source interval reconciliation

When two sources `X` and `Y` both describe the same phenomenon over overlapping
time:

1. **Do not compare snapshots.** Align both onto the same interval lattice
   first.
2. For each interval, apply the per-semantics reconciliation:
   - persistent: `X` and `Y` must agree on what holds throughout; a difference
     is a genuine conflict.
   - cumulative: `X` and `Y` may legitimately differ if their coverage windows
     differ; normalise to a common window before comparing.
3. A conflict that survives interval alignment is **retained**, not resolved by
   picking a source: record both values, the interval it occurs on, and each
   source's authority. Many apparent instant-level conflicts dissolve here —
   they were resolution mismatches (one source is end-of-day, the other is
   real-time).

## The `unobserved` policy

For every field and every entity, a window with no data has an explicit
meaning — chosen, not defaulted:

| policy | when correct | never |
|---|---|---|
| `carry forward` (last value holds) | persistent field, source only emits on change | for cumulative fields |
| `zero` | cumulative count, and the source is known-complete for the window | when coverage itself is uncertain |
| `unobserved` (null, excluded from metrics) | coverage gap, feed outage, entity outside sample | recording it as `disappear` / churn |
| `disappear` (entity ended) | there is a positive end event | inferred from mere absence |

The defining test: **is there positive evidence of the state, or only absence of
data?** Absence of data is `unobserved`.

## Evaluation metrics

| metric | definition | target |
|---|---|---|
| classification coverage | fraction of time-varying fields with a persistent/cumulative mark | 100% |
| round-trip disclosure | fraction of convertible fields with a round-trip class *and* a stored/loss decision | 100% |
| identity-transition precision | transitions with positive evidence / all recorded transitions | 1.0 (no diffed transitions) |
| gluing-check pass rate | fields passing the gluing check on the test cover | 100%; any failure is a modelling bug |
| order-independence | fields whose reconstruction is cut-point independent | 100% |
| resolution correctness | coarse properties evaluated by restrict-then-check / all coarse properties | 100% |
| unobserved discipline | coverage gaps recorded as `unobserved` / all coverage gaps | 1.0 |
| reconciliation conflict retention | surviving cross-source conflicts retained with both values / all surviving conflicts | 1.0 |

`check.py`-style gates catch mechanical defects (an unclassified field, a summed
persistent field, a diffed transition). They do not catch bad judgement — a
field classified persistent that is really cumulative will pass every gate and
fail the gluing check only if your test cover happens to exercise it. Choose
test covers that span an identity transition and a coverage gap.

## Failure modes

- **Snapshot-sequence-in-disguise.** A `history` table with `(id, valid_from,
  valid_to, ...)` but no transition log — you can see states change, not why.
  Symptom: churn metrics that spike on data-pipeline incidents.
- **Semantic bleed.** One column that is a running total for some rows and a
  point-in-time value for others (e.g. "balance" that is end-of-day except for
  the current day). Split it.
- **Overlap double-count.** Monthly figure = sum of daily figures, but the month
  boundary day is in both months' daily tables. The gluing check catches it.
- **Gap-as-event.** A member absent during a feed outage recorded as churned,
  then re-acquired — a phantom cohort.
- **Derived-view trap.** "We'll compute the quarterly distinct count from the
  daily actives" — fine only if the field is left-rigid (daily membership
  monotone within the quarter). With churn it under- or over-counts depending
  on the aggregation.
- **Resolution collapse.** "Power user" (a monthly property) evaluated per
  session, producing a flapping flag.

## When a snapshot sequence is actually fine

Use a plain snapshot sequence — and skip this skill — when **all** of:

- entities have stable, non-recycled keys and no merges/splits ever occur;
- every field is unambiguously point-in-time (persistent) and never aggregated
  over time;
- there is a single source with complete, gap-free coverage;
- no query asks a "to date" / "over the period" / "ever" question;
- no property needs a resolution coarser than the snapshot interval.

If any of those fails, the relations between snapshots carry information, and a
sequence drops it.
