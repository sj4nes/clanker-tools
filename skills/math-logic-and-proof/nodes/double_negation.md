# double_negation

## Type
mathematical_identity  (epistemic status: `mathematical_identity`; **split**:
`p → ¬¬p` is `intuitionistic`, `¬¬p → p` is `needs_DNE`)

## Statement
`¬¬p ⊨⊨ p` — a formula and its double negation are logically equivalent (have
the same truth value under every assignment). As two implications:
- `p → ¬¬p` — **intuitionistic**;
- `¬¬p → p` (double-negation **elimination**, DNE) — **classical**, one of the
  equivalent forms of excluded middle.

## Symbols
- `p`: a wff / propositional atom (`Wff`).

## Prerequisites (tsort edges into this node)
`logical_equivalence`.

## Proof
Truth table (2 rows): `¬¬p` and `p` agree. Proof-theoretically:
- `p → ¬¬p`: assume `p`, assume `¬p`, `⊥` by `¬E`; discharge — `fun hp hn => hn hp`.
- `¬¬p → p`: **not** derivable in minimal/intuitionistic ND. Adding it (or LEM,
  or `raa_rule`, or Peirce's law) to intuitionistic logic yields classical
  logic.

## Constructive grade
`needs_DNE` for the node as a whole (its `¬¬p → p` half). `dni` (`p → ¬¬p`) is
`intuitionistic`. In a Kripke model, `¬¬p` holds at a world `w` iff `p` holds at
some world reachable from every world reachable from `w` — strictly weaker than
`p` at `w`.

## Lean status
`lean_status: core`. `validation/proof-checks.lean`:
`dni : p → ¬¬p` (term-mode, no axioms) and
`dne : ¬¬p → p := Classical.byContradiction …` (`#print axioms` shows
`Classical.choice` — flagged).

## Type / well-formedness check
`well_formed`. `¬¬p` is `¬(¬p)`, a `Wff`; the equivalence is schematic in `p`
(holds for every wff, including open first-order formulas under an assignment).

## Specialization / boundary cases
- `p` **decidable** (e.g. an equality of naturals, a `Bool`): `¬¬p → p` holds
  intuitionistically — the classical caveat is vacuous. This is why arguments
  about `ℕ` rarely feel the difference.
- `¬¬¬p ⊨⊨ ¬p` (triple negation collapses) — **intuitionistic** in both
  directions (`¬` of `dni` + `dni` applied to `¬p`). Only the *first* double
  negation is classical.
- `p = q ∨ ¬q`: `¬¬(q ∨ ¬q)` is an intuitionistic theorem, but `q ∨ ¬q` is not —
  the exact gap.

## Hypothesis-dropped counterexamples
- **drop classical logic**: `¬¬(P ∨ ¬P) → (P ∨ ¬P)` is not intuitionistically
  provable; Kripke countermodel — two worlds `w₀ ⊑ w₁`, `P` false at `w₀`, true
  at `w₁`: `¬¬P` holds at `w₀` (P is not refutable) but `P` does not.
- there is no "small `p`" escape at the schematic level — it is exactly the
  decidability of `p` that governs whether DNE applies.

## Common misuse
Treating `¬¬p` and `p` as interchangeable in a constructive/type-theoretic
setting; using `¬¬p → p` and calling the proof constructive; forgetting that
`¬¬` **distributes over `∧`** intuitionistically but **not over `∨`**
(`¬¬(p ∨ q)` does not give `¬¬p ∨ ¬¬q`); the "double negation shift"
`(∀x ¬¬P x) → ¬¬∀x P x` is *not* intuitionistically valid.

## Related nodes (non-prerequisite)
- `equivalent_to`: `raa_rule` (over intuitionistic ND — `edges/relations.tsv`);
  excluded middle; Peirce's law.
- `feeds`: `contraposition` (its classical direction), `raa_rule`,
  `proof_by_contradiction`, `negation_normal_form`.
- `related`: the **double-negation (Glivenko / Gödel–Gentzen) translation** —
  `p` is classically provable iff `¬¬pᴺ` is intuitionistically provable.

## Sources
[vandalen_5e] §1.5, ch. 5 (Kripke semantics, the translation);
[enderton_logic_2e] §1.2; [chiswell_hodges] §2.4.
