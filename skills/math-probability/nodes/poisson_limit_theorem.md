# poisson_limit_theorem

## Type
theorem

## Statement
If X_n ~ Binomial(n, p_n) with n p_n -> lambda in (0, inf), then X_n converges in distribution to Poisson(lambda): P(X_n = k) -> e^{-lambda} lambda^k / k! for each k.

## Symbols
- `X_n` — Binomial(n, p_n), type: Omega -> {0,...,n}
- `lambda` — the limiting mean, type: positive real

## Epistemic status
proved_theorem

## Prerequisites (tsort edges into this node)
binomial_distribution, poisson_distribution, sequence_limit

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: pmf: C(n,k) p_n^k (1-p_n)^{n-k} = [n!/(n-k)! n^k] (n p_n)^k/k! (1 - p_n)^{n-k} -> 1 . lambda^k/k! . e^{-lambda}. Or via MGF convergence + mgf_uniqueness
derives_from: mgf_uniqueness
lean_status: cited — Durrett Thm 3.6.1; Billingsley Thm 23.2

## Type / well-formedness check
the 'law of rare events': many trials, each very unlikely, with a stable expected count. Proof by direct pmf limit, or by MGF: (1 - p_n + p_n e^t)^n = (1 + (n p_n)(e^t - 1)/n)^n -> exp(lambda(e^t - 1)).

## Specialization / boundary cases
- n = 1000 trials of probability 1/1000: number of successes approx Poisson(1) -- the bc worksheet shows the pmf at k = 3 converging
- raisins per cookie, mutations per genome, connection requests per millisecond

## Hypothesis-dropped counterexamples
- **n_p_n_converges_to_a_finite_positive_limit**: if n p_n -> inf the correct limit is Gaussian (CLT); if n p_n -> 0 the count is 0 a.s. in the limit
- **p_n_to_0**: with p fixed (not -> 0), Binomial(n, p) has mean np -> inf and is approximately Gaussian, not Poisson

## Common misuse
- using the Poisson approximation when np is large and p is not small (use the normal approximation)
- applying it with a fixed p

## Related nodes (non-prerequisite)
- instance_of: convergence_in_distribution
- connects: binomial_distribution, poisson_distribution

## Sources
durrett_pte, billingsley_probability_measure
