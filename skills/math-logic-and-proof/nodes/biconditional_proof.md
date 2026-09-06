# biconditional_proof

## Type
definition  (epistemic status: `definition`; `constructive_grade: intuitionistic`)

## Statement
To prove `P ↔ Q`: prove `P → Q` and prove `Q → P` separately, then combine.
Since `(P ↔ Q) ⊨⊨ (P → Q) ∧ (Q → P)` (`biconditional_as_conjunction`), the two
implications together *are* the biconditional.

## Symbols
- `P`, `Q`: formulas.
- the two lemmas: `P → Q` ("⟹", necessity) and `Q → P` ("⟸", sufficiency).

## Prerequisites (tsort edges into this node)
`biconditional_as_conjunction`, `direct_proof`.

## Content
`∧I` applied to two `direct_proof`s (or a `direct_proof` and a
`proof_by_contrapositive`, etc. — the two directions may use different
strategies). For a chain `P₁ ↔ P₂ ↔ … ↔ Pₙ` one may instead prove a cycle of
implications `P₁ → P₂ → … → Pₙ → P₁`, which establishes all pairwise
equivalences with `n` implications instead of `n(n−1)`.

## Constructive grade
`intuitionistic` — `∧I` and the unfolding `↔` = `(→) ∧ (←)` are minimal-logic.
The grade of a concrete `biconditional_proof` is the max of the grades of its
two halves: `P ↔ Q` is only as constructive as its harder direction.

## Lean status
`lean_status: core`. Every `⟨mp, mpr⟩` / `constructor` on an `Iff` goal in
`validation/proof-checks.lean` is this: `not_or_iff`, `impl_iff_or`,
`contrapose_iff`, `exportation`, `not_exists_iff`, `not_and_iff`.

## Type / well-formedness check
`well_formed`. Both directions must have **the same** `P` and `Q` — a frequent
error is proving `P → Q` and `Q → P'` for a subtly different `P'` (e.g. `Q`
stated with `≤` in one direction and `<` in the other). For a cycle proof, the
cycle must actually close (return to the start node).

## Specialization / boundary cases
- `P = Q`: `P ↔ P` is `biconditional_as_conjunction` of two `direct_proof`s of
  `P → P` — trivial.
- "the following are equivalent" (TFAE) lists: the cycle-of-implications form.
- definitional equivalences: one direction is often "unfold the definition",
  the other has the content.

## Where it fails / traps
- **proving only one direction** and asserting the biconditional — the single
  most common gap; `P → Q` alone is not `P ↔ Q`.
- **circular cycle proof that does not close**: `P₁ → P₂ → P₃` proves
  `P₁ → P₃` but nothing about `P₃ → P₁`.
- **using `P ↔ Q` as a hypothesis in proving one of its own halves**.

## Common misuse
Skipping the "obvious" direction; mismatched `P`/`Q` between directions;
assuming a one-directional lemma is bidirectional when later citing it.

## Related nodes (non-prerequisite)
- `derives_from`: `biconditional_as_conjunction` + `direct_proof`.
- `uses`: `direct_proof`, `proof_by_contrapositive`, `proof_by_contradiction`
  (either half, independently).
- `related`: `uniqueness_proof` (also a "two obligations" pattern).

## Sources
[velleman_3e] §3.4; [hammack_bop] ch. 7.
