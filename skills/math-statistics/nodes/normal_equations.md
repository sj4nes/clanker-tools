# normal_equations

## Type
identity

## Statement
The OLS minimizer satisfies the normal equations X^T X beta_hat = X^T y; with X of full column rank, beta_hat = (X^T X)^{-1} X^T y.

## Symbols
- `X^T X` — the p x p Gram matrix, symmetric positive definite when rank(X) = p
- `X^T y` — the p-vector of predictor-response inner products
- `X^T (y - X beta_hat) = 0` — equivalently: the residual vector is orthogonal to every column of X

## Epistemic status
mathematical_identity  ·  regime: exact

## Prerequisites (tsort edges into this node)
linear_algebra_background, ordinary_least_squares

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: set the gradient of || y - X b ||^2 to zero: -2 X^T (y - X b) = 0
derives_from: linear_algebra_background
lean_status: instance — validation/proof-checks.lean Stat.normal_equations_stationary -- grad || y - X b ||^2 = -2 X^T(y - Xb), checked for a fixed 2x2 design via decide on integer matrices

## Type / well-formedness check
The stationarity condition for the least-squares objective: grad_b || y - X b ||^2 = -2 X^T (y - X b) = 0. An exact algebraic identity. Numerically one solves it via QR or Cholesky of X, not by forming (X^T X)^{-1}.

## Specialization / boundary cases
- orthogonal design (X^T X diagonal): beta_hat_j = (x_j^T y)/(x_j^T x_j) -- each coefficient is a separate simple regression
- adding a column orthogonal to the existing ones does not change the existing coefficients (Frisch-Waugh, partitioned_regression)
- centered predictors: the intercept decouples as ybar

## Hypothesis-dropped counterexamples
- **X_full_rank**: singular X^T X (collinearity): the normal equations have infinitely many solutions; the fitted values X beta_hat are still unique (the projection), but the coefficients are not

## Common misuse
- forming and inverting X^T X explicitly for an ill-conditioned design -- squares the condition number; use QR
- reading a near-singular (X^T X)^{-1}'s huge diagonal entries as 'the data' rather than as collinearity

## Related nodes (non-prerequisite)
- required_by: ols_is_projection, ols_distribution_under_normal_errors
- uses: ordinary_least_squares, linear_algebra_background

## Sources
seber_lee_linear_regression, golub_van_loan_matrix_computations
