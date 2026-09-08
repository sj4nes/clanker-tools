# dominated_family

## Type
hypothesis

## Statement
The model is dominated if there is one sigma-finite measure mu such that every P_theta has a density f(x; theta) = dP_theta / dmu.

## Symbols
- `mu` — the dominating measure, type: sigma-finite measure on the sample space (usually Lebesgue or counting)
- `f(x; theta)` — the density / likelihood contribution, type: measurable function >= 0 with int f dmu = 1

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
prob_pdf, statistical_model

## Hypotheses
(none — unconditional within scope)
## Well-definedness
mu is not unique but the model being dominated is a genuine property; the Radon-Nikodym derivative f(.; theta) is mu-a.e. unique.

## Type / well-formedness check
An absolute-continuity statement P_theta << mu holding for ALL theta with ONE mu. Gives a common reference so likelihoods L(theta) = prod f(x_i; theta) are comparable across theta.

## Specialization / boundary cases
- discrete model: mu = counting measure, f = the pmf
- continuous model on R^k: mu = Lebesgue, f = the pdf
- a mixed discrete-continuous model: mu = Lebesgue + counting on the atoms

## Hypothesis-dropped counterexamples
- **dominated_family**: Theta = R, P_theta = the point mass delta_theta. No single sigma-finite mu dominates all of them (an uncountable family of mutually singular measures). The likelihood is not well defined and the whole density-based apparatus (score, Fisher information, factorization) is unavailable.

## Common misuse
- writing down a 'likelihood' for a model that is not dominated (e.g. uniform(0, theta) IS dominated by Lebesgue -- fine -- but comparing densities of singular laws is not)
- forgetting the support may still depend on theta even in a dominated family (uniform(0, theta)); that is the separate support_independent_of_theta condition

## Related nodes (non-prerequisite)
- required_by: likelihood_function, neyman_fisher_factorization

## Sources
lehmann_romano_tsh, schervish_theory_of_statistics
