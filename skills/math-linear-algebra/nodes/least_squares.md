# least_squares

## Type
theorem

## Statement
x minimises ||Ax - b|| if and only if A^T A x = A^T b (the NORMAL EQUATIONS). A solution always exists; it is unique iff A has full column rank, and then x = (A^TA)^{-1}A^Tb with fitted values Ax = P_{col(A)} b.

## Symbols
- `A` — type: element of R^{m x n}, typically m > n
- `A^TA` — the Gram matrix of the columns, type: n x n symmetric PSD

## Epistemic status
proved_theorem  ·  field_scope: real_or_complex

## Prerequisites (tsort edges into this node)
adjoint_kernel_image, best_approximation, column_space, linear_system, matrix_rank, orthogonal_projection, transpose

## Hypotheses
F = R (or C with ^*), full column rank for uniqueness

## Proof provenance
technique: Ax is the closest point of col(A) to b iff b - Ax is orthogonal to col(A) iff A^T(b - Ax) = 0 (best_approximation plus adjoint_kernel_image)
derives_from: best_approximation
lean_status: dim_core — LinAlg.normal_equations_residual_orthogonal (n = 2)

## Type / well-formedness check
Well-formed over R. The normal equations are ALWAYS consistent (A^Tb is in col(A^TA) = row(A)), so a minimiser always exists even when A is rank deficient -- uniqueness is the only thing that can fail.

## Specialization / boundary cases
- A square invertible: the normal equations reduce to Ax = b
- A with orthonormal columns: A^TA = I, so x = A^Tb -- the projection coefficients directly
- the 3-point regression design used in math-statistics' instance checks

## Hypothesis-dropped counterexamples
- **full_column_rank**: if rank A < n the normal equations have a whole affine family of solutions; the minimum-NORM one is A^+b via the pseudoinverse (moore_penrose_pseudoinverse). Collinear predictors in regression are exactly this case
- **conditioning**: kappa(A^TA) = kappa(A)^2, so forming the normal equations SQUARES the condition number. For an A with kappa = 10^8 the normal equations lose all double precision, while qr_factorisation does not. This is why no serious least-squares solver forms A^TA

## Common misuse
- solving least squares by explicitly forming and inverting A^TA (see above) -- use QR or SVD
- concluding no solution exists when A is rank deficient: a minimiser always exists, it is merely non-unique

## In the wild
- ordinary least squares regression -- the normal equations ARE the OLS estimating equations, and math-statistics' linear_model block rests on this node
- curve fitting, calibration, and the linear step of Gauss-Newton and Levenberg-Marquardt

## Related nodes (non-prerequisite)
- special_case_of: best_approximation
- required_by: hat_matrix, qr_factorisation, moore_penrose_pseudoinverse

## Sources
strang_5e, golub_van_loan_4e
