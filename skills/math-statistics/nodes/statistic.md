# statistic

## Type
definition

## Statement
A statistic is a measurable function T = T(X_1, ..., X_n) of the sample that does not depend on theta.

## Symbols
- `T` — the statistic, type: measurable map X^n -> Y (some measurable space)
- `T(X)` — its value on the sample, type: random element of Y

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
iid_sample, prob_random_variable

## Hypotheses
(none — unconditional within scope)
## Well-definedness
T(X) is a random variable because T is measurable and X is; its law depends on theta through the law of X.

## Type / well-formedness check
Measurability is the only formal requirement. The 'no theta' clause is what makes T computable from data alone -- an estimator, a test statistic, a sufficient statistic are all statistics.

## Specialization / boundary cases
- the sample mean, sample variance, order statistics, the maximum -- all statistics
- the sample itself, X = (X_1,...,X_n), is the trivial (always sufficient) statistic
- a constant map is a (useless, always ancillary) statistic

## Hypothesis-dropped counterexamples
- **no_theta_dependence**: sum_i (X_i - mu_0)^2 with a KNOWN mu_0 is a statistic; sum_i (X_i - mu)^2 with the unknown true mu is NOT a statistic -- it cannot be computed

## Common misuse
- calling a quantity a statistic when it secretly uses the unknown parameter (e.g. 'standardize by the true sigma')
- forgetting that the LAW of a statistic still depends on theta -- 'statistic' does not mean 'pivotal'

## Related nodes (non-prerequisite)
- specializes_to: estimator, test_function, sufficiency, ancillary_statistic

## Sources
casella_berger_2e
