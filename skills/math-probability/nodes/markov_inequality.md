# markov_inequality

## Type
theorem

## Statement
X >= 0, a > 0 => P(X >= a) <= E[X]/a. See results/markov_inequality.yaml.

## Symbols
- `X` — a nonnegative random variable, type: Omega -> [0, inf)

## Epistemic status
proved_theorem

## Prerequisites (tsort edges into this node)
expectation, expectation_monotonicity, indicator_rv, probability_measure

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: a 1_{X>=a} <= X pointwise, take expectations
derives_from: expectation_monotonicity
lean_status: core — validation/proof-checks.lean Prob.markov_finite

## Type / well-formedness check
see the hand-written results/markov_inequality.yaml for the full treatment.

## Specialization / boundary cases
- X = (Y - EY)^2, a = k^2: Chebyshev
- X = e^{tY}: Chernoff

## Hypothesis-dropped counterexamples
- **X_nonnegative**: a mean-0 symmetric two-point X has P(X >= a) = 1/2 while E[X]/a = 0

## Common misuse
- applying to a signed variable

## Related nodes (non-prerequisite)
- full_entry: results/markov_inequality.yaml

## Sources
billingsley_probability_measure, durrett_pte
