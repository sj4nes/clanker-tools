# dvoretzky_kiefer_wolfowitz

## Type
theorem

## Statement
The DKW inequality: P( sup_x | F_hat_n(x) - F(x) | > t ) <= 2 exp(-2 n t^2) for every t > 0 and every F (Massart's tight constant 2). Hence [F_hat_n(x) +- eps_n] with eps_n = sqrt( log(2/alpha) / (2n) ) is a simultaneous 1 - alpha confidence band for the whole CDF.

## Symbols
- `eps_n = sqrt( log(2/alpha) / (2n) )` — the half-width of the distribution-free simultaneous band
- `the bound is uniform in F` — distribution-free and finite-sample -- no asymptotics

## Epistemic status
proved_theorem  ·  regime: distribution_free

## Prerequisites (tsort edges into this node)
empirical_cdf, prob_hoeffding

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: reduction to a one-sided bound via a reflection/peeling argument, then a Hoeffding-type bound on the maximal deviation; Massart 1990 for the sharp constant 2
derives_from: prob_hoeffding
lean_status: cited — CITED -- Dvoretzky-Kiefer-Wolfowitz 1956; Massart 1990 (tight constant). The connection to Hoeffding's bound on each F_hat_n(x) - F(x) is the entry point.

## Type / well-formedness check
A finite-sample, distribution-free concentration inequality for the sup-distance -- the quantitative (rate) form of Glivenko-Cantelli. It gives an honest confidence BAND for F, unlike pointwise CLT intervals.

## Specialization / boundary cases
- n = 100, alpha = 0.05: eps_n approx 0.136 -- a band +-0.136 around F_hat_n contains the entire true F with 95% confidence
- gives a conservative distribution-free Kolmogorov-Smirnov critical value (the exact KS null is slightly tighter)
- sample size for a band of half-width eps: n = log(2/alpha) / (2 eps^2)

## Hypothesis-dropped counterexamples
- **iid**: for dependent data the exponential rate degrades; block or spectral corrections are needed
- **the_2_constant**: the pre-Massart bound had a larger constant; using exp(-2nt^2) without the factor 2 in front slightly undercovers for the two-sided band

## Common misuse
- using pointwise +-1.96 sqrt(F_hat(1-F_hat)/n) intervals and drawing them as a band -- that band undercovers substantially
- forgetting the band is for F itself, not for future observations (that would be a tolerance interval)

## In the wild
- honest confidence bands for CDFs and survival curves; distribution-free two-sample comparison
- off-policy evaluation in reinforcement learning uses DKW-style bounds on the CDF of returns

## Related nodes (non-prerequisite)
- strengthens: glivenko_cantelli
- uses: prob_hoeffding, empirical_cdf

## Sources
dkw_1956, massart_1990
