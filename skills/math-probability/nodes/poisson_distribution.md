# poisson_distribution

## Type
definition

## Statement
X ~ Poisson(lambda), lambda > 0: P(X = k) = e^{-lambda} lambda^k / k! for k = 0, 1, 2, .... E[X] = Var(X) = lambda. M_X(t) = exp(lambda(e^t - 1)).

## Symbols
- `X` — a Poisson count, type: Omega -> {0,1,2,...}
- `lambda` — the rate / mean, type: positive real

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
expectation, mgf, pmf, series_convergence, variance

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: mean: sum k e^{-lambda} lambda^k/k! = lambda sum e^{-lambda} lambda^{k-1}/(k-1)! = lambda. Variance via E[X(X-1)] = lambda^2 then Var = lambda^2 + lambda - lambda^2. MGF: sum e^{tk} e^{-lambda} lambda^k/k! = e^{-lambda} e^{lambda e^t}
derives_from: series_convergence
lean_status: core — validation/instance-checks.bc -- Poisson(2) E and Var = 2

## Type / well-formedness check
the law of counts of rare events: the limit of Binomial(n, lambda/n) as n -> inf (poisson_limit_theorem), and the one-parameter family with equal mean and variance. Sums of independent Poissons are Poisson (rates add).

## Specialization / boundary cases
- number of decay events per second; typos per page; arrivals in a fixed interval of a Poisson process
- lambda large: Poisson(lambda) approx N(lambda, lambda) (a CLT via the sum-of-Poissons representation)
- the index of dispersion Var/mean = 1 -- overdispersed count data (Var > mean) needs negative binomial instead

## Hypothesis-dropped counterexamples
- **lambda_gt_0**: lambda = 0 degenerates to X = 0 a.s.
- **equal_mean_and_variance**: real count data with Var > mean (contagion, heterogeneity) is NOT Poisson -- fitting Poisson underestimates the variance and overstates significance

## Common misuse
- using Poisson for overdispersed counts
- assuming independence of counts in disjoint intervals without the Poisson-process assumption

## Related nodes (non-prerequisite)
- limit_of: binomial_distribution (poisson_limit_theorem)
- overdispersed_alternative: negative binomial
- process_version: Poisson process (boundary)

## Sources
grimmett_stirzaker, durrett_pte
