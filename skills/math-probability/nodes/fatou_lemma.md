# fatou_lemma

## Type
bridge

## Statement
For measurable f_n >= 0, integral (liminf f_n) dmu <= liminf integral f_n dmu.

## Symbols
- `f_n, f` — measurable functions, type: Omega -> R
- `mu` — a (sigma-finite) measure, type: measure

## Epistemic status
proved_theorem

## Prerequisites (tsort edges into this node)
abstract_integral, limsup_liminf

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
- **nonnegativity_f_n**: f_n = -1_{[n,n+1]}: liminf f_n = 0 with integral 0, but liminf integral f_n = -1 -- the inequality direction needs f_n >= 0

## Common misuse
- applying the wrong theorem for the situation (MCT needs monotone; DCT needs a dominator; Fatou only gives an inequality)

## Related nodes (non-prerequisite)
- developed_in: a future math-measure-and-integration capsule

## Sources
folland_real_analysis, billingsley_probability_measure
