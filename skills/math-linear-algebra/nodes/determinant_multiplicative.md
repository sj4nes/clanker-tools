# determinant_multiplicative

## Type
theorem

## Statement
det(AB) = det(A) det(B) for square A, B of the same size. Hence det is a group homomorphism from GL_n(F) to F^*.

## Symbols
- `GL_n(F)` — the group of invertible n x n matrices

## Epistemic status
proved_theorem  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
determinant, determinant_row_operations, elementary_matrix, matrix_multiplication

## Hypotheses
A, B square of the same size

## Proof provenance
technique: for fixed B, the map A -> det(AB) is an alternating multilinear function of the ROWS of A, equal to det(B) when A = I; by uniqueness it equals det(B)det(A). (Equivalently: factor A into elementary matrices and apply determinant_row_operations to each.)
derives_from: determinant_row_operations
lean_status: dim_core — LinAlg.det_mul (n = 2)

## Type / well-formedness check
Well-formed for equal square shapes. This is the deepest elementary property of the determinant and is what all its invariance results (similarity, volume) reduce to.

## Specialization / boundary cases
- B = A^{-1}: det(A)det(A^{-1}) = 1, so det(A^{-1}) = 1/det(A)
- B = P^{-1}, A = PA': recovers determinant_similarity_invariant
- det(A^k) = (det A)^k

## Hypothesis-dropped counterexamples
- **squareness_and_equal_size**: for rectangular factors both sides are undefined; the Cauchy-Binet formula is the correct generalisation and is NOT a product of determinants
- **addition_has_no_analogue**: det(A+B) != det A + det B, and there is no useful formula

## Common misuse
- expecting an additive analogue
- using det(AB) = det(A)det(B) to conclude rank(AB) = rank(A)rank(B) -- rank is not multiplicative (rank_inequalities)

## In the wild
- the change-of-variables Jacobian factor composes multiplicatively under composition of maps, which is exactly this theorem
- the determinant of a product of elementary operations is how elimination tracks det in O(n^3)

## Related nodes (non-prerequisite)
- required_by: determinant_invertible_iff, determinant_similarity_invariant, determinant_volume

## Sources
hoffman_kunze_2e, lang_algebra_3e
