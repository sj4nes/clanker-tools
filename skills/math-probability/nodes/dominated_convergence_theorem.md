# dominated_convergence_theorem

## Type
bridge

## Statement
If f_n -> f a.e. and |f_n| <= g a.e. for an integrable g, then f is integrable and integral f_n dmu -> integral f dmu (and integral |f_n - f| dmu -> 0).

## Symbols
- `f_n, f` — measurable functions, type: Omega -> R
- `mu` — a (sigma-finite) measure, type: measure

## Epistemic status
proved_theorem

## Prerequisites (tsort edges into this node)
abstract_integral, sequence_limit

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
- **integrable_dominator_g**: f_n = n 1_{(0, 1/n]} on ([0,1], lambda): f_n -> 0 a.e. but integral f_n = 1; no integrable g dominates (sup_n f_n is not integrable)

## Common misuse
- applying the wrong theorem for the situation (MCT needs monotone; DCT needs a dominator; Fatou only gives an inequality)

## Related nodes (non-prerequisite)
- developed_in: a future math-measure-and-integration capsule

## Sources
folland_real_analysis, billingsley_probability_measure
