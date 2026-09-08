# interchange_derivative_integral

## Type
hypothesis

## Statement
d/dtheta int f(x; theta) dmu(x) = int d/dtheta f(x; theta) dmu(x), and likewise for int g(x) f(x; theta): the theta-derivative passes under the integral sign.

## Symbols
- `f(x; theta)` — the density
- `the dominating condition` — |d/dtheta f(x; theta)| <= h(x) locally, with int h dmu < inf

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
dominated_family, ra_interchange_limit_integral

## Hypotheses
(none — unconditional within scope)
## Well-definedness
A regularity condition on the model; typically verified once via a dominating function.

## Type / well-formedness check
The hypothesis of the measure-theoretic 'differentiation under the integral' theorem (ra_interchange_limit_integral supplies the sufficient condition). Needed twice: once for the score identity, once more for the information equality.

## Specialization / boundary cases
- exponential families on their natural parameter's interior: holds automatically (analyticity of A)
- N, Poisson, Gamma, Beta in their standard parametrizations: holds
- the sufficient condition (ra_interchange_limit_integral): a local integrable envelope for the theta-derivative

## Hypothesis-dropped counterexamples
- **interchange_derivative_integral**: combine with a moving support (uniform(0, theta)) or heavy tails and the swap introduces a boundary term or diverges: E[score] != 0, so score_identity, information_equality, cramer_rao_lower_bound all fail. The robust replacement is the sandwich variance.

## Common misuse
- treating it as automatic -- it is the single most-skipped hypothesis in applied derivations
- assuming that because the MLE 'worked' the interchange was valid

## Related nodes (non-prerequisite)
- required_by: score_identity, information_equality, cramer_rao_lower_bound
- licensed_by: ra_interchange_limit_integral

## Sources
lehmann_casella_tpe, schervish_theory_of_statistics
