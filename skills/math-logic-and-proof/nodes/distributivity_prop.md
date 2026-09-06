# distributivity_prop

## Type
mathematical_identity  (epistemic status: `mathematical_identity`;
`constructive_grade: intuitionistic`)

## Statement
- `p ∧ (q ∨ r) ⊨⊨ (p ∧ q) ∨ (p ∧ r)`
- `p ∨ (q ∧ r) ⊨⊨ (p ∨ q) ∧ (p ∨ r)`

`∧` and `∨` each distribute over the other — the propositional-logic instance of
a **distributive lattice** (indeed a Boolean algebra).

## Symbols
- `p`, `q`, `r`: wffs / atoms.

## Prerequisites (tsort edges into this node)
`logical_equivalence`.

## Proof
Truth tables (8 rows each), or term-mode. Both laws and both directions are
**intuitionistic**:
- `p ∧ (q ∨ r) → (p ∧ q) ∨ (p ∧ r)`: `fun ⟨a, bc⟩ => bc.elim (fun b => Or.inl
  ⟨a, b⟩) (fun c => Or.inr ⟨a, c⟩)`.
- converse: `fun h => h.elim (fun ⟨a, b⟩ => ⟨a, Or.inl b⟩) …`.
The `∨`-over-`∧` law follows by the same pattern (or by duality).

## Constructive grade
`intuitionistic` — no `Classical`. `∧`/`∨` distributivity holds in every Heyting
algebra, not just Boolean ones (unlike `de_morgan_prop`'s `∧`-law or
`double_negation`).

## Lean status
`lean_status: core`. `validation/proof-checks.lean`:
`distrib_and_or : (p ∧ (q ∨ r)) ↔ ((p ∧ q) ∨ (p ∧ r))` — term-mode, no axioms.

## Type / well-formedness check
`well_formed`, schematic in `p`, `q`, `r`. Note it is `∧` over `∨` *and* `∨`
over `∧` — arithmetic intuition (where `·` distributes over `+` but not `+`
over `·`) is misleading here; both hold.

## Specialization / boundary cases
- `r = ⊥`: `p ∧ (q ∨ ⊥) ⊨⊨ (p ∧ q) ∨ (p ∧ ⊥) ⊨⊨ p ∧ q` — sanity check.
- `q = r`: `p ∧ (q ∨ q) ⊨⊨ (p ∧ q) ∨ (p ∧ q)` — with idempotence, `p ∧ q`.
- **finitary → arbitrary**: `p ∧ ⋁ᵢ qᵢ ⊨⊨ ⋁ᵢ (p ∧ qᵢ)` (and the dual) lift the
  law to indexed disjunctions/conjunctions — used in the quantifier
  distribution laws (`∃x (P ∧ Q x) ⊨⊨ P ∧ ∃x Q x` when `x ∉ FV(P)`).
- the engine of **CNF/DNF conversion** (`conjunctive_normal_form`,
  `disjunctive_normal_form`): repeatedly distribute to push one connective
  outward.

## Hypothesis-dropped counterexamples
Every hypothesis is essential in the sense that the law is an *equivalence*
(both directions hold); there is no hypothesis to drop. Contrast: the
**quantifier** analogues are one-directional —
`∀x (P x ∨ Q x)` does **not** give `(∀x P x) ∨ (∀x Q x)`
(`quantifier_distribution`), and `∃x (P x ∧ Q x)` does **not** give
`(∃x P x) ∧ (∃x Q x)`.

## Common misuse
Assuming only one of the two laws holds (both do); expecting the *quantifier*
distribution to be an equivalence (it is not); forgetting the side condition
`x ∉ FV(P)` when pulling `P` past a quantifier in the infinitary form; treating
non-classical logics as still distributive when they may not be (quantum logic
drops distributivity — out of scope).

## Related nodes (non-prerequisite)
- `feeds`: `conjunctive_normal_form`, `disjunctive_normal_form`.
- `dual_of`: itself (the two laws swap under `∧ ↔ ∨`).
- `contrast`: `quantifier_distribution` (one-directional).
- `related`: distributive lattice / Boolean algebra structure.

## Sources
[enderton_logic_2e] §1.2; [vandalen_5e] §1.2; [chiswell_hodges] §2.4.
