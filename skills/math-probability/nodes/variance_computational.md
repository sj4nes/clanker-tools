# variance_computational

## Type
identity

## Statement
Var(X) = E[X^2] - (E[X])^2.

## Symbols
- `X` — a random variable in L^2(P), type: L^2(P)

## Epistemic status
mathematical_identity

## Prerequisites (tsort edges into this node)
expectation_linearity, variance

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: E[(X - EX)^2] = E[X^2] - 2 EX E[X] + (EX)^2 = E[X^2] - (EX)^2, by expectation_linearity
derives_from: expectation_linearity
lean_status: core — validation/proof-checks.lean Prob.centid (GENUINE, universal list-induction identity Sum p(x-m)^2 = Sum px^2 - 2m Sum px + m^2 Sum p)

## Type / well-formedness check
expand (X - E[X])^2 = X^2 - 2 E[X] X + E[X]^2 and apply linearity of expectation, treating E[X] as a constant.

## Specialization / boundary cases
- X ~ Bernoulli(p): E[X^2] = p, so Var = p - p^2 = p(1-p)
- X ~ Poisson(lambda): E[X^2] = lambda^2 + lambda, Var = lambda
- the sample analogue: (1/n) sum x_i^2 - xbar^2 -- but this is biased; divide by n-1 for the unbiased estimator

## Hypothesis-dropped counterexamples
- **finite_second_moment**: if E[X^2] = inf both sides are +inf (or ill-posed); the identity is only useful when Var is finite

## Common misuse
- the population-vs-sample n vs n-1 confusion (Bessel's correction)
- numerical catastrophic cancellation when E[X^2] and E[X]^2 are both large and close -- use a centered/streaming algorithm

## Related nodes (non-prerequisite)
- derives_from: expectation_linearity
- computes: variance

## Sources
billingsley_probability_measure, durrett_pte
