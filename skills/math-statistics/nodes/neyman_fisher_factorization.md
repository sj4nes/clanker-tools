# neyman_fisher_factorization

## Type
theorem

## Statement
T is sufficient for theta iff the density factors as f(x; theta) = g(T(x); theta) h(x) for some functions g >= 0 and h >= 0 with h not depending on theta.

## Symbols
- `g(t; theta)` — the theta-dependent factor, a function of the data ONLY through T
- `h(x)` — the theta-free residual factor

## Epistemic status
proved_theorem  ·  regime: exact

## Prerequisites (tsort edges into this node)
likelihood_function, prob_pmf, sufficiency

## Hypotheses
dominated_family

## Proof provenance
technique: discrete: direct computation of P(X = x | T = t); general: Halmos-Savage / Radon-Nikodym factorization
derives_from: sufficiency
lean_status: core — validation/proof-checks.lean Stat.factorization_discrete -- the identity P(X=x|T=t) = g(t)h(x) / sum_{x': T(x')=t} g(t)h(x') with the g(t) cancelling

## Type / well-formedness check
An iff. The practical test for sufficiency: write the joint density and see whether theta interacts with the data only through T(x). In the dominated case this is rigorous (Halmos-Savage); the discrete case is a direct conditional-probability computation.

## Specialization / boundary cases
- Bernoulli: f = p^{sum x_i}(1-p)^{n - sum x_i} = [p/(1-p)]^{sum x_i} (1-p)^n . 1  => T = sum x_i sufficient
- N(mu, sigma^2): the exponent expands to a function of (sum x_i, sum x_i^2) plus a theta-free term
- uniform(0, theta): f = theta^{-n} 1{x_(n) <= theta} . 1{x_(1) >= 0}  => T = x_(n) sufficient

## Hypothesis-dropped counterexamples
- **dominated_family**: for a family of mutually singular laws there is no common density to factor; sufficiency must be checked directly from the conditional law

## Common misuse
- forgetting the theta-free indicator 1{x_(1) >= 0} type factors, which belong in h
- reading a factorization through T and T' as making BOTH minimal sufficient -- it makes (T, T') sufficient

## In the wild
- the one-line route to 'sum T(X_i) is sufficient' for every exponential family
- in GLMs, shows the sufficient statistic for beta is X^T y (design matrix times response)

## Related nodes (non-prerequisite)
- proof_route_for: sufficiency
- required_by: exponential_family_sufficient_statistic, sufficiency_principle

## Sources
casella_berger_2e, lehmann_casella_tpe
