# beta_distribution

## Type
definition

## Statement
X ~ Beta(a, b), a, b > 0: density f_X(x) proportional to x^{a-1} (1-x)^{b-1} on (0, 1) (normalizer B(a,b) = Gamma(a)Gamma(b)/Gamma(a+b)). E[X] = a/(a+b), Var(X) = ab / ((a+b)^2 (a+b+1)).

## Symbols
- `X` — a beta variable, type: Omega -> (0,1)
- `a, b` — shape parameters, type: positive real

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
expectation, pdf, variance

## Hypotheses
(none — unconditional within scope)

## Well-definedness
the Beta function B(a,b) = integral_0^1 x^{a-1}(1-x)^{b-1} dx converges for a, b > 0 and normalizes the density.

## Type / well-formedness check
the canonical family for a random PROBABILITY or proportion. Beta(1,1) = Uniform(0,1). It is the conjugate prior for a Bernoulli/binomial rate: prior Beta(a,b) + k successes in n trials -> posterior Beta(a + k, b + n - k).

## Specialization / boundary cases
- a = b = 1: Uniform(0,1)
- a = b: symmetric about 1/2; a = b large: concentrated near 1/2 (approx normal)
- a, b < 1: U-shaped, mass near 0 and 1
- the k-th order statistic of n iid Uniform(0,1) is Beta(k, n - k + 1)
- if Y_1 ~ Gamma(a, 1), Y_2 ~ Gamma(b, 1) independent, then Y_1/(Y_1 + Y_2) ~ Beta(a, b)

## Hypothesis-dropped counterexamples
- **support_is_the_unit_interval**: for a proportion that can be exactly 0 or 1, a zero-or-one-inflated beta is needed; plain beta puts zero mass on the endpoints

## Common misuse
- using it for a quantity outside [0,1] without rescaling
- reading Beta(a,b) mean as a/b (it is a/(a+b))

## Related nodes (non-prerequisite)
- conjugate_to: bernoulli_distribution, binomial_distribution
- generalizes: continuous_uniform_distribution on (0,1)
- multivariate: Dirichlet

## Sources
grimmett_stirzaker, durrett_pte
