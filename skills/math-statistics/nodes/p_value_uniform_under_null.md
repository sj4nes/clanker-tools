# p_value_uniform_under_null

## Type
proposition

## Statement
If the test statistic T has a continuous distribution and the null H0 is simple, then the p-value p(X) is exactly Uniform(0,1) under H0; hence P_{H0}(p(X) <= alpha) = alpha and rejecting when p <= alpha has size exactly alpha.

## Symbols
- `p(X) = 1 - F_0(T(X))` — for an upper-tail test, F_0 the null CDF of T -- a probability integral transform

## Epistemic status
proposition  ·  regime: exact

## Prerequisites (tsort edges into this node)
p_value, prob_cdf, prob_uniform_continuous

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: probability integral transform: if T ~ F_0 continuous then F_0(T) ~ Uniform(0,1), so p(X) = 1 - F_0(T(X)) ~ Uniform(0,1)
derives_from: prob_cdf
lean_status: core — the PIT step F(T) ~ Uniform is cited to math-probability:probability_integral_transform; the corollary is one line

## Type / well-formedness check
An exact distributional fact, a direct corollary of the probability integral transform (F_0(T) ~ Uniform when T ~ F_0 continuous). It is what makes the p-value a calibrated evidence scale and lets p-values be combined (Fisher's method, etc.).

## Specialization / boundary cases
- a histogram of p-values across many true nulls should look flat -- a spike near 0 signals real effects, a spike near 1 signals a misspecified (conservative) test or dependence
- under the ALTERNATIVE, the p-value distribution is stochastically smaller than Uniform (concentrated near 0), and more so with higher power
- discrete T: p(X) is stochastically LARGER than Uniform -- P(p <= alpha) < alpha, the test is conservative

## Hypothesis-dropped counterexamples
- **T_continuous**: binomial / Poisson / permutation tests with few distinct values: the p-value takes finitely many values and P(p <= alpha) jumps below alpha -- 'mid-p' or randomized p-values restore uniformity
- **H0_simple**: with a composite null the p-value defined via the sup is Uniform at the least-favorable null point and stochastically larger elsewhere

## Common misuse
- assuming a uniform p-value histogram for discrete tests
- combining dependent p-values with Fisher's method as if independent

## Related nodes (non-prerequisite)
- uses: p_value, prob_cdf

## Sources
casella_berger_2e, murdoch_tsai_adcock_2008
