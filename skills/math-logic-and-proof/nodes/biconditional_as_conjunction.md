# biconditional_as_conjunction

## Type
mathematical_identity  (epistemic status: `mathematical_identity`;
`constructive_grade: intuitionistic`)

## Statement
`(p ↔ q) ⊨⊨ (p → q) ∧ (q → p)`. The biconditional **is** the conjunction of the
two implications — in most treatments this is the *definition* of `↔`.

## Symbols
- `p`, `q`: wffs / atoms.

## Prerequisites (tsort edges into this node)
`logical_equivalence`.

## Proof
If `↔` is primitive: truth table (`p ↔ q` true iff `p`, `q` have the same value,
iff both implications hold). If `↔` is *defined* as `(p → q) ∧ (q → p)` (this
capsule's convention, `wff_syntax`): the identity is `rfl`. Term-mode:
`⟨fun h => ⟨h.mp, h.mpr⟩, fun ⟨a, b⟩ => ⟨a, b⟩⟩`.

## Constructive grade
`intuitionistic` — pure `∧`/`→` manipulation, no classical principle. `p ↔ q`
is constructively **stronger** than `(p → q) ∨ (q → p)` (which is a classical
tautology) — do not confuse the conjunction with the disjunction.

## Lean status
`lean_status: core`. `validation/proof-checks.lean`:
`biconditional_as_conj : (p ↔ q) ↔ ((p → q) ∧ (q → p))`. In Lean `Iff` is
literally the structure with fields `mp`, `mpr`, so this is `⟨_, _⟩`-level.

## Type / well-formedness check
`well_formed`. Both implications must have **the same** `p` and `q` — a proof
of `p → q` and `q → p'` for `p' ≠ p` does not give `p ↔ q`. `↔` binds loosest
(`conventions.md`), so `p ↔ q → r` parses as `p ↔ (q → r)`.

## Specialization / boundary cases
- `p = q`: `p ↔ p ⊨⊨ (p → p) ∧ (p → p) ⊨⊨ ⊤`.
- `q = ⊤`: `(p ↔ ⊤) ⊨⊨ p`.
- `q = ¬p`: `(p ↔ ¬p)` is a **contradiction** (`⊨⊨ ⊥`) — no assignment makes a
  formula equivalent to its own negation.
- chained: `p ↔ q ↔ r` — with associativity of `↔`, true iff an **even** number
  of `p, q, r` are false (the "`↔` is XNOR / parity" fact).
- **proof strategy**: `biconditional_proof` — prove the two conjuncts
  separately.

## Hypothesis-dropped counterexamples
An equivalence with both directions holding — no hypothesis to drop. But note
`(p ↔ q)` is strictly stronger than each of: `(p → q) ∨ (q → p)` (classical
tautology, no content), `(p ∧ q) ∨ (¬p ∧ ¬q)` (equivalent classically, needs
LEM to get from `↔`), `¬(p ⊕ q)` (equivalent classically).

## Common misuse
Proving one implication and asserting `↔`; confusing `(p → q) ∧ (q → p)` with
`(p → q) ∨ (q → p)`; mismatched `p`/`q` across the two directions; assuming
`p ↔ q` lets you *substitute* `q` for `p` everywhere (it does, via
`substitution_of_equivalents` — but that is a separate theorem, and fails inside
opaque contexts like quotation or modal operators, out of scope).

## Related nodes (non-prerequisite)
- `defines` (in this capsule): the connective `↔` (`wff_syntax`).
- `used_by`: `biconditional_proof`, `logical_equivalence` (which is `↔` at the
  meta level — "`⊨ p ↔ q`").
- `related`: XNOR / parity; `substitution_of_equivalents`.

## Sources
[enderton_logic_2e] §1.0–1.2; [vandalen_5e] §1.1; [chiswell_hodges] §2.1.
