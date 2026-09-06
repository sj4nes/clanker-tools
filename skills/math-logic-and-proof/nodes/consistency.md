# consistency

## Type
definition  (epistemic status: `definition`; `constructive_grade: intuitionistic`)

## Statement
A set of wffs `Γ` is **consistent** iff `Γ ⊬ ⊥` — equivalently (given
`explosion_ex_falso`) iff there is **some** wff `φ` with `Γ ⊬ φ`. Otherwise `Γ`
is **inconsistent** (and then `Γ ⊢ φ` for every `φ`).

## Symbols
- `Γ`: a set of wffs; `⊥`: falsum (`true_false_constants`).

## Prerequisites (tsort edges into this node)
`derivability`, `true_false_constants`.

## Content
The syntactic health condition. Equivalent forms (all provable in the calculus):
- `Γ ⊬ ⊥`;
- for some `φ`, `Γ ⊬ φ` ("`Γ` is not trivial");
- for every `φ`, not both `Γ ⊢ φ` and `Γ ⊢ ¬φ`;
- **at least one** of `Γ ∪ {φ}`, `Γ ∪ {¬φ}` is consistent, for every `φ` (the
  step iterated in `lindenbaum_lemma_prop`);
- **(the payoff of `post_completeness_theorem`)** `Γ` is **satisfiable**.

**Finite character**: `Γ` consistent iff every finite `Γ₀ ⊆ Γ` is consistent
(a derivation of `⊥` uses finitely many premises) — the basis of
`compactness_prop`.

## Constructive grade
`intuitionistic` as a definition (`Γ ⊢ ⊥ → ⊥`). *Deciding* consistency of a
given `Γ` is another matter — decidable for finite `Γ` (`tautology_decidable`
on `⋀Γ`), undecidable in general for infinite recursively-presented `Γ`.

## Lean status
`lean_status: core` (the notion). In `validation/proof-checks.lean` it would be
`¬ Deriv Γ Wff.fls`; `soundness` gives "satisfiable ⟹ consistent"
(contrapositive of `Deriv Γ fls → Entails Γ fls`, and `Entails Γ fls` is
absurd).

## Type / well-formedness check
`well_formed`. `Γ` and `⊥` in the same language. `Γ ⊬ ⊥` is a `Π₁` statement
over **derivations** — a syntactic, `naive_collection`-free notion (this node is
on the proof-theoretic floor).

## Specialization / boundary cases
- `Γ = ∅`: consistent (`soundness_prop`: `⊬ ⊥`).
- `Γ` **maximal consistent**: for every `φ`, exactly one of `φ`, `¬φ ∈ Γ`
  (`maximal_consistent_set`).
- `Γ` finite: consistent iff `⋀Γ` is `satisfiability` iff `¬⋀Γ` is not a
  tautology.
- first-order: `consistency_fol`, same definition; but `Con(PA)`, `Con(ZFC)` are
  not provable in those theories (`godel_incompleteness_second`).

## Hypothesis-dropped counterexamples
- `Γ = {φ, ¬φ}`: inconsistent — `¬E` gives `⊥`, then `explosion_ex_falso` gives
  everything.
- `Γ = {p, p → q, ¬q}`: inconsistent (derive `q` then `⊥`).
- "**I cannot find a contradiction**" is **not** a proof of consistency — you
  need a model (semantic) or a syntactic argument (e.g. every rule preserves a
  property `⊥` lacks).

## Common misuse
Treating "no contradiction found" as consistency; confusing consistency
(syntactic) with **satisfiability** (semantic) — equivalent by
soundness+completeness but distinct notions; confusing consistency with
**completeness** (deciding every sentence — orthogonal); forgetting consistency
is inherited by subsets but not by unions.

## Related nodes (non-prerequisite)
- `equivalent_to` (via completeness): `satisfiability` of `Γ`.
- `feeds`: `maximal_consistent_set`, `lindenbaum_lemma_prop`,
  `post_completeness_theorem`, `compactness_prop`.
- `first_order`: `consistency_fol`; `godel_incompleteness_second`.
- `contrast`: completeness of a theory.

## Sources
[enderton_logic_2e] §2.4; [vandalen_5e] §1.4; [chiswell_hodges] §3.3.
