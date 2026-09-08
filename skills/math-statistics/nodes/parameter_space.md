# parameter_space

## Type
definition

## Statement
The parameter space Theta is the set of admissible parameter values; the model is indexed by it.

## Symbols
- `Theta` — the parameter space, type: subset of R^d
- `int(Theta)` — its interior; theta_0 in int(Theta) is a standard regularity condition

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
parametric_model

## Hypotheses
(none — unconditional within scope)
## Well-definedness
Constraints defining Theta (sigma^2 > 0, p in [0,1], a correlation in [-1,1], a covariance matrix positive definite) are part of the model specification.

## Type / well-formedness check
Theta is a set; 'admissible' means the modeller asserts every theta in Theta is a priori possible and no theta outside it is.

## Specialization / boundary cases
- Theta = (0, inf) for a variance or a rate
- Theta = [0, 1] for a probability -- note the boundary points, where interior-point regularity fails
- Theta = R^d for a location / regression-coefficient vector
- Theta = { positive definite d x d matrices } for a covariance parameter

## Hypothesis-dropped counterexamples
- **admissibility_of_the_constraint**: if the true p is 0 or 1 (on the boundary of [0,1]) the MLE is still consistent but sqrt(n)-asymptotic normality fails -- the limit is one-sided

## Common misuse
- forgetting that a boundary true value breaks the interior-point regularity condition
- using an unconstrained optimizer that leaves Theta (a negative variance estimate)

## Related nodes (non-prerequisite)
- commonly_confused_with: null_hypothesis

## Sources
casella_berger_2e, lehmann_casella_tpe
