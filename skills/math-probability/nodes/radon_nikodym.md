# radon_nikodym

## Type
bridge

## Statement
If nu << mu (nu(A) = 0 whenever mu(A) = 0) with mu, nu sigma-finite, there is a mu-a.e.-unique measurable h >= 0 with nu(A) = integral_A h dmu. h = dnu/dmu.

## Symbols
- `f_n, f` — measurable functions, type: Omega -> R
- `mu` — a (sigma-finite) measure, type: measure

## Epistemic status
proved_theorem

## Prerequisites (tsort edges into this node)
abstract_integral, measure

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: cited construction from the abstract integral
derives_from: abstract_integral
lean_status: cited — Folland Real Analysis 2e ch. 2; Billingsley SS16

## Type / well-formedness check
CITED. The exchange-of-limit toolkit for the integral; each is stated for a general measure and specialised to P for expectations (MCT/DCT/Fatou for E, Fubini for E[XY] and convolutions).

## Specialization / boundary cases
- mu = P: the probability form used for E[lim] = lim E, differentiating an MGF, and Scheffe's lemma

## Hypothesis-dropped counterexamples
- **absolute_continuity_nu_ll_mu**: nu = delta_0, mu = Lebesgue on R: nu({0}) = 1 but mu({0}) = 0, so nu is NOT << mu and has no density; nu is purely singular

## Common misuse
- applying the wrong theorem for the situation (MCT needs monotone; DCT needs a dominator; Fatou only gives an inequality)

## Related nodes (non-prerequisite)
- developed_in: a future math-measure-and-integration capsule

## Sources
folland_real_analysis, billingsley_probability_measure
