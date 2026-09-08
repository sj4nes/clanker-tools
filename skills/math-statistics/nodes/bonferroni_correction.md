# bonferroni_correction

## Type
proposition

## Statement
Testing each of m hypotheses at level alpha/m controls the family-wise error rate at alpha, for ANY dependence structure among the tests.

## Symbols
- `alpha/m` — the per-comparison level
- `equivalently` — reject H_{0,i} if its p-value p_i <= alpha/m; or adjust p_i -> min(1, m p_i)

## Epistemic status
proposition  ·  regime: exact

## Prerequisites (tsort edges into this node)
multiple_testing_fwer, prob_markov_ineq

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: Boole / union bound over the true nulls: P(any true null rejected) <= sum_{i true null} P(reject H_{0,i}) <= m_0 alpha/m <= alpha
derives_from: prob_markov_ineq
lean_status: core — the union bound P(union A_i) <= sum P(A_i) is cited to math-probability:boole_inequality; the arithmetic m_0 alpha/m <= alpha is proof-checks.lean Stat.bonferroni_bound

## Type / well-formedness check
A finite-sample FWER bound. Proof: Boole's inequality (the union bound) -- FWER = P(union of false rejections) <= sum P(false rejection_i) <= m_0 (alpha/m) <= alpha, where m_0 <= m is the number of true nulls.

## Specialization / boundary cases
- Holm's step-down procedure uniformly improves on Bonferroni at no cost (also FWER, any dependence) -- always prefer it
- m = 2 (co-primary endpoints): test each at 0.025
- for POSITIVELY dependent tests Bonferroni is conservative; Sidak (1 - (1-alpha)^{1/m}) is slightly tighter under independence

## Hypothesis-dropped counterexamples
- **none_all_hypotheses_essential**: the bound holds unconditionally; its weakness is conservatism (low power) when m is large or tests are positively dependent, not invalidity

## Common misuse
- using raw Bonferroni when Holm is strictly better
- applying it to 10^6 genomic tests -- valid but essentially no power; use FDR
- correcting for tests you happened to run but that were not part of the pre-specified family (over-correction)

## In the wild
- the standard adjustment for a small number of pre-specified secondary endpoints in clinical trials
- 'genome-wide significance' p < 5e-8 is Bonferroni for ~1e6 independent common variants

## Related nodes (non-prerequisite)
- uses: multiple_testing_fwer, prob_markov_ineq
- improved_by: 

## Sources
bonferroni_1936, holm_1979, lehmann_romano_tsh
