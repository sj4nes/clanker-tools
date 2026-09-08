# normal_mean_ci_unknown_variance

## Type
proposition

## Statement
For X_1..X_n iid N(mu, sigma^2) with sigma^2 UNKNOWN, the interval Xbar +- t_{n-1, 1-alpha/2} S / sqrt(n) has coverage exactly 1 - alpha for every (mu, sigma^2). This is 'the' confidence interval for a mean.

## Symbols
- `t_{n-1, 1-alpha/2}` — the upper alpha/2 quantile of t_{n-1} (> z, converging to it as n grows)
- `the width 2 t S/sqrt(n)` — now RANDOM through S

## Epistemic status
proposition  ·  regime: exact

## Prerequisites (tsort edges into this node)
pivot_method, t_statistic_distribution

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: pivot method with Q = sqrt(n)(Xbar - mu)/S ~ t_{n-1}
derives_from: t_statistic_distribution
lean_status: core

## Type / well-formedness check
Exact. Invert the pivot sqrt(n)(Xbar - mu)/S ~ t_{n-1} (t_statistic_distribution). The t quantile (wider than z) is the exact price of estimating sigma.

## Specialization / boundary cases
- n = 2, alpha = 0.05: t_{1, 0.975} = 12.7 -- the interval is enormous, honestly reflecting near-zero information about sigma
- n >= 30: t_{n-1} approx z, the t- and z-intervals nearly coincide
- paired data: apply to the within-pair differences

## Hypothesis-dropped counterexamples
- **normality**: for skewed data at small n coverage departs from 1 - alpha (the t-interval is more robust than the chi^2 variance interval but not immune); a bootstrap-t or BCa interval can do better
- **iid**: positively correlated observations => S underestimates Var(Xbar) => the interval is too narrow => undercoverage

## Common misuse
- using z instead of t at small n (undercoverage)
- applying it to a proportion with small np (use Wilson / Clopper-Pearson)
- reporting it after choosing the outcome variable based on which gave the smallest p-value

## In the wild
- the default 'mean +- CI' in every statistics package, spreadsheet, and scientific paper
- dual to the one-sample t-test (confidence_set_test_duality)

## Related nodes (non-prerequisite)
- uses: pivot_method, t_statistic_distribution
- approximates: wald_interval
- commonly_confused_with: normal_mean_ci_known_variance

## Sources
student_1908, casella_berger_2e
