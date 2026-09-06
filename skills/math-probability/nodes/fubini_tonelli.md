# fubini_tonelli

## Type
bridge

## Statement
For sigma-finite mu, nu: if f >= 0 (Tonelli) or f is (mu x nu)-integrable (Fubini), the double integral equals both iterated integrals.

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
- **sigma_finiteness_or_integrability**: f(x,y) = (x^2 - y^2)/(x^2 + y^2)^2 on (0,1)^2: the two iterated integrals are +pi/4 and -pi/4 -- f is not integrable, so Fubini does not apply

## Common misuse
- applying the wrong theorem for the situation (MCT needs monotone; DCT needs a dominator; Fatou only gives an inequality)

## Related nodes (non-prerequisite)
- developed_in: a future math-measure-and-integration capsule

## Sources
folland_real_analysis, billingsley_probability_measure
