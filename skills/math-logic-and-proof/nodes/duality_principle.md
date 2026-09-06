# duality_principle

## Type
proposition  (epistemic status: `proposition`; `constructive_grade: intuitionistic`)

## Statement
For a wff `φ` built from atoms, `¬`, `∧`, `∨`, `⊤`, `⊥`, let `φ^∂` be the
**dual**: swap `∧ ↔ ∨` and `⊤ ↔ ⊥` throughout (leaving atoms and `¬` alone).
Then

    φ^∂(p₁, …, pₙ)   ⊨⊨   ¬ φ(¬p₁, …, ¬pₙ).

Consequences: (i) if `φ ≡ ψ` then `φ^∂ ≡ ψ^∂`; (ii) if `⊨ φ` then `⊨ ¬(φ^∂)`
i.e. `φ^∂` is a contradiction; (iii) every Boolean-algebra identity comes in a
dual pair.

## Symbols
- `φ`: a wff in the `{¬, ∧, ∨, ⊤, ⊥}` fragment (no `→`, `↔` — eliminate them
  first via `implication_as_disjunction`, `biconditional_as_conjunction`).
- `φ^∂`: its dual.

## Prerequisites (tsort edges into this node)
`logical_equivalence`, `de_morgan_prop`.

## Proof
Structural induction on `φ`, with `de_morgan_prop` at the connective steps:
`(φ ∧ ψ)^∂ = φ^∂ ∨ ψ^∂` and `¬((φ ∧ ψ)(¬p⃗)) ≡ ¬(φ(¬p⃗)) ∨ ¬(ψ(¬p⃗))`
(De Morgan) `≡ φ^∂(p⃗) ∨ ψ^∂(p⃗)` (IH). Atoms: `p^∂ = p` and `¬(¬p) ≡ p`
(`double_negation`). `⊤^∂ = ⊥`, `¬(⊤) ≡ ⊥`.

## Constructive grade
`intuitionistic` — the induction uses only the **intuitionistically valid**
directions of De Morgan (`¬(p ∨ q) ≡ ¬p ∧ ¬q`, and the constructive halves of
the `∧`-law) together with `double_negation` on **atoms** (where `¬¬p → p` may
still need LEM if the atom is undecided — so strictly the atom step is
`needs_LEM` at the schematic level, `intuitionistic` for decidable atoms). The
node is listed `intuitionistic` because the *pattern* (swap connectives) is
purely syntactic; the semantic equivalence inherits De Morgan's grade.

## Lean status
`lean_status: cited`. Not a named theorem in `validation/proof-checks.lean`
(it needs a `dualize : Wff → Wff` function and the induction). The engine —
`de_morgan_prop` — **is** checked (`not_or_iff`, `not_and_iff`). `bc
validation/instance-checks.bc` can exhibit a dual pair by truth table.

## Type / well-formedness check
`well_formed` for the `{¬, ∧, ∨, ⊤, ⊥}` fragment. `→` and `↔` have **no
self-contained dual** — they must be rewritten first. The dual is a syntactic
operation on the parse tree (`wff_unique_readability` makes it well-defined).

## Specialization / boundary cases
- **lattice / Boolean-algebra identities**: `p ∧ (p ∨ q) ≡ p` dualizes to
  `p ∨ (p ∧ q) ≡ p` — the two `absorption` laws; the two `distributivity_prop`
  laws; the two `de_morgan_prop` laws; comm/assoc of `∧` ↔ comm/assoc of `∨`.
  Prove one, get the other free.
- **self-dual** formulas: `φ ≡ φ^∂` — e.g. `(p ∧ q) ∨ (q ∧ r) ∨ (r ∧ p)`
  (majority) up to the atom-negation.
- `⊨ φ` ⟺ `φ^∂` unsatisfiable — the tautology/contradiction dual pair.

## Hypothesis-dropped counterexamples
- **`φ` contains `→`**: `(p → q)^∂` is undefined; `p → q ≡ ¬p ∨ q`, whose dual is
  `¬p ∧ q ≡ ¬(p ∨ ¬q)` — you must eliminate `→` first.
- **forget to negate the atoms**: `φ^∂(p⃗)` alone is **not** `¬φ(p⃗)` in general
  (e.g. `φ = p`: `φ^∂ = p ≢ ¬p`). The atom negation is part of the statement.
- **apply to a non-Boolean logic**: intuitionistic logic is **not** self-dual
  (`∧`/`∨` and `⊤`/`⊥` do not swap cleanly — there is no `¬¬` collapse), so the
  principle fails.

## Common misuse
Dualizing a formula with `→`/`↔` still in it; omitting the atom negation;
claiming `φ^∂ ≡ ¬φ` (true only after also negating atoms); using duality in
intuitionistic or other non-self-dual logics.

## Related nodes (non-prerequisite)
- `uses`: `de_morgan_prop`, `double_negation`.
- `pairs`: the two `absorption`, `distributivity_prop`, `de_morgan_prop` laws;
  `tautology` / `contradiction_unsat`.
- `related`: Boolean-algebra duality; the order-reversal of a lattice.

## Sources
[enderton_logic_2e] §1.2; [halmos_boolean]; [chiswell_hodges] §2.4.
