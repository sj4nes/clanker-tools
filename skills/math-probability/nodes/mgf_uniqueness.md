# mgf_uniqueness

## Type
theorem

## Statement
If M_X(t) = M_Y(t) < inf for all t in an open interval around 0, then P_X = P_Y.

## Symbols
- `M_X, M_Y` — MGFs finite near 0, type: (-h, h) -> R

## Epistemic status
proved_theorem

## Prerequisites (tsort edges into this node)
distribution_pushforward, mgf

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: analytic continuation of M to the complex strip |Re z| < h; on the imaginary axis it is the characteristic function, whose inversion determines the law
derives_from: dynkin_pi_lambda
lean_status: cited — Billingsley Thm 30.1; Curtiss 1942

## Type / well-formedness check
finiteness on a neighborhood of 0 forces the law to have exponentially decaying tails, and such laws are determined by their moment sequence (the moment problem is determinate); alternatively the MGF extends to a strip in C and equals the CF, which always determines the law (cf_properties).

## Specialization / boundary cases
- sum of independent Poissons: M = product of exp(lambda_i(e^t - 1)) = exp((sum lambda_i)(e^t - 1)) => Poisson(sum lambda_i)
- sum of independent N(mu_i, sigma_i^2): M = exp(sum mu_i t + (sum sigma_i^2) t^2 / 2) => N(sum mu_i, sum sigma_i^2)

## Hypothesis-dropped counterexamples
- **finiteness_on_an_interval**: agreement of M_X and M_Y only AT t = 0 (both equal 1) says nothing; and two different laws can share every moment (lognormal and a discrete perturbation) -- but then neither has an MGF finite near 0

## Common misuse
- concluding P_X = P_Y from M_X = M_Y at finitely many points
- using MGF uniqueness for heavy-tailed laws (no MGF -- must use the CF)

## Related nodes (non-prerequisite)
- cf_analogue: phi_X = phi_Y => P_X = P_Y, UNCONDITIONALLY
- uses: dynkin_pi_lambda
- used_by: normal_affine_closure, poisson_limit_theorem

## Sources
billingsley_probability_measure, durrett_pte
