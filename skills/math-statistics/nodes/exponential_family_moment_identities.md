# exponential_family_moment_identities

## Type
identity

## Statement
For an exponential family, grad A(eta) = E_eta[T(X)] and Hess A(eta) = Cov_eta(T(X)); in particular the Fisher information in eta is I(eta) = Hess A(eta).

## Symbols
- `grad A, Hess A` — gradient and Hessian of the cumulant function
- `E_eta[T], Cov_eta(T)` — mean vector and covariance matrix of the sufficient statistic

## Epistemic status
mathematical_identity  ·  regime: exact

## Prerequisites (tsort edges into this node)
cumulant_function, prob_covariance, prob_lotus, ra_differentiability

## Hypotheses
natural_parameter_space

## Proof provenance
technique: differentiate A(eta) = log int h e^{eta.T} dmu twice on int(H)
derives_from: cumulant_function
lean_status: core — validation/proof-checks.lean Stat.expfam_grad_A -- the quotient-rule algebra d/deta log(int h e^{eta T}) = E[T]

## Type / well-formedness check
Identities on int(H). Proof: differentiate A(eta) = log int h e^{eta.T} under the integral sign (legal on int(H) by the analyticity of A); first derivative gives the mean, second gives the covariance.

## Specialization / boundary cases
- Bernoulli: A'(eta) = p (mean of T = X), A''(eta) = p(1-p) (variance)
- the score U(eta) = sum_i T(x_i) - n grad A(eta) = 'observed minus expected sufficient statistic' -- zero exactly at the MLE
- gives the information equality for free: I(eta) = Var(U_1) = Hess A(eta) = -E[Hess log f]

## Hypothesis-dropped counterexamples
- **natural_parameter_space**: at a boundary eta the interchange of d/deta and int fails; grad A need not equal E[T] (which may be infinite)

## Common misuse
- using E[T] = grad A when eta is a curved / constrained parameter -- the chain rule adds a Jacobian
- assuming Hess A is positive DEFINITE without the minimal-representation (full-rank) assumption

## In the wild
- variational inference: the mean parameters mu = grad A(eta) and the Legendre dual A*(mu) are the whole computational backbone of exponential-family graphical models (Wainwright-Jordan)
- GLM fitting: the mean-variance relationship Var = A''(A'^{-1}(mu)) is the GLM variance function

## Related nodes (non-prerequisite)
- equivalent_to: information_equality
- required_by: mean_value_parametrization, exponential_family_completeness

## Sources
brown_exponential_families, wainwright_jordan_graphical_models
