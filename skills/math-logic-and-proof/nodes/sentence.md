# sentence

## Type
definition  (epistemic status: `definition`; `constructive_grade: intuitionistic`)

## Statement
A **sentence** (closed formula) is a `first_order_wff` `σ` with `FV(σ) = ∅` — no
free variables. Its truth in a `structure` `𝔄` is **assignment-independent**:
`𝔄 ⊨ σ [s]` has the same value for every `s`, written simply `𝔄 ⊨ σ`.

## Symbols
- `σ`, `τ`: sentences.

## Prerequisites (tsort edges into this node)
`free_bound_variables`.

## Content
Sentences are what **theories** are made of (`model`, `semantic_consequence_fol`,
`consistency_fol`, `henkin_theory`). Every wff `φ(x₁, …, xₙ)` has:
- **universal closure** `∀x₁ … ∀xₙ φ` — valid iff `φ` is valid;
- **existential closure** `∃x₁ … ∃xₙ φ` — satisfiable iff `φ` is satisfiable.

`𝔄 ⊨ σ` well-defined for sentences is a corollary of `coincidence_lemma`
(truth depends only on `s ↾ FV(σ) = s ↾ ∅`).

## Constructive grade
`intuitionistic` — `FV(σ) = ∅` is a decidable property.

## Lean status
`lean_status: cited`. Mathlib: `FirstOrder.Language.Sentence` = a
`BoundedFormula` with `0` free variables (the de Bruijn context is empty).

## Type / well-formedness check
`well_formed`. `FV(σ) = ∅` — bound variables are fine, free ones forbidden. A
sentence still has quantifier structure; "closed" refers only to free variables.
`𝔄 ⊨ σ` is a `Prop` (no assignment parameter).

## Specialization / boundary cases
- `∀x (x = x)` — a valid sentence.
- `∃x (x = x)` — valid (nonempty domain); false under free logic.
- a **quantifier-free** sentence: built from atomic `sentences` (relation
  symbols applied to closed terms) — its truth is a finite check in a finite
  structure.
- `Th(𝔄)` — the set of all sentences true in `𝔄`; a **complete** consistent
  theory.

## Hypothesis-dropped counterexamples
- **a wff with a free variable used as a "sentence"**: `P(x)` — its truth in `𝔄`
  depends on `s(x)`; "`𝔄 ⊨ P(x)`" is ambiguous (some conventions read it as the
  universal closure, a trap).
- **`∀I` on a formula, treating the matrix as closed**: forgetting the free
  variable requires the eigenvariable condition.

## Common misuse
Calling a formula with free variables a sentence; writing "`𝔄 ⊨ φ`" for open
`φ` without saying which closure / assignment; assuming "closed" means "no
quantifiers"; forgetting existential closure preserves satisfiability, universal
closure preserves validity (not vice versa).

## Related nodes (non-prerequisite)
- `defined_from`: `free_bound_variables`.
- `assemble_into`: `model`, `semantic_consequence_fol`, `consistency_fol`,
  `henkin_theory`.
- `related`: universal / existential closure; `Th(𝔄)`.

## Sources
[enderton_logic_2e] §2.2; [chiswell_hodges] ch. 5; [vandalen_5e] §3.1.
