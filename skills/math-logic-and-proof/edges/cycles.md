# Cycles found and how they were resolved — Release 0.1

`tsort` (BSD, stderr-checked) reports the graph acyclic as shipped. The
following apparent cycles arose during construction and were resolved *before*
the graph was frozen.

## 1. `free_for` ↔ `substitution`
**Apparent cycle.** A first draft made `substitution` a prerequisite of
`free_for` ("capture is about what substitution does") *and* `free_for` a
`valid_when` prerequisite of `substitution` ("only substitute when free-for").
**Resolution — reclassify.** The *total syntactic operation* `substitution`
(replace every free occurrence, capturing or not) and the *side condition*
`free_for` (no free variable of `t` falls under a matching quantifier of `φ`)
are **independent**: each needs only `free_bound_variables` (+ `term_syntax`,
`quantifier_syntax`). Every node that substitutes *under a binder* —
`substitution_lemma_semantic`, `nd_rules_quantifier`,
`hilbert_quantifier_axioms`, `prenex_normal_form` — requires **both**. No edge
runs between the two.

## 2. `eigenvariable_condition` ↔ `nd_rules_quantifier`
**Apparent cycle.** The condition "the fresh variable does not occur free in the
conclusion or any open assumption" was drafted as depending on the rules, while
the rules `∀I`/`∃E` are `valid_when` the condition.
**Resolution — reclassify.** `eigenvariable_condition` is stated in terms of
`free_bound_variables` + `quantifier_syntax` alone (it is a predicate about
variable occurrences, not about the rules). `nd_rules_quantifier` then requires
it. One edge, one direction.

## 3. `alpha_equivalence` direction slip
A transcription error pointed `alpha_equivalence → free_bound_variables`.
Corrected to `free_bound_variables → alpha_equivalence` (renaming is *defined
using* the free/bound distinction).

## 4. `structure` ↔ `first_order_logic_with_equality`
Drafted with edges both ways. **Resolution.**
`first_order_logic_with_equality` is a *convention/axiom* ("`=` is a logical
symbol, always interpreted as identity") and is a **root**; `structure` requires
it (the interpretation must respect it), not vice versa.

## 5. `⊢` ↔ `⊨` (never encoded)
Soundness needs both; completeness needs both. **Not a cycle:** `derivability`
and `semantic_consequence` are independent nodes with **no edge between them**;
`soundness_prop` / `post_completeness_theorem` (and their FOL twins) are theorem
nodes with edges *into* them from both sides.

## 6. `∀` ↔ `∃`, truth ↔ satisfaction, weak ↔ strong induction
See `conventions.md` "Cycle resolutions": `∀` and `∃` both get primitive
formation rules (`quantifier_syntax`) with `exists_forall_duality` a proved
equivalence; `satisfaction` is a single node defined by recursion; weak
induction is primitive (`metatheoretic_induction`) with `induction_equivalence`
proving strong induction and well-ordering equivalent to it.

## 7. Cross-capsule syntax ↔ collections
Not a `tsort` edge in *either* capsule. Documented as a bidirectional `grounds`
relation in `edges/cross-capsule.md`.
