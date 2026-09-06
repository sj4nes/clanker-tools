# naive_collection

## Type
primitive  (a root — **discharged from above** by
`math-sets-functions-cardinality`; `constructive_grade: n/a`)

## Statement
Informal "set of" / "collection of" talk, used **only** in the semantic nodes:
a `structure` has a domain "set"; `validity` quantifies over "all structures";
`model` collects the structures satisfying a theory; completeness speaks of
"the class of models". `naive_collection` is the placeholder for exactly this
talk.

## Symbols
- `A`, `M`: a domain / a class of structures — a `naive_collection`.

## Prerequisites (tsort edges into this node)
none in this capsule — **primitive**. Discharged **externally**: see
`edges/cross-capsule.md`.

## Why it is here, and why primitive
The foundations are genuinely circular: **model theory needs sets, set theory
needs logic**. The capsule's resolution (`conventions.md`):
- the **syntactic / proof-theoretic** subgraph (`symbol` → wffs → ND/Hilbert →
  `derivability` → `consistency`) is **self-contained** and touches
  `naive_collection` **nowhere**;
- every **semantic** node carries `metatheory: naive_collections` and a
  `requires naive_collection` edge;
- `naive_collection` stays primitive **here** and is discharged **from above**
  by `math-sets-functions-cardinality`'s ZF(C) axioms — exactly mirroring how
  that capsule's `proposition_logic` primitive is discharged **from here**.

Neither capsule's `tsort` graph contains the loop; it is a documented
bidirectional `grounds` relation.

## Constructive grade
`n/a` — it is a primitive standing in for external set theory, not a logical
law.

## Lean status
`lean_status: none` (a stance, not a theorem). In `validation/proof-checks.lean`
the propositional semantics uses `v : Nat → Bool` (no collection needed); a
first-order `Structure` would carry a `Type` domain — Lean's `Type` universe
playing the role of `naive_collection`, itself grounded in type theory rather
than ZFC.

## Type / well-formedness check
`well_formed` as a placeholder. What the semantic nodes actually require of it:
a domain that is a **nonempty** collection (`objects.md`); the ability to
quantify "for every element of the domain" (the `∀`/`∃` clauses of
`tarski_satisfaction`); and to form "the class of all models" (a proper class in
ZFC, handled by reflection / set-sized approximations). The capsule does **not**
develop any of this — it defers to the set capsule.

## Specialization / boundary cases
- **propositional semantics**: needs no `naive_collection` at all — a
  `truth_assignment` is a function into `{T,F}`, and `tautology` quantifies over
  the `2ⁿ` assignments to a wff's atoms (finite). This is why `post_completeness_theorem`
  for a **countable** language is choice-free while `godel_completeness_theorem`
  for an uncountable one is not.
- **countable first-order language**: the term model's domain is a quotient of a
  countable set — a mild `naive_collection`.
- **the class of all models**: a proper class; `compactness_fol` /
  `lowenheim_skolem` statements quantify over it.

## Hypothesis-dropped counterexamples
- **try to make it primitive AND develop set theory here**: circular — the set
  capsule's proofs use this capsule's logic.
- **drop the "semantic only" restriction** (let a syntactic node depend on it):
  the self-contained proof-theoretic floor is lost, and the whole stack rests on
  something two storeys up.

## Common misuse
Using set-theoretic constructions inside the syntactic subgraph; treating "the
class of all models" as a set without care (`Russell`-style); forgetting that
propositional semantics is collection-free; assuming the circularity is a defect
rather than the honest state of the foundations.

## Related nodes (non-prerequisite)
- `discharged_by` (external): the ZF(C) axioms of
  `math-sets-functions-cardinality` (`edges/cross-capsule.md`).
- `required_by`: `structure`, `assignment`, `model`, `validity`,
  `semantic_consequence_fol`, `soundness_*`, `godel_completeness_theorem`,
  `compactness_fol`, `lowenheim_skolem_*`.
- `not_required_by`: the entire propositional and proof-theoretic subgraph.

## Sources
[enderton_logic_2e] §2.2 (structures presuppose sets); [chiswell_hodges] ch. 5;
`conventions.md`, `edges/cross-capsule.md` (the stance).
