# two_sample_t_test

## Type
proposition

## Statement
For independent normal samples X_1..X_n ~ N(mu_X, sigma^2) and Y_1..Y_m ~ N(mu_Y, sigma^2) with EQUAL variances, the pooled statistic (Xbar - Ybar - delta_0) / (S_p sqrt(1/n + 1/m)) ~ t_{n+m-2} under H0: mu_X - mu_Y = delta_0, giving an exact-level test. When variances are unequal, Welch's statistic with Satterthwaite degrees of freedom is used (approximate).

## Symbols
- `S_p^2 = [(n-1)S_X^2 + (m-1)S_Y^2] / (n+m-2)` — the pooled variance estimate
- `Welch df` — nu = (S_X^2/n + S_Y^2/m)^2 / [ (S_X^2/n)^2/(n-1) + (S_Y^2/m)^2/(m-1) ]

## Epistemic status
proposition  ·  regime: exact

## Prerequisites (tsort edges into this node)
prob_normal_affine_closure, size_of_test, t_statistic_distribution

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: Xbar - Ybar ~ N(mu_X - mu_Y, sigma^2(1/n + 1/m)); (n+m-2)S_p^2/sigma^2 ~ chi^2_{n+m-2} independent of it (sum of two independent scaled sample variances); assemble the t definition
derives_from: t_statistic_distribution
lean_status: core

## Type / well-formedness check
Exact under normality + equal variances (the pooled statistic is pivotal, ~ t_{n+m-2}). Welch's version is only approximately t-distributed (the Behrens-Fisher problem has no exact solution with a pivotal statistic).

## Specialization / boundary cases
- n = m and equal variances: pooled and Welch give nearly identical results
- very unequal variances or sample sizes: pooled test can be badly miscalibrated -- Welch is the safer default (and is now the default in R's t.test)
- the ANOVA F-test with k = 2 groups equals the pooled two-sample t^2

## Hypothesis-dropped counterexamples
- **equal_variances_for_the_pooled_version**: n=5 with sigma_X = 1 and m=50 with sigma_Y = 4: the pooled t-test's true size can be 0.15+ at nominal 0.05 -- pooling a large-sample large-variance group drags S_p^2 wrongly. Use Welch.
- **normality**: same small-sample skew caveat as the one-sample test
- **independence_between_samples**: matched/paired data must use the one-sample test on differences -- treating pairs as independent throws away the pairing and usually loses power

## Common misuse
- defaulting to the equal-variance pooled test without checking (or just using Welch, which costs little when variances ARE equal)
- analysing paired data as two independent samples

## In the wild
- comparing a treatment and control group mean -- the single most common hypothesis test in the applied sciences and in A/B testing

## Related nodes (non-prerequisite)
- uses: t_statistic_distribution, prob_normal_affine_closure
- special_case_of: overall_f_test

## Sources
welch_1947, lehmann_romano_tsh, casella_berger_2e
