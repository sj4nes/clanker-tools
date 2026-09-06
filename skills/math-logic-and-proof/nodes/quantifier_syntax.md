# quantifier_syntax

## Type
definition  (epistemic status: `definition`; `constructive_grade: intuitionistic`
as syntax)

## Statement
Two variable-binding formation rules: if `φ` is a first-order wff and `x` a
variable, then `∀x φ` ("for all `x`, `φ`") and `∃x φ` ("there exists `x` such
that `φ`") are first-order wffs. `x` becomes **bound** in `∀x φ` / `∃x φ`; its
**scope** is `φ`.

## Symbols
- `∀`, `∃`: the quantifier symbols; `x`: the bound variable; `φ`: the matrix.

## Prerequisites (tsort edges into this node)
`symbol`.

## Content
The single feature separating first-order from propositional logic. Both `∀` and
`∃` are given **primitive** formation rules (not one defined from the other) —
this avoids the `∀`/`∃` definitional cycle (`edges/cycles.md`); `exists_forall_duality`
then proves `∃x φ ≡ ¬∀x ¬φ` as a **theorem**, so the intuitionistic reading is
also available. Binding introduces `free_bound_variables`, `substitution`'s
capture concern (`free_for`), `alpha_equivalence`, and the eigenvariable
conditions of `nd_rules_quantifier`.

## Constructive grade
`intuitionistic` — as syntax. The **laws** governing quantifiers split:
`¬∃ ↔ ∀¬` is intuitionistic, `¬∀ ↔ ∃¬` is `needs_LEM` (`quantifier_negation`).

## Lean status
`lean_status: cited`. Mathlib: `BoundedFormula.all` / `.ex` (de Bruijn-indexed
binders). In Lean's own logic, `∀ x, p x` / `∃ x, p x` are the built-in binders
(`Pi` type / `Exists`).

## Type / well-formedness check
`well_formed`. `∀x`, `∃x` bind a **variable**, not a term or a formula. Nested
quantifiers on the **same** variable (`∀x ∀x φ`) are allowed but the inner one
shadows the outer (the outer becomes vacuous — `vacuous_quantification`).
Quantifier **rank** (max nesting depth) is a `formula_complexity` measure
driving `prenex_normal_form`, `coincidence_lemma`, `truth_lemma_fol`.

## Specialization / boundary cases
- `x` not free in `φ`: `∀x φ ≡ φ ≡ ∃x φ` (nonempty domain —
  `vacuous_quantification`).
- bounded quantifiers `∀x (P x → …)`, `∃x (P x ∧ …)`: abbreviations, not new
  syntax.
- **∃!** (unique existence): `∃x (φ ∧ ∀y (φ[y/x] → y = x))` — an abbreviation
  (`uniqueness_proof`).
- **guarded / restricted quantification**, **generalized quantifiers**
  ("most", "infinitely many"): extensions, out of scope.

## Hypothesis-dropped counterexamples
- **quantify a term** (`∀(f x) φ`): ill-formed — only variables bind.
- **second-order quantification** (`∀R φ` over relations): a different logic
  (SOL) — no complete proof system (`godel_completeness_theorem` fails).
- **empty domain** (free logic): `∀x φ` vacuously true, `∃x φ` false — breaks
  the `∀`/`∃` duality; this capsule fixes nonempty domains (`objects.md`).

## Common misuse
Binding a term instead of a variable; forgetting that `∀`/`∃` on a
non-occurring variable is vacuous; second-order quantification by analogy;
assuming empty-domain semantics; swapping `∀x∃y` and `∃y∀x` (`quantifier_order`).

## Related nodes (non-prerequisite)
- `feeds`: `first_order_wff`, `free_bound_variables`, `substitution`,
  `nd_rules_quantifier`, `tarski_satisfaction` (the `∀`/`∃` clauses).
- `governed_by`: `quantifier_negation`, `quantifier_order`,
  `quantifier_distribution`, `exists_forall_duality`.
- `contrast`: second-order / generalized quantifiers.

## Sources
[enderton_logic_2e] §2.1; [chiswell_hodges] ch. 5; [vandalen_5e] §3.1.
