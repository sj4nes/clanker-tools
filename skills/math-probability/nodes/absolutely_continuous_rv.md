# absolutely_continuous_rv

## Type
definition

## Statement
X is absolutely continuous if its law P_X is absolutely continuous with respect to Lebesgue measure: lambda(B) = 0 implies P_X(B) = 0. Equivalently F_X(x) = integral_{-inf}^x f for some f.

## Symbols
- `X` — a random variable, type: Omega -> R
- `lambda` — Lebesgue measure, type: measure on B(R)

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
distribution_pushforward, lebesgue_measure_caratheodory, radon_nikodym

## Hypotheses
(none — unconditional within scope)

## Well-definedness
P_X << lambda is a well-defined relation between measures; by Radon-Nikodym (P_X finite, lambda sigma-finite) it is equivalent to the existence of a density.

## Type / well-formedness check
'absolutely continuous' is a property of the LAW relative to lambda, distinct from F_X being a continuous function (the Cantor function is continuous but its law is singular). Radon-Nikodym then supplies the density f_X = dP_X/dlambda.

## Specialization / boundary cases
- Uniform, exponential, normal, gamma, beta: all absolutely continuous
- P(X = x) = 0 for every x (no atoms) is necessary but NOT sufficient (singular continuous laws also have no atoms)

## Hypothesis-dropped counterexamples
- **absolute_continuity_vs_continuous_cdf**: the Cantor distribution: F_X continuous and strictly increasing on the Cantor set, F_X' = 0 lambda-a.e., P_X concentrated on a lambda-null set -- continuous CDF, no density

## Common misuse
- equating 'continuous random variable' with 'continuous CDF'
- assuming a density exists whenever there are no atoms

## Related nodes (non-prerequisite)
- requires: radon_nikodym
- complement_of: discrete_rv
- third_case: singular continuous

## Sources
billingsley_probability_measure, folland_real_analysis
