# implication_as_disjunction

## Type
mathematical_identity  (epistemic status: `mathematical_identity`; **split**:
`←` intuitionistic, `→` `needs_LEM`)

## Statement
`(p → q) ⊨⊨ (¬p ∨ q)` — material implication is a disjunction. Also
`¬(p → q) ⊨⊨ (p ∧ ¬q)`.

## Symbols
- `p`, `q`: wffs / atoms.

## Prerequisites (tsort edges into this node)
`logical_equivalence`.

## Proof
Truth table: `p → q` is false only at `p = T, q = F`, exactly where `¬p ∨ q` is
false.
- `(¬p ∨ q) → (p → q)`: **intuitionistic** — `rintro (hp | hq) hpp` then
  `absurd hpp hp` / `hq`.
- `(p → q) → (¬p ∨ q)`: **needs LEM** — case on `p`: if `p`, `Or.inr (h p)`; if
  `¬p`, `Or.inl`.

## Constructive grade
`needs_LEM` for the node (its `→` half). `impl_iff_or`'s `←` direction is
`intuitionistic`. The `¬(p→q) ⊨⊨ p ∧ ¬q` form: `←` intuitionistic,
`→` needs LEM (it is `de_morgan` on `¬(¬p ∨ q)` plus DNE on the `p`).

## Lean status
`lean_status: core`. `validation/proof-checks.lean`:
`impl_iff_or : (p → q) ↔ (¬p ∨ q)` — `constructor`, `→` via `Classical.em`,
`←` term-mode.

## Type / well-formedness check
`well_formed`, schematic in `p`, `q`. Material implication (this identity) is
**not** the same as entailment `⊨` or derivability `⊢` — `p → q` is a wff,
`p ⊨ q` / `p ⊢ q` are metastatements; conflating them is the "paradoxes of
material implication" confusion.

## Specialization / boundary cases
- `q = ⊥`: `(p → ⊥) ⊨⊨ (¬p ∨ ⊥) ⊨⊨ ¬p` — the definition of `¬p` as `p → ⊥`.
- `p = ⊥`: `(⊥ → q) ⊨⊨ (¬⊥ ∨ q) ⊨⊨ ⊤` — **ex falso**, and this direction is
  intuitionistic (`vacuous_trivial_proof`).
- `p = ⊤`: `(⊤ → q) ⊨⊨ q`.
- `p` decidable: the whole equivalence is intuitionistically valid.

## Hypothesis-dropped counterexamples
- **drop classical logic**: `(p → q) → (¬p ∨ q)` fails — take `q = p`:
  `(p → p)` is a theorem, but `¬p ∨ p` is not intuitionistically provable. So
  the `→` direction is exactly as strong as LEM.
- the `←` direction and the `q = ⊥` / `p = ⊥` specializations survive
  constructively.

## Common misuse
Rewriting `p → q` as `¬p ∨ q` inside a constructive proof; confusing material
implication with entailment (`p → q` can be vacuously true while `p ⊨ q` is a
substantive claim); using `¬(p → q) ⟹ p` (needs LEM) casually; forgetting
`(p → q) ∨ (q → p)` is a *classical* tautology with no constructive content.

## Related nodes (non-prerequisite)
- `feeds`: `de_morgan_prop` (proof route), `negation_normal_form` (eliminate
  `→`), `vacuous_trivial_proof`, `contraposition`.
- `related`: the paradoxes of material implication;
  relevance logic (drops this identity — out of scope).

## Sources
[enderton_logic_2e] §1.2; [vandalen_5e] §1.2; [chiswell_hodges] §2.4.
