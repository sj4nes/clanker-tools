# lotus

## Type
theorem

## Statement
Law of the unconscious statistician: for measurable g, E[g(X)] = integral_R g dP_X, which equals sum_x g(x) p_X(x) (discrete) or integral g(x) f_X(x) dx (density) -- no need to find the law of g(X).

## Symbols
- `g` — a measurable function, type: R -> R
- `X` — a random variable, type: Omega -> R

## Epistemic status
proved_theorem

## Prerequisites (tsort edges into this node)
abstract_integral, distribution_pushforward, expectation, pdf, pmf

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: change of variables for the pushforward measure: true for indicators g = 1_B (definition of P_X), extend by linearity to simple g, by MCT to g >= 0, by parts to integrable g
derives_from: distribution_pushforward
lean_status: cited — Billingsley Thm 16.13

## Type / well-formedness check
the change-of-variables formula for the pushforward: integral_Omega (g o X) dP = integral_R g d(P o X^{-1}). Requires E[|g(X)|] < inf for a finite answer.

## Specialization / boundary cases
- g(x) = x: E[X] from the law directly
- g(x) = x^k: the k-th moment
- g(x) = e^{tx}: the MGF
- g(x) = 1_B(x): E[1_B(X)] = P(X in B)

## Hypothesis-dropped counterexamples
- **integrability_of_g_X**: g(x) = x on a Cauchy X: E[g(X)] = integral x/(pi(1+x^2)) dx does not converge absolutely -- LOTUS gives no finite value

## Common misuse
- computing the law of g(X) unnecessarily
- applying it when E[|g(X)|] = inf

## Related nodes (non-prerequisite)
- used_by: moment, mgf, characteristic_function, variance

## Sources
billingsley_probability_measure, durrett_pte
