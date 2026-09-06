# lub_property

## Type
theorem  (epistemic status: `constructive_result`)

## Statement
Every nonempty `S ⊆ ℝ` that is bounded above has a supremum in `ℝ`, and it is
the union of the cuts in `S`:

    sup S  =  ⋃_{A ∈ S} A .

## Symbols
- `S`: a set of reals — i.e. a set of Dedekind cuts
- `⋃ S`: the union of all those cuts, a subset of `ℚ`

## Prerequisites (tsort edges into this node)
`real_number`, `dedekind_cut`, `real_order`, `rational_is_ordered_field`
(transitively: `rational_number` → `integer` → `natural_number` → `peano_axioms`
→ `set`).

## Hypotheses
`S ≠ ∅`; `S` bounded above (some cut `B` with `A ⊆ B` for all `A ∈ S`).

## Proof
Let `U = ⋃_{A∈S} A`. **`U` is a cut** (the entire content):

1. *nonempty* — pick `A ∈ S` (`S ≠ ∅`); `A ≠ ∅`, so `U ⊇ A ≠ ∅`.
2. *proper* — `U ⊆ B` and `B ≠ ℚ`, so `U ≠ ℚ`.
3. *downward closed* — if `p ∈ U` and `q < p`, then `p ∈ A` for some `A ∈ S`,
   and `A` is downward closed, so `q ∈ A ⊆ U`.
4. *no greatest element* — if `p ∈ U` were greatest, `p ∈ A` for some `A ∈ S`,
   and `p` would be greatest in `A`, contradicting that `A` is a cut.

Then `U` is an **upper bound**: `A ⊆ U` for every `A ∈ S`, i.e. `A ≤ U`. And
`U` is **least**: any upper bound `B` has `A ⊆ B` for all `A`, hence `U = ⋃ A ⊆
B`, i.e. `U ≤ B`. So `U = sup S`. ∎

**Checked with Lean:** `cited` — the statement is set-level (sets of sets of
rationals) and is not formalised in the Mathlib-free environment. The
underlying ℚ-order facts are in `proof-checks.lean` §1–3.

## Epistemic status: why `constructive_result`
No choice, no non-constructive existential: the supremum is the **specific set**
`⋃ S`. This is the sharpest contrast with
[`math-real-analysis`](../../math-real-analysis/SKILL.md), where this exact
statement is the **axiom** `lub_axiom` and its consequences (Bolzano–Weierstrass,
EVT, IVT, …) are labelled `nonconstructive_result` precisely because the `sup`
is *not* exhibited there.

## Type / well-formedness check
`well_formed` (`validation/type-checks.md#lub_property`). The whole check *is*
"the union of the cuts is again a cut" (objects.md rule 3).

## Specialization / boundary cases
- `S = { q* : q ∈ ℚ, q < 1 }` → `sup S = 1* = { p : p < 1 }`.
- `S = { q* : q ∈ ℚ, q² < 2 }` → `sup S` is the `√2` cut (`nth_root_exists`).
- `sup { A } = A`.

## Hypothesis-dropped counterexamples
- **drop `S ≠ ∅`:** `sup ∅` would be the least real — there is none.
- **drop bounded above:** `⋃ S = ℚ`, which is **not a cut** — no sup.
- **ambient field `ℚ` instead of `ℝ`:** *false* — `rational_incomplete_lub`.
  This theorem is the reason `ℝ` was constructed.

## Common misuse
Assuming `sup S ∈ S`; importing the statement into `ℚ`; calling it an axiom.

## Related nodes (non-prerequisite)
- `equivalent_to`: `real_dedekind_completeness`; nested-interval + Archimedean
  (in `math-real-analysis`)
- `contrasts_with`: `rational_incomplete_lub`
- **discharges**: the `math-real-analysis` node `lub_axiom` (there an axiom,
  here a theorem)
- feeds: `real_archimedean`, `rational_dense_in_real`, `nth_root_exists`,
  `dedekind_cauchy_equivalent`, `real_uniqueness`

## Sources
[rudin_principles] Appendix, step 5; [landau] §§42–43; [dedekind_1872].
