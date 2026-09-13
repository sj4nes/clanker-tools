# qr_factorisation

## Type
construction

## Statement
A in F^{m x n} with m >= n and full column rank factors as A = QR with Q in F^{m x n} having orthonormal columns and R in F^{n x n} upper triangular with positive diagonal; the factorisation is then UNIQUE. Least squares becomes Rx = Q^Tb, a triangular solve.

## Symbols
- `Q` — orthonormal columns spanning col(A)
- `R` — upper triangular, the Gram-Schmidt coefficients

## Epistemic status
constructive_result  ·  field_scope: real_or_complex

## Prerequisites (tsort edges into this node)
gram_schmidt, least_squares, matrix_multiplication, orthonormal_basis, triangular_matrix

## Hypotheses
m >= n, rank A = n for the unique reduced form

## Proof provenance
technique: run gram_schmidt on the columns of A; e_j depends only on v_1..v_j, which is exactly upper-triangularity of R. Uniqueness because Q^*A = R forces R, and positivity of the diagonal fixes the signs
derives_from: gram_schmidt
lean_status: cited

## Type / well-formedness check
Well-formed under full column rank; the positivity normalisation of the diagonal is what pins down uniqueness (otherwise Q and R can absorb signs or phases).

## Specialization / boundary cases
- A square invertible: QR with both factors square, and |det A| = prod |R_ii|
- A with orthonormal columns already: Q = A, R = I
- A^TA = R^TR, so R is the Cholesky factor of the Gram matrix -- the link to cholesky_factorisation

## Hypothesis-dropped counterexamples
- **full_column_rank**: a rank-deficient A has no unique QR; column-pivoted QR (AP = QR) is the standard remedy and also reveals the numerical rank
- **why_QR_over_the_normal_equations**: solving Rx = Q^Tb has condition number kappa(A), while the normal equations have kappa(A)^2. For kappa(A) = 10^8 this is the difference between 8 lost digits and 16

## Common misuse
- using classical Gram-Schmidt to compute Q in floating point (see gram_schmidt): Householder reflections or MGS are the stable implementations
- assuming QR is available for a rank-deficient matrix without pivoting

## In the wild
- the default dense least-squares solver in LAPACK and in every statistics package's lm() implementation -- R's lm uses a pivoted QR, not the normal equations
- the QR algorithm for eigenvalues repeatedly factors and re-multiplies, converging to schur_triangularisation

## Related nodes (non-prerequisite)
- special_case_of: gram_schmidt

## Sources
golub_van_loan_4e, trefethen_bau
