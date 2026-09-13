# change_of_basis

## Type
theorem

## Statement
If P = [I]_{B<-B'} is the change-of-basis matrix then [v]_B = P[v]_{B'} and [T]_{B'} = P^{-1}[T]_B P. Matrices of the same operator in different bases are SIMILAR.

## Symbols
- `P` — the change-of-basis matrix, whose COLUMNS are the B-coordinates of the B'-basis vectors

## Epistemic status
proved_theorem  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
coordinate_isomorphism, invertible_matrix, matrix_mult_is_composition, matrix_of_linear_map, ordered_basis

## Hypotheses
V finite-dimensional, both bases ordered

## Proof provenance
technique: apply matrix_mult_is_composition to T = I o T o I with the appropriate bases
derives_from: matrix_mult_is_composition
lean_status: cited

## Type / well-formedness check
Well-formed; P is invertible because I is. Note the direction: P's columns express the NEW basis in the OLD one, and coordinates therefore transform by P, not P^{-1} -- the classic source of inverted transformations.

## Specialization / boundary cases
- B = B': P = I and the formula is trivial
- T diagonalisable: some P makes [T]_{B'} diagonal, which IS diagonalisable

## Hypothesis-dropped counterexamples
- **invertibility_of_P**: a non-basis 'B'' gives a singular P and no conjugation formula
- **vectors_versus_operators**: vectors transform by P and operator matrices by P^{-1}(.)P. Applying the vector rule to an operator (or vice versa) is the standard covariance/contravariance error

## Common misuse
- using P where P^{-1} is needed: fix the convention (columns of P are the new basis in old coordinates) and check on a 2x2 example every time

## Related nodes (non-prerequisite)
- required_by: similarity

## Sources
hoffman_kunze_2e
