# Interval estimation

Workflow step 5. Every interval ships with its **regime label** and its nominal
level. Nodes are in the [`math-statistics`](../../math-statistics/SKILL.md)
capsule.

## A confidence interval is an inverted test

`confidence_set_test_duality`: the set of parameter values `θ₀` that a level-`α`
test does **not** reject, given the data, is a `1 − α` `confidence_set`. So
every testing method induces an interval method and vice versa. `coverage_probability`
is `P_θ(θ ∈ C(X))` — it is a property of the **procedure**, not of one interval.

The cleanest route is a **pivot** (`pivotal_quantity`, `pivot_method`): a
function `Q(X, θ)` whose distribution does not depend on `θ`. Invert a
probability statement about `Q` into one about `θ`.

## Exact intervals (regime: exact) — the Gaussian core

Constructed in the capsule from the normal and gamma, no asymptotics:

| Target | Pivot | Interval | Node |
|---|---|---|---|
| normal mean, `σ` known | `(X̄ − μ)/(σ/√n) ~ N(0,1)` | `X̄ ± z_{1−α/2} σ/√n` | `normal_mean_ci_known_variance` |
| normal mean, `σ` unknown | `(X̄ − μ)/(S/√n) ~ t_{n−1}` | `X̄ ± t_{n−1, 1−α/2} S/√n` | `normal_mean_ci_unknown_variance` |
| normal variance | `(n−1)S²/σ² ~ χ²_{n−1}` | `[(n−1)S²/χ²_{up}, (n−1)S²/χ²_{lo}]` | `normal_variance_ci`, `scaled_sample_variance_chi_squared` |
| ratio of two normal variances | `F` pivot | invert `f_test_equality_of_variances` | `f_distribution` |

The `t` pivot needs `X̄ ⟂ S²` (`normal_sample_mean_variance_independence`, via
`basu_theorem`) and `(n−1)S²/σ² ~ χ²_{n−1}`. The variance interval is
**asymmetric** and highly sensitive to non-normality (much more than the mean
interval).

Verification: at `n = 5` the `t` interval covers `0.950`; substituting the
`z` critical value undercovers at `0.880`
([`../verification/infer_sim.py`](../verification/infer_sim.py), `t_vs_z_coverage`).

## Asymptotic intervals (regime: asymptotic)

- **Wald** (`large_sample_wald_interval`, `wald_interval`):
  `θ̂ ± z_{1−α/2} · se(θ̂)` with `se` from the inverse observed information or a
  sandwich estimate. Simplest, but: not transformation-invariant, and it can
  cover badly near a boundary. The **binomial proportion** Wald interval is the
  textbook failure — coverage drops well below nominal near `p = 0` or `1` and
  oscillates with `n`. Use the **score / Wilson** interval instead (invert
  `score_test`), or Agresti–Coull, or Clopper–Pearson for guaranteed
  (conservative) coverage. Verified: Wald `0.835` vs Wilson `0.963` at
  `p = 0.08, n = 40`
  ([`infer_sim.py`](../verification/infer_sim.py), `wald_vs_wilson_proportion`).
- **Profile-likelihood / LR interval**: invert `likelihood_ratio_test` — the set
  `{θ₀ : −2[ℓ(θ̂) − ℓ(θ₀)] ≤ χ²_{1, 1−α}}` (`wilks_theorem`). Transformation-invariant,
  respects boundaries, usually better small-sample behaviour than Wald — prefer
  it when the likelihood is available.
- **Delta method** (`delta_method_standard_error`): for a smooth `g`,
  `se(g(θ̂)) ≈ |g′(θ̂)| · se(θ̂)`; multivariate `∇g(θ̂)ᵀ Σ̂ ∇g(θ̂)`. Build the
  interval on the scale where the normal approximation is best (log for a
  ratio/rate, logit for a proportion, Fisher-z for a correlation), then
  back-transform the endpoints.

## Distribution-free intervals (regime: distribution_free)

- **Bootstrap** (`bootstrap`, `bootstrap_consistency` — **cited**): resample the
  data with replacement `B` times, recompute the statistic, and form an interval
  from the resample distribution (percentile; better, BCa or bootstrap-`t`).
  Consistent for **smooth** functionals of the CDF. **Fails** for:
  - the maximum / minimum or any parameter at the edge of support — the resample
    max can never exceed the sample max, so the percentile interval is
    systematically wrong (verified: coverage `0.000` for `max` of Uniform(0, θ),
    [`infer_sim.py`](../verification/infer_sim.py), `bootstrap_regular_vs_not`);
  - statistics with no finite variance (a Cauchy-type mean);
  - very small `n`; strong dependence not respected by the resampling scheme
    (use a block bootstrap for time series, a cluster bootstrap for clustered
    data).
- **DKW band** (`dvoretzky_kiefer_wolfowitz`): `P(sup_x |F̂(x) − F(x)| > ε) ≤
  2e^{−2nε²}` gives a **finite-sample, simultaneous** confidence band for the
  entire CDF at every `n` — one of the few honest small-sample distribution-free
  tools.
- **Quantile intervals**: an interval for a population quantile from a pair of
  order statistics has **exact binomial coverage** (`order_statistic`,
  `sample_quantile`), no distributional assumption.

## Reporting

Report `[lo, hi]`, the level, the regime, the method, and the comparison to the
threshold that matters. Do not report a bare p-value in place of an interval —
it communicates neither magnitude nor precision.
