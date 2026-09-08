# scaled_sample_variance_chi_squared

## Type
theorem

## Statement
If X_1, ..., X_n are iid N(mu, sigma^2), then (n - 1) S^2 / sigma^2 ~ chi^2_{n-1}, independent of Xbar.

## Symbols
- `(n-1) S^2/sigma^2 = sum (X_i - Xbar)^2 / sigma^2` — a sum of squared standardized residuals
- `n - 1` — df: n standardized observations minus 1 linear constraint (they are centered at Xbar)

## Epistemic status
proved_theorem  ·  regime: exact

## Prerequisites (tsort edges into this node)
chi_squared_distribution, cochran_theorem, normal_sample_mean_variance_independence, prob_normal

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: Cochran: decompose chi^2_n = Q_1 + Q_2 with Q_2 = squared standardized Xbar ~ chi^2_1 independent of Q_1 = (n-1)S^2/sigma^2; ranks 1 + (n-1) = n force Q_1 ~ chi^2_{n-1}
derives_from: cochran_theorem
lean_status: instance — the rank/idempotency bookkeeping (projection I - (1/n) J has rank n-1, is idempotent) is proof-checks.lean Stat.centering_projection_rank for fixed n via trace = rank for a symmetric idempotent

## Type / well-formedness check
An exact distributional identity. Proof: write sum ((X_i - mu)/sigma)^2 = sum ((X_i - Xbar)/sigma)^2 + ((Xbar - mu)/(sigma/sqrt n))^2. The left side is chi^2_n; the last term is chi^2_1 and (by the independence theorem) independent of the first; so the first is chi^2_{n-1} by the subtractive form of chi-squared additivity (Cochran).

## Specialization / boundary cases
- n = 2: S^2 = (X_1 - X_2)^2 / 2, so S^2/sigma^2 = ((X_1 - X_2)/(sigma sqrt 2))^2 ~ chi^2_1 -- matches n - 1 = 1
- gives E[S^2] = sigma^2 (mean of chi^2_{n-1} is n-1) and Var(S^2) = 2 sigma^4/(n-1)
- the pivot for the normal-variance confidence interval (normal_variance_ci)

## Hypothesis-dropped counterexamples
- **normality**: for non-normal data (n-1)S^2/sigma^2 is not chi^2_{n-1}; its mean is still n-1 (bias_of_sample_variance holds generally) but its variance and shape depend on the kurtosis. The chi^2 variance interval is then badly miscalibrated -- far worse than the t interval for the mean is under non-normality.

## Common misuse
- using the chi^2_{n-1} reference for a variance CI with visibly non-normal data -- this procedure has NO robustness
- using chi^2_n (forgetting the lost df from centering)

## Related nodes (non-prerequisite)
- uses: cochran_theorem, normal_sample_mean_variance_independence
- required_by: t_statistic_distribution, normal_variance_ci, f_test_equality_of_variances

## Sources
casella_berger_2e, cochran_1934
