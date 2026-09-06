# atomic_formula

## Type
definition  (epistemic status: `definition`; `constructive_grade: intuitionistic`)

## Statement
The **atomic formulas** of `ℒ` are:
- `R t₁ … tₙ` for an `n`-ary relation symbol `R ∈ ℒ` and terms `t₁, …, tₙ`;
- `t₁ = t₂` for terms `t₁`, `t₂` (equality is always available —
  `first_order_logic_with_equality`).

These are the base case of `first_order_wff` — the first-order analogue of
propositional atoms.

## Symbols
- `R`: a relation symbol; `t₁, …, tₙ`: terms.

## Prerequisites (tsort edges into this node)
`term_syntax`, `signature`, `first_order_logic_with_equality`.

## Content
An atomic formula is the smallest unit that carries a **truth value** (under a
`structure` + `assignment`): `𝔄 ⊨ R t₁ … tₙ [s]` iff
`(s̄(t₁), …, s̄(tₙ)) ∈ R^𝔄` (`tarski_satisfaction`, base clause); `𝔄 ⊨ t₁ = t₂ [s]`
iff `s̄(t₁) = s̄(t₂)`. **Literals** are atomic formulas and their negations
(the basis of first-order NNF / clauses).

## Constructive grade
`intuitionistic` — a decidable inductive base clause.

## Lean status
`lean_status: cited`. Mathlib: `FirstOrder.Language.BoundedFormula.rel` and
`.equal` are the atomic constructors.

## Type / well-formedness check
`well_formed`. `R` applied to **exactly** its arity many **terms** (not
formulas); `=` between **two terms**. `R t₁ … tₙ` is a **formula**, not a term —
it cannot be an argument to a function symbol. Equality is between terms of the
single sort.

## Specialization / boundary cases
- `ℒ = ∅`: the only atomic formulas are `t₁ = t₂` (with `t₁, t₂` variables or
  nothing else) — pure equality logic.
- 0-ary "relation symbols" = propositional atoms — recovering propositional
  logic as the quantifier-free, term-free fragment.
- `x = x` — the reflexivity instance; always true (`equality_axioms`).
- **equality-free FOL**: drop the `t₁ = t₂` clause — a variant where `=` is just
  another binary relation (not forced to be identity).

## Hypothesis-dropped counterexamples
- **arity mismatch**: `R(t)` for binary `R`.
- **relation symbol nested in a term**: `f(R t₁ t₂)` — `R t₁ t₂` is a formula.
- **`=` between a term and a formula**: ill-typed.
- **`=` not interpreted as identity** (equality-free variant): `equality_congruence`
  and the `term_model` construction fail.

## Common misuse
Confusing `R t₁ t₂` (formula) with `f t₁ t₂` (term); arity errors; using `=`
where the intended meaning is an equivalence relation (that needs a relation
symbol + axioms, not logical `=`); forgetting propositional atoms are the 0-ary
case.

## Related nodes (non-prerequisite)
- `built_from`: `term_syntax`, `signature`, `first_order_logic_with_equality`.
- `base_of`: `first_order_wff`.
- `analogue`: propositional atom (`wff_syntax`).
- `evaluated_by`: `tarski_satisfaction` (base clause).

## Sources
[enderton_logic_2e] §2.1; [chiswell_hodges] ch. 5; [vandalen_5e] §3.1.
