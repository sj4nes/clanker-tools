# binomial_distribution

## Type
definition

## Statement
X ~ Binomial(n, p): the number of successes in n independent Bernoulli(p) trials. P(X = k) = C(n, k) p^k (1-p)^{n-k}. E[X] = np, Var(X) = np(1-p), M_X(t) = (1 - p + p e^t)^n.

## Symbols
- `X` — a binomial count, type: Omega -> {0,1,...,n}
- `n` — number of trials, type: positive integer
- `p` — success probability, type: real in [0,1]

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
bernoulli_distribution, expectation_linearity, iid, mgf_sum_independent, pmf, variance_of_sum

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: mean by expectation_linearity over the indicator sum; variance by variance_of_sum with independence; MGF by mgf_sum_independent
derives_from: mgf_sum_independent
lean_status: core — validation/proof-checks.lean -- Binomial(4,1/2) mean/var decide instances + Prob.var_of_sum_raw

## Type / well-formedness check
X = sum_{i=1}^n Y_i with Y_i iid Bernoulli(p); the mean and variance follow from linearity and independence (variance_of_sum), not from the combinatorial sum.

## Specialization / boundary cases
- n = 1: Bernoulli(p)
- p = 1/2: symmetric about n/2
- n large, p small, np = lambda: approx Poisson(lambda) (poisson_limit_theorem)
- n large, p fixed: (X - np)/sqrt(np(1-p)) approx N(0,1) (de Moivre-Laplace, a case of the CLT)

## Hypothesis-dropped counterexamples
- **independence_of_trials**: correlated trials (e.g. sampling without replacement) give the hypergeometric distribution, with the SAME mean np but SMALLER variance (finite-population correction)
- **identical_p**: varying p_i per trial gives the Poisson-binomial distribution; mean sum p_i, variance sum p_i(1-p_i)

## Common misuse
- using it for sampling without replacement
- assuming Var = np (that is the Poisson limit; binomial Var = np(1-p) < np)

## Related nodes (non-prerequisite)
- sum_of: bernoulli_distribution
- limits_to: poisson_distribution, normal_distribution
- without_replacement: hypergeometric

## Sources
grimmett_stirzaker, durrett_pte
