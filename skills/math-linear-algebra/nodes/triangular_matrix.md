# triangular_matrix

## Type
definition

## Statement
A is upper triangular if A_{ij} = 0 for i > j, lower triangular if A_{ij} = 0 for i < j, diagonal if both. Each class is closed under sums and products; a triangular matrix is invertible iff no diagonal entry is 0, and the inverse is triangular of the same type.

## Symbols
- `A_{ii}` — the diagonal entries, which are the eigenvalues of a triangular matrix

## Epistemic status
definition  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
invertible_matrix, matrix, matrix_multiplication

## Hypotheses
A square

## Proof provenance
technique: products by index bookkeeping; invertibility because the determinant is the product of the diagonal (determinant_triangular), and the inverse by back substitution
derives_from: matrix_multiplication
lean_status: cited

## Type / well-formedness check
Well-formed for square A. Closure under products is a direct index argument; closure of the inverse follows by back substitution.

## Specialization / boundary cases
- diagonal matrices commute with each other -- one of the few commuting families
- the eigenvalues of a triangular matrix are exactly its diagonal entries, read off char_poly_roots_are_eigenvalues with determinant_triangular

## Hypothesis-dropped counterexamples
- **triangularity_is_basis_dependent**: every matrix over C is SIMILAR to a triangular one (schur_triangularisation), so triangularity says nothing about the operator -- only about the basis chosen. Contrast diagonalisable, which IS a property of the operator
- **upper_times_lower**: the product of an upper and a LOWER triangular matrix is generally neither

## Common misuse
- assuming a triangular matrix is diagonalisable: [[1,1],[0,1]] is triangular and not diagonalisable (non_diagonalisable_counterexample)

## Related nodes (non-prerequisite)
- required_by: determinant_triangular, lu_factorisation, qr_factorisation, cholesky_factorisation

## Sources
hoffman_kunze_2e
