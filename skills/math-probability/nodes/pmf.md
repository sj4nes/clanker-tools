# pmf

## Type
definition

## Statement
The probability mass function of a discrete X is p_X(x) = P(X = x). It satisfies p_X >= 0 and sum_{x in S} p_X(x) = 1, and P(X in B) = sum_{x in B} p_X(x).

## Symbols
- `p_X` — the pmf, type: S -> [0,1]
- `S` — the countable support, type: countable set

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
discrete_rv, distribution_pushforward

## Hypotheses
(none — unconditional within scope)

## Well-definedness
sum_{x in S} P(X = x) = P(X in S) = 1 by countable additivity over the disjoint singletons; nonnegativity is immediate.

## Type / well-formedness check
the pmf is the density of P_X with respect to counting measure on S; it determines the discrete law completely.

## Specialization / boundary cases
- Bernoulli: p(1) = p, p(0) = 1 - p
- Poisson: p(k) = e^{-lambda} lambda^k / k!

## Hypothesis-dropped counterexamples
- **discreteness**: for an absolutely continuous X, p_X(x) = P(X = x) = 0 everywhere -- the object that works is the pdf

## Common misuse
- reading p_X(x) as a probability density (it is an actual probability)
- forgetting the normalization when constructing a model

## Related nodes (non-prerequisite)
- analogue_of: pdf (counting vs Lebesgue reference measure)
- used_by: lotus, expectation

## Sources
billingsley_probability_measure, durrett_pte
