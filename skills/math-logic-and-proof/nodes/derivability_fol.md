# derivability_fol

## Type
definition  (epistemic status: `definition`; `constructive_grade: split` —
`⊢` is calculus-neutral; classicality via `raa_rule` / Hilbert schema 3)

## Statement
`Γ ⊢ φ` (first-order) holds iff there is a derivation of `φ` from `Γ` in the
first-order calculus: `nd_derivation` extended by `nd_rules_quantifier` (with the
`eigenvariable_condition`) and `equality_axioms`; or, equivalently
(`nd_hilbert_equivalence` extended), the Hilbert calculus with
`hilbert_quantifier_axioms`. The choice of calculus is immaterial.

## Symbols
- `Γ`: a set of first-order formulas; `φ`: a formula.

## Prerequisites (tsort edges into this node)
`nd_derivation`, `nd_rules_quantifier`, `eigenvariable_condition`,
`equality_axioms`, `hilbert_quantifier_axioms`, `nd_hilbert_equivalence`.

## Content
The first-order syntactic consequence relation — the object of `soundness_fol`,
`godel_completeness_theorem`, `compactness_fol`, `consistency_fol`. Structural
properties (reflexivity, monotonicity, cut, **finite character**) carry over
from `derivability`. Finite character — a derivation cites finitely many
premises — is what makes `compactness_fol` fall out of completeness.

**First-order-specific**: the deduction theorem holds only with the free-variable
side condition (`{P(x)} ⊢ ∀x P(x)` but `⊬ P(x) → ∀x P(x)`); the two side
conditions (`free_for`, `eigenvariable_condition`) are part of what "a
derivation" means.

## Constructive grade
`split` — `Γ ⊢ φ` records "a derivation exists"; whether it is intuitionistic
depends on whether it uses `raa_rule` / Hilbert schema 3. `Γ ⊢ p ∨ ¬p` classically;
not intuitionistically.

## Lean status
`lean_status: cited`. `validation/proof-checks.lean` builds only the
**propositional** calculi (`Deriv`, `H`). Mathlib has a first-order proof system
with a completeness theorem — the reference for this node.

## Type / well-formedness check
`well_formed`. `Γ`, `φ` one language. Every use of `∀E`/`∃I` in a derivation
carries a discharged `free_for` obligation; every `∀I`/`∃E` an
`eigenvariable_condition`. `Γ ⊢ φ` is a **metastatement**, not a wff (the
use–mention slip vs `⋀Γ → φ`).

## Specialization / boundary cases
- `Γ = ∅`: `⊢ φ` — `φ` is **valid** (`validity`, by completeness).
- propositional reduct: `derivability`.
- `Γ` inconsistent: `Γ ⊢ φ` for every `φ` (`explosion_ex_falso`).
- `Γ` infinite: `Γ ⊢ φ` reduces to a finite sub-derivation — `compactness_fol`.

## Hypothesis-dropped counterexamples
- **drop the eigenvariable condition**: `{P(x)} ⊢ ∀x P(x)` derivable but not
  valid — `soundness_fol` fails.
- **drop `free_for` on `∀E`**: `∀x∃y(y≠x) ⊢ ∃y(y≠y)`.
- **omit the equality axioms**: `=` is not forced to behave; `x = x` unprovable.
- **treat `⊢` as `⊨` without soundness/completeness**: extensionally equal for
  classical FOL — but that is two theorems; for intuitionistic FOL
  `⊢ᵢ ⊊ ⊨_classical`.

## Common misuse
Skipping side conditions; the first-order deduction-theorem trap; writing
`Γ ⊢ φ` as `⋀Γ → φ`; assuming a proof exists from truth alone; forgetting
finite character.

## Related nodes (non-prerequisite)
- `semantic_counterpart`: `semantic_consequence_fol`.
- `abstracts`: first-order `nd_derivation` / `hilbert_derivation`.
- `feeds`: `soundness_fol`, `consistency_fol`, `godel_completeness_theorem`,
  `compactness_fol`, `undecidability_fol_validity`, `godel_incompleteness_first`.
- `propositional`: `derivability`.

## Sources
[enderton_logic_2e] §2.4; [chiswell_hodges] ch. 4; [vandalen_5e] ch. 3.
