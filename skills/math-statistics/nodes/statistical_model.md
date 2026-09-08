# statistical_model

## Type
structure

## Statement
A statistical model is a family P = { P_theta : theta in Theta } of candidate probability laws for the observed data on a common sample space.

## Symbols
- `P` — the model (a set of probability laws)
- `P_theta` — the law indexed by theta, type: probability measure on the sample space
- `Theta` — the index set, type: an arbitrary set (parametric if a subset of R^d)
- `(X, A)` — the sample space and its sigma-algebra

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
prob_probability_space

## Hypotheses
(none — unconditional within scope)
## Well-definedness
Nothing to check beyond: each P_theta is a genuine probability measure. The model is an assumption about the data-generating mechanism, not a derived object.

## Type / well-formedness check
P_theta is a probability measure for each theta; Theta is a set; the map theta -> P_theta need not be injective (that is identifiability) or continuous.

## Specialization / boundary cases
- Theta a single point: the model is fully specified, no inference to do
- Theta = all laws on X: the fully nonparametric model
- Theta a subset of R^d: a parametric model (next node)

## Common misuse
- conflating the model with the truth -- 'all models are wrong'; the true law need not lie in P (misspecification)
- letting a statistic or the data enter the definition of P_theta

## Related nodes (non-prerequisite)
- specializes_to: parametric_model
- commonly_confused_with: identifiability

## Sources
casella_berger_2e, lehmann_casella_tpe
