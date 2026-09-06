# henkin_theory

## Type
construction  (epistemic status: `constructive_result`; `constructive_grade:
needs_LEM` countable / `needs_full_classical` uncountable)

## Statement
A **Henkin theory** is a set `T*` of `ℒ⁺`-sentences that is
1. **maximal consistent** (for every `ℒ⁺`-sentence `σ`, exactly one of `σ`,
   `¬σ` is in `T*`), and
2. has the **witness property**: whenever `∃x φ(x) ∈ T*`, there is a closed
   `ℒ⁺`-term `t` (in fact a Henkin constant) with `φ(t/x) ∈ T*`.

The construction: start from a consistent `ℒ`-theory `T`, apply
`henkin_constants` to get `T⁺` over `ℒ⁺`, then apply `lindenbaum_lemma_fol` to
get a maximal consistent `T* ⊇ T⁺`.

## Symbols
- `T*`: the Henkin theory (`Theory` over `ℒ⁺`).
- the witness for `∃x φ`: the Henkin constant `c_φ` (its axiom
  `(∃x φ) → φ(c_φ/x)` is in `T⁺ ⊆ T*`).

## Prerequisites (tsort edges into this node)
`henkin_constants`, `maximal_consistent_set`, `lindenbaum_lemma_fol`.

## Why maximality preserves the witness property
The Henkin axioms are in `T⁺ ⊆ T*`. If `∃x φ ∈ T*`, then by the Henkin axiom and
modus ponens (`T*` deductively closed, being maximal consistent), `φ(c_φ/x) ∈ T*`.
Lindenbaum adds no new existentials without their witnesses because it adds no
new **symbols** — every `ℒ⁺`-existential already had its constant from
`henkin_constants`.

## Properties of `T*` used downstream (`truth_lemma_fol`)
For every `ℒ⁺`-sentence `σ`:
- `¬σ ∈ T*` ⟺ `σ ∉ T*` (maximality + consistency);
- `σ ∧ τ ∈ T*` ⟺ `σ ∈ T*` and `τ ∈ T*`;
- `σ ∨ τ ∈ T*` ⟺ `σ ∈ T*` or `τ ∈ T*` (needs maximality: `quantifier_negation`
  / classical MCS reasoning);
- `∃x φ ∈ T*` ⟺ `φ(t/x) ∈ T*` for some closed term `t` (witness property).

These four are exactly the recursion clauses that make the term model's
satisfaction match membership in `T*`.

## Constructive grade
Inherits from `lindenbaum_lemma_fol`: `needs_LEM` (countable `ℒ`),
`needs_full_classical` (uncountable). The `∨` and `∃` clauses above are where
classical completeness of `T*` is used.

## Lean status
`lean_status: cited`. Mathlib: the `IsMaximal` + Henkin-witness bundle in
`FirstOrder.Language`'s completeness proof.

## Type / well-formedness check
`well_formed`. `T*` is over `ℒ⁺`, **not** `ℒ` — the reduct to `ℒ` is what
finally models the original `T`. "Witness property" quantifies over closed
`ℒ⁺`-terms (`term_syntax`), a `naive_collection`.

## Specialization / boundary cases
- `T` already a maximal consistent Henkin theory: `T* = T`.
- `T` = a complete theory with definable Skolem functions (e.g. a model's full
  theory in a Skolemised language): the term model is an elementary substructure
  of the model.
- countable `ℒ`: `T*` is a complete consistent theory in a countable language,
  and its term model is countable.

## Hypothesis-dropped counterexamples
- **maximal but not Henkin** (no witnesses): `T* = ` a complete consistent
  theory with `∃x φ ∈ T*` but no `φ(t/x)` for any closed `t` — the term model
  then fails `𝔐 ⊨ ∃x φ` even though `∃x φ ∈ T*`. Witness property is essential.
- **Henkin but not maximal**: the `¬` and `∨` clauses fail — `truth_lemma_fol`
  cannot recurse.
- **witnesses added but `T` inconsistent**: no `T*`.

## Common misuse
Believing the term model is a model of `T*` "by construction" without the truth
lemma (it is a *theorem*, `truth_lemma_fol`); forgetting `T*` lives in the
extended language; assuming `T*` is the theory of some pre-existing structure
(it becomes so only via the term model); conflating the witness constant with a
real object.

## Related nodes (non-prerequisite)
- `built_from`: `henkin_constants` + `lindenbaum_lemma_fol`.
- `feeds`: `term_model`, `truth_lemma_fol`, `godel_completeness_theorem`.
- `related`: a complete theory with the "existence property" (constructive
  analogue — intuitionistic theories).

## Sources
[enderton_logic_2e] §2.5; [chiswell_hodges] §5.3; [vandalen_5e] §3.1.
