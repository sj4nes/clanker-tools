# expectation_linearity

## Type
theorem

## Statement
E[aX + bY] = a E[X] + b E[Y] for integrable X, Y. No independence needed. See results/expectation_linearity.yaml.

## Symbols
- `X, Y` — integrable random variables, type: L^1(P)

## Epistemic status
proved_theorem

## Prerequisites (tsort edges into this node)
abstract_integral, expectation

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: linearity of the Lebesgue integral
derives_from: abstract_integral
lean_status: core — validation/proof-checks.lean Prob.expectation_additivity

## Type / well-formedness check
see the hand-written results/expectation_linearity.yaml for the full treatment.

## Specialization / boundary cases
- indicators: E[sum 1_{A_i}] = sum P(A_i) -- mean of a count
- binomial mean np with no combinatorial sum

## Hypothesis-dropped counterexamples
- **integrability**: X ~ Cauchy, Y = -X: X + Y = 0 has mean 0 but E[X], E[Y] undefined

## Common misuse
- believing independence is required

## Related nodes (non-prerequisite)
- full_entry: results/expectation_linearity.yaml

## Sources
billingsley_probability_measure, durrett_pte
