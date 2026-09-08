# ols_distribution_under_normal_errors

## Type
theorem

## Statement
In the linear model with eps ~ N(0, sigma^2 I): beta_hat ~ N(beta, sigma^2 (X^T X)^{-1}), RSS/sigma^2 ~ chi^2_{n-p}, and beta_hat is independent of RSS. Hence every coefficient contrast is exactly normal and studentizes to an exact t.

## Symbols
- `sigma^2 (X^T X)^{-1}` — the exact covariance of beta_hat; its j-th diagonal is Var(beta_hat_j)
- `beta_hat _||_ RSS` — the multivariate analogue of Xbar _||_ S^2, from H and I - H being orthogonal projectors

## Epistemic status
proved_theorem  ·  regime: exact

## Prerequisites (tsort edges into this node)
cochran_theorem, linear_algebra_background, normal_equations, normal_sample_mean_variance_independence, prob_normal_affine_closure

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: beta_hat linear-in-Gaussian => Gaussian with the stated moments; (Hy, (I-H)y) orthogonal projections of N(mu, sigma^2 I) => independent, and (I-H)y-part gives RSS/sigma^2 ~ chi^2_{n-p} (Cochran)
derives_from: cochran_theorem
lean_status: cited — the independence-of-orthogonal-Gaussian-projections step is proof-checks.lean Stat.gaussian_orthogonal_independent, reused from the normal_sample_mean_variance_independence node

## Type / well-formedness check
An exact finite-sample distributional result. beta_hat = (X^T X)^{-1} X^T y is a fixed linear map of the Gaussian y, hence Gaussian; RSS is a quadratic form in (I - H) y; H y (which determines beta_hat) and (I - H) y are orthogonal linear images of a spherical Gaussian, hence independent (Cochran).

## Specialization / boundary cases
- p = 1, X = 1: beta_hat = Xbar ~ N(mu, sigma^2/n), RSS/sigma^2 ~ chi^2_{n-1} -- exactly the one-sample normal results
- the coefficient t-statistic (beta_hat_j - beta_j)/(sigma_hat sqrt((X^TX)^{-1}_jj)) ~ t_{n-p} exactly (coefficient_t_test)
- a linear-hypothesis F-statistic ~ F_{q, n-p} exactly (overall_f_test)

## Hypothesis-dropped counterexamples
- **gaussian_errors**: non-normal errors: beta_hat is only ASYMPTOTICALLY normal (CLT for (X^T X)^{-1} X^T eps, valid if no single row of X dominates -- max leverage h_ii -> 0); RSS/sigma^2 is not chi^2; the t/F p-values are approximate
- **homoskedastic_uncorrelated**: Cov(eps) = sigma^2 V != sigma^2 I: beta_hat ~ N(beta, sigma^2 (X^TX)^{-1} X^T V X (X^TX)^{-1}) -- the 'sandwich' covariance; the naive (X^TX)^{-1} SEs are wrong

## Common misuse
- trusting exact t/F inference with small n and heavy-tailed or heteroskedastic residuals
- using the model-based covariance when a few points have very high leverage (the CLT for beta_hat then converges slowly)

## Related nodes (non-prerequisite)
- uses: normal_equations, cochran_theorem, prob_normal_affine_closure
- required_by: coefficient_t_test, overall_f_test
- strengthens: gauss_markov_theorem

## Sources
seber_lee_linear_regression, rao_linear_statistical_inference
