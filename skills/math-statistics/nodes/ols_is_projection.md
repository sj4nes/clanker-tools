# ols_is_projection

## Type
theorem

## Statement
The OLS fitted values are the orthogonal projection of y onto the column space of X: y_hat = X beta_hat = H y, where H = X (X^T X)^{-1} X^T is the hat matrix -- symmetric, idempotent (H^2 = H), with rank(H) = trace(H) = p. The residual vector e = (I - H) y is orthogonal to col(X).

## Symbols
- `H` — the 'hat' matrix (it puts the hat on y), an orthogonal projector onto col(X)
- `I - H` — the residual-maker / annihilator matrix, projector onto col(X)^perp, rank n - p
- `h_ii` — the leverage of observation i -- its influence on its own fitted value; sum h_ii = p

## Epistemic status
proved_theorem  ·  regime: exact

## Prerequisites (tsort edges into this node)
linear_algebra_background, normal_equations

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: H = X(X^T X)^{-1} X^T: check H^T = H and H^2 = X(X^T X)^{-1}(X^T X)(X^T X)^{-1} X^T = H; rank = trace = tr((X^T X)^{-1} X^T X) = tr(I_p) = p
derives_from: linear_algebra_background
lean_status: instance — validation/proof-checks.lean Stat.hat_matrix_idempotent -- H^2 = H and tr(H) = p for a fixed integer 3x2 design via decide

## Type / well-formedness check
A geometric statement: least squares IS orthogonal projection. Uses linear_algebra_background (projection matrices, idempotency, rank = trace for idempotents). H and I - H being complementary orthogonal projectors of ranks p and n - p is what drives every distributional result below (via Cochran).

## Specialization / boundary cases
- one predictor = the constant: H = (1/n) J, y_hat_i = ybar for all i -- 'regression on an intercept' is just the mean
- leverage h_ii in [1/n, 1]; h_ii > 2p/n flags a high-leverage point
- the Pythagorean decomposition ||y||^2 = ||Hy||^2 + ||(I-H)y||^2 is the ANOVA / R^2 identity

## Hypothesis-dropped counterexamples
- **X_full_rank**: rank-deficient X: H is still the (unique) projector onto col(X), of rank rank(X) < p; beta_hat is non-unique but y_hat = Hy is unique

## Common misuse
- interpreting a coefficient without checking leverage / influence diagnostics (a single high-leverage point can determine beta_hat)
- forgetting sum of leverages = p when judging whether a design spreads influence well

## Related nodes (non-prerequisite)
- required_by: residual_sum_of_squares, partitioned_regression
- uses: normal_equations, linear_algebra_background

## Sources
seber_lee_linear_regression, hoaglin_welsch_1978
