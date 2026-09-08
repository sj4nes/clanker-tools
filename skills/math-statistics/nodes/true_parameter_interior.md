# true_parameter_interior

## Type
hypothesis

## Statement
The true parameter theta_0 lies in the interior of Theta, not on its boundary.

## Symbols
- `theta_0` — the (unknown) data-generating parameter
- `int(Theta)` — the topological interior of the parameter space

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
parameter_space

## Hypotheses
(none — unconditional within scope)
## Well-definedness
An assumption about the truth; unverifiable from data but often defensible (a variance is not exactly 0, a probability is not exactly 1).

## Type / well-formedness check
A location statement about theta_0 relative to Theta. It is what allows a two-sided Taylor expansion of the score around theta_0 and guarantees the MLE is eventually an interior stationary point.

## Specialization / boundary cases
- theta_0 = 1/2 for a Bernoulli p in (0,1): interior, holds
- theta_0 on the boundary: p = 0, a variance component = 0, a correlation = 1

## Hypothesis-dropped counterexamples
- **true_parameter_interior**: testing H0: sigma^2_between = 0 in a random-effects model -- the null is on the boundary of [0, inf). The LRT statistic -2 log Lambda is NOT chi^2_1 under H0; it is a 50:50 mixture of chi^2_0 and chi^2_1 (Self-Liang / Chernoff). Using the chi^2_1 critical value makes the test conservative.
- **also**: p_hat for a truly-degenerate coin (p = 0): sqrt(n)(p_hat - 0) does not converge to a two-sided normal

## Common misuse
- using standard chi^2 critical values for a variance-component or a one-sided boundary test
- reporting a symmetric Wald interval for a parameter whose true value is at the edge of its range

## Related nodes (non-prerequisite)
- required_by: mle_score_equation, mle_asymptotic_normality, wilks_theorem

## Sources
van_der_vaart_asymptotic, self_liang_1987
