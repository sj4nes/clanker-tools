# similarity

## Type
definition

## Statement
A ~ B if B = P^{-1}AP for some invertible P. An equivalence relation whose classes are exactly the operators on an n-dimensional space, one class per operator up to choice of basis.

## Symbols
- `~` — similarity, type: equivalence relation on F^{n x n}

## Epistemic status
definition  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
change_of_basis, equivalence_relation, invertible_matrix

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: equivalence-relation axioms via the group structure of invertible matrices
derives_from: change_of_basis
lean_status: cited

## Type / well-formedness check
Well-formed as an equivalence relation: reflexive with P = I, symmetric via P^{-1}, transitive by composing. The correspondence with operators is exactly change_of_basis.

## Specialization / boundary cases
- P a permutation matrix: similarity by simultaneous row and column permutation
- A diagonalisable: A is similar to a diagonal matrix

## Hypothesis-dropped counterexamples
- **invertibility_of_P**: with singular P the relation is neither symmetric nor transitive
- **similarity_versus_congruence**: P^{-1}AP and P^T A P agree only when P is ORTHOGONAL. Similarity preserves eigenvalues; congruence preserves only inertia. Confusing them is the standard quadratic-form error -- see congruence

## Common misuse
- using congruence to compute eigenvalues, or similarity to classify quadratic forms
- assuming similar matrices are equal in any entrywise sense: they share invariants only (similar_invariants)

## Related nodes (non-prerequisite)
- contrasts_with: congruence
- required_by: similar_invariants, diagonalisable

## Sources
hoffman_kunze_2e, horn_johnson_2e
