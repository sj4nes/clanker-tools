# wilks_theorem

## Type
theorem

## Statement
Under H0 and the MLE regularity conditions, if Theta_0 is a smooth r-dimensional-lower subset of the d-dimensional Theta, then -2 log Lambda(X) -> chi^2_{d - r} in distribution as n -> inf, where d - r is the number of restrictions.

## Symbols
- `d - r = number of free parameters fixed by H0` — the chi^2 degrees of freedom
- `Lambda` — the GLR statistic

## Epistemic status
proved_theorem  ·  regime: asymptotic

## Prerequisites (tsort edges into this node)
chi_squared_distribution, fisher_information_positive_definite, likelihood_ratio_test, mle_asymptotic_normality, ra_taylor_theorem

## Hypotheses
true_parameter_interior, fisher_information_positive_definite, log_likelihood_smooth

## Proof provenance
technique: quadratic expansion of the log-likelihood at the two MLEs; -2 log Lambda = (score)^T (projection) (score) + o_p(1), a chi^2_{d-r} by Cochran-type algebra on the asymptotically N(0, I) score
derives_from: mle_asymptotic_normality
lean_status: cited — CITED -- Wilks 1938; van der Vaart Thm 16.7. The 'difference of two quadratic forms is chi^2_{d-r}' idempotency step reuses proof-checks.lean Stat.cochran_idempotent.

## Type / well-formedness check
An asymptotic null-distribution result -- it makes the LRT usable without deriving an exact null law. Proof: Taylor-expand ell around theta_hat and around theta_hat_0 (the constrained MLE); both expansions are quadratic forms in asymptotically-normal score vectors with covariance I; the difference is a chi^2_{d-r} by the projection/idempotency algebra.

## Specialization / boundary cases
- one restriction (d - r = 1): -2 log Lambda -> chi^2_1, and sqrt(-2 log Lambda) is asymptotically |N(0,1)| -- matches the Wald and score tests
- testing q of p regression coefficients zero: -2 log Lambda -> chi^2_q (and q F_{q, n-p} -> chi^2_q, so the exact F-test and Wilks agree in the limit)
- the LRT confidence region { theta_0 : -2 log Lambda(theta_0) <= chi^2_{d, 1-alpha} } -- the profile-likelihood region

## Hypothesis-dropped counterexamples
- **true_parameter_interior**: H0 on the boundary (sigma^2_component = 0, testing k vs k+1 mixture components): -2 log Lambda is NOT chi^2_r -- it is a mixture (e.g. 0.5 chi^2_0 + 0.5 chi^2_1) or has an even more complex limit. Using chi^2_r is conservative here.
- **log_likelihood_smooth**: non-regular models (uniform endpoint): -2 log Lambda has a non-chi^2 limit (often exponential-related)
- **nested_and_smooth_Theta_0**: if Theta_0 is not a smooth submanifold (e.g. a single point in a curved family, or a non-identified restriction) the df count d - r can be wrong

## Common misuse
- using chi^2_r critical values for variance-component or number-of-components tests (boundary null)
- trusting the chi^2 approximation at small n -- Bartlett's correction or a bootstrap null distribution is often needed
- counting restrictions wrong when Theta_0 is defined by nonlinear constraints

## In the wild
- the reference distribution for essentially every 'likelihood ratio test' / 'analysis of deviance' reported in applied statistics
- sequential testing of the number of factors / components / change-points

## Related nodes (non-prerequisite)
- uses: likelihood_ratio_test, mle_asymptotic_normality, chi_squared_distribution
- required_by: three_tests_asymptotically_equivalent, pearson_chi_squared_gof

## Sources
wilks_1938, van_der_vaart_asymptotic, self_liang_1987
