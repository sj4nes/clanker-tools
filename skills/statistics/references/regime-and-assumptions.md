# Regime, regularity conditions, and data provenance

Every theorem this skill invokes is a node of the
[`math-statistics`](../../math-statistics/SKILL.md) capsule. This file expands
the two questions the SKILL asks before any number is reported: *which regime
does the guarantee live in* and *which assumptions is it standing on*.

## The four regimes

Source: [`indexes/regime-index.md`](../../math-statistics/indexes/regime-index.md).
Reading an `asymptotic` guarantee as an `exact` finite-sample one is the single
most common misuse in applied statistics.

| Regime | What the guarantee means | Holds because | Breaks when |
|---|---|---|---|
| `exact` | Coverage / size is the nominal value at the stated `n`, for **every** `n` | an exact pivot exists — a function of data and parameter whose distribution is fully known and parameter-free (`pivotal_quantity`, `pivot_method`) | the distributional model (almost always normality, or a specific family) is wrong |
| `asymptotic` | Coverage / size → nominal as `n → ∞`; at finite `n` it is an approximation of unknown accuracy | a CLT / Slutsky / delta-method argument (`prob_clt`, `prob_slutsky`, `prob_delta_method`) plus a consistent variance estimate | `n` small; parameter near a boundary; Fisher information weak; heavy tails; many nuisance parameters |
| `distribution_free` | Holds with no parametric family — sometimes with an explicit finite-sample band, more often asymptotically | the object is a smooth functional of the empirical CDF and the plug-in principle transfers its limit (`glivenko_cantelli`, `plug_in_principle`) | the functional is non-smooth (max, min, a boundary); the statistic has no finite variance; the sample is tiny |
| `bayesian` | A posterior probability statement, **exact given the prior and the model** | Bayes' rule; the posterior is a deductive consequence of prior + likelihood | the prior carries unacknowledged weight; agreement with a frequentist interval (`bernstein_von_mises`) is itself only asymptotic |

Finite-sample-exact procedures worth reaching for first (all `regime: exact`):
`one_sample_t_test`, `two_sample_t_test`, `normal_mean_ci_unknown_variance`,
`normal_variance_ci`, `f_test_equality_of_variances`, `neyman_pearson_lemma`,
`karlin_rubin_theorem`, `rao_blackwell_theorem` (variance drop),
`p_value_uniform_under_null` (the null distribution of the p-value).

Honest finite-sample tools in the distribution-free world:
`dvoretzky_kiefer_wolfowitz` (a uniform band for the whole CDF at every `n`),
and order-statistic / `sample_quantile` intervals (exact binomial coverage).

## The six regularity conditions

First-class `hypothesis` nodes in the capsule
([`indexes/hypothesis-index.md`](../../math-statistics/indexes/hypothesis-index.md)),
each with a prerequisite edge into every likelihood-based result (CRLB, MLE
asymptotics, Wilks, the score identity, the information equality). Each result's
`counterexamples_when_dropped` names what fails.

| Condition (node) | What it requires | Canonical failure |
|---|---|---|
| `support_independent_of_theta` | the set `{x : f(x; θ) > 0}` does not depend on `θ` | Uniform(0, θ): the MLE is `max Xᵢ`, is biased, converges at rate `n` not `√n`, and the CRLB does not apply |
| `interchange_derivative_integral` | `∂/∂θ ∫ = ∫ ∂/∂θ` (dominated-convergence / Leibniz conditions hold) | densities with `θ`-dependent support again; some heavy-tailed families |
| `true_parameter_interior` | `θ₀` is in the **interior** of the parameter space, not on its boundary | testing `σ² = 0` in a variance-components model → `−2 log Λ` is a **50:50 mixture** of `χ²₀` and `χ²₁`, not `χ²₁` |
| `fisher_information_positive_definite` | `I(θ₀)` is finite and non-singular | a flat direction in the log-likelihood → non-identified, infinite-variance limit |
| `log_likelihood_smooth` | `ℓ(θ)` is (usually thrice) differentiable in `θ` near `θ₀` | Laplace / double-exponential location at the median; change-point models |
| `identifiability` | distinct `θ` give distinct distributions `P_θ` | label-switching in mixtures; **Neyman–Scott**: one nuisance parameter per observation → the MLE of the common variance is inconsistent (converges to `σ²/2`) |

If any condition is known to fail, the likelihood-based interval or test is not
valid as stated — switch to an exact small-sample method, a profile-likelihood
interval with a simulated reference distribution, a boundary-corrected mixture,
or a distribution-free procedure, and say which.

## Data provenance — assumptions about how the rows came to exist

The model in step 3 assumes a data-generating process. Audit it in step 2.

- **Sampling mechanism.** Census / probability sample (with a known design) /
  convenience / opt-in / administrative extract. Only a probability sample lets
  a plain `iid_sample` analysis estimate a population quantity without a
  weighting or modelling argument.
- **Selection and inclusion.** Filters applied before you saw the data;
  survivorship (units that failed are absent); truncation (units outside a range
  never recorded) vs censoring (partially observed — needs a survival model, not
  deletion); selection on the outcome (conditioning on a collider) — this
  **creates** associations that are not there in the population.
- **Missingness mechanism.** MCAR (missing at random, unconditionally — complete
  case is unbiased, just less efficient), MAR (missing depends only on observed
  variables — complete case can be biased; multiple imputation or IPW under the
  model), MNAR (missing depends on the unobserved value itself — no method fixes
  it without an untestable model; do a sensitivity analysis over MNAR
  parameters). **MAR vs MNAR is not testable from the data** — argue it from the
  collection process.
- **Clustering, weights, design.** Repeated measures, students in classes,
  visits per patient, sampling strata and stages. The number of **independent
  units** is the number of clusters or periods, not the number of rows.
  Analysing clustered data as `iid` (pseudoreplication) fabricates precision —
  standard errors come out `√(design effect)` too small, where
  `DE = 1 + (m − 1)ρ`.
- **Measurement.** Instrument error, recall error, coding drift over time,
  differential measurement error by group (which biases comparisons even when
  each group's error is unbiased on its own).

Record, in the provenance audit, whether the data can support the stated
estimand **at all** before proceeding.
