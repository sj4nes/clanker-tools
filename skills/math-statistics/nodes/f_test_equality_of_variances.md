# f_test_equality_of_variances

## Type
proposition

## Statement
For independent normal samples of sizes n and m, S_X^2 / S_Y^2 ~ F_{n-1, m-1} under H0: sigma_X^2 = sigma_Y^2; reject when the ratio is outside [F_{n-1,m-1,alpha/2}, F_{n-1,m-1,1-alpha/2}]. Exact under normality, but highly non-robust to non-normality.

## Symbols
- `the ratio of sample variances` — each S^2 scaled to a chi^2, the ratio is an F

## Epistemic status
proposition  ·  regime: exact

## Prerequisites (tsort edges into this node)
f_distribution, scaled_sample_variance_chi_squared, size_of_test

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: (n-1)S_X^2/sigma_X^2 ~ chi^2_{n-1} _||_ (m-1)S_Y^2/sigma_Y^2 ~ chi^2_{m-1}; under H0 the sigma^2's cancel in the ratio, giving F_{n-1,m-1} by definition
derives_from: f_distribution
lean_status: core

## Type / well-formedness check
Exact under normality (ratio of independent scaled chi-squares). Its Achilles heel: the F-test for variances is extremely sensitive to kurtosis -- far more than the t-test for means. Levene's and Brown-Forsythe tests are robust alternatives.

## Specialization / boundary cases
- used as a (poor) preliminary check before a pooled two-sample t-test -- this two-stage procedure is now discouraged; just use Welch
- one-sided: test whether a new process REDUCES variance
- k-sample generalization: Bartlett's test (also non-robust) or Levene's test (robust)

## Hypothesis-dropped counterexamples
- **normality**: with heavy-tailed data (kurtosis > 3) the F-test for variances has true size FAR above nominal -- e.g. 0.20 at nominal 0.05 for t_5 data. This is the textbook example of a procedure that must not be used without near-exact normality.
- **independence**: paired or correlated samples invalidate the chi^2 factorization

## Common misuse
- using it to 'justify' pooling in a two-sample t-test (the two-stage procedure has poor overall properties)
- applying it to non-normal data -- prefer Levene / Brown-Forsythe

## Related nodes (non-prerequisite)
- uses: f_distribution, scaled_sample_variance_chi_squared
- robust_alternative: 

## Sources
casella_berger_2e, box_1953
