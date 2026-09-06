# correlation

## Type
definition

## Statement
rho(X, Y) = Cov(X, Y) / (sd(X) sd(Y)), defined when Var(X), Var(Y) in (0, inf). rho in [-1, 1]; |rho| = 1 iff Y is a.s. an affine function of X.

## Symbols
- `rho` — the correlation coefficient, type: real in [-1,1]
- `X, Y` — random variables with positive finite variance, type: L^2(P)

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
cauchy_schwarz_expectation, covariance, variance

## Hypotheses
(none — unconditional within scope)

## Well-definedness
requires sd(X), sd(Y) > 0 (non-degenerate) and finite; then |Cov(X,Y)| <= sd(X) sd(Y) by Cauchy-Schwarz, so rho in [-1, 1].

## Type / well-formedness check
the scale-invariant, dimensionless version of covariance -- the cosine of the angle between the centered variables in L^2(P). The bound |rho| <= 1 is Cauchy-Schwarz applied to the centered variables.

## Specialization / boundary cases
- Y = aX + b, a > 0: rho = 1; a < 0: rho = -1
- X, Y independent: rho = 0
- bivariate normal: rho is the single parameter governing dependence -- and here rho = 0 DOES imply independence

## Hypothesis-dropped counterexamples
- **positive_finite_variances**: a constant Y has sd(Y) = 0 -- rho is 0/0, undefined
- **linearity_of_the_relationship**: Y = X^2 with X ~ Uniform(-1,1): perfect functional dependence but rho = 0 -- correlation only sees LINEAR association

## Common misuse
- reading rho = 0 as independence (only true for jointly normal)
- reading |rho| near 1 as 'causation' or as a good fit for a nonlinear relationship
- comparing rho across samples of very different range (restriction of range attenuates rho)

## Related nodes (non-prerequisite)
- normalizes: covariance
- bounded_by: cauchy_schwarz_expectation

## Sources
grimmett_stirzaker, durrett_pte
