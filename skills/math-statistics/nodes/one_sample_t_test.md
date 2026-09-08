# one_sample_t_test

## Type
proposition

## Statement
For X_1..X_n iid N(mu, sigma^2), the test that rejects H0: mu = mu_0 when |sqrt(n)(Xbar - mu_0)/S| > t_{n-1, 1-alpha/2} has size exactly alpha; it is the two-sided UMP-unbiased test and the LRT for this problem.

## Symbols
- `t = sqrt(n)(Xbar - mu_0)/S` — the t-statistic, ~ t_{n-1} under H0 (t_statistic_distribution)
- `the one-sided version` — rejects when t > t_{n-1, 1-alpha}, UMP for H0: mu <= mu_0

## Epistemic status
proposition  ·  regime: exact

## Prerequisites (tsort edges into this node)
power_function, size_of_test, t_statistic_distribution

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: t_statistic_distribution: under H0 the statistic is exactly t_{n-1}, free of the nuisance sigma^2; so P_{H0}(|t| > t_{n-1,1-alpha/2}) = alpha for every sigma^2
derives_from: t_statistic_distribution
lean_status: core

## Type / well-formedness check
An exact-level test. The statistic is pivotal under the whole composite null {mu = mu_0, sigma^2 > 0} because its null law t_{n-1} does not involve sigma^2 -- so the size is alpha for every sigma^2.

## Specialization / boundary cases
- paired design: apply to the within-pair differences d_i = X_i - Y_i, testing H0: mean difference = 0
- one-sided: H0: mu <= mu_0 vs H1: mu > mu_0, reject for large t -- UMP by Karlin-Rubin (MLR in Xbar)
- the dual t confidence interval is Xbar +- t S/sqrt(n) (normal_mean_ci_unknown_variance)

## Hypothesis-dropped counterexamples
- **normality**: small skewed samples: the actual size deviates from alpha (up to ~0.08-0.10 for strongly skewed n ~ 10); large n rescues the LEVEL via the CLT (t -> N(0,1) regardless of parent) but not necessarily the power comparison
- **iid**: correlated data (repeated measures analysed as independent): the true SE of Xbar is underestimated, t is inflated, the test over-rejects badly

## Common misuse
- using it on clearly non-normal small samples instead of a signed-rank or bootstrap test
- running paired data as two independent samples (or vice versa)
- reading a non-significant result from an underpowered study as evidence of no effect

## In the wild
- the workhorse significance test of experimental psychology, biology, and medicine
- quality control: is a batch's mean within spec?

## Related nodes (non-prerequisite)
- uses: t_statistic_distribution, size_of_test
- special_case_of: likelihood_ratio_test
- dual_of: normal_mean_ci_unknown_variance

## Sources
student_1908, lehmann_romano_tsh
