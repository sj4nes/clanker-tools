# Identity-transition log — <model name>

## Identity model (one block per entity type)

```yaml
entity_type: <name>
key: <the identifier field(s)>
key_stability: <can the key be reused / recycled? how is that detected?>
transitions_that_apply: [persist, appear, disappear, merge, split, unobserved]
detection:
  persist:     <how "same entity, carried forward" is established — NOT key match alone>
  appear:      <how a genuinely new entity is distinguished from first-observed>
  disappear:   <how a genuine end is distinguished from unobserved>
  merge:       <what evidence records N prior entities becoming one>
  split:       <what evidence records one prior entity becoming N>
unobserved_policy: <what an entity absent from a window means; how it is stored>
```

## Transition log (one row per entity crossing a time boundary)

| at (instant/interval) | entity key(s) before | transition | entity key(s) after | attribute changes | evidence | notes |
|---|---|---|---|---|---|---|
| 2026-06-15 | team:a, team:b | merge | team:a | b's 4 members reassigned to a | ticket OPS-812 | b's id retired, not reused |
| 2026-06-20 → 06-27 | member:99 | unobserved | member:99 | — | source feed outage | NOT recorded as disappear |
| 2026-07-01 | — | appear | member:143 | — | signup event | genuinely new |

## Checklist

- [ ] No transition is inferred from key equality or a row diff alone — each has
      `evidence`.
- [ ] Every coverage gap is `unobserved`, never `disappear`.
- [ ] `merge` / `split` rows name all entities on both sides.
- [ ] Retired keys are marked non-reusable, or key-recycling detection is
      documented.
- [ ] Churn metrics built from this log exclude `unobserved` rows.
