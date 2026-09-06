# lowenheim_skolem_up

## Type
metatheorem  (epistemic status: `metatheorem`; `constructive_grade:
needs_full_classical`)

## Statement
If a theory `T` in a language `ℒ` has an **infinite** model, then for every
cardinal `κ ≥ max(ℵ₀, |ℒ|)` it has a model of cardinality **exactly** `κ`
(equivalently, `≥ κ`, then apply downward LS to hit `κ`).

## Symbols
- `T`: a set of `ℒ`-sentences with some infinite model `𝔄`.
- `κ`: any cardinal `≥ max(ℵ₀, |ℒ|)`.

## Prerequisites (tsort edges into this node)
`compactness_fol`, `non_finite_axiomatizability`.

## Proof
Add `κ` fresh constants `{cᵢ : i < κ}` to `ℒ` and the axioms `cᵢ ≠ cⱼ` for
`i ≠ j`. Every **finite** subset of `T ∪ {cᵢ ≠ cⱼ}` mentions only finitely many
constants and is satisfied by the infinite model `𝔄` (interpret the finitely
many constants as distinct elements — possible because `𝔄` is infinite). By
`compactness_fol` the whole set has a model `𝔅`; `𝔅` has `≥ κ` elements (the
`cᵢ` are distinct). Reduct to `ℒ`, then `lowenheim_skolem_down` to a model of
size exactly `κ`.

## Constructive grade
`needs_full_classical` — via `compactness_fol` (Lindenbaum / ultrafilter) and,
for the "exactly `κ`" refinement, downward LS (choice).

## Lean status
`lean_status: cited`. Mathlib: `FirstOrder.Language.exists_model_card_eq` /
the upward LS lemmas.

## Type / well-formedness check
`well_formed`. Needs `𝔄` **genuinely infinite** — a theory all of whose models
are finite (e.g. "there are exactly 3 elements") has no infinite model, and the
theorem says nothing. `κ ≥ |ℒ|` is required (with `|ℒ|` constants you cannot
force fewer than `|ℒ|` elements away).

## Specialization / boundary cases
- `T` = theory of `(ℝ, +, ·, <)` (real closed fields): has real-closed fields of
  every infinite cardinality — countable ones (real algebraic numbers), and
  ones far bigger than `2^ℵ₀`.
- `T` = theory of an infinite group / an algebraically closed field of fixed
  characteristic: models of every infinite size.
- `T` = `PA`: non-standard models of every infinite cardinality.
- combined with downward LS ⇒ **`non_categoricity`**: no first-order `T` with an
  infinite model has models of only one infinite cardinality.

## Hypothesis-dropped counterexamples
- **`T` has only finite models**: "exactly 5 elements" — no infinite model, so
  no larger models; the hypothesis is essential.
- **`κ < |ℒ|`**: a language with `ℵ₁` constant symbols and axioms making them
  distinct has no model smaller than `ℵ₁`.
- **second-order logic**: second-order Peano arithmetic has an infinite model
  (`ℕ`) but **no** uncountable model — upward LS fails for SOL. First-order-ness
  is essential.

## Common misuse
Applying it to a theory whose models are all finite; forgetting the `|ℒ|` lower
bound on `κ`; expecting the large model to be "like" the original (it is only
elementarily equivalent — same first-order theory, wildly different structure);
using it in second-order logic.

## Related nodes (non-prerequisite)
- `companion`: `lowenheim_skolem_down`.
- `proved_using`: `compactness_fol`.
- `implies` (with downward LS): `non_categoricity`.
- `technique_shared_with`: `non_finite_axiomatizability` (the fresh-constants
  trick).

## Sources
[enderton_logic_2e] §2.6; [chiswell_hodges] ch. 6; [hodges_shorter] §3.1;
[vandalen_5e] §3.2.
