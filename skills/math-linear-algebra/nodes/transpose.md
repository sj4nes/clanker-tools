# transpose

## Type
definition

## Statement
(A^T)_{ij} = A_{ji}, mapping F^{m x n} to F^{n x m}. It is linear, involutive ((A^T)^T = A), and ANTI-multiplicative: (AB)^T = B^T A^T.

## Symbols
- `A^T` — type: element of F^{n x m}

## Epistemic status
definition  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
index_convention, matrix, matrix_multiplication, transpose_convention

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: entrywise: ((AB)^T)_{ij} = (AB)_{ji} = sum_k A_{jk}B_{ki} = sum_k (B^T)_{ik}(A^T)_{kj}
derives_from: matrix_multiplication
lean_status: dim_core — LinAlg.transpose_mul_rev, LinAlg.transpose_involutive (n = 2)

## Type / well-formedness check
Well-formed for any shape. The order reversal in (AB)^T is forced by shape conformability alone, and is the matrix shadow of the contravariance of dual_map.

## Specialization / boundary cases
- A symmetric: A^T = A
- A a column vector: A^T is a row vector, and x^T y is the standard bilinear pairing
- det(A^T) = det(A) -- see determinant_transpose

## Hypothesis-dropped counterexamples
- **order_reversal**: assuming (AB)^T = A^T B^T is ill-typed unless the shapes happen to be square, and false even then -- take the noncommuting pair from matrix_mult_noncommutative
- **over_C**: the transpose is NOT the adjoint over C; A^T A can be singular for a full-rank complex A (take A = [[1, i]]), whereas A^* A cannot. Use conjugate_transpose

## Common misuse
- using A^T in a complex inner-product argument

## Related nodes (non-prerequisite)
- dual_of: dual_map
- required_by: conjugate_transpose, quadratic_form, least_squares

## Sources
hoffman_kunze_2e
