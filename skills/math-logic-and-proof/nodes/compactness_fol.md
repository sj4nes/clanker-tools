# compactness_fol

## Type
metatheorem  (epistemic status: `metatheorem`; `constructive_grade:
needs_full_classical` — inherits from `godel_completeness_theorem`)

## Statement
A set of first-order sentences `Γ` has a model if and only if **every finite
subset** of `Γ` has a model. Equivalently (via `soundness_fol` +
`godel_completeness_theorem`): `Γ` is satisfiable iff `Γ` is consistent iff
every finite `Γ₀ ⊆ Γ` is satisfiable.

## Symbols
- `Γ`: a set of `ℒ`-sentences; `Γ₀`: a finite subset.

## Prerequisites (tsort edges into this node)
`godel_completeness_theorem`, `derivability_fol`, `model`.

## Proof
- **from completeness** (the capsule's route): if `Γ` has no model, then by
  `godel_completeness_theorem` (contrapositive of model-existence) `Γ` is
  inconsistent, so `Γ ⊢ ⊥`; a derivation uses only finitely many premises
  `Γ₀ ⊆ Γ`, so `Γ₀ ⊢ ⊥`, so by `soundness_fol` `Γ₀` has no model.
- **ultraproduct route** (out of scope): take a model `𝔐_{Γ₀}` of each finite
  `Γ₀`, form the ultraproduct over an ultrafilter on the finite subsets; Łoś's
  theorem gives a model of `Γ`. Uses an ultrafilter (BPIT).

## Constructive grade
`needs_full_classical` — the completeness route inherits from
`godel_completeness_theorem` / `lindenbaum_lemma_fol`; the ultraproduct route
needs an ultrafilter. There is no constructive compactness theorem.

## Lean status
`lean_status: cited` (corrected from `partial` — audited 2026-09-11; see
`BACKLOG.md`). Inherits the status of `godel_completeness_theorem`, itself
corrected to `cited`: `validation/proof-checks.lean` has no first-order
content for this node to inherit a genuine kernel proof from. Cited:
[enderton_logic_2e] Thm 25.16. Mathlib has
`FirstOrder.Language.Theory.isSatisfiable_iff_isFinitelySatisfiable`, not
connected here.

## Type / well-formedness check
`well_formed`. "Model" is a `naive_collection` fact; the theorem quantifies over
**all** structures. Stated for **sentences** (no free variables); for formulas
one closes under the free variables first.

## Specialization / boundary cases
- **arbitrarily large finite models ⟹ an infinite model**: add fresh constants
  `c₁, c₂, …` and axioms `cᵢ ≠ cⱼ`; every finite subset is satisfied by a
  large-enough finite model, so the whole set has a model — necessarily
  infinite.
- **non-standard models of arithmetic**: `PA ∪ {c > 0, c > 1, c > 2, …}` is
  finitely satisfiable (interpret `c` as a big numeral), so has a model — with
  an element exceeding every standard `n`.
- **non-standard analysis**: the hyperreals come from compactness applied to the
  theory of `(ℝ, +, ·, <, r)_{r∈ℝ}` plus "`ε` is a positive infinitesimal".
- propositional reduct: `compactness_prop`.

## Hypothesis-dropped counterexamples
- **drop finite satisfiability** — the sole nontrivial hypothesis, essential:
  `{P(c), ¬P(c)}` has an unsatisfiable finite subset and no model.
- **drop first-order-ness**: compactness **fails** for second-order logic and
  for infinitary `L_{ω₁,ω}` — in SOL "the domain is infinite" and "the domain
  is finite" are each single sentences, whose consequences violate compactness.
  It also fails for logics with a "there are finitely many `x`" quantifier.
- as a **non-expressibility tool**: "well-founded", "finite", "connected
  (graph)", "torsion (group)", "the standard model of PA", "archimedean ordered
  field" — none first-order-axiomatisable, each shown so by compactness.

## Common misuse
Trying to first-order-axiomatise finiteness / well-foundedness / a specific
infinite cardinality; expecting the model of `Γ` to resemble the finite models;
using it in a second-order or infinitary setting; forgetting the sentences must
share one language.

## Related nodes (non-prerequisite)
- `special_case_of`: `godel_completeness_theorem` (model-existence corollary).
- `generalises`: `compactness_prop`.
- `feeds`: `lowenheim_skolem_up`, `non_categoricity`,
  `non_finite_axiomatizability`.
- `equivalent_to` (over ZF): the ultrafilter route needs only BPIT, not full AC.

## Sources
[enderton_logic_2e] §2.6; [chiswell_hodges] ch. 6; [hodges_shorter] §5.1 (Łoś);
[vandalen_5e] §3.2.
