# donsker_theorem

## Type
theorem

## Statement
Donsker's theorem (the functional CLT for the empirical process): the empirical process G_n = sqrt(n)(F_hat_n - F) converges in distribution, in the space of bounded functions on R with the sup metric, to a tight mean-zero Gaussian process G -- the F-Brownian bridge, with Cov(G(s), G(t)) = F(s and t) - F(s)F(t). More generally, the empirical process indexed by a Donsker class of functions converges to a Gaussian process.

## Symbols
- `G_n` — the empirical process
- `G` — the limiting Gaussian process (Brownian bridge composed with F)
- `a Donsker class` — a function class over which this uniform CLT holds (finite uniform entropy / bracketing)

## Epistemic status
proved_theorem  ·  regime: distribution_free

## Prerequisites (tsort edges into this node)
empirical_cdf, glivenko_cantelli, prob_clt

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: finite-dimensional CLT + asymptotic tightness (stochastic equicontinuity) of the empirical process; for general classes, chaining under a uniform-entropy or bracketing-entropy condition
derives_from: glivenko_cantelli
lean_status: cited — CITED -- Donsker 1952; van der Vaart-Wellner 1996. Not formalized.

## Type / well-formedness check
The process-level strengthening of the pointwise CLT for F_hat_n, and the rate-level strengthening of Glivenko-Cantelli. It is the analytic engine behind the limiting null distributions of the Kolmogorov-Smirnov and Cramer-von Mises statistics, and behind the functional delta method (hence bootstrap consistency for smooth functionals). Boundary node: stated, cited.

## Specialization / boundary cases
- sup_x |G_n(x)| -> sup |Brownian bridge| gives the Kolmogorov-Smirnov limiting distribution (Kolmogorov's formula)
- int G_n^2 dF -> int (Brownian bridge)^2 gives the Cramer-von Mises limit
- the functional delta method: for Hadamard-differentiable T, sqrt(n)(T(F_hat_n) - T(F)) -> T'_F(G) -- the source of asymptotic normality for quantiles, trimmed means, L-statistics, and the bootstrap's validity

## Hypothesis-dropped counterexamples
- **Donsker_class**: the class of ALL indicator functions of finite sets is not Donsker -- and neither is a class with infinite uniform entropy; over such classes the empirical process does not converge (it is not even tight). This is what separates 'nice' nonparametric problems from genuinely hard ones.
- **iid**: dependent data need mixing conditions and give a different (long-range vs short-range) limit

## Common misuse
- assuming a supremum functional of the empirical process has a normal limit -- it has an extreme-value / Brownian-bridge-supremum limit
- invoking Donsker for a function class whose complexity (entropy) has not been checked

## Related nodes (non-prerequisite)
- uses: glivenko_cantelli, prob_clt, empirical_cdf
- strengthens: glivenko_cantelli, dvoretzky_kiefer_wolfowitz

## Sources
donsker_1952, van_der_vaart_wellner, billingsley_convergence_of_probability_measures
