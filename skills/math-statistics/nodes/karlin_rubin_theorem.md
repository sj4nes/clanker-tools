# karlin_rubin_theorem

## Type
theorem

## Statement
If the family has monotone likelihood ratio in T, then for testing H0: theta <= theta_0 against H1: theta > theta_0 the test phi(x) = 1{ T(x) > c } (with c set so E_{theta_0}[phi] = alpha) is uniformly most powerful at level alpha: it maximizes beta_phi(theta) for every theta > theta_0 simultaneously.

## Symbols
- `UMP` — uniformly most powerful -- the SAME test is most powerful against every alternative at once
- `the size is attained at theta_0` — MLR makes beta_phi nondecreasing in theta, so sup over theta <= theta_0 is at theta_0

## Epistemic status
proved_theorem  ·  regime: exact

## Prerequisites (tsort edges into this node)
monotone_likelihood_ratio, neyman_pearson_lemma, power_function

## Hypotheses
monotone_likelihood_ratio

## Proof provenance
technique: Neyman-Pearson against an arbitrary theta_1 > theta_0 yields the region {T > c}, which does not depend on theta_1 (MLR); beta_phi nondecreasing (MLR) controls the composite null at theta_0
derives_from: neyman_pearson_lemma
lean_status: cited — the 'NP region is {T > c} independent of theta_1' step follows from MLR monotonicity; the beta nondecreasing lemma is proof-checks.lean Stat.mlr_power_monotone for a two-point family

## Type / well-formedness check
An optimality theorem for one-sided composite hypotheses. Proof: fix any theta_1 > theta_0; by Neyman-Pearson the MP test of theta_0 vs theta_1 rejects for large f(.; theta_1)/f(.; theta_0), which by MLR is 'large T' -- the same region {T > c} regardless of theta_1. Monotonicity of beta_phi handles the composite null.

## Specialization / boundary cases
- N(theta, sigma^2 known): the one-sided z-test 1{ Xbar > mu_0 + z sigma/sqrt(n) } is UMP for H0: mu <= mu_0
- Bernoulli: the one-sided binomial test is UMP for H0: p <= p_0
- one-sided F-test for a variance ratio; one-sided test for a noncentrality parameter

## Hypothesis-dropped counterexamples
- **monotone_likelihood_ratio**: Cauchy location, or any family without MLR: no UMP one-sided test exists -- different alternatives are best detected by different regions
- **one_sided**: for H0: theta = theta_0 vs H1: theta != theta_0 (two-sided) there is no UMP test even under MLR; one restricts to unbiased tests (UMPU) and gets the equal-tailed two-sided test

## Common misuse
- applying it to a two-sided alternative
- assuming the one-sided test is 'the' test when a two-sided alternative is scientifically appropriate -- the one-sided test has power below alpha in the wrong direction

## Related nodes (non-prerequisite)
- uses: monotone_likelihood_ratio, neyman_pearson_lemma
- generalizes_from: neyman_pearson_lemma

## Sources
karlin_rubin_1956, lehmann_romano_tsh
