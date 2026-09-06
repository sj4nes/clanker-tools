# weak_law_large_numbers

## Type
theorem

## Statement
If X_1, X_2, ... are iid with E|X_1| < inf and mean mu, then the sample mean Xbar_n = (X_1 + ... + X_n)/n -> mu IN PROBABILITY.

## Symbols
- `X_i` — an iid sequence, type: N -> L^1(P)
- `mu` — the common mean E[X_1], type: real
- `Xbar_n` — the sample mean, type: Omega -> R

## Epistemic status
proved_theorem

## Prerequisites (tsort edges into this node)
characteristic_function, chebyshev_inequality, convergence_in_probability, expectation_linearity, iid, variance_of_sum

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: finite-variance route: Var(Xbar_n) = sigma^2/n, so P(|Xbar_n - mu| > eps) <= sigma^2/(n eps^2) -> 0 (Chebyshev). General route: truncate X_i at n, control the mean shift and the variance of the truncated part; or phi_{Xbar_n}(t) = phi_{X_1}(t/n)^n -> e^{i mu t}, the CF of the constant mu
derives_from: chebyshev_inequality
lean_status: core — validation/proof-checks.lean Prob.chebyshev_reduction_fwd + Prob.var_of_sum_raw

## Type / well-formedness check
convergence mode: IN PROBABILITY (weaker than the SLLN's a.s.). Finite mean is enough; the classical finite-variance proof is a one-line Chebyshev bound, the general case uses truncation or characteristic functions.

## Specialization / boundary cases
- X_i ~ Bernoulli(p): the relative frequency of successes -> p in probability (Bernoulli's theorem, 1713)
- pairwise independence and finite variance are ENOUGH for this mode (the Chebyshev proof only uses pairwise uncorrelatedness)
- Monte Carlo integration: (1/n) sum g(U_i) -> integral g in probability

## Hypothesis-dropped counterexamples
- **finite_mean**: X_i ~ Cauchy: Xbar_n ~ Cauchy for every n -- no convergence to any constant (cauchy_no_mean)
- **identically_distributed_ish**: for non-identical independent X_i, Xbar_n -> the average of the means in probability provided (1/n^2) sum Var(X_i) -> 0

## Common misuse
- claiming a.s. convergence (that is the SLLN, which also only needs a finite mean)
- a rate: the WLLN gives no explicit n; use Chebyshev/Hoeffding for that
- the gambler's fallacy: Xbar_n -> mu does NOT mean the SUM sum(X_i - mu) stays bounded (it grows like sqrt(n))

## Related nodes (non-prerequisite)
- strengthened_by: strong_law_large_numbers
- uses: chebyshev_inequality
- tag: p

## Sources
durrett_pte, billingsley_probability_measure
