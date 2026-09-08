# empirical_cdf

## Type
definition

## Statement
The empirical CDF of X_1, ..., X_n is F_hat_n(x) = (1/n) sum_{i=1}^n 1{X_i <= x}: the CDF of the empirical distribution P_hat_n that puts mass 1/n at each observation.

## Symbols
- `F_hat_n` — the ECDF, a random right-continuous step function
- `P_hat_n` — the empirical measure

## Epistemic status
definition  ·  regime: distribution_free

## Prerequisites (tsort edges into this node)
iid_sample, prob_bernoulli, prob_cdf

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: pointwise: n F_hat_n(x) is a sum of iid Bernoulli(F(x)) indicators
derives_from: prob_bernoulli
lean_status: core

## Type / well-formedness check
A statistic-valued function. For each fixed x, n F_hat_n(x) ~ Binomial(n, F(x)), so E[F_hat_n(x)] = F(x) (unbiased) and Var(F_hat_n(x)) = F(x)(1 - F(x))/n. As a process it is the basis of all distribution-free inference.

## Specialization / boundary cases
- F_hat_n(x) -> F(x) a.s. pointwise (SLLN) and uniformly (Glivenko-Cantelli)
- sqrt(n)(F_hat_n(x) - F(x)) -> N(0, F(x)(1-F(x))) pointwise (CLT), -> a Brownian bridge as a process (Donsker)
- the inverse F_hat_n^{-1} gives sample quantiles

## Hypothesis-dropped counterexamples
- **none_all_hypotheses_essential**: the ECDF is defined for any sample; its consistency (Glivenko-Cantelli) needs only iid -- no moment or smoothness assumption

## Common misuse
- over-interpreting the jagged steps of F_hat_n at small n as features of F
- using pointwise CLT bands as if they were simultaneous (they undercover as a band -- use DKW)

## In the wild
- Q-Q plots, P-P plots, and the Kolmogorov-Smirnov / Cramer-von Mises goodness-of-fit tests are all built on F_hat_n
- survival analysis: the Kaplan-Meier estimator is the ECDF generalized to censored data

## Related nodes (non-prerequisite)
- required_by: glivenko_cantelli, dvoretzky_kiefer_wolfowitz, plug_in_estimator, bootstrap, sample_quantile
- uses: prob_bernoulli

## Sources
van_der_vaart_asymptotic, wasserman_all_of_statistics
