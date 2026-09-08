# exponential_family

## Type
structure

## Statement
A family is a k-parameter exponential family if its densities can be written f(x; eta) = h(x) exp( eta . T(x) - A(eta) ) for a natural parameter eta in R^k, sufficient statistic T(x) in R^k, carrier h >= 0, and log-partition A(eta).

## Symbols
- `eta` — the natural (canonical) parameter, type: point of the natural parameter space in R^k
- `T(x)` — the natural sufficient statistic, type: R^k-valued function of the data
- `h(x)` — the carrier / base density, type: nonnegative, theta-free
- `A(eta)` — the log-partition (cumulant) function, type: real, convex

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
dominated_family, prob_expectation, prob_exponential, statistic

## Hypotheses
(none — unconditional within scope)
## Well-definedness
Well defined wherever A(eta) < inf; the family is the set of such densities. The MINIMAL representation (linearly independent T_j, 1) is unique up to affine change.

## Type / well-formedness check
The representation is not unique (affine reparametrizations of (eta, T) and rescalings of h). 'k-parameter' means the minimal such k (T has no a.s. affine dependency). A curved exponential family restricts eta to a lower-dimensional manifold and is NOT a k-parameter exponential family.

## Specialization / boundary cases
- Bernoulli(p): eta = log(p/(1-p)), T(x) = x, A(eta) = log(1 + e^eta), h = 1
- N(mu, sigma^2): eta = (mu/sigma^2, -1/(2 sigma^2)), T(x) = (x, x^2) -- a 2-parameter family
- Poisson, exponential, gamma, beta, binomial(n fixed), multinomial, chi-squared -- all exponential families
- uniform(0, theta), Cauchy, Student's t (df unknown) -- NOT exponential families (support moves / no finite-dim sufficient statistic)

## Hypothesis-dropped counterexamples
- **finite_k**: the location-scale Cauchy family has no sufficient statistic of dimension < n (Pitman-Koopman-Darmois: among families with fixed support, exactly the exponential families admit a fixed-dimension sufficient statistic). All the clean exp-family results below then fail.

## Common misuse
- assuming a curved exponential family (eta constrained to a curve) inherits completeness or the clean CRLB-attainment result -- it does not
- forgetting the carrier h(x) when it encodes a support constraint

## In the wild
- generalized linear models (logistic, Poisson, gamma regression) ARE exponential-family response models -- the IRLS fitting algorithm and the deviance are exp-family constructs
- the maximum-entropy distribution under moment constraints is always an exponential family with T = the constrained functions (statistical mechanics, NLP max-ent models)

## Related nodes (non-prerequisite)
- illustrated_by: prob_normal, prob_bernoulli, prob_poisson
- required_by: natural_parameter_space, exponential_family_sufficient_statistic, crlb_attainment

## Sources
brown_exponential_families, lehmann_casella_tpe
