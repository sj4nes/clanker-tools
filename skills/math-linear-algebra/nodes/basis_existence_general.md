# basis_existence_general

## Type
theorem

## Statement
Every vector space has a basis. Proved by Zorn's lemma applied to the poset of independent subsets ordered by inclusion. Over ZF this statement is EQUIVALENT to the axiom of choice (Blass 1984).

## Symbols
- `B` — a maximal independent subset, type: subset of V

## Epistemic status
proved_theorem (non-constructive) (uses choice)  ·  field_scope: any_field  ·  choice_grade: needs_full_AC

## Prerequisites (tsort edges into this node)
axiom_of_choice, basis, zorns_lemma

## Hypotheses
Zorn's lemma (equivalently AC)

## Proof provenance
technique: Zorn on independent subsets; a maximal independent set spans, since a vector outside its span could be adjoined
derives_from: zorns_lemma
lean_status: cited

## Type / well-formedness check
Well-formed. The Zorn hypothesis holds because the union of a chain of independent sets is independent -- a fact that uses the FINITENESS of linear combinations, since any vanishing combination involves finitely many vectors and hence lies in one member of the chain.

## Specialization / boundary cases
- V finite-dimensional: reduces to basis_existence_finite, which needs no choice at all
- V = R as a Q-vector space: a Hamel basis exists but none can be written down; its existence yields a non-measurable set and a discontinuous additive function R -> R

## Hypothesis-dropped counterexamples
- **the_axiom_of_choice**: Blass showed that in ZF, 'every vector space has a basis' implies AC. So there are models of ZF containing a vector space with NO basis. This is the only genuinely non-choice-free result in the capsule

## Common misuse
- using it to justify 'pick a basis' in an infinite-dimensional argument and then treating the basis as computable or even nameable
- confusing a Hamel basis (this theorem, finite combinations) with a Schauder/orthonormal basis of a Hilbert space (infinite convergent series) -- different objects with different existence theorems

## In the wild
- the existence of a non-measurable set and of pathological additive functions, both standard consequences in measure theory
- the routine 'extend to a basis' step in algebra, valid unconditionally only in finite dimension

## Related nodes (non-prerequisite)
- equivalent_to: axiom_of_choice
- contrasts_with: basis_existence_finite

## Sources
blass_1984, hoffman_kunze_2e
