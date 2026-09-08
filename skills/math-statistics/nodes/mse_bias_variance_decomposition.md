# mse_bias_variance_decomposition

## Type
identity

## Statement
MSE(theta) = Var_theta(theta_hat) + b(theta)^2: mean squared error equals variance plus squared bias.

## Symbols
- `Var_theta(theta_hat)` — the sampling variance of the estimator
- `b(theta) = E_theta[theta_hat] - theta` — the bias

## Epistemic status
mathematical_identity  ·  regime: exact

## Prerequisites (tsort edges into this node)
bias, mean_squared_error, prob_expectation_linearity, prob_variance

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: expand the square (theta_hat - theta)^2 = (theta_hat - E theta_hat)^2 + 2(theta_hat - E theta_hat)(E theta_hat - theta) + (E theta_hat - theta)^2 and take expectations; middle term vanishes
derives_from: prob_expectation_linearity
lean_status: core — validation/proof-checks.lean Stat.mse_decomp -- E[(t - c)^2] = E[(t - E t)^2] + (E t - c)^2 with c = theta, over the finite-support model of E

## Type / well-formedness check
An exact algebraic identity, not an approximation. Proof: write theta_hat - theta = (theta_hat - E theta_hat) + (E theta_hat - theta); square; the cross term is 2 (E theta_hat - theta) E[theta_hat - E theta_hat] = 0.

## Specialization / boundary cases
- unbiased estimator: MSE = Var (bias term drops)
- the constant estimator theta_hat = c: Var = 0, MSE = (c - theta)^2 -- all bias
- ridge / shrinkage: trades a small positive bias^2 for a larger Var reduction, lowering MSE over a region of theta

## Hypothesis-dropped counterexamples
- **finite_second_moment**: if Var(theta_hat) = inf the identity reads inf = inf + b^2 and carries no information

## Common misuse
- citing 'bias-variance tradeoff' as if bias and variance always move oppositely -- they need not; some estimators improve both
- ignoring that the decomposition is pointwise in theta -- a shrinkage estimator wins for small ||theta||, loses for large

## In the wild
- the organizing principle of supervised machine learning: model complexity is tuned to minimize estimated MSE = bias^2 + variance (cross-validation, the double-descent curve)
- the MISE-optimal bandwidth of a kernel density estimator balances an O(h^4) squared bias against an O(1/(nh)) variance -- see kde_bias_variance_tradeoff

## Related nodes (non-prerequisite)
- required_by: james_stein, kde_bias_variance_tradeoff
- uses: bias, mean_squared_error

## Sources
casella_berger_2e, hastie_tibshirani_friedman_esl
