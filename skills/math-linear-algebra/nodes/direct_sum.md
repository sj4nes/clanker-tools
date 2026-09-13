# direct_sum

## Type
definition

## Statement
V = U (+) W means V = U + W and U ∩ W = {0}. Equivalently, every v in V has a UNIQUE decomposition v = u + w with u in U and w in W.

## Symbols
- `(+)` — direct sum
- `U ∩ W` — the intersection, required trivial

## Epistemic status
definition  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
basis_unique_representation, subspace_intersection, sum_of_subspaces

## Hypotheses
U, W subspaces of V

## Proof provenance
technique: if x in U ∩ W is nonzero, x = x + 0 = 0 + x are distinct decompositions; conversely two decompositions differ by an element of U ∩ W
derives_from: subspace_intersection
lean_status: cited

## Type / well-formedness check
Well-formed. The equivalence of the two formulations is part of the node's content: uniqueness of the decomposition is exactly the triviality of the intersection, since a nonzero x in U ∩ W gives x + 0 = 0 + x as two decompositions.

## Specialization / boundary cases
- R^2 = (x-axis) (+) (y-axis), but also R^2 = (x-axis) (+) (diagonal) -- a complement is NOT unique
- V = U (+) U^perp for a finite-dimensional subspace of an inner product space (orthogonal_decomposition) -- the ORTHOGONAL complement is the canonical choice among many complements

## Hypothesis-dropped counterexamples
- **trivial_intersection**: in R^2 with U = W = the x-axis, U + W = U but the decomposition is wildly non-unique. The sum formula dim(U+W) = dim U + dim W then fails (1 != 2)
- **pairwise_triviality_for_three_or_more**: for three subspaces, PAIRWISE trivial intersections do NOT suffice: the x-axis, y-axis, and diagonal in R^2 meet pairwise in {0}, yet the sum of the three is not direct -- (1,1) decomposes in more than one way. The correct condition is that each U_i meets the sum of the others trivially

## Common misuse
- assuming a complement is unique, or that 'the' complement is meaningful without an inner product
- extending directness from two summands to many by checking only pairwise intersections (see the counterexample above)

## Related nodes (non-prerequisite)
- required_by: dimension_formula_sum, orthogonal_decomposition, primary_decomposition

## Sources
axler_lada_4e
