# random_variable

## Type
definition

## Statement
A random variable is a measurable function X: (Omega, F, P) -> (R, B(R)). A random vector is the R^d-valued case. { X in B } := X^{-1}(B) in F for every Borel B, so P(X in B) is defined.

## Symbols
- `X` — the random variable, type: Omega -> R measurable
- `(Omega, F, P)` — the base probability space, type: probability space

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
borel_sigma_algebra, measurable_function, probability_space

## Hypotheses
(none — unconditional within scope)

## Well-definedness
measurability makes { X <= x } an event for every x, so the CDF and the pushforward law are well-defined; sums, products, and limits of random variables are random variables.

## Type / well-formedness check
a random variable is not random and not a variable -- it is a fixed measurable function; the randomness is in P. Two random variables can be equal in law without being equal as functions. sigma(X) = X^{-1}(B(R)) is the information X carries.

## Specialization / boundary cases
- X = 1_A: a Bernoulli random variable
- X constant = c: measurable w.r.t. any F; sigma(X) = { empty, Omega }
- X = g(Y) for measurable g: sigma(X) subset sigma(Y) (Doob-Dynkin)

## Hypothesis-dropped counterexamples
- **measurability**: an arbitrary function Omega -> R (e.g. the indicator of a non-measurable set) is not a random variable -- P(X in B) is undefined

## Common misuse
- treating X(omega) as 'the random outcome' rather than a function
- assuming equality in distribution implies equality a.s.

## Related nodes (non-prerequisite)
- used_by: distribution_pushforward, expectation, independence_random_variables
- generalizes_to: random element of a Polish space

## Sources
billingsley_probability_measure, durrett_pte
