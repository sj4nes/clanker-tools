# consistency_fol

## Type
definition  (epistemic status: `definition`; `constructive_grade: intuitionistic`)

## Statement
A first-order theory `T` (a set of `ℒ`-sentences) is **consistent** iff
`T ⊬ ⊥` — equivalently, iff there is some sentence `σ` with `T ⊬ σ`
(otherwise `T` proves everything, in particular `⊥`). Written `Con(T)`.

## Symbols
- `T`: a set of `ℒ`-sentences (`Theory`).
- `⊥`: falsum; `T ⊢ ⊥` means a derivation of `⊥` from finitely many members of
  `T` exists (`derivability_fol`).

## Prerequisites (tsort edges into this node)
`derivability_fol`, `consistency` (the propositional notion, specialised).

## Content
The first-order specialisation of `consistency`. Key equivalent forms, all
provable in the calculus:
- `T ⊬ ⊥`;
- for some `σ`, `T ⊬ σ` ("`T` is not trivial");
- `T ∪ {σ}` or `T ∪ {¬σ}` is consistent, for every `σ` (one of the two
  extensions always stays consistent) — the step iterated in
  `lindenbaum_lemma_fol`;
- **(the payoff of `godel_completeness_theorem`)** `T` has a model.

**Finite character**: `T` is consistent iff every finite `T₀ ⊆ T` is consistent,
because a derivation of `⊥` uses only finitely many premises. This is what makes
`compactness_fol` fall out of completeness.

## Constructive grade
`intuitionistic` as a definition (`T ⊢ ⊥ → ⊥`). Deciding consistency of a given
`T` is another matter — undecidable in general (`undecidability_fol_validity`,
`godel_incompleteness_second`).

## Lean status
`lean_status: core` (the notion). `Deriv`/`H` in `validation/proof-checks.lean`
are propositional; `consistency` there would be `¬ Deriv Γ Wff.fls`. The
first-order `derivability_fol` and its consistency are `stated` (the FOL
calculus is not fully formalised without Mathlib).

## Type / well-formedness check
`well_formed`. `T` and `⊥` must be in the **same language** `ℒ`. "`T` is
consistent" is a `Π₁` statement over derivations (a `naive_collection` of finite
syntactic objects — but syntax only, no models: this node is on the *syntactic*
side of the capsule and does **not** depend on `naive_collection`).

## Specialization / boundary cases
- `T = ∅`: consistent (pure logic proves no contradiction — `soundness_fol`).
- `T` = the axioms of a group / a field / `PA` / `ZFC`: consistent (they have
  models); `Con(PA)`, `Con(ZFC)` are not provable *in* those theories
  (`godel_incompleteness_second`).
- `T` **complete and consistent**: for every `σ`, exactly one of `σ`, `¬σ ∈ T`
  (if `T` is deductively closed).
- `T` **maximal consistent**: `henkin_theory` after Lindenbaum.

## Hypothesis-dropped counterexamples / failure
- `T = {σ, ¬σ}`: inconsistent — proves `⊥` by `¬E`, hence everything (`explosion`).
- `T = PA ∪ {¬Con(PA)}`: **consistent** if `PA` is (by the second incompleteness
  theorem), yet has only non-standard models — a reminder that consistency does
  not imply "has a *nice* model".
- dropping "same language": `T` in `ℒ`, `σ` in `ℒ′ ⊋ ℒ` — `T ⊢ σ` is not even
  well-formed.

## Common misuse
Treating "I cannot find a contradiction" as a proof of consistency; assuming a
consistent theory has a standard / intended model; confusing `T ⊬ ⊥` with `T`
being **complete** (deciding every sentence) — orthogonal properties; forgetting
consistency is preserved under `⊆` (a subtheory of a consistent theory is
consistent) but **not** under arbitrary unions.

## Related nodes (non-prerequisite)
- `specialises`: `consistency` (propositional).
- `feeds`: `henkin_constants`, `lindenbaum_lemma_fol`,
  `godel_completeness_theorem` (model-existence form), `compactness_fol`.
- `constrained_by`: `godel_incompleteness_second` (`T ⊬ Con(T)`).

## Sources
[enderton_logic_2e] §2.4; [vandalen_5e] §3.1; [chiswell_hodges] §5.3.
