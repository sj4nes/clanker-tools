# ordinary_least_squares

## Type
definition

## Statement
The ordinary least squares estimator is beta_hat = argmin_{b in R^p} || y - X b ||^2: the coefficient vector minimizing the residual sum of squares.

## Symbols
- `|| y - X b ||^2 = sum_i (y_i - x_i^T b)^2` — the least-squares criterion
- `beta_hat = (X^T X)^{-1} X^T y` — the closed-form solution (normal_equations)

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
linear_model, ra_differentiability

## Hypotheses
(none — unconditional within scope)
## Type / well-formedness check
A definition via an optimization problem. The objective is strictly convex in b when X has full column rank, so the minimizer is unique and given by the normal equations. OLS = MLE under Gaussian errors; OLS = method of moments for the moment condition E[X eps] = 0.

## Specialization / boundary cases
- p = 1, no intercept: beta_hat = sum x_i y_i / sum x_i^2
- simple regression: slope = Cov_hat(x, y)/Var_hat(x), intercept = ybar - slope xbar
- OLS = MLE of beta under eps ~ N(0, sigma^2 I) (maximizing the Gaussian likelihood minimizes the SSE)

## Hypothesis-dropped counterexamples
- **full_rank_X**: collinear X: the argmin is a whole affine subspace; OLS is undefined (ridge / pseudoinverse picks the minimum-norm solution)

## Common misuse
- fitting OLS with more predictors than observations (p > n) -- no unique solution, need regularization
- including a variable and its exact linear function (dummy-variable trap)
- interpreting a coefficient's sign/magnitude without noting it is 'holding the other X fixed', which may be impossible in the data

## Related nodes (non-prerequisite)
- required_by: normal_equations, gauss_markov_theorem, partitioned_regression
- uses: linear_model
- special_case_of: 

## Sources
seber_lee_linear_regression, casella_berger_2e
