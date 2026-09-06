# semantic_consequence_fol

## Type
definition  (epistemic status: `definition`; `constructive_grade: n/a`)

## Statement
`Γ ⊨ φ` (first-order): for **every** structure `𝔄` and **every** assignment `s`,
if `𝔄 ⊨ γ [s]` for all `γ ∈ Γ` then `𝔄 ⊨ φ [s]`. Equivalently (for sentences):
every model of `Γ` is a model of `φ` — `Mod(Γ) ⊆ Mod({φ})`.

## Symbols
- `Γ`: a set of formulas (premises); `φ`: a formula.

## Prerequisites (tsort edges into this node)
`tarski_satisfaction`, `model`.

## Content
The first-order counterpart of `derivability_fol` (`Γ ⊢ φ`). `soundness_fol`:
`⊢ ⊆ ⊨`. `godel_completeness_theorem`: `⊨ ⊆ ⊢`. Together `Γ ⊨ φ ⟺ Γ ⊢ φ`.
Equivalent forms:
- `Γ ⊨ φ` iff `Γ ∪ {¬φ}` is unsatisfiable;
- `Γ ⊨ φ` iff (by `compactness_fol`) some **finite** `Γ₀ ⊆ Γ` has `Γ₀ ⊨ φ`;
- for finite `Γ`: `Γ ⊨ φ` iff `⊨ (⋀Γ → φ)` (validity).

## Constructive grade
`n/a` — quantifies over the proper class of structures. Establishing a specific
`Γ ⊨ φ` via the completeness route is `needs_full_classical`.

## Lean status
`lean_status: cited`. Mathlib: `T ⊨ φ` (`Theory.Models`). The propositional
analogue `Entails` is in `validation/proof-checks.lean`.

## Type / well-formedness check
`well_formed`. `Γ`, `φ` one language. **`Γ ⊨ φ` is a metastatement**, not a wff —
no nesting, no quantifying over it. The use–mention slip: `Γ ⊨ φ` vs the wff
`⋀Γ → φ` (related by validity, for **finite** `Γ` — for infinite `Γ` needs
`compactness_fol`).

## Specialization / boundary cases
- `Γ = ∅`: `⊨ φ` — `validity`.
- `φ ∈ Γ`: `Γ ⊨ φ` trivially; **monotone** (`Γ ⊨ φ`, `Γ ⊆ Δ` ⟹ `Δ ⊨ φ`);
  **transitive** (cut).
- `Γ` unsatisfiable: `Γ ⊨ φ` for **every** `φ` (vacuously — no model).
- open formulas: `Γ ⊨ φ` quantifies over assignments too (so free variables act
  "universally" but *shared* between premises and conclusion).

## Hypothesis-dropped counterexamples
- **check models of `φ` instead of `Γ`**: reverses it — `P(c) ⊨ ∃x P(x)` holds,
  `∃x P(x) ⊨ P(c)` does not.
- **infinite `Γ`, deduction-theorem form**: `⊨ (⋀Γ → φ)` is not a wff for
  infinite `Γ`; need `compactness_fol`.
- **treat free variables as existential**: `{P(x)} ⊨ ∀x P(x)`? — **no**; the
  free `x` is shared, so `{P(x)} ⊨ P(x)` but not `∀x P(x)` (this is the
  deduction-theorem free-variable subtlety).

## Common misuse
Writing `Γ ⊨ φ` as the wff `⋀Γ → φ`; checking the wrong side of the
implication; the free-variable trap (`{P(x)} ⊭ ∀x P(x)`); forgetting the vacuous
case for unsatisfiable `Γ`; the deduction-theorem form for infinite `Γ` without
compactness.

## Related nodes (non-prerequisite)
- `syntactic_counterpart`: `derivability_fol`.
- `related`: `soundness_fol`, `godel_completeness_theorem`, `compactness_fol`.
- `special_case`: `validity` (`Γ = ∅`), `logical_equivalence_fol`.
- `propositional`: `semantic_consequence`.

## Sources
[enderton_logic_2e] §2.2; [chiswell_hodges] ch. 5; [vandalen_5e] §3.1.
