# cumulant_function

## Type
definition

## Statement
A(eta) = log int h(x) exp(eta . T(x)) dmu(x): the log of the normalizing constant, a convex function on H, analytic on int(H).

## Symbols
- `A(eta)` — the cumulant / log-partition function, type: convex real function on H
- `grad A(eta)` — = E_eta[T(X)], the mean-value map
- `Hess A(eta)` — = Cov_eta(T(X)), positive semidefinite (definite in the minimal representation)

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
exponential_family, natural_parameter_space

## Hypotheses
(none — unconditional within scope)
## Well-definedness
A(eta) is finite exactly on H and determines the family given (h, T, mu).

## Type / well-formedness check
Convex (Holder); strictly convex in a minimal representation. Its gradient and Hessian are the first two cumulants of T -- see exponential_family_moment_identities.

## Specialization / boundary cases
- Bernoulli: A(eta) = log(1 + e^eta); A'(eta) = e^eta/(1+e^eta) = p; A''(eta) = p(1-p)
- N(mu, sigma^2), eta_1 = mu/sigma^2: partial in eta_1 recovers mu
- Poisson: A(eta) = e^eta = lambda; A' = A'' = lambda (mean = variance)

## Common misuse
- confusing A(eta) (the log-partition) with the cumulant GENERATING function of X
- differentiating A outside int(H)

## Related nodes (non-prerequisite)
- required_by: exponential_family_moment_identities, mean_value_parametrization

## Sources
brown_exponential_families, wainwright_jordan_graphical_models
