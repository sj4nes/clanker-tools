# uncorrelated_not_independent

## Type
counterexample

## Statement
Zero covariance does not imply independence. Example: X ~ Uniform(-1, 1), Y = X^2. Then Cov(X, Y) = E[X^3] - E[X] E[X^2] = 0 - 0 = 0, but Y is a deterministic function of X.

## Symbols
- `X` — Uniform(-1,1), type: Omega -> (-1,1)
- `Y` — X^2, type: Omega -> [0,1)

## Epistemic status
counterexample

## Prerequisites (tsort edges into this node)
continuous_uniform_distribution, covariance, independence_random_variables

## Hypotheses
(none — unconditional within scope)

## Well-definedness
E[X] = 0 and E[X^3] = 0 by symmetry, so Cov(X, X^2) = 0 exactly; yet sigma(Y) subset sigma(X) non-trivially.

## Type / well-formedness check
correlation measures only LINEAR association; the relationship here is purely quadratic (even), so it is invisible to covariance. P(Y < 1/4 | X > 1/2) = 0 != P(Y < 1/4), witnessing dependence.

## Specialization / boundary cases
- general principle: for any symmetric X with finite third moment, X and |X| (or X^2) are uncorrelated but dependent
- the one place the converse DOES hold: (X, Y) jointly Gaussian => uncorrelated implies independent

## Hypothesis-dropped counterexamples
- **this_IS_the_counterexample**: it shows independence_expectation is a one-way implication

## Common misuse
- concluding independence from a zero sample correlation
- using rho as a general dependence measure (it is not -- consider distance correlation / mutual information)
- assuming a regression with R^2 = 0 means no relationship

## Related nodes (non-prerequisite)
- limits: independence_expectation
- exception: jointly Gaussian (normal_distribution)

## Sources
grimmett_stirzaker, durrett_pte
