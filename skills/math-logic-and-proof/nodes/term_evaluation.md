# term_evaluation

## Type
definition  (epistemic status: `definition`; `constructive_grade: n/a` —
`naive_collection`)

## Statement
The **value** `s̄(t)` (also `t^{𝔄,s}`, `⟦t⟧`) of a term `t` in a structure `𝔄`
under an assignment `s`, by recursion on term structure:

    s̄(x)            = s(x)                          (x a variable)
    s̄(c)            = c^𝔄                           (c a constant)
    s̄(f t₁ … tₙ)    = f^𝔄( s̄(t₁), …, s̄(tₙ) )        (f an n-ary function symbol)

`s̄(t) ∈ |𝔄|` — a term always denotes a domain **element**, never a truth value.

## Symbols
- `s̄(t)`: the value; `s`: an `assignment`; `𝔄`: a `structure`.

## Prerequisites (tsort edges into this node)
`term_syntax`, `assignment`, `structure`, `inductive_definition`.

## Content
The first-order analogue of "look up the atom in `v`", one layer deeper: the
base case is `s(x)` / `c^𝔄`, the recursive case applies the interpreted
function. It feeds the **atomic clause** of `tarski_satisfaction`
(`𝔄 ⊨ R t₁ … tₙ [s]` iff `(s̄(t₁), …, s̄(tₙ)) ∈ R^𝔄`) and the **term-model
evaluation lemma** (`t^𝔐 = [t]`).

## Constructive grade
`n/a` — evaluates into a `naive_collection` domain.

## Lean status
`lean_status: cited`. Mathlib: `FirstOrder.Language.Term.realize`. Not in
`validation/proof-checks.lean`.

## Type / well-formedness check
`well_formed`. Well-founded recursion on **term structure** (unique readability
of terms). Each `f^𝔄` is total, so `s̄(t)` is defined for every term and every
`s` (`s` total). Codomain `|𝔄|` throughout. **Key lemma** (used everywhere):
`s̄(u[t/x]) = (s(x ↦ s̄(t)))‾(u)` — evaluating a substituted term = evaluating
under the updated assignment.

## Specialization / boundary cases
- **closed term** `t`: `s̄(t)` is `s`-independent — `t^𝔄`.
- **variable**: `s̄(x) = s(x)` — the base case.
- **term model**: `t^𝔐 = [t]` (each closed term denotes its own `≈`-class).
- `ℒ_arith`, `𝔄 = ℕ`: `s̄(S(S(0))) = 2`, `s̄(x + S 0) = s(x) + 1`.

## Hypothesis-dropped counterexamples
- **partial `f^𝔄`**: `s̄(f t₁ … tₙ)` undefined when the arguments land outside
  `dom(f^𝔄)`.
- **`s` undefined at a variable of `t`**: value undefined.
- **treat an atomic formula as a term**: `s̄(R t₁ t₂)` is a category error — `R
  t₁ t₂` has no domain value, it has a truth value.

## Common misuse
Confusing `s̄(t)` (an element) with `𝔄 ⊨ φ [s]` (a truth value); forgetting the
substitution lemma for terms; assuming closed terms need an assignment;
partial function interpretations.

## Related nodes (non-prerequisite)
- `feeds`: `tarski_satisfaction` (atomic clause), `term_model`,
  `substitution_lemma_semantic`.
- `propositional_shadow`: `v(p)` (the atom lookup).
- `analogue`: `truth_value_recursion` (one layer up, into `Bool`).

## Sources
[enderton_logic_2e] §2.2; [chiswell_hodges] ch. 5; [vandalen_5e] §3.1.
