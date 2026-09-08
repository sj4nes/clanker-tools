# Lean proof cores -- what the kernel verified vs what is cited

Run: `lean validation/proof-checks.lean`  (exit 0, no `sorry`, no `axiom`, no warnings).
Toolchain: Lean 4.33.1, **no Mathlib**.  Lean core `omega` / `grind` / `decide`
close the finitary algebraic identities and inequalities each statistical
statement reduces to once the integral, the CLT, and the Gaussian sampling
theory are granted.

`lean_status` in each `results/<id>.yaml`:

- **`core`** -- a GENUINE, universal theorem in `proof-checks.lean` (holds for all inputs).
- **`instance`** -- a `decide`d closed proposition over ONE fixed small integer
  design.  A sanity check, **not** a universal proof.
- **`cited`** -- proved in the literature (named source), not re-formalized here.
  Every deep asymptotic result of the capsule is `cited`.

## GENUINE, universal (`lean_status: core`)

| Lean name | Statement (finitary form) | Behind node(s) |
|---|---|---|
| `sq_nonneg'` | `0 ≤ z·z` over ℤ | support lemma |
| `lsum_map_mul`, `lsum_map_sub` | `Σ c·xᵢ = c·Σxᵢ`, `Σ(bᵢ−aᵢ) = Σbᵢ − Σaᵢ` | support lemmas |
| `score_mean_zero` | `Σ fᵢ(θ₀) = Σ fᵢ(θ₁)` ⇒ `Σ(fᵢ(θ₁) − fᵢ(θ₀)) = 0` -- the score is `∂(Σf) = Σ(∂f) = 0` | `score_identity` |
| `information_equality` | per point `∂²fᵢ = fᵢ(∂²log fᵢ + (∂log fᵢ)²)`, and `Σ∂²fᵢ = 0` ⇒ `E[∂²log f] = −E[(∂log f)²]` | `information_equality`, `score_test` |
| `centid` | `Σ pᵢ(xᵢ−m)² = Σ pᵢxᵢ² − 2m Σ pᵢxᵢ + m² Σ pᵢ` (list induction + `grind`) | `mse_bias_variance_decomposition`, `law_of_total_variance` (cited node), `exponential_family_moment_identities`, `variance` |
| `mse_decomp` = `posterior_mean_completes_square` | `n·Σ pᵢ(xᵢ−a)² = (Σpᵢxᵢ − na)² + (n·Σpᵢxᵢ² − (Σpᵢxᵢ)²)` -- complete the square; first term `= n²(mean−a)²` (min at `a = mean`), second `= n·Var` (free of `a`) | `mse_bias_variance_decomposition`, `posterior_mean_rule`, `bayes_rule_minimizes_bayes_risk` |
| `bayes_rule_pointwise` | a weighted sum of nonnegative terms is `≥ 0` -- a rule minimising each inner (posterior) term minimises the outer average | `bayes_rule_minimizes_bayes_risk`, `bayes_estimator` |
| `ssq_expand` | `Σ(n·xᵢ − s)² = n²·Σxᵢ² − 2n·s·Σxᵢ + s²·count` (list induction) | `bias_of_sample_variance` |
| `bias_sample_var` | specialise `n := count`, `s := Σx`: `Σ(count·xᵢ − Σx)² = count·(count·Σxᵢ² − (Σx)²)` -- cross-multiplied `E[Σ(Xᵢ−Xbar)²] = (n−1)σ²` | `bias_of_sample_variance`, `sample_variance`, `unbiased_error_variance_estimator` (see `instance`) |
| `anova_cross_term_zero` | `Σᵢ(count·xᵢ − Σx) = 0` -- the vanishing cross term in the SS decomposition | `one_way_anova_identity` |
| `crlb_cauchy_schwarz` | `(a₁s₁+a₂s₂)² ≤ (a₁²+a₂²)(s₁²+s₂²)` (2-vector Cauchy-Schwarz; difference `= (a₁s₂−a₂s₁)² ≥ 0`) | `cramer_rao_lower_bound` |
| `neyman_pearson_swap` | `φ* = 1{k f₀ < f₁}`, `φ ∈ [0,1]` ⇒ `(φ* − φ)(f₁ − k f₀) ≥ 0` pointwise | `neyman_pearson_lemma` |
| `rao_blackwell_var` | `within` a sum of `≥ 0` terms ⇒ `between ≤ between + Σ within` -- law of total variance ⇒ `Var(E[θ̂|T]) ≤ Var(θ̂)` | `rao_blackwell_theorem`, `lehmann_scheffe_theorem` |
| `factorization_discrete` | `(g·h)·H = (g·H)·h` -- the `g(t)` cancels in `P(X=x\|T=t)`, so the conditional law is θ-free | `neyman_fisher_factorization`, `exponential_family_sufficient_statistic` |
| `basu_step` | `joint = c·marginal` termwise ⇒ `Σ joint = c·Σ marginal` -- constant conditional given `T` ⇒ independence | `basu_theorem`, `normal_sample_mean_variance_independence` (see `instance`) |
| `bonferroni_bound` | `m₀ ≤ m`, `α ≥ 0` ⇒ `m₀·α ≤ m·α` | `bonferroni_correction` |
| `consistency_chebyshev` | `ε²·tail ≤ var`, `ε ≥ 1`, `tail ≥ 0` ⇒ `tail ≤ var` -- Chebyshev ⇒ `Var → 0` forces the tail probability `→ 0` | `consistency`, `method_of_moments` |
| `chisq_mgf_add` | `a' + b' = (2a' + 2b')/2` -- the MGF exponent arithmetic behind `χ²_a·χ²_b = χ²_{a+b}` | `chi_squared_additivity` |
| `interior_max_stationary` | interior max: `fL ≤ fM ∧ fR ≤ fM` ⇒ both one-sided differences `≥ 0` (derivative sign forced to 0) | `mle_score_equation` |
| `mle_invariance_monotone` | `g` monotone, `L(θ₁) ≤ L(θ₂)` ⇒ `g(θ₁) ≤ g(θ₂)` -- `argmax(g∘L) = g(argmax L)` (2-point) | `mle_invariance` |
| `pivot_coverage` | `{a ≤ Q ≤ b}` as a Bool identity -- `{θ ∈ C(x)} = {a ≤ Q(x,θ) ≤ b}`, so coverage `= 1 − α` for every θ | `pivot_method`, the exact normal CIs |
| `ci_test_duality` | `{θ₀ ∈ C(x)} = {x ∈ A(θ₀)}` -- the CI/test transpose identity | `confidence_set_test_duality` |
| `sandwich_reduces_when_info_equality` | `a = b` ⇒ `a·b·a = a·a·a` -- the sandwich `A⁻¹BA⁻¹` collapses to `A⁻¹` when `A = B = I(θ)` | `sandwich_variance`, `mle_asymptotic_normality` (cited) |
| `kde_amise_optimal_h` | `4A·h⁵ = B` -- stationarity of `A·h⁴ + B/h`, the `h ∝ n^{−1/5}` rate | `kde_bias_variance_tradeoff` |
| `mlr_power_monotone` | MLR ⇒ the Neyman-Pearson region `{T > c}` is θ₁-free (2-point) | `karlin_rubin_theorem` |
| `expfam_grad_A` | re-export of `centid` under the name the exp-family YAMLs cite | `exponential_family_moment_identities`, `mean_value_parametrization` |
| `sample_mean_linear` | `Σ c·xᵢ = c·Σ xᵢ` | `sample_mean` |

## INSTANCE checks -- ONE fixed integer design (`lean_status: instance`)

Design `X = [[1,0],[1,1],[1,2]]`, `n = 3`, `p = 2`; `XᵀX = [[3,3],[3,5]]`,
`6·H = [[5,2,-1],[2,2,2],[-1,2,5]]`.  Each is a closed integer proposition
`decide`d by the kernel.  **A passing instance is a sanity check, not a
universal proof.**

| Lean name | Check | Behind node(s) |
|---|---|---|
| `hat_matrix_idempotent` | `(6H)² = 6·(6H)` entrywise (H² = H); `tr(6H) = 6·p` | `ols_is_projection` |
| `rss_expectation` | `tr(I − H) = n − p = 1` | `unbiased_error_variance_estimator` |
| `centering_projection_rank` | `(3M)² = 3·(3M)` for `M = I − J/3`; `tr(3M) = 3·(n−1)` | `scaled_sample_variance_chi_squared` |
| `cochran_idempotent` | `(6I − 6H)·(6H) = 0` -- H ⟂ (I−H), ranks `2 + 1 = n` | `cochran_theorem`, `wilks_theorem` (cited) |
| `normal_equations_stationary` | `(XᵀX)·(6β̂) = 6·Xᵀy` for `y = (1,2,2)` | `normal_equations` |
| `gauss_markov_cross_term` | `Xᵀd = 0` for `d = (1,−2,1)` -- the cross term vanishes | `gauss_markov_theorem` |
| `fwl_block_elimination` | residualised `X₂ᵀM₁X₂ = 2`, `X₂ᵀM₁y = 3` ⇒ `β̂₂ = 1/2` matches the full regression | `partitioned_regression` |
| `gaussian_orthogonal_independent` | `(1,1,1) ⟂ (1,−1,0)` and `⟂ (0,1,−1)` -- the geometry behind `Xbar ⟂ S²` | `normal_sample_mean_variance_independence`, `ols_distribution_under_normal_errors` (cited) |

## CITED (`lean_status: cited`) -- not formalized here

Every deep result: `mle_consistency`, `mle_asymptotic_normality`,
`wilks_theorem`, `karlin_rubin_theorem`, `glivenko_cantelli`,
`dvoretzky_kiefer_wolfowitz`, `bootstrap_consistency`, `bernstein_von_mises`,
`three_tests_asymptotically_equivalent`, `pearson_chi_squared_gof`,
`exponential_family_completeness`, `le_cam_lan_theory`,
`hajek_convolution_theorem`, `local_asymptotic_minimax`, `donsker_theorem`,
`minimax_rate`, `complete_class`, `james_stein`; plus every `prob_*` / `ra_*` /
`linear_algebra_background` root (proved in the sibling capsule or a standard
linear-algebra text).  Sources in `sources/bibliography.md`.

## Counts

38 `core`, 6 `instance`, 103 `cited` (58 of which are `prob_*`/`ra_*`/`linear_algebra_background` roots).
The epistemic-status label of a node is never upgraded past what the kernel or a
cited checked proof establishes.
