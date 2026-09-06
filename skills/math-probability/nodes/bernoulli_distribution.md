# bernoulli_distribution

## Type
definition

## Statement
X ~ Bernoulli(p), p in [0,1]: P(X = 1) = p, P(X = 0) = 1 - p. E[X] = p, Var(X) = p(1-p), M_X(t) = 1 - p + p e^t. The indicator of a probability-p event.

## Symbols
- `X` — a Bernoulli variable, type: Omega -> {0,1}
- `p` — success probability, type: real in [0,1]

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
expectation, indicator_rv, mgf, pmf, variance

## Hypotheses
(none — unconditional within scope)

## Well-definedness
a two-point law with masses p and 1 - p summing to 1; well-defined for every p in [0,1].

## Type / well-formedness check
the building block: any event A gives 1_A ~ Bernoulli(P(A)). E[X] = E[X^2] = p (since X^2 = X), so Var = p - p^2.

## Specialization / boundary cases
- p = 1/2: the fair coin, maximum variance 1/4
- p in {0,1}: degenerate (constant), variance 0
- sum of n iid Bernoulli(p) = Binomial(n, p)

## Hypothesis-dropped counterexamples
- **p_in_0_1**: p outside [0,1] is not a probability

## Common misuse
- confusing the parameter p with the outcome
- forgetting Var is maximized at p = 1/2, not p = 1

## Related nodes (non-prerequisite)
- generalizes_to: binomial_distribution
- is: an indicator random variable (indicator_rv)

## Sources
grimmett_stirzaker, durrett_pte
