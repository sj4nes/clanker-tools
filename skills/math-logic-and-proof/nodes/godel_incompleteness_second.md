# godel_incompleteness_second

## Type
theorem  (epistemic status: **`stated_not_proved`**; `constructive_grade: n/a`)

## Statement
A consistent, recursively axiomatised theory `T` that can formalise a modest
amount of arithmetic (enough to prove the **Hilbert–Bernays–Löb derivability
conditions**) **cannot prove** the sentence `Con(T)` expressing its own
consistency:

    Con(T) ∧ rec_axiomatised(T) ∧ T ⊢ (HBL conditions)   ⟹   T ⊬ Con(T).

## Symbols
- `T`: a first-order theory; `Con(T) := ¬Prov_T(⌜0 = 1⌝)`, a `Π₁` sentence.

## Prerequisites (tsort edges into this node)
`godel_incompleteness_first`, `consistency_fol`.

## Proof (sketch — not in scope)
Formalise the first theorem's argument "`Con(T) → ¬Prov_T(⌜G_T⌝)`" **inside**
`T`; combined with the diagonal equivalence `T ⊢ G_T ↔ ¬Prov_T(⌜G_T⌝)`, this
gives `T ⊢ Con(T) → G_T`. If also `T ⊢ Con(T)`, then `T ⊢ G_T`, contradicting
the first theorem. Requires the three **Löb derivability conditions**:
`T ⊢ φ ⟹ T ⊢ Prov(⌜φ⌝)`; `T ⊢ Prov(⌜φ→ψ⌝) → (Prov(⌜φ⌝) → Prov(⌜ψ⌝))`;
`T ⊢ Prov(⌜φ⌝) → Prov(⌜Prov(⌜φ⌝)⌝)`.

## Constructive grade
`n/a` — a boundary node; the proof (elsewhere) is effective.

## Lean status
`lean_status: none`. Cited: [smith_godel_2e] part IV. (Mathlib / other systems
have partial formalisations; not connected here.)

## Type / well-formedness check
`well_formed` as a schema over `T`. The arithmetic hypothesis is **stronger**
than the first theorem's ("interprets `Q`") — the second theorem needs `T` to
support the *internal* formalisation of provability (roughly `PA`, or `Q` +
induction for `Σ₁` formulas).

## Specialization / boundary cases
- `T = PA`: `PA ⊬ Con(PA)`; but `PA + Con(PA)` is a strictly stronger consistent
  theory — which then cannot prove *its* own consistency.
- `T = ZFC`: `ZFC ⊬ Con(ZFC)`; `Con(ZFC)` follows from "there is an inaccessible
  cardinal".
- **Gentzen (1936)**: `Con(PA)` **is** provable by transfinite induction up to
  `ε₀` — in a system not contained in `PA`. No contradiction.
- **Löb's theorem** generalises: `T ⊢ (Prov(⌜φ⌝) → φ) ⟹ T ⊢ φ`; the second
  incompleteness theorem is the case `φ = ⊥`.

## Hypothesis-dropped counterexamples
- **`T` too weak** (only first-theorem strength, interprets `Q` but not the HBL
  conditions): may not support the internal argument.
- **`T` inconsistent**: proves `Con(T)` (it proves everything).
- **`T` not recursively axiomatised**: `Th(ℕ)` proves `Con(PA)`.

## Common misuse
"No theory can be proved consistent" — false; consistency is provable in
stronger systems (Gentzen, large cardinals). Reading it as evidence that `PA` /
`ZFC` *is* inconsistent. Thinking a proof of `Con(T)` inside `T` would be
reassuring anyway (an inconsistent `T` would also provide one). Confusing with
the first theorem (this one is specifically about `Con(T)`).

## Related nodes (non-prerequisite)
- `strengthens`: `godel_incompleteness_first`.
- `generalised_by`: Löb's theorem; provability logic **GL**.
- `feeds`: `incompleteness_of_PA_ZFC`.
- `related`: Gentzen's consistency proof, ordinal analysis, the HBL derivability
  conditions.

## Sources
[smith_godel_2e] part IV; [bbj_5e] ch. 18; Gödel (1931); Löb (1955).
