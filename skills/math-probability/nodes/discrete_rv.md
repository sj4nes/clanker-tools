# discrete_rv

## Type
definition

## Statement
X is discrete if it takes values in a countable set S (its support); equivalently P(X in S) = 1 for some countable S.

## Symbols
- `X` — a random variable, type: Omega -> R
- `S` — the countable support, type: countable subset of R

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
countable_set, random_variable

## Hypotheses
(none — unconditional within scope)

## Well-definedness
a countable S with P(X in S) = 1 makes P_X purely atomic; the smallest such S is { x : P(X = x) > 0 }.

## Type / well-formedness check
the law is then a countable sum of point masses P_X = sum_{x in S} p_X(x) delta_x, entirely described by the pmf.

## Specialization / boundary cases
- S finite: a simple random variable, a finite sum of indicators
- S = N: e.g. Poisson, geometric

## Hypothesis-dropped counterexamples
- **countability_of_S**: if the smallest such S is uncountable then no pmf exists -- e.g. any absolutely continuous X has P(X = x) = 0 for every x

## Common misuse
- assuming every random variable is discrete or continuous (mixed and singular laws exist)

## Related nodes (non-prerequisite)
- used_by: pmf, conditional_expectation_elementary
- complement_of: absolutely_continuous_rv

## Sources
billingsley_probability_measure, durrett_pte
