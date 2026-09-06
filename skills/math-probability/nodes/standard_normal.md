# standard_normal

## Type
definition

## Statement
Z ~ N(0, 1): density phi(z) = e^{-z^2/2} / sqrt(2 pi), CDF Phi(z) = integral_{-inf}^z phi. E[Z] = 0, Var(Z) = 1, phi_Z(t) = e^{-t^2/2}, all odd moments 0, E[Z^{2k}] = (2k-1)!!.

## Symbols
- `Z` — a standard normal variable, type: Omega -> R
- `Phi` — its CDF, type: R -> (0,1)

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
characteristic_function, normal_distribution, transformation_univariate

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: Z = (X - mu)/sigma for X ~ N(mu, sigma^2) via transformation_univariate; phi_Z(t) = e^{-t^2/2} by completing the square in E[e^{itZ}]
derives_from: transformation_univariate
lean_status: core — validation/instance-checks.bc -- Phi(1) = 0.8413...

## Type / well-formedness check
the reference point: any N(mu, sigma^2) variable is mu + sigma Z, and any normal probability reduces to Phi. The CLT limit is stated as convergence to Z.

## Specialization / boundary cases
- Phi(0) = 1/2; Phi(1) approx 0.8413; Phi(1.96) approx 0.975 (the 95% two-sided quantile)
- Z^2 ~ chi-squared_1; Z_1/Z_2 ~ Cauchy for independent Z_i; sum of k iid Z_i^2 ~ chi-squared_k
- Mills ratio: P(Z > z)/phi(z) -> 1/z as z -> inf

## Hypothesis-dropped counterexamples
- **none_it_is_a_fixed_law**: the standard normal is a single distribution; the caution is downstream (assuming data is standard normal after a bad standardization)

## Common misuse
- using a normal-approximation quantile (1.96) when the sample is small or heavy-tailed (use t)
- confusing phi (density) with Phi (CDF)

## Related nodes (non-prerequisite)
- rescales_to: normal_distribution
- clt_limit: central_limit_theorem
- squares_to: chi-squared

## Sources
billingsley_probability_measure, durrett_pte
