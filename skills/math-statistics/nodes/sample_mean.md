# sample_mean

## Type
definition

## Statement
The sample mean of X_1, ..., X_n is Xbar_n = (1/n) sum_{i=1}^n X_i.

## Symbols
- `Xbar_n` — the sample mean, type: statistic valued in R (or R^k)

## Epistemic status
definition  ·  regime: exact

## Prerequisites (tsort edges into this node)
iid_sample, prob_expectation_linearity

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: linearity of expectation for the mean; independence for the /n variance
derives_from: prob_expectation_linearity
lean_status: core — E[(1/n) sum X_i] = (1/n) sum E[X_i]; the finite-support instance is proof-checks.lean Stat.sample_mean_linear

## Type / well-formedness check
A statistic (no theta). E_theta[Xbar] = E_theta[X_1] (linearity), Var_theta(Xbar) = Var_theta(X_1)/n (iid). Sufficient for the mean in a normal or exponential-family location model.

## Specialization / boundary cases
- Xbar is the MLE of mu in N(mu, sigma^2), the UMVUE of the mean, and the method-of-moments estimator -- all coincide
- Xbar -> E[X_1] a.s. (SLLN) and sqrt(n)(Xbar - mu) -> N(0, sigma^2) (CLT)
- for a normal sample, Xbar ~ N(mu, sigma^2/n) EXACTLY (not just asymptotically)

## Hypothesis-dropped counterexamples
- **finite_mean**: Xbar of iid Cauchy is again Cauchy(mu, 1) -- it does not concentrate and is a useless estimator of the center (use the median)

## Common misuse
- reporting Xbar +- SD (the spread of the data) instead of Xbar +- SE = Xbar +- SD/sqrt(n) (the spread of the estimate)
- using Xbar for a heavy-tailed or contaminated sample -- one outlier moves it arbitrarily

## Related nodes (non-prerequisite)
- required_by: sample_variance, normal_sample_mean_variance_independence, normal_mean_ci_known_variance

## Sources
casella_berger_2e
