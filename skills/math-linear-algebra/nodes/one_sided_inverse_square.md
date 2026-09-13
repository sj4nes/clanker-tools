# one_sided_inverse_square

## Type
proposition

## Statement
For SQUARE A, B over a field: AB = I implies BA = I. A one-sided inverse of a square matrix is automatically two-sided.

## Symbols
- `A, B` — square matrices of the same size

## Epistemic status
proposition  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
injective_surjective_equivalence, invertible_matrix, rank_nullity

## Hypotheses
A, B square of the same size, F a field

## Proof provenance
technique: AB = I makes the map x -> Ax surjective, hence injective by injective_surjective_equivalence, hence bijective; then B = A^{-1}
derives_from: injective_surjective_equivalence
lean_status: cited

## Type / well-formedness check
Well-formed. The proposition is a dimension statement in disguise and inherits its hypotheses from injective_surjective_equivalence.

## Specialization / boundary cases
- n = 1: ab = 1 in a field gives ba = 1 by commutativity

## Hypothesis-dropped counterexamples
- **squareness**: for A in F^{2x3} and B in F^{3x2} one can have AB = I_2 with BA != I_3 -- BA has rank at most 2 < 3, so it cannot be I_3
- **finite_dimensionality**: on F[t] the shift pair LR = I, RL != I is the standing counterexample (see invertible_operator)
- **F_a_field**: over the ring Z, A = [2] has no inverse at all, though over the module-theoretic analogue one-sidedness can behave worse

## Common misuse
- extending the convenience to rectangular matrices or to operators on function spaces

## Related nodes (non-prerequisite)
- illustrated_by: infinite_dimensional_boundary

## Sources
hoffman_kunze_2e
