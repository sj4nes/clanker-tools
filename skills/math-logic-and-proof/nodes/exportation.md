# exportation

## Type
mathematical_identity  (epistemic status: `mathematical_identity`;
`constructive_grade: intuitionistic`)

## Statement
`((p ∧ q) → r) ⊨⊨ (p → (q → r))` — "currying" for propositions. A single
implication with a conjunctive antecedent is equivalent to a nested (curried)
implication.

## Symbols
- `p`, `q`, `r`: wffs / atoms.

## Prerequisites (tsort edges into this node)
`logical_equivalence`.

## Proof
Term-mode, `intuitionistic` in both directions:
- `→`: `fun h hp hq => h ⟨hp, hq⟩`.
- `←`: `fun h ⟨hp, hq⟩ => h hp hq`.
This is exactly the type isomorphism `(A × B → C) ≃ (A → B → C)` under
Curry–Howard.

## Constructive grade
`intuitionistic` — a definitional isomorphism of proof terms; holds in every
cartesian closed category / Heyting algebra.

## Lean status
`lean_status: core`. `validation/proof-checks.lean`:
`exportation : ((p ∧ q) → r) ↔ (p → q → r)` — term-mode, no axioms. It is also
implicit in every multi-hypothesis lemma statement in the file (Lean writes
`h1 → h2 → goal`, never `h1 ∧ h2 → goal`).

## Type / well-formedness check
`well_formed`, schematic. `→` is **right-associative** (`conventions.md`), so
`p → q → r` parses as `p → (q → r)` — the identity would be false read as
`(p → q) → r`. This parenthesisation convention is what makes the curried form
the natural one.

## Specialization / boundary cases
- `n`-ary: `((p₁ ∧ … ∧ pₙ) → r) ⊨⊨ (p₁ → p₂ → … → pₙ → r)` — the standard way a
  theorem with `n` hypotheses is stated.
- `r = ⊥`: `¬(p ∧ q) ⊨⊨ (p → ¬q)` — a genuinely useful special case (and note
  `(p → ¬q) ⊨⊨ (q → ¬p)` by commutativity of `∧`, giving a cheap
  contraposition-like move that is **fully intuitionistic**).
- the `deduction_theorem` iterated is the proof-theoretic counterpart:
  `Γ, p, q ⊢ r ⟺ Γ ⊢ p → q → r`.

## Hypothesis-dropped counterexamples
Equivalence, both directions intuitionistic — nothing to drop. The near-miss:
`((p ∨ q) → r) ⊨⊨ (p → r) ∧ (q → r)` — a *different* law (disjunctive
antecedent gives a **conjunction** of implications, not a nested one); confusing
the two is common.

## Common misuse
Reading `p → q → r` as `(p → q) → r`; expecting a disjunctive antecedent to
curry the same way (it splits into a conjunction instead); thinking exportation
needs classical logic (it is the most constructive identity in the block).

## Related nodes (non-prerequisite)
- `related`: `deduction_theorem` (proof-theoretic analogue); Curry–Howard
  currying `(A × B → C) ≃ (A → B → C)`.
- `contrast`: `((p ∨ q) → r) ⊨⊨ (p → r) ∧ (q → r)` (disjunctive antecedent).
- `feeds`: the standard multi-hypothesis theorem-statement form used throughout
  the capsule.

## Sources
[enderton_logic_2e] §1.2; [vandalen_5e] §1.2; Sørensen & Urzyczyn,
*Lectures on the Curry–Howard Isomorphism* (currying).
