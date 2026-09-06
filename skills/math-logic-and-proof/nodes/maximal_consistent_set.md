# maximal_consistent_set

## Type
definition  (epistemic status: `definition`; `constructive_grade: intuitionistic`
as a definition)

## Statement
A set of wffs `Δ` is **maximal consistent** iff it is `consistency`-consistent
and no consistent set properly contains it — equivalently, `Δ` is consistent and
for **every** wff `φ`, `φ ∈ Δ` or `¬φ ∈ Δ`.

## Symbols
- `Δ`: the maximal consistent set (an "MCS").

## Prerequisites (tsort edges into this node)
`consistency`.

## Content
The syntactic stand-in for a truth assignment. A maximal consistent `Δ` behaves
like the "theory of a model":
- **deductively closed**: `Δ ⊢ φ` ⟹ `φ ∈ Δ` (else `Δ ∪ {φ}` would be a
  consistent proper extension);
- **`¬φ ∈ Δ` iff `φ ∉ Δ`**;
- **`φ ∧ ψ ∈ Δ` iff `φ ∈ Δ` and `ψ ∈ Δ`**;
- **`φ ∨ ψ ∈ Δ` iff `φ ∈ Δ` or `ψ ∈ Δ`** (needs maximality — uses
  `de_morgan_prop` / classical reasoning);
- **`φ → ψ ∈ Δ` iff (`φ ∉ Δ` or `ψ ∈ Δ`)**.

These clauses are exactly what `truth_lemma_prop` needs: define `v(p) := [p ∈
Δ]`, then `v ⊨ φ ⟺ φ ∈ Δ` by `structural_induction_wff`.

`lindenbaum_lemma_prop`: every consistent set extends to a maximal consistent
one.

## Constructive grade
`intuitionistic` as a definition. The `∨` / `→` membership clauses use classical
reasoning about `Δ` (`needs_LEM`), and **obtaining** an MCS
(`lindenbaum_lemma_prop`) is `needs_LEM` (countable) / `needs_full_classical`
(uncountable).

## Lean status
`lean_status: cited`. Not built in `validation/proof-checks.lean` (the
propositional completeness proof is `cited`); a Mathlib-style development would
define it and prove the membership clauses by cases on maximality.

## Type / well-formedness check
`well_formed`. "Maximal" = maximal **among consistent subsets of the wffs of the
language**, ordered by `⊆` — not "contains every wff". An MCS is a *set of
wffs*, not a structure; it *induces* one (`truth_lemma_prop`).

## Specialization / boundary cases
- `Δ` = the deductive closure of a **complete** consistent theory: already an
  MCS.
- `Δ` from `∅` via Lindenbaum: a "random" complete consistent theory,
  enumeration-dependent.
- first-order: an MCS with the **witness property** is a `henkin_theory`.
- there are `2^𝔠` MCSs over a countably infinite atom set (they correspond to
  ultrafilters on the Lindenbaum algebra / points of its Stone space).

## Hypothesis-dropped counterexamples
- **consistent but not maximal**: the `¬` clause fails — `φ ∉ Δ` does not give
  `¬φ ∈ Δ`, so `truth_lemma_prop` cannot recurse through `¬`.
- **maximal but inconsistent**: does not exist (inconsistent ⟹ contains `⊥` ⟹
  contains everything, not "maximal consistent").
- **"maximal" read as "all wffs"**: that set is inconsistent.

## Common misuse
Reading "maximal" as "the set of all wffs"; assuming an MCS is unique;
forgetting deductive closure is a *consequence* (not part of the definition);
treating an MCS as a model rather than as inducing one; using the `∨` clause
without noting it needs maximality (classical).

## Related nodes (non-prerequisite)
- `obtained_by`: `lindenbaum_lemma_prop`.
- `induces`: a truth assignment (`truth_lemma_prop`).
- `first_order_analogue`: `henkin_theory` (MCS + witness property).
- `dual`: an ultrafilter on the Lindenbaum–Tarski Boolean algebra; a point of
  its Stone space.

## Sources
[enderton_logic_2e] §1.7 / §2.5; [vandalen_5e] §1.5; [chiswell_hodges] §3.3.
