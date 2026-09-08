# Estimators and their optimality theory

Workflow step 4. Nodes are in the
[`math-statistics`](../../math-statistics/SKILL.md) capsule.

## The methods

| Method | Node | Idea | When it is the right call |
|---|---|---|---|
| Method of moments | `method_of_moments` | set sample moments equal to population moments, solve for `θ` | a quick consistent starting value; when the likelihood is intractable |
| Maximum likelihood | `maximum_likelihood_estimator`, `mle_score_equation` | maximise `ℓ(θ)`; solve `score = 0` | a trusted parametric model with regularity holding; gives `mle_invariance` (the MLE of `g(θ)` is `g(θ̂)`) |
| M-estimator | `m_estimator` | solve a general estimating equation `Σ ψ(Xᵢ, θ) = 0` | robustness (bounded `ψ`), or when only a moment condition is trusted, not a full likelihood |
| Bayes estimator | `bayes_estimator` | a summary of the posterior (see `references/bayesian-track.md`) | a defensible prior exists; small samples where it stabilises the estimate |
| Plug-in / substitution | `plug_in_principle`, `plug_in_estimator` | estimate a distribution functional `T(P)` by `T(P̂)` with the empirical CDF | distribution-free targets (a quantile, a Gini coefficient, a correlation) |

## Comparing estimators: MSE, not unbiasedness

`mse_bias_variance_decomposition`: `MSE(θ̂) = Var(θ̂) + bias(θ̂)²`. An unbiased
estimator with large variance can be **dominated** by a biased one — this is not
a corner case:

- `bias_of_sample_variance`: dividing by `n` (the MLE) gives lower MSE for a
  normal variance than dividing by `n − 1` (the unbiased choice), for every `n`.
- `james_stein`: in dimension `p ≥ 3`, shrinking the vector of sample means
  toward a point strictly dominates the MLE under summed squared-error loss —
  the MLE is **inadmissible**.

Compare candidates on `mean_squared_error`, or on the decision-relevant
`risk_function` if the loss is asymmetric (see `references/bayesian-track.md`
for the decision-theory scaffold: `loss_function`, `risk_function`,
`admissibility`, `minimax_rule`, `bayes_risk`).

## The variance floor: Cramér–Rao

`cramer_rao_lower_bound`: under the regularity conditions, any unbiased `θ̂`
satisfies `Var(θ̂) ≥ 1 / I(θ)` (scalar) or `≥ I(θ)⁻¹` (matrix, in the
Loewner order), where `I(θ)` is the Fisher information — computable two ways by
the `information_equality`: `I(θ) = Var(score) = −E[∂²ℓ/∂θ²]`.

`crlb_attainment`: the bound is attained **at every `n`** by an unbiased
estimator **iff** the model is an exponential family and `θ̂` is the mean-value
parameter (the expectation of the natural sufficient statistic). Outside that
case:

- no finite-sample-efficient unbiased estimator exists;
- the bound is only an **asymptotic** target — the MLE reaches it in the limit
  (`asymptotic_efficiency`, `√n(θ̂ − θ) ⇒ N(0, I(θ)⁻¹)`), a `regime: asymptotic`
  statement, and `mle_asymptotic_normality` is **cited**, not kernel-proved.

Worked CRLB checks (Bernoulli / Poisson attained, normal variance not) are in
[`../verification/checks.bc`](../verification/checks.bc).

## Data reduction: use the sufficient statistic

If a sufficient statistic `T` exists (`sufficiency`,
`neyman_fisher_factorization` — the density factors as
`g(T(x); θ) · h(x)`), inference should depend on the data only through `T`.
`minimal_sufficiency` is the coarsest such `T`.

- `rao_blackwell_theorem`: for any estimator `δ`, the conditional expectation
  `E[δ | T]` has the same bias and variance no larger — strictly smaller unless
  `δ` was already a function of `T`. It uses `prob_law_total_variance`.
- `lehmann_scheffe_theorem`: if `T` is also **complete** (`completeness_statistic`
  — no non-trivial unbiased estimator of zero is a function of `T`;
  `exponential_family_completeness` gives it for full-rank exponential families),
  then `E[δ | T]` for an unbiased `δ` is the **unique** minimum-variance unbiased
  estimator (`umvue`).
- `basu_theorem`: a complete sufficient statistic is independent of any
  ancillary statistic (`ancillary_statistic` — one whose distribution does not
  depend on `θ`). This is how `X̄ ⟂ S²` is proved for the normal
  (`normal_sample_mean_variance_independence`).

Recipe for a UMVUE: find any unbiased estimator (however crude — an indicator
often works), then Rao–Blackwellise it against the complete sufficient
statistic. Verified for `e^{−λ}` under Poisson data in
[`../verification/infer_sim.py`](../verification/infer_sim.py)
(`rao_blackwell_poisson`).

## When the parametric model is doubtful

- **Sandwich / Huber–White variance** (`sandwich_variance`): for an M-estimator
  solving `Σ ψ = 0`, the variance `A⁻¹ B A⁻ᵀ` (with `A = E[−∂ψ/∂θ]`,
  `B = E[ψ ψᵀ]`) is consistent even when the working model is wrong, as long as
  the estimating equation still has mean zero at the target. This is the
  standard fix for a mis-specified likelihood ("model-robust standard errors").
- **Bootstrap** (`bootstrap`, `bootstrap_consistency`): see
  `references/interval-estimation.md` — consistent for smooth functionals,
  **inconsistent** at the boundary, for the maximum, and for infinite-variance
  statistics.
