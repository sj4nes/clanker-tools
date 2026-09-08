# exponential_family_sufficient_statistic

## Type
theorem

## Statement
In an exponential family f(x; eta) = h(x) exp(eta . T(x) - A(eta)), for an iid sample the statistic sum_{i=1}^n T(X_i) is sufficient for eta (and minimal sufficient in the minimal representation).

## Symbols
- `sum_i T(X_i)` — the natural sufficient statistic of the sample, type: R^k, dimension k regardless of n
- `n` — sample size -- the KEY point: the sufficient statistic's dimension does not grow with n

## Epistemic status
proved_theorem  ·  regime: exact

## Prerequisites (tsort edges into this node)
exponential_family, neyman_fisher_factorization

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: Neyman-Fisher factorization applied to the product density
derives_from: neyman_fisher_factorization
lean_status: cited — the discrete factorization identity is in proof-checks.lean Stat.factorization_discrete; the exp-family instance is immediate

## Type / well-formedness check
A sufficiency claim; it follows immediately from Neyman-Fisher factorization: the joint density is [prod h(x_i)] exp(eta . sum T(x_i) - n A(eta)), which is g(sum T(x_i); eta) times h-part.

## Specialization / boundary cases
- Bernoulli: sum X_i (the count) is sufficient -- the individual outcomes are not needed
- N(mu, sigma^2): (sum X_i, sum X_i^2), equivalently (Xbar, S^2), is sufficient
- Poisson: sum X_i; exponential: sum X_i; gamma(a known, rate): sum X_i

## Hypothesis-dropped counterexamples
- **exponential_family**: outside exponential families the minimal sufficient statistic generally has dimension growing with n -- e.g. for iid Cauchy or uniform-location the full order statistic is minimal sufficient. Pitman-Koopman-Darmois makes this an iff (fixed support).

## Common misuse
- reducing to sum T(X_i) and then using a method that needs the full data (a goodness-of-fit test against the exp-family itself)
- assuming (Xbar, S^2) is sufficient for a non-normal location-scale family

## Related nodes (non-prerequisite)
- special_case_of: neyman_fisher_factorization
- required_by: crlb_attainment

## Sources
lehmann_casella_tpe, brown_exponential_families
