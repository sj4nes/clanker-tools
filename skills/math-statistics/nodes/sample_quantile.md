# sample_quantile

## Type
definition

## Statement
The sample p-quantile is F_hat_n^{-1}(p) = inf{ x : F_hat_n(x) >= p }, essentially the order statistic X_(ceil(np)); it is the plug-in estimate of the population quantile Q(p) = F^{-1}(p).

## Symbols
- `Q(p) = F^{-1}(p)` — the population quantile being estimated
- `the sample median` — p = 1/2

## Epistemic status
definition  ·  regime: distribution_free

## Prerequisites (tsort edges into this node)
empirical_cdf, order_statistic

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: Bahadur representation: q_hat(p) = Q(p) + (p - F_hat_n(Q(p))) / f(Q(p)) + o_p(n^{-1/2}); then the CLT for F_hat_n(Q(p))
derives_from: empirical_cdf
lean_status: cited

## Type / well-formedness check
A statistic (an order statistic, up to interpolation convention -- there are ~9 in common use). When F has positive density f(Q(p)) at the quantile, sqrt(n)(q_hat(p) - Q(p)) -> N(0, p(1-p) / f(Q(p))^2).

## Specialization / boundary cases
- sample median of iid N(mu, sigma^2): sqrt(n)(median - mu) -> N(0, pi sigma^2 / 2) -- asymptotic variance pi/2 times that of Xbar (ARE 2/pi, relative_efficiency)
- distribution-free CI for Q(p): [X_(r), X_(s)] with r, s from the Binomial(n, p) quantiles -- exact coverage, no density needed
- the sample quantile function traced over p is the Q-Q-plot ordinate

## Hypothesis-dropped counterexamples
- **positive_density_at_the_quantile**: if f(Q(p)) = 0 (a gap in the support, or estimating an extreme quantile p -> 0) the sqrt(n)-normal limit fails -- the rate and shape change
- **unique_quantile**: a flat stretch of F at level p makes Q(p) an interval; the sample quantile is unstable there

## Common misuse
- reporting a normal-approximation SE for a sample quantile without a density estimate (the f(Q(p)) in the variance is itself hard to estimate) -- prefer the distribution-free order-statistic interval
- estimating a 0.999 quantile from n = 200 observations -- essentially no information in the tail

## Related nodes (non-prerequisite)
- uses: order_statistic, empirical_cdf

## Sources
van_der_vaart_asymptotic, hyndman_fan_1996
