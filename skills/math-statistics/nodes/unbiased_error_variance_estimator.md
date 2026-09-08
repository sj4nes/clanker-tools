# unbiased_error_variance_estimator

## Type
proposition

## Statement
In the linear model, sigma_hat^2 = RSS / (n - p) is unbiased for sigma^2: E[sigma_hat^2] = sigma^2, for any error distribution with mean 0, variance sigma^2, and uncorrelated components (no normality needed).

## Symbols
- `n - p` — the residual / error degrees of freedom -- observations minus fitted parameters
- `the MLE (Gaussian) divides by n` — and is biased low by a factor (n-p)/n

## Epistemic status
proposition  ·  regime: exact

## Prerequisites (tsort edges into this node)
linear_algebra_background, prob_expectation_linearity, residual_sum_of_squares

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: E[eps^T A eps] = sigma^2 tr(A) for Cov(eps) = sigma^2 I; here A = I - H, tr(I - H) = n - p
derives_from: prob_expectation_linearity
lean_status: instance — validation/proof-checks.lean Stat.rss_expectation -- E[eps^T(I-H)eps] = sigma^2 tr(I-H); the trace identity tr(I - H) = n - p for a fixed integer design via decide, reusing Stat.bias_sample_var's E[quadratic form] algebra

## Type / well-formedness check
An exact identity, distribution-free (only E[eps]=0, Cov(eps) = sigma^2 I needed). Proof: E[RSS] = E[eps^T (I - H) eps] = sigma^2 tr(I - H) = sigma^2 (n - p). The regression generalization of bias_of_sample_variance (which is the p = 1, X = 1 case, giving n - 1).

## Specialization / boundary cases
- p = 1 (intercept only): n - p = n - 1, recovers S^2 (bias_of_sample_variance)
- sigma_hat = sqrt(sigma_hat^2) is the 'residual standard error' printed in every regression summary
- the SEs of the coefficients are sigma_hat sqrt( ((X^T X)^{-1})_jj )

## Hypothesis-dropped counterexamples
- **Cov(eps) = sigma^2 I**: heteroskedastic or autocorrelated errors: E[RSS/(n-p)] != sigma^2 (there is no single sigma^2); the model-based SEs are wrong -- use White / Newey-West robust SEs
- **correct_mean_model**: omitted nonlinearity inflates RSS, so sigma_hat^2 is biased UP -- the lack-of-fit test exploits this

## Common misuse
- using the divisor n (the MLE) and reporting biased-low SEs
- trusting sigma_hat^2 and the coefficient SEs when residual plots show non-constant variance

## Related nodes (non-prerequisite)
- uses: residual_sum_of_squares, prob_expectation_linearity, linear_algebra_background
- generalizes_from: bias_of_sample_variance

## Sources
seber_lee_linear_regression, casella_berger_2e
