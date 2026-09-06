# tautology

## Type
definition  (epistemic status: `definition`; `constructive_grade: intuitionistic`
as a definition; deciding it for an infinite atom set involves `∀v`)

## Statement
A wff `φ` is a **tautology** (`⊨ φ`, valid) iff `v ⊨ φ` for **every**
truth assignment `v` — `⟦φ⟧_v = T` for all `v`.

## Symbols
- `φ`: a wff.
- `⊨ φ`: "`φ` is a tautology" (no left operand — contrast `Γ ⊨ φ`,
  `semantic_consequence`).

## Prerequisites (tsort edges into this node)
`truth_table`, `satisfaction`.

## Content
The semantic notion of "logically true". By `post_completeness_theorem`,
`⊨ φ` iff `⊢ φ` (a derivation exists) — so tautology = propositional theorem.
By `tautology_decidable`, `⊨ φ` is decidable (finite `truth_table`).

Relations: `⊨ φ` iff `¬φ` is a `contradiction_unsat`; `φ ⊨⊨ ψ`
(`logical_equivalence`) iff `⊨ (φ ↔ ψ)`; `Γ ⊨ ψ` for finite `Γ` iff
`⊨ (⋀Γ → ψ)`.

## Constructive grade
`intuitionistic` **as a definition**. But: `φ` being a *classical* tautology
does not mean `φ` is *intuitionistically provable* — `p ∨ ¬p` and `¬¬p → p` are
tautologies with no intuitionistic proof. The `prop_laws` split-grade nodes are
exactly the tautologies whose *derivation* needs LEM/DNE.

## Lean status
`lean_status: core` (the predicate) / `instance` (deciding a concrete `φ`).
`validation/proof-checks.lean`: `Wff.Taut a := ∀ v, eval v a = true`, with
`taut_iff_neg_contra` (`Taut a ↔ Contradiction (neg a)`). `bc
validation/instance-checks.bc` verifies the hypothetical syllogism is a
tautology by enumerating all 8 rows.

## Type / well-formedness check
`well_formed`. `⊨ φ` quantifies over **all** assignments — a check on a subset of
assignments is not a tautology proof. The relevant assignments are the `2ⁿ`
restrictions to `atoms(φ)` (`truth_table`), so the `∀v` is effectively finite
per wff.

## Specialization / boundary cases
- `φ = ⊤` (`p → p`): a tautology.
- `φ` with no atoms and no `⊥`: a tautology iff it evaluates to `T`.
- **substitution instance**: if `φ(p₁,…,pₙ)` is a tautology, so is
  `φ(ψ₁,…,ψₙ)` for any wffs `ψᵢ` (uniform substitution preserves tautologyhood).
- `⊨ (φ → φ)`, `⊨ (φ ∨ ¬φ)`, `⊨ ¬(φ ∧ ¬φ)`, `⊨ ((φ → ψ) → ((ψ → χ) → (φ → χ)))`
  — the standard stock.

## Hypothesis-dropped counterexamples
- **check a subset of rows**: `p ∨ q` is `T` in 3 of 4 rows — not a tautology
  (fails at `p = q = F`); a 3-row "verification" is worthless.
- **confuse with satisfiable**: `p` is satisfiable (`satisfiability`) but not a
  tautology.
- **confuse classical tautology with intuitionistic theorem**: `¬¬p → p` is the
  standard witness.

## Common misuse
Calling a satisfiable formula a tautology; verifying on some assignments only;
assuming a classical tautology is constructively provable; treating "`⊨ φ`" and
"`φ` is true" as if `φ` had a fixed meaning (a wff is true *under an assignment*;
a tautology is true under all).

## Related nodes (non-prerequisite)
- `dual_of`: `contradiction_unsat` (via `¬`).
- `equivalent_to` (via completeness): "`φ` is a propositional theorem".
- `decided_by`: `truth_table`, `tautology_decidable`.
- `feeds`: `tautology_decidable`, and (semantically) `soundness_prop` /
  `post_completeness_theorem`.

## Sources
[enderton_logic_2e] §1.2; [vandalen_5e] §1.2; [chiswell_hodges] §2.3.
