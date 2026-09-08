# gauss_markov_theorem

## Type
theorem

## Statement
In the linear model with E[eps] = 0 and Cov(eps) = sigma^2 I (NO normality, NO independence beyond uncorrelatedness), the OLS estimator c^T beta_hat is the best linear unbiased estimator (BLUE) of c^T beta for every c: among all estimators a^T y that are linear in y and unbiased for c^T beta, OLS has the smallest variance.

## Symbols
- `BLUE` — Best (min variance) Linear Unbiased Estimator
- `'linear'` — linear in the response y (a^T y for a fixed vector a)
- `the competitor` — any a^T y with E[a^T y] = c^T beta for all beta

## Epistemic status
proved_theorem  ·  regime: exact

## Prerequisites (tsort edges into this node)
linear_algebra_background, ordinary_least_squares, prob_covariance, unbiased_estimator

## Hypotheses
unbiased_estimator

## Proof provenance
technique: decompose a competing linear unbiased estimator as OLS plus d^T y with X^T d = 0; the variance is Var(OLS) + sigma^2 ||d||^2, cross term killed by X^T d = 0
derives_from: linear_algebra_background
lean_status: core — validation/proof-checks.lean Stat.gauss_markov_cross_term -- the cross term c^T (X^T X)^{-1} X^T d = 0 given X^T d = 0, and Var = Var_OLS + sigma^2 ||d||^2 >= Var_OLS, for a fixed integer design via decide

## Type / well-formedness check
An exact, finite-sample optimality result within the linear-unbiased class, requiring only first and second moments of eps. Proof: write any linear unbiased estimator as c^T beta_hat + d^T y with d^T X = 0 (unbiasedness); then Var = Var(c^T beta_hat) + sigma^2 ||d||^2 + 2 sigma^2 c^T (X^T X)^{-1} X^T d, and the cross term is 0 because X^T d = 0; so Var = Var(c^T beta_hat) + sigma^2 ||d||^2 >= Var(c^T beta_hat).

## Specialization / boundary cases
- OLS is BLUE even for heavy-tailed (finite-variance) errors -- normality is NOT needed for this
- with normal errors, OLS is additionally the MVUE among ALL unbiased estimators (not just linear), and is the MLE
- if Cov(eps) = sigma^2 V (known V != I): GLS beta_hat_GLS = (X^T V^{-1} X)^{-1} X^T V^{-1} y is BLUE, and OLS is no longer efficient

## Hypothesis-dropped counterexamples
- **Cov(eps) = sigma^2 I**: heteroskedasticity (Cov(eps) = diag(sigma_i^2)): OLS is still unbiased but NOT BLUE -- weighted least squares with weights 1/sigma_i^2 beats it; and OLS's usual SEs are wrong
- **autocorrelated errors (time series)**: OLS inefficient; GLS / Cochrane-Orcutt or Newey-West SEs needed
- **linearity_and_correct_mean**: if E[y] != X beta, OLS is biased and 'BLUE' is moot

## Common misuse
- citing Gauss-Markov to claim OLS is 'optimal' when errors are heteroskedastic or correlated -- it is not, and the theorem's hypotheses are exactly what fails
- believing Gauss-Markov requires normal errors (it does not) or delivers optimality among all (not just linear) estimators (it does not, without normality)

## In the wild
- the theoretical warrant for defaulting to OLS in applied regression -- and, by its failure cases, the motivation for WLS, GLS, FGLS, and robust standard errors throughout econometrics

## Related nodes (non-prerequisite)
- uses: ordinary_least_squares, linear_algebra_background, prob_covariance
- strengthened_by: ols_distribution_under_normal_errors

## Sources
rao_linear_statistical_inference, seber_lee_linear_regression
