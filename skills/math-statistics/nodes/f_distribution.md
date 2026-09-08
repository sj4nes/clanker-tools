# f_distribution

## Type
construction

## Statement
The F distribution with (d1, d2) degrees of freedom is the law of F = (U/d1) / (V/d2) where U ~ chi^2_{d1} is independent of V ~ chi^2_{d2}. Mean d2/(d2 - 2) for d2 > 2.

## Symbols
- `d1, d2` — numerator and denominator degrees of freedom
- `F_{d1,d2}` — the distribution on (0, inf)

## Epistemic status
constructive_result  ·  regime: exact

## Prerequisites (tsort edges into this node)
chi_squared_distribution, prob_independence_rv

## Hypotheses
(none — unconditional within scope)
## Well-definedness
Ratio of a.s.-positive independent variables; density by change of variables.

## Type / well-formedness check
A construction (ratio of two independent scaled chi-squares). Well-defined for d1, d2 > 0. If T ~ t_k then T^2 ~ F_{1,k}. 1/F_{d1,d2} ~ F_{d2,d1}.

## Specialization / boundary cases
- d1 = 1: F_{1,d2} = (t_{d2})^2
- d2 -> inf: d1 * F_{d1,d2} -> chi^2_{d1} (the denominator -> 1)
- the ANOVA and regression overall-F tests use F_{q, n-p}

## Hypothesis-dropped counterexamples
- **independence_U_V**: in an unbalanced or misspecified ANOVA the numerator and denominator sums of squares can be dependent -- the nominal F reference is then wrong (Cochran's theorem is exactly the check that they are independent)
- **both_chi_squared**: under the alternative, U is NONCENTRAL chi^2 -- the test statistic has a noncentral F distribution, which is how power is computed

## Common misuse
- reporting an F-test after a data-driven model search without accounting for selection -- the null F distribution assumes the models were fixed in advance
- using F for a variance-ratio test with non-normal data -- the F-test for equal variances is notoriously non-robust to non-normality (unlike the t-test for means)

## In the wild
- the overall significance test in every linear regression and ANOVA table
- the F-test for nested model comparison; Levene's / Bartlett's variance-homogeneity checks

## Related nodes (non-prerequisite)
- required_by: f_test_equality_of_variances, overall_f_test

## Sources
casella_berger_2e, fisher_1924
