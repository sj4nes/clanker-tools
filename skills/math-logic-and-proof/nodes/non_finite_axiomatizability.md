# non_finite_axiomatizability

## Type
example  (epistemic status: `metatheorem` consequence; `constructive_grade:
needs_full_classical`)

## Statement
Many first-order theories cannot be axiomatised by finitely many sentences (nor,
in some cases, by any first-order theory at all). The standard tool is
`compactness_fol`.

- **"the domain is infinite"** is first-order-axiomatisable but only by the
  **infinite** schema `{λ_n : n ≥ 2}`, `λ_n =` "there are at least `n` distinct
  elements". It is **not finitely** axiomatisable: any finite subset has a
  finite model.
- **"the domain is finite"**, **well-foundedness**, **connectedness of a
  graph**, **being a torsion group**, **the archimedean property**, **"is
  isomorphic to `(ℕ, <)`"** are **not first-order** at all.
- **`PA`**, **`ZF`**, **the theory of fields of characteristic `0`** are
  first-order but **not finitely** axiomatisable (the latter needs
  `{1+1 ≠ 0, 1+1+1 ≠ 0, …}`).

## Symbols
- `T`: a first-order theory.
- "finitely axiomatisable": there is a single sentence `σ` (a finite
  conjunction) with the same models as `T`.

## Prerequisites (tsort edges into this node)
`compactness_fol`.

## The compactness argument (for "infinite" not finitely axiomatisable)
Suppose a single `σ` axiomatised "infinite". Then `{¬σ} ∪ {λ_n : n ≥ 2}` — "`σ`
fails but there are at least `n` elements for every `n`" — is **finitely
satisfiable** (any finite subset needs only finitely many `λ_n`, satisfied by a
large finite model, which also satisfies `¬σ` since it is finite). By
compactness it has a model: infinite (satisfies every `λ_n`) yet `⊨ ¬σ` —
contradicting "`σ` axiomatises infinite". ∎

For **"finite" is not first-order**: `{ψ} ∪ {λ_n}` where `ψ` claims finiteness is
finitely satisfiable but has no model.

## Constructive grade
`needs_full_classical` — via `compactness_fol`.

## Lean status
`lean_status: cited`. The infinite-model theory
(`FirstOrder.Language.Theory.infinite`) and the non-finite-axiomatisability
arguments appear in Mathlib's model theory.

## Type / well-formedness check
`well_formed`. Distinguish three claims, increasingly strong: (a) not finitely
axiomatisable; (b) not axiomatisable by any first-order theory; (c) the
*complement* class is not first-order (often the easiest to show and it implies
(a) for the original if the class is first-order). "Infinite" is (a); "finite"
and "well-founded" are (b).

## Specialization / boundary cases
- **fields of characteristic `p`** (fixed prime `p`): **finitely** axiomatisable
  (`1 + … + 1 = 0`, `p` times) — the contrast case.
- **algebraically closed fields**: not finitely axiomatisable (need "every
  degree-`n` polynomial has a root" for every `n`).
- **"exactly `n` elements"**: finitely axiomatisable (`λ_n ∧ ¬λ_{n+1}`).
- **`ACF₀`**: not finitely axiomatisable, but *complete* — non-finite-
  axiomatisability and completeness are independent properties.

## Hypothesis-dropped counterexamples / limits
- the argument **needs infinitely many `λ_n`** available — for a class where the
  witnessing schema is finite, finite axiomatisability may hold.
- **second-order logic**: "finite", "well-founded", "`≅ (ℕ,<)`" are all single
  second-order sentences — non-first-order-definability is a first-order
  phenomenon.
- a theory can be non-finitely-axiomatisable yet **recursively** axiomatisable
  (`PA`, `ZF`) — that is all `godel_incompleteness_first` needs.

## Common misuse
Assuming any property with an infinite schema is not finitely axiomatisable
(sometimes a clever single sentence works); conflating "not finitely
axiomatisable" with "not recursively axiomatisable" (`PA` is the latter's
counterexample); trying to first-order-express finiteness/well-foundedness;
forgetting the complement-class trick.

## Related nodes (non-prerequisite)
- `proved_using`: `compactness_fol`.
- `technique_shared_with`: `lowenheim_skolem_up` (fresh constants / `λ_n`
  schema).
- `related`: `non_categoricity` (both express first-order logic's limited
  expressive power); the Craig / Lyndon interpolation and Beth definability
  results (out of scope).

## Sources
[enderton_logic_2e] §2.6; [chiswell_hodges] ch. 6; [hodges_shorter] §5.2;
[bbj_5e] ch. 12.
