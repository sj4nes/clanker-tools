# t_statistic_distribution

## Type
theorem

## Statement
If X_1, ..., X_n are iid N(mu, sigma^2), then the studentized statistic sqrt(n) (Xbar - mu) / S ~ t_{n-1}, exactly, for every n >= 2.

## Symbols
- `sqrt(n)(Xbar - mu)/sigma ~ N(0,1)` — the numerator once sigma is put back
- `S/sigma = sqrt( [(n-1)S^2/sigma^2] / (n-1) )` — sqrt of a chi^2_{n-1}/(n-1)
- `n - 1` — the t degrees of freedom

## Epistemic status
proved_theorem  ·  regime: exact

## Prerequisites (tsort edges into this node)
normal_sample_mean_variance_independence, prob_normal_affine_closure, scaled_sample_variance_chi_squared, students_t_distribution

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: assemble the definition of t_{n-1} from Z ~ N(0,1), V ~ chi^2_{n-1}, Z _||_ V -- the three pieces supplied by the CLT-exact normal mean, the scaled sample variance, and the independence theorem
derives_from: students_t_distribution
lean_status: core — the assembly is definitional; the three inputs are their own nodes. instance-checks.bc tabulates t_{n-1} quantiles vs the normal for small n

## Type / well-formedness check
An exact sampling-distribution identity. Proof: sqrt(n)(Xbar - mu)/S = [ sqrt(n)(Xbar - mu)/sigma ] / [ S/sigma ] = Z / sqrt(V/(n-1)) with Z ~ N(0,1), V = (n-1)S^2/sigma^2 ~ chi^2_{n-1}, and Z _||_ V by normal_sample_mean_variance_independence. That is exactly the definition of t_{n-1}.

## Specialization / boundary cases
- n = 2: sqrt(2)(Xbar - mu)/S = (X_1 + X_2 - 2mu) / |X_1 - X_2| ~ t_1 = Cauchy -- the extreme small-sample case, infinitely heavy tails
- n large: t_{n-1} -> N(0,1); for n >= 30 the difference in the 97.5th percentile is under 5%
- the pivot (it does not depend on mu or sigma) for the one-sample t confidence interval and test

## Hypothesis-dropped counterexamples
- **normality**: for skewed data at small n the statistic is not t-distributed (both Xbar/S independence and the chi^2 denominator fail); the t-test's actual level can be well off 5%. For large n the CLT + Slutsky rescue it (-> N(0,1)) REGARDLESS of the parent, which is why the t-test is 'robust in level' asymptotically but not for small skewed samples.
- **iid**: correlated observations inflate the true variance of Xbar while S^2 underestimates it -- the t-statistic is then too large and the test over-rejects

## Common misuse
- applying the exact t distribution to small, skewed samples and trusting the p-value to three digits
- using it after a data-dependent choice of which mean to test (multiplicity / selection)
- reading a non-significant small-n t-test as evidence of no effect (low power)

## In the wild
- the single most-used inferential procedure in the experimental sciences: the two-sample and paired t-tests, the regression coefficient t-tests
- Gosset's original 1908 use: n ~ 4 samples in Guinness's barley and brewing experiments

## Related nodes (non-prerequisite)
- uses: students_t_distribution, normal_sample_mean_variance_independence, scaled_sample_variance_chi_squared
- required_by: one_sample_t_test, two_sample_t_test, normal_mean_ci_unknown_variance, coefficient_t_test

## Sources
student_1908, casella_berger_2e
