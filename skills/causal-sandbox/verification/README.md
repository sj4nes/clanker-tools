# `causal-sandbox` skill — verification run

The `causal-sandbox` skill is methodology-only (no bespoke CLI), so verification
means: build the kind of sandbox the skill prescribes on a known-answer domain
and confirm each prescribed mechanism behaves as claimed — including the negative
contrasts the guardrails exist to prevent.

**Worlds.**

- **inventory** — `consume` (−5/step), guarded `reorder` (fires the step stock
  first drops below threshold), `restock` (+30), and a `noop` with an empty
  write-set. Deterministic under a fixed priority scheduler; confluent. Chosen
  because the day-by-day stock levels, the reorder-crossing step, and the
  zero-hit step are all exact integer arithmetic (`checks.bc`).
- **roles** — `grant_default` (a new user gets `viewer`) and `revoke_all` (a
  flagged user loses it). On a user who is both new and flagged, the two rules
  reach different states in the two firing orders — a genuine non-confluent pair.

## Run

```
sh skills/causal-sandbox/verification/run.sh
```

Tooling: `bc` (integer arithmetic, no `-l`), Python 3 stdlib only, macOS. ~1 s.

## What each check demonstrates (SKILL.md mechanism → result)

| Check | Prescribed mechanism | Result |
|---|---|---|
| 1 (bc) | the arithmetic the engine trace must reproduce | reorder fires after consume #4 at stock 20; restock recovers to 50; with threshold 3 stock lands exactly on 0 at consume #8 — **pass** |
| 2 forward / causal graph | event B depends on A iff A is the **last writer**, before B, of a key B reads | `consume#3 → reorder` edge present (via `stock`); `reorder → restock` present (via `pending`); `consume#0 → reorder` **absent** — the earlier writes are correctly shadowed by the last one — **pass** |
| 3 backward / minimal intervention | search over **initial facts**, fewest changes first | "stock hit 0" → the 1-change fix is `threshold := 25`; the candidate space is initial facts only, so "skip the day-4 consume" is not even expressible — **pass** |
| 4 confluence pass | flag a rule pair iff the two firing orders reach different states | `grant_default`/`revoke_all` on one user is flagged; two `grant_default`s on different users are not — **pass** |
| 5 the guardrail with teeth | a causal claim on a non-confluent slice is order-dependent | "`revoke_all` caused `holds=False`" is true under ⟨grant, revoke⟩ (final `False`, `revoke_all` the last writer) and false under ⟨revoke, grant⟩ (final `True`, `grant_default` the last writer) — the single claim was a coin toss — **pass** |
| 6 engine verification | degenerate cases + read/write-set enforcement | no enabled rule → 0 events (frozen); empty-write rule leaves state unchanged; replay byte-identical; a rule that writes or reads an undeclared field is **rejected** — **pass** |

## Findings folded into the skill

- **`dict(state, **changes)` does not work when state keys are tuples** (Python
  requires string keyword keys). The engine uses a `upd(state, changes)` helper
  instead. Noted here because a reader building a real sandbox with
  tuple-structured facts (`("holds", u, r)`) will hit the same wall; the
  `references/rules-and-causality.md` fact model uses exactly that shape.

Nothing in `SKILL.md` or the reference files needed a correctness fix; the
prescribed workflow produced the right rule register, the right causal graph, and
the right confluence verdict.

## Gates are necessary, not sufficient

These checks catch mechanical defects — an undeclared write, a wrong causal edge,
a missed conflict. They do **not** catch a rule whose *guard or effect is a wrong
model of the domain*: a mis-declared write-set that happens not to collide in the
test scenario passes every check. Real use needs a scenario cover that exercises
each rule's full write-set against every other rule's read-set, and a domain
owner who has signed off on each rule's `source`.
