# order_statistic

## Type
definition

## Statement
The order statistics of X_1, ..., X_n are the sorted values X_(1) <= X_(2) <= ... <= X_(n); X_(1) = min, X_(n) = max, and X_((n+1)/2) is the median (n odd).

## Symbols
- `X_(k)` — the k-th smallest observation, type: statistic
- `the full order statistic` — (X_(1),...,X_(n)) -- always sufficient, and minimal sufficient for a nonparametric family

## Epistemic status
definition  ·  regime: distribution_free

## Prerequisites (tsort edges into this node)
iid_sample

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: the event {X_(k) <= x} = {at least k of the X_i are <= x} ~ Binomial(n, F(x)) tail
derives_from: prob_binomial
lean_status: core

## Type / well-formedness check
A statistic (permutation of the data). For a continuous parent, X_(k) has density n C(n-1, k-1) F(x)^{k-1} (1 - F(x))^{n-k} f(x); F(X_(k)) ~ Beta(k, n - k + 1).

## Specialization / boundary cases
- X_(n) for uniform(0, theta): the sufficient statistic and (after bias correction) the UMVUE of theta
- F(X_(k)) ~ Beta(k, n-k+1): distribution-free, the basis of nonparametric quantile confidence intervals
- the range X_(n) - X_(1) and the interquartile range are functions of order statistics

## Hypothesis-dropped counterexamples
- **continuous_parent_for_the_clean_Beta_result**: with ties (discrete data) the Beta-distribution results for F(X_(k)) fail; mid-rank corrections are needed

## Common misuse
- using extreme order statistics (min, max) for inference about the center -- they are driven by the tails and converge at non-standard rates (extreme value theory)
- assuming order statistics are independent -- they are strongly dependent (X_(k) <= X_(k+1) always)

## Related nodes (non-prerequisite)
- required_by: sample_quantile
- uses: prob_binomial

## Sources
david_nagaraja_order_statistics, casella_berger_2e
