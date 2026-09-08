# completeness_statistic

## Type
definition

## Statement
A statistic T is complete if E_theta[g(T)] = 0 for every theta implies g(T) = 0 almost surely (for every theta); bounded completeness restricts to bounded g.

## Symbols
- `g` — an arbitrary (measurable, or bounded) function on the range of T
- `the family of laws of T` — must be 'rich enough' to kill every unbiased-of-zero g

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
prob_expectation, statistic

## Hypotheses
(none — unconditional within scope)
## Well-definedness
A property of { law of T under P_theta : theta }.

## Type / well-formedness check
A property of the FAMILY of distributions of T, not of a single distribution. It says the only unbiased estimator of 0 based on T is 0 -- which forces uniqueness of unbiased estimators that are functions of T.

## Specialization / boundary cases
- full-rank exponential family: the natural sufficient statistic is complete (Laplace-transform uniqueness)
- uniform(0, theta): X_(n) is complete -- E_theta[g(X_(n))] = 0 for all theta forces g = 0 by differentiating in theta
- Bernoulli count sum X_i in {0,...,n}: complete (a degree-n polynomial with n+1 roots is zero)

## Hypothesis-dropped counterexamples
- **completeness**: N(theta, theta^2) curved family: T = (sum X_i, sum X_i^2) is sufficient but E_theta[2(sum X_i)^2 - (n+1) sum X_i^2] = 0 for all theta with the bracket not identically 0 -- not complete. Lehmann-Scheffe then cannot certify a UMVUE.

## Common misuse
- asserting completeness for a curved or parameter-restricted family
- confusing completeness (about the family of laws of T) with sufficiency (about conditional laws given T)

## Related nodes (non-prerequisite)
- required_by: basu_theorem, lehmann_scheffe_theorem, exponential_family_completeness
- commonly_confused_with: minimal_sufficiency

## Sources
lehmann_casella_tpe, lehmann_romano_tsh
