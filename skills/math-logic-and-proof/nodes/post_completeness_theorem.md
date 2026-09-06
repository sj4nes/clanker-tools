# post_completeness_theorem

## Type
metatheorem  (epistemic status: `metatheorem`; `constructive_grade:
needs_full_classical`)

## Statement
If `Γ ⊨ φ` (propositional) then `Γ ⊢ φ`. Equivalently, the **model-existence**
form: every `consistency`-consistent set of wffs is **satisfiable**. With
`soundness_prop`, `Γ ⊨ φ ⟺ Γ ⊢ φ` — semantic and syntactic consequence coincide
for classical propositional logic.

## Symbols
- `Γ`: a set of wffs (possibly infinite); `φ`: a wff.

## Prerequisites (tsort edges into this node)
`lindenbaum_lemma_prop`, `truth_lemma_prop`, `soundness_prop`,
`semantic_consequence`, `consistency`.

## Proof (model existence form)
Given `Γ` consistent: extend to a `maximal_consistent_set` `Δ`
(`lindenbaum_lemma_prop`); the induced assignment `v_Δ` satisfies exactly `Δ`
(`truth_lemma_prop`), so `v_Δ ⊨ Δ ⊇ Γ`. For the `⊨ ⟹ ⊢` form: `Γ ⊨ φ` and
`Γ ⊬ φ` ⟹ `Γ ∪ {¬φ}` consistent ⟹ has a model ⟹ contradicts `Γ ⊨ φ`.

## Constructive grade
`needs_full_classical` — inherits from `lindenbaum_lemma_prop` (LEM for a
countable atom set; Zorn/BPIT for an arbitrary one) and the classical `¬`/`∨`
clauses of `truth_lemma_prop`. There is no constructive completeness for
classical semantics (intuitionistic logic is complete for **Kripke** semantics —
a different theorem).

## Lean status
`lean_status: cited`. `validation/proof-checks.lean` proves `soundness` (the
converse) outright; the completeness direction is `cited`. A plain-Lean proof
for a **countable** atom set is feasible (Lindenbaum by `Nat`-recursion + LEM,
truth lemma by `structural_induction_wff`, no Mathlib) and is the natural next
Lean target.

## Type / well-formedness check
`well_formed`. `Γ`, `φ` one language. For **finite** `Γ` it reduces to "every
tautology is a theorem"; for infinite `Γ`, model existence is the substantive
statement and `compactness_prop` falls out.

## Specialization / boundary cases
- `Γ = ∅`: `⊨ φ` ⟹ `⊢ φ` — every `tautology` is a propositional theorem.
- `Γ` finite: `⊨ (⋀Γ → φ)` ⟹ `⊢ (⋀Γ → φ)`.
- the **propositional fragment** of `godel_completeness_theorem` (no terms, no
  Henkin witnesses).
- **immediately implies `compactness_prop`**.

## Hypothesis-dropped counterexamples
- **intuitionistic calculus**: not complete for Boolean semantics — `¬¬p → p`
  and `p ∨ ¬p` are tautologies with no intuitionistic derivation.
- **drop consistency** (model-existence form): an inconsistent `Γ` has no model.
- **an incomplete rule set** (missing, say, `∨E`): some `Γ ⊨ φ` not derivable.

## Common misuse
Confusing with `functional_completeness` (expressing every truth function) —
different notion; confusing with `godel_incompleteness` (about a *theory*, not
the logic); expecting a practical proof-search procedure (it is an existence
result — `tautology_decidable` gives a decision procedure, not a short proof).

## Related nodes (non-prerequisite)
- `converse_is`: `soundness_prop`.
- `special_case_of` / `generalised_by`: `godel_completeness_theorem`.
- `implies`: `compactness_prop`.
- `commonly_confused_with`: `functional_completeness`, `godel_incompleteness_first`.

## Sources
[enderton_logic_2e] §1.7; [vandalen_5e] §1.5; Post (1921); [chiswell_hodges]
§3.3.
