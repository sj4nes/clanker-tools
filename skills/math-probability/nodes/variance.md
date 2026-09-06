# variance

## Type
definition

## Statement
Var(X) = E[(X - E[X])^2], defined when E[X^2] < inf. sd(X) = sqrt(Var(X)). Var(X) >= 0, with Var(X) = 0 iff X is a.s. constant.

## Symbols
- `X` — a random variable with E[X^2] < inf, type: L^2(P)
- `sd(X)` — standard deviation, type: nonnegative real

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
expectation, expectation_linearity

## Hypotheses
(none — unconditional within scope)

## Well-definedness
(X - E[X])^2 >= 0 so its expectation is well-defined in [0, inf]; finite iff E[X^2] < inf (expand and use E[X]^2 < inf).

## Type / well-formedness check
the mean squared deviation from the mean; needs a finite second moment (which by moment_ladder implies a finite first moment, so E[X] exists). It is the L^2(P) squared distance from X to the constant E[X].

## Specialization / boundary cases
- X = 1_A: Var = P(A)(1 - P(A)), maximized at P(A) = 1/2
- X = c constant: Var = 0
- X ~ N(mu, sigma^2): Var = sigma^2 (the parameter)

## Hypothesis-dropped counterexamples
- **finite_second_moment**: X ~ t-distribution with 2 degrees of freedom, or Cauchy: E[X^2] = inf, Var undefined -- the CLT fails, the sample variance does not stabilize

## Common misuse
- reporting Var in the units of X^2 when sd is wanted
- assuming Var(X + Y) = Var(X) + Var(Y) without uncorrelatedness

## Related nodes (non-prerequisite)
- requires: lp_space (L^2)
- computed_by: variance_computational
- used_by: chebyshev_inequality, covariance

## Sources
billingsley_probability_measure, durrett_pte
