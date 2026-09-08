# mean_value_parametrization

## Type
definition

## Statement
The mean-value (expectation) parametrization replaces eta by mu = E_eta[T(X)] = grad A(eta); the map eta -> mu is a diffeomorphism from int(H) onto the interior of the convex hull of T's support.

## Symbols
- `mu` — the mean parameter, type: point of int(conv(supp T))
- `grad A` — the mean map, a bijection on the interiors by strict convexity of A

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
exponential_family_moment_identities

## Hypotheses
(none — unconditional within scope)
## Well-definedness
Bijective on the interiors; the inverse is the gradient of the Legendre dual A*(mu) = sup_eta (eta.mu - A(eta)) (negative entropy).

## Type / well-formedness check
A reparametrization, well-posed because grad A is injective (Hess A = Cov(T) PD in the minimal representation). The Fisher information transforms as I(mu) = (Hess A)^{-1} = Cov_eta(T)^{-1}.

## Specialization / boundary cases
- Bernoulli: mu = p (the natural sufficient statistic's mean); eta = logit(p)
- N: mu = (E X, E X^2); the moment parametrization
- the MLE in the mean parametrization is simply mu_hat = Tbar = (1/n) sum T(x_i) -- always unbiased for mu

## Common misuse
- forgetting the Jacobian when moving a variance or an interval between the eta and mu parametrizations
- assuming mu_hat = Tbar is the MLE of a FUNCTION of mu -- it is, by invariance, only for the identity

## Related nodes (non-prerequisite)
- dual_of: cumulant_function
- required_by: 

## Sources
brown_exponential_families, wainwright_jordan_graphical_models
