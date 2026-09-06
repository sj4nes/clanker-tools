# absorption

## Type
mathematical_identity  (epistemic status: `mathematical_identity`;
`constructive_grade: intuitionistic`)

## Statement
- `p ∧ (p ∨ q) ⊨⊨ p`
- `p ∨ (p ∧ q) ⊨⊨ p`

The two **absorption laws** of a lattice: combining `p` with something built
from `p` collapses back to `p`.

## Symbols
- `p`, `q`: wffs / atoms.

## Prerequisites (tsort edges into this node)
`logical_equivalence`.

## Proof
Term-mode, `intuitionistic`:
- `p ∧ (p ∨ q) → p`: `fun ⟨a, _⟩ => a`.
- `p → p ∧ (p ∨ q)`: `fun a => ⟨a, Or.inl a⟩`.
The `∨`-form is dual.

## Constructive grade
`intuitionistic` — lattice identities, valid in every Heyting algebra.

## Lean status
`lean_status: core`. `validation/proof-checks.lean`:
`absorption_and : (p ∧ (p ∨ q)) ↔ p` — term-mode, no axioms.

## Type / well-formedness check
`well_formed`, schematic. The `q` is genuinely irrelevant to the truth value —
useful as a **simplification** rewrite (delete a subformula) in normal-form and
circuit-minimisation contexts.

## Specialization / boundary cases
- `q = ⊤`: `p ∧ (p ∨ ⊤) ⊨⊨ p ∧ ⊤ ⊨⊨ p` — consistent.
- `q = p`: `p ∧ (p ∨ p) ⊨⊨ p ∧ p ⊨⊨ p` — via idempotence.
- **term rewriting**: absorption + idempotence + commutativity are the rewrite
  rules that shrink a Boolean expression; combined with distributivity and De
  Morgan they drive Quine–McCluskey / Karnaugh minimisation.
- lattice-theoretic: absorption is one of the four axioms defining a lattice
  (with `∧`, `∨` comm + assoc); it forces the two idempotence laws.

## Hypothesis-dropped counterexamples
Equivalences — nothing to drop. Instructive near-misses:
- `p ∧ (q ∨ r)` does **not** absorb (no shared `p`) — it *distributes*
  (`distributivity_prop`).
- `p ∨ (q ∧ r)` likewise distributes, does not absorb.
- `p → (p ∨ q)` is a tautology but `(p → (p ∨ q)) ⊭⊨ p` — absorption is about
  `∧`/`∨`, not `→`.

## Common misuse
Applying "absorption" when the inner formula does not actually contain the outer
`p` (that is distribution, not absorption); using it on `→`; forgetting it is an
*equivalence* so it can be applied in either direction (introduce or eliminate
the `∨ q` / `∧ q`).

## Related nodes (non-prerequisite)
- `derives_from` (as a consequence): follows from
  `commutativity_associativity_idempotence` + `distributivity_prop`, but is
  listed as an independent identity (lattice axiom).
- `feeds`: normal-form simplification; `conjunctive_normal_form` /
  `disjunctive_normal_form` clause reduction.
- `related`: lattice axioms, Boolean-function minimisation.

## Sources
[enderton_logic_2e] §1.2; [vandalen_5e] §1.2; [halmos_boolean].
