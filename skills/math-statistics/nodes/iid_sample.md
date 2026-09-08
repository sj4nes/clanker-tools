# iid_sample

## Type
definition

## Statement
An i.i.d. sample of size n from the model is X_1, ..., X_n drawn independently, all from one common P_theta in P.

## Symbols
- `n` — the sample size, type: positive integer
- `X_i` — the i-th observation, type: random element of the sample space
- `X` — the whole sample (X_1,...,X_n), type: random element of X^n

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
prob_iid, statistical_model

## Hypotheses
(none — unconditional within scope)
## Well-definedness
The observations share the sample space and the sigma-algebra; 'identically distributed' fixes one theta.

## Type / well-formedness check
Joint law is the n-fold product P_theta^{(n)}. One theta governs all n observations (not one per observation).

## Specialization / boundary cases
- n = 1: a single observation; the likelihood is f(x_1; theta)
- the joint density is prod_{i=1}^n f(x_i; theta) -- the product structure is what makes the log-likelihood a SUM
- non-iid extensions (regression with fixed covariates, time series) replace the product by the actual joint density

## Hypothesis-dropped counterexamples
- **independence**: if the X_i are positively correlated, the effective sample size is below n; a variance estimate treating them as independent is too small and confidence intervals undercover
- **identical_distribution**: if each X_i has its own theta_i there is nothing to estimate without a link; the model is not a fixed-d parametric model

## Common misuse
- applying iid-sample theory to clustered or longitudinal data (students within schools) without a random-effects or cluster-robust adjustment
- treating a convenience sample as a random sample from the target population

## Related nodes (non-prerequisite)
- required_by: likelihood_function, sample_mean, empirical_cdf

## Sources
casella_berger_2e
