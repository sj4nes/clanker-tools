# covariance

## Type
definition

## Statement
Cov(X, Y) = E[(X - E[X])(Y - E[Y])] = E[XY] - E[X]E[Y], defined when X, Y in L^2. Cov(X, X) = Var(X).

## Symbols
- `X, Y` — random variables in L^2(P), type: L^2(P)

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
expectation, expectation_linearity, variance

## Hypotheses
(none — unconditional within scope)

## Well-definedness
XY in L^1 by Cauchy-Schwarz (|E[XY]| <= ||X||_2 ||Y||_2 < inf); the centered form equals the raw form by linearity.

## Type / well-formedness check
a measure of linear co-variation; the product XY is integrable by Cauchy-Schwarz when X, Y in L^2. Cov > 0 / < 0 / = 0 means positive / negative / no linear association (NOT independence).

## Specialization / boundary cases
- Y = X: Cov(X, X) = Var(X)
- Y = aX + b: Cov(X, Y) = a Var(X)
- X, Y independent: Cov = 0 (independence_expectation)

## Hypothesis-dropped counterexamples
- **finite_second_moments**: if E[X^2] or E[Y^2] is infinite, E[XY] may not exist and Cov is undefined

## Common misuse
- reading Cov = 0 as independence (uncorrelated_not_independent)
- comparing covariances across different unit scales -- use correlation

## Related nodes (non-prerequisite)
- normalized_to: correlation
- bilinear_via: covariance_bilinear
- used_by: variance_of_sum

## Sources
billingsley_probability_measure, durrett_pte
