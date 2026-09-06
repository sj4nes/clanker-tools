# continuous_uniform_distribution

## Type
definition

## Statement
X ~ Uniform(a, b): density f_X(x) = 1/(b - a) on [a, b], 0 elsewhere. E[X] = (a+b)/2, Var(X) = (b-a)^2/12. CDF F_X(x) = (x - a)/(b - a) on [a, b].

## Symbols
- `X` — a uniform variable, type: Omega -> [a,b]
- `a < b` — the endpoints, type: real

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
expectation, pdf, variance

## Hypotheses
(none — unconditional within scope)

## Well-definedness
f_X >= 0 and integral_a^b 1/(b-a) dx = 1; well-defined for any a < b.

## Type / well-formedness check
the maximum-entropy law on a bounded interval; the target of the probability integral transform (F_X(X) ~ Uniform(0,1)) and the source for inversion sampling (F^{-1}(U) ~ any law).

## Specialization / boundary cases
- Uniform(0,1): the RNG primitive; E = 1/2, Var = 1/12
- -log(U) ~ Exponential(1); U^{1/n} ~ Beta(n, 1); (U_1, ..., U_n) order statistics ~ Beta
- sum of 12 iid Uniform(0,1) minus 6 is approximately N(0,1) (a crude Gaussian generator)

## Hypothesis-dropped counterexamples
- **bounded_support**: there is no uniform distribution on R or on (0, inf) -- 'improper uniform' priors are not probability measures (they still yield proper posteriors sometimes)

## Common misuse
- assuming a uniform prior is 'non-informative' (it is not invariant under reparameterization)
- using Var = (b-a)^2/4 (that is the range squared over 4, not the variance)

## Related nodes (non-prerequisite)
- transform_target: probability_integral_transform
- order_statistics: beta_distribution

## Sources
grimmett_stirzaker, durrett_pte
