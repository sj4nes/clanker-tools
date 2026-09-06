# distribution_pushforward

## Type
definition

## Statement
The distribution (law) of X is the probability measure P_X on (R, B(R)) defined by P_X(B) = P(X in B) = P(X^{-1}(B)). It is the pushforward P o X^{-1}.

## Symbols
- `P_X` — the law of X, type: probability measure on B(R)
- `X` — a random variable, type: Omega -> R

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
measure, preimage_algebra, probability_measure, random_variable

## Hypotheses
(none — unconditional within scope)

## Well-definedness
P_X inherits countable additivity from P via the preimage algebra (X^{-1} commutes with countable disjoint unions); P_X(R) = P(Omega) = 1.

## Type / well-formedness check
P_X packages everything about X that does not depend on the underlying Omega; equality in law is P_X = P_Y. The pushforward of a probability measure by a measurable map is a probability measure (preimage of B(R) is a sigma-algebra, countable additivity transfers).

## Specialization / boundary cases
- X discrete: P_X = sum_x p_X(x) delta_x
- X absolutely continuous: P_X(B) = integral_B f_X dlambda
- X = c constant: P_X = delta_c

## Hypothesis-dropped counterexamples
- **measurability_of_X**: without it X^{-1}(B) need not be an event and P_X(B) is undefined

## Common misuse
- conflating the law P_X (a measure on R) with the random variable X (a function on Omega)
- assuming P_X determines X (it does not -- only up to equality in law)

## Related nodes (non-prerequisite)
- used_by: cdf, expectation, lotus
- equivalent_to: the CDF F_X (cdf_determines_law)

## Sources
billingsley_probability_measure, durrett_pte
