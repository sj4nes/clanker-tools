# pearson_chi_squared_gof

## Type
theorem

## Statement
For n observations classified into k cells with null cell probabilities p_j(theta) (d parameters estimated by an efficient method), the Pearson statistic X^2 = sum_{j=1}^k (O_j - E_j)^2 / E_j (O_j observed, E_j = n p_j(theta_hat)) converges under H0 to chi^2_{k - 1 - d}.

## Symbols
- `O_j` — observed count in cell j
- `E_j = n p_j(theta_hat)` — expected count under the fitted null
- `k - 1 - d` — cells, minus 1 (counts sum to n), minus d estimated parameters

## Epistemic status
proved_theorem  ·  regime: asymptotic

## Prerequisites (tsort edges into this node)
chi_squared_distribution, likelihood_ratio_test, prob_binomial, prob_clt, prob_poisson

## Hypotheses
fisher_information_positive_definite

## Proof provenance
technique: multivariate CLT for the cell counts -> N(0, Sigma); X^2 is the corresponding quadratic form; a rank argument gives df k - 1, reduced by d for efficiently estimated parameters (Fisher's df correction)
derives_from: score_test
lean_status: cited — CITED -- Pearson 1900; Fisher 1924 (df correction); Cramer 1946. X^2 as the multinomial score statistic is the modern view.

## Type / well-formedness check
An asymptotic null-distribution result. X^2 is (asymptotically) the score statistic for the multinomial model, hence chi^2; it is also asymptotically equivalent to the LR statistic G^2 = 2 sum O_j log(O_j/E_j) (three_tests_asymptotically_equivalent).

## Specialization / boundary cases
- testing a fully specified distribution (d = 0): df = k - 1
- test of independence in an r x c table: d = (r-1) + (c-1) estimated margins, df = (r-1)(c-1)
- rule of thumb: valid when all E_j >= 5 (else exact / Monte Carlo tests)

## Hypothesis-dropped counterexamples
- **parameters_estimated_efficiently_AND_from_grouped_data**: if theta is estimated from the RAW (ungrouped) data rather than the cell counts, the limiting distribution is BETWEEN chi^2_{k-1-d} and chi^2_{k-1} (Chernoff-Lehmann) -- using chi^2_{k-1-d} then over-rejects
- **large_expected_counts**: sparse tables (many E_j < 5): the chi^2 approximation fails; the statistic is not chi^2 and can be wildly miscalibrated

## Common misuse
- using chi^2_{k-1-d} when parameters were fit to ungrouped data (Chernoff-Lehmann)
- applying it to sparse contingency tables without an exact test
- reading a non-significant GOF test as 'the model fits' (low power against many alternatives)

## In the wild
- the chi^2 test of independence -- the most common categorical-data analysis in the social sciences
- goodness-of-fit checks in genetics (Hardy-Weinberg), physics (histogram fits), and A/B testing (does the traffic split match design?)

## Related nodes (non-prerequisite)
- uses: likelihood_ratio_test, chi_squared_distribution, prob_clt
- special_case_of: wilks_theorem

## Sources
pearson_1900, fisher_1924, cramer_1946
