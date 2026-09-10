# Field register — <model name>

One row per time-varying field (attribute, relationship, or metric). Copy the
block per field.

```yaml
field: <name>
belongs_to: <entity type or "derived metric">
semantics: persistent | cumulative
#   persistent  = value holds THROUGHOUT the interval; rebuilt by AGREEMENT
#                 (intersection / restriction) of sub-intervals
#   cumulative  = value ACCUMULATES OVER the interval; rebuilt by AGGREGATION
#                 (union / sum) of sub-intervals

query_phrasing: <the phrase a correct query uses>
#   persistent: "as of <date>", "in force on", "current"
#   cumulative: "to date", "over the period", "ever", "total"

aggregation_over_time: <the operation that combines sub-intervals>
#   persistent example: "intersection of the sets in force on each sub-day"
#   cumulative example: "union of daily active-member sets" / "sum of daily counts"

conversion_to_other_view:
  rule: <how to derive the other semantics>
  #   persistent -> cumulative (K): accumulate — union / sum / max-extent
  #   cumulative -> persistent (P): extract the common part — intersection
  reversible: yes | no

round_trip_class: rigid | left-rigid | right-rigid | loose
#   rigid       : both round trips recover the original — store either view
#   left-rigid  : persistent->cumulative->persistent is exact — safe to store
#                 cumulatively and derive the persistent view (not the reverse)
#   right-rigid : cumulative->persistent->cumulative is exact — safe to store
#                 persistently and derive the cumulative view (not the reverse)
#   loose       : neither round trip recovers — STORE BOTH or document the loss
sufficient_condition_used: <e.g. "membership only grows over the interval
                                  (inclusions) -> left-rigid" or "n/a — churns">

storage_decision: <which view(s) are stored, and where>
loss_if_single_view: <what the un-stored view cannot recover — required if loose>

resolution: <coarsest time granularity at which this field is defined>
unobserved_policy: <what a missing window means for this field —
                    never silently "disappear" or "zero">
provenance: <source system(s) and the field(s) they map from>
```

## Register summary table

| field | semantics | round-trip class | stored as | resolution |
|---|---|---|---|---|
| active_status | persistent | left-rigid | valid-time row versions | day |
| logins | cumulative | right-rigid | daily running count | day |
| team_membership | persistent | loose | both (as-of table + ever-member set) | day |

## Checklist

- [ ] Every time-varying field appears exactly once.
- [ ] No field is "both" — if a column carries persistent semantics for some
      rows and cumulative for others, it is two fields.
- [ ] Every `loose` field has a `storage_decision` of "both" **or** a
      `loss_if_single_view` note.
- [ ] No pipeline step sums a `persistent` field or intersects / point-in-times
      a `cumulative` one.
- [ ] Every field has an explicit `unobserved_policy`.
