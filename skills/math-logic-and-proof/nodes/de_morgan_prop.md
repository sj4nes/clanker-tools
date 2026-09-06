# de_morgan_prop

## Type
mathematical_identity  (epistemic status: `mathematical_identity`; **split** —
see grade)

## Statement
- `¬(p ∧ q) ⊨⊨ ¬p ∨ ¬q`
- `¬(p ∨ q) ⊨⊨ ¬p ∧ ¬q`

## Symbols
- `p`, `q`: wffs / atoms (`Wff`).

## Prerequisites (tsort edges into this node)
`logical_equivalence`, `implication_as_disjunction`.

## Proof
Truth tables (4 rows each) — both equivalences hold classically. Constructively:
- `¬(p ∨ q) ⟺ (¬p ∧ ¬q)`: **both directions intuitionistic**.
  `→`: `fun h => ⟨fun hp => h (Or.inl hp), fun hq => h (Or.inr hq)⟩`.
  `←`: `fun ⟨hp, hq⟩ h => h.elim hp hq`.
- `(¬p ∨ ¬q) → ¬(p ∧ q)`: **intuitionistic** (`cap_not_and_of_disj`).
- `¬(p ∧ q) → (¬p ∨ ¬q)`: **needs LEM** — case on `p`: if `p`, then `¬q` (else
  `p ∧ q`), give `Or.inr`; if `¬p`, give `Or.inl`.

## Constructive grade
`needs_LEM` for the node overall — its `¬(p∧q) → (¬p∨¬q)` component is
equivalent to **weak excluded middle** `¬p ∨ ¬¬p`. The `¬(p∨q)` law and three of
the four `∧`-law implications are `intuitionistic`. This is the propositional
template for the identical split in `quantifier_negation`
(`¬∀ → ∃¬` is `needs_LEM`, `¬∃ ↔ ∀¬` is `intuitionistic`).

## Lean status
`lean_status: core`. `validation/proof-checks.lean`: `not_or_iff` (term-mode,
no axioms), `not_and_iff` (`→` via `Classical.em`), `cap_not_and_of_disj`
(term-mode). `bc validation/instance-checks.bc` tabulates the 4-row agreement
with the grade note.

## Type / well-formedness check
`well_formed`. Schematic in `p`, `q` (any wffs, including first-order matrices
under an assignment). The negation must be driven **all the way in** and each
connective flipped — `¬(p ∧ q)` becomes `¬p ∨ ¬q`, not `¬p ∧ ¬q`.

## Specialization / boundary cases
- iterate: `¬(p ∧ q ∧ r) ⊨⊨ ¬p ∨ ¬q ∨ ¬r`.
- **infinitary / quantified**: `¬∀x P x ⊨⊨ ∃x ¬P x` (needs LEM),
  `¬∃x P x ⊨⊨ ∀x ¬P x` (intuitionistic) — `quantifier_negation`, same split.
- `p`, `q` **decidable**: the whole equivalence is intuitionistically valid.
- `q = ¬p`: `¬(p ∧ ¬p) ⊨⊨ ¬p ∨ ¬¬p` — the non-contradiction/weak-LEM pair.

## Hypothesis-dropped counterexamples
- **drop classical logic**: `¬(p ∧ ¬p)` is an intuitionistic theorem, but
  `¬p ∨ ¬¬p` is **not** — so `¬(p ∧ q) → (¬p ∨ ¬q)` fails. Kripke countermodel:
  one world forcing neither `p` nor `¬p`.
- the `¬(p ∨ q)` law and the converse `∧`-law have **no** hypothesis to drop —
  they are intuitionistically valid.

## Common misuse
Distributing `¬` without flipping the connective; assuming the whole thing is
constructive (only three of four `∧`-implications are); applying the
`needs_LEM` direction in a constructive proof and calling it done; swapping
quantifier **order** when negating (that is `quantifier_order`).

## Related nodes (non-prerequisite)
- `dual_of`: itself (the two laws are dual under `∧ ↔ ∨`, `⊤ ↔ ⊥`).
- `generalises_to`: `quantifier_negation`.
- `feeds`: `negation_normal_form`, `sheffer_stroke`, `duality_principle`,
  `truth_lemma_prop`, `proof_by_cases`.

## Sources
[enderton_logic_2e] §1.2; [vandalen_5e] §1.2 and ch. 5;
[chiswell_hodges] §2.4.
