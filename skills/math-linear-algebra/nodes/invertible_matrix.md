# invertible_matrix

## Type
definition

## Statement
A in F^{n x n} is invertible (nonsingular) if AB = BA = I for some B. The inverse is unique, (A^{-1})^{-1} = A, (AB)^{-1} = B^{-1}A^{-1}, and (A^T)^{-1} = (A^{-1})^T.

## Symbols
- `A^{-1}` — the inverse, type: element of F^{n x n}

## Epistemic status
definition  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
identity_matrix, matrix_multiplication

## Hypotheses
A square

## Proof provenance
technique: uniqueness by associativity; the product rule by direct verification
derives_from: matrix_multiplication
lean_status: core — LinAlg.inv_unique, LinAlg.inv_mul_rev (monoid arguments: associativity + two-sided identity only)

## Type / well-formedness check
Well-formed only for SQUARE A: a rectangular matrix can have a one-sided inverse but never a two-sided one, since AB = I_m and BA = I_n would force m = n by rank.

## Specialization / boundary cases
- n = 1: A = [a] is invertible iff a != 0
- A diagonal: invertible iff no diagonal entry is 0, with the reciprocals on the diagonal

## Hypothesis-dropped counterexamples
- **squareness**: a 2x3 matrix of rank 2 has a right inverse but no left inverse; the two one-sided inverses are not unique either
- **order_reversal**: (AB)^{-1} = A^{-1}B^{-1} is false whenever A and B do not commute

## Common misuse
- computing A^{-1} to solve Ax = b: elimination is faster and better conditioned; the inverse is a theoretical object, not an algorithm
- concluding invertibility from 'det A is not too small' -- see condition_number

## Related nodes (non-prerequisite)
- required_by: invertibility_equivalences, similarity

## Sources
hoffman_kunze_2e, strang_5e
