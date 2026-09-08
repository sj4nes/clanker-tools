# identifiability

## Type
hypothesis

## Statement
The model is identifiable if theta != theta' implies P_theta != P_theta': the map theta -> P_theta is injective.

## Symbols
- `theta, theta'` — distinct candidate parameter values
- `P_theta` — the law they index

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
parametric_model

## Hypotheses
(none — unconditional within scope)
## Well-definedness
Identifiability is a property of the PARAMETRIZATION, not the data. A non-identifiable model can be repaired by quotienting Theta or adding a constraint.

## Type / well-formedness check
An injectivity statement about theta -> P_theta. Equivalent (dominated case): f(x; theta) = f(x; theta') for a.e. x implies theta = theta'.

## Specialization / boundary cases
- a full-rank exponential family in its natural parametrization is identifiable
- N(mu, sigma^2) is identifiable in (mu, sigma^2); it is NOT identifiable in (mu, sigma) vs (mu, -sigma) if sigma is allowed negative
- a two-component mixture is identifiable only up to permutation of the labels ('label switching')

## Hypothesis-dropped counterexamples
- **identifiability**: the model X ~ N(alpha + beta, 1) with theta = (alpha, beta): alpha and beta are not separately identifiable -- only their sum is. The MLE of (alpha, beta) is not consistent (it wanders along the ridge alpha + beta = const); the Fisher information matrix is singular. This is exactly why fisher_information_positive_definite is a separate hypothesis.

## Common misuse
- assuming the MLE is consistent without checking identifiability (mle_consistency requires it)
- reading a tight confidence interval for a non-identified parameter as informative -- it reflects the prior / penalty, not the data

## Related nodes (non-prerequisite)
- commonly_confused_with: fisher_information_positive_definite
- required_by: mle_consistency

## Sources
van_der_vaart_asymptotic, lehmann_casella_tpe
