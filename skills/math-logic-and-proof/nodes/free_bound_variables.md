# free_bound_variables

## Type
definition  (epistemic status: `definition`; `constructive_grade: intuitionistic`)

## Statement
An **occurrence** of a variable `x` in a wff `φ` is **bound** if it lies within
the scope of a quantifier `∀x` or `∃x`; otherwise it is **free**. `FV(φ)` is the
set of variables with at least one free occurrence:

    FV(atomic) = variables in it
    FV(¬φ) = FV(φ);  FV(φ ∘ ψ) = FV(φ) ∪ FV(ψ)
    FV(∀x φ) = FV(∃x φ) = FV(φ) \ {x}

A variable can occur both free and bound in one wff (`P(x) ∧ ∀x Q(x)`).

## Symbols
- `FV(φ)`: the finite set of free variables; scope of `∀x`/`∃x` = the matrix.

## Prerequisites (tsort edges into this node)
`first_order_wff`, `quantifier_syntax`, `recursion_on_wff`.

## Content
The distinction that makes first-order syntax subtle. It underlies:
- **`sentence`** = wff with `FV(φ) = ∅`;
- **`substitution`** — replace *free* occurrences only;
- **`free_for`** — the no-capture condition (about `x`'s free occurrences vs the
  quantifiers of `φ`);
- **`coincidence_lemma`** — satisfaction depends only on `s ↾ FV(φ)`;
- **`eigenvariable_condition`** — "not free in the conclusion or open
  assumptions".

## Constructive grade
`intuitionistic` — `FV` is a computable recursion on `first_order_wff`.

## Lean status
`lean_status: cited`. In a de Bruijn representation (Mathlib) "free" = an index
`≥` the binding depth; there is no name to be free or bound, which sidesteps
capture entirely. Named-variable treatments carry `FV` explicitly.

## Type / well-formedness check
`well_formed`. **Occurrence** (a position) vs **variable** (the symbol): "`x` is
free in `φ`" means *some occurrence* is free; "`x` is bound in `φ`" that *some
occurrence* is bound — not mutually exclusive. The matrix `φ` of `∀x φ` has `x`
**free** (it is `∀x φ` where `x` is bound); reasoning about `φ` alone must
remember this.

## Specialization / boundary cases
- `x ∉ FV(φ)`: `∀x φ ≡ φ` (`vacuous_quantification`).
- `FV(φ) = ∅`: `φ` is a `sentence`; its truth is assignment-independent.
- **closed term substitution**: `φ[c/x]` — `c` has no variables, so no capture
  regardless of `φ`'s quantifiers.
- **α-renaming** (`alpha_equivalence`): changes which *names* are bound, not
  `FV`.

## Hypothesis-dropped counterexamples
- **confuse free/bound occurrence with the variable**: "`x` is bound in
  `P(x) ∧ ∀x Q(x)`" — only the second occurrence; the first is free, and a
  substitution `[t/x]` hits it.
- **treat the matrix as a sentence**: in proving `∀x φ` by `∀I`, forgetting `x`
  is genuinely free in `φ` (needs the eigenvariable condition).
- **de Bruijn confusion**: mixing named and indexed conventions.

## Common misuse
Saying "`x` is bound" when only one occurrence is; substituting for a bound
occurrence; forgetting the matrix has free variables; ignoring that a variable
can be both free and bound in one wff.

## Related nodes (non-prerequisite)
- `defines`: `sentence`.
- `feeds`: `substitution`, `free_for`, `alpha_equivalence`,
  `coincidence_lemma`, `eigenvariable_condition`.
- `sidestepped_by`: de Bruijn indices (Mathlib).

## Sources
[enderton_logic_2e] §2.1; [chiswell_hodges] §7.1; [vandalen_5e] §3.1.
