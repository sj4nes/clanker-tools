# truth_lemma_prop

## Type
proved_lemma  (epistemic status: `proved_lemma`; `constructive_grade: needs_LEM`
— the `¬`/`∨` clauses use completeness of the MCS)

## Statement
Let `Δ` be a `maximal_consistent_set` of propositional wffs. Define the truth
assignment `v_Δ(p) := T` iff `p ∈ Δ`. Then for **every** wff `φ`:

    v_Δ ⊨ φ   ⟺   φ ∈ Δ.

In particular `v_Δ ⊨ Δ`, so `Δ` (hence any `Γ ⊆ Δ`) is satisfiable.

## Symbols
- `Δ`: a maximal consistent set; `v_Δ`: the induced assignment.

## Prerequisites (tsort edges into this node)
`maximal_consistent_set`, `truth_assignment`, `derivability`, `de_morgan_prop`.

## Proof
By `structural_induction_wff` on `φ`, using the MCS membership clauses
(`maximal_consistent_set`):
- **atomic `p`**: `v_Δ ⊨ p ⟺ v_Δ(p) = T ⟺ p ∈ Δ` (definition).
- **`¬φ`**: `v_Δ ⊨ ¬φ ⟺ v_Δ ⊭ φ ⟺` (IH) `φ ∉ Δ ⟺ ¬φ ∈ Δ` (maximality +
  consistency). **Classical step.**
- **`φ ∧ ψ`**: from IH + `φ ∧ ψ ∈ Δ ⟺ φ ∈ Δ ∧ ψ ∈ Δ`.
- **`φ ∨ ψ`**: from IH + `φ ∨ ψ ∈ Δ ⟺ φ ∈ Δ ∨ ψ ∈ Δ` — needs maximality
  (`de_morgan_prop`-style). **Classical step.**
- **`φ → ψ`**: reduce via `implication_as_disjunction`.

## Constructive grade
`needs_LEM` — the `¬` and `∨` clauses rest on `Δ` being **complete**
(`φ ∈ Δ` or `¬φ ∈ Δ`), a classical property from `lindenbaum_lemma_prop`. The
atomic and `∧` clauses are constructive.

## Lean status
`lean_status: cited`. Not built (propositional completeness is `cited`). The
**shape** — a structural induction over `Wff` relating a syntactic predicate to
`eval` — is exactly what `validation/proof-checks.lean`'s `equiv_*` and
`taut_iff_neg_contra` lemmas do at small scale.

## Type / well-formedness check
`well_formed`. Requires `Δ` **maximal consistent** (for the `¬`/`∨` clauses) —
a merely consistent `Δ` is not enough. `v_Δ` is a total `truth_assignment`
(defined on every atom). The induction is over **all wffs**, not just atoms.

## Specialization / boundary cases
- `Δ` = deductive closure of a complete consistent theory `T`: `v_Δ` is a model
  of `T`.
- propositional fragment of `truth_lemma_fol` (no terms, no quantifiers, no
  Henkin witnesses).
- combined with `lindenbaum_lemma_prop`: **model existence** — every consistent
  `Γ` is satisfiable — which is `post_completeness_theorem`.

## Hypothesis-dropped counterexamples
- **`Δ` consistent but not maximal**: the `¬` clause fails — `φ ∉ Δ` no longer
  gives `¬φ ∈ Δ`, so `v_Δ ⊨ ¬φ` and `¬φ ∈ Δ` can disagree.
- **`Δ` not deductively closed** (if that were separate): `φ ∧ ψ` clause breaks.
- **constructive metatheory**: no complete `Δ` (Lindenbaum fails) ⟹ no truth
  lemma ⟹ completeness fails constructively.

## Common misuse
Applying it to a merely consistent set; proving only one direction (`Δ ⊆ Th(v_Δ)`)
and claiming the model; forgetting the `∨`/`¬` clauses need maximality;
conflating `v_Δ ⊨ φ` (semantic) with `Δ ⊢ φ` (syntactic) — they coincide *here*,
which is the lemma's content, not an assumption.

## Related nodes (non-prerequisite)
- `uses`: `maximal_consistent_set` (membership clauses), `structural_induction_wff`.
- `combines_with`: `lindenbaum_lemma_prop` ⟹ `post_completeness_theorem`.
- `first_order_analogue`: `truth_lemma_fol` (adds the `∃` witness clause).

## Sources
[enderton_logic_2e] §1.7 / §2.5; [vandalen_5e] §1.5; [chiswell_hodges] §3.3.
