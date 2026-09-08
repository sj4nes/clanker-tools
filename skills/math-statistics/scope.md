# Scope — Release 0.1

**Mathematical statistics from the statistical model to the classical
large-sample theory — the theorem layer under a future `statistics`
analysis-methodology skill and the `bayes-bridge` connector.**

Built with the [`math-theorem-tree`](../math-theorem-tree/SKILL.md) method. Sits
directly on top of [`math-probability`](../math-probability/SKILL.md) (Release
0.1) and, through it, on `math-real-analysis` and
`math-sets-functions-cardinality`. It is the statistical-inference analogue of
the way `math-real-analysis` sits on `math-number-systems`.

## What it discharges upward into `math-probability`

Taken as **cited primitives** (root nodes, `bridge` type, `lean_status: cited`,
each pointing at a named `math-probability` node):

- `probability_space`, `random_variable`, `random_vector`, `cdf`, `pmf`, `pdf`,
  `joint_distribution`, `marginal_distribution`, `conditional_distribution`;
- `expectation`, `lotus`, `expectation_linearity`, `variance`, `covariance`,
  `correlation`, `mgf`, `characteristic_function`, `moment`;
- `independence_random_variables`, `iid`, `independence_factorization`;
- the distribution families used as models — `bernoulli_distribution`,
  `binomial_distribution`, `poisson_distribution`, `geometric_distribution`,
  `continuous_uniform_distribution`, `exponential_distribution`,
  `gamma_distribution`, `beta_distribution`, `normal_distribution`,
  `standard_normal`, `normal_affine_closure`, `cauchy_no_mean`;
- the four convergence modes (`convergence_almost_sure`,
  `convergence_in_probability`, `convergence_in_lp`,
  `convergence_in_distribution`) and `convergence_implications`;
- the limit theorems — `weak_law_large_numbers`, `strong_law_large_numbers`,
  `central_limit_theorem`, `lindeberg_clt`, `levy_continuity_theorem`,
  `slutsky_theorem`, `continuous_mapping_theorem`, `delta_method`,
  `portmanteau_theorem`;
- `conditional_expectation_abstract`, `tower_property`,
  `law_of_total_variance`, `conditional_expectation_l2_projection`;
- the inequalities — `markov_inequality`, `chebyshev_inequality`,
  `jensen_inequality`, `cauchy_schwarz_expectation`, `holder_inequality`,
  `hoeffding_inequality`.

## What it takes from `math-real-analysis` (root nodes, cited)

`continuity`, `differentiability`, `taylor_theorem` (with Lagrange remainder),
`mean_value_theorem`, `compactness` (for existence of an argmax/argmin),
`convex_function`, `uniform_convergence`, `interchange_limit_integral`
(dominated convergence for the "differentiate under the integral sign" step).

## What it takes as CITED BACKGROUND without a capsule (foundational gap)

**Finite-dimensional linear algebra.** There is no `math-linear-algebra` capsule
yet. A single `bridge` node `linear_algebra_background` enumerates exactly what
is assumed — vector space and subspace, matrix rank, transpose, inverse,
symmetric and positive-(semi)definite matrices, the spectral theorem for real
symmetric matrices, orthogonal projection onto a subspace and the projection
matrix, the trace, `rank`–`nullity`, and quadratic forms. Every regression and
quadratic-form result edges to it. **Flagged for a future capsule below this
one.**

## Included

### 1. The statistical model and likelihood
- `statistical_model`, `parametric_model`, `parameter_space`,
  `identifiability`, `dominated_family`, `iid_sample`, `statistic`;
- `likelihood_function`, `log_likelihood`, `score_function`,
  `fisher_information` (scalar) and `fisher_information_matrix`;
- the **score identity** `E_θ[score] = 0` and the **information equality**
  `I(θ) = Var_θ(score) = −E_θ[∂²ℓ/∂θ²]`;
- the **regularity conditions** as first-class `hypothesis` nodes:
  `support_independent_of_theta`, `interchange_derivative_integral`,
  `true_parameter_interior`, `fisher_information_positive_definite`,
  `log_likelihood_thrice_differentiable`, `identifiable_at_truth`.

### 2. Exponential families
- `exponential_family` (canonical / natural parametrization),
  `natural_parameter_space`, `cumulant_function`, `mean_value_parametrization`,
  `exponential_family_sufficient_statistic`,
  `exponential_family_moment_identities` (cumulant-function derivatives),
  `exponential_family_completeness` (full-rank ⇒ complete).

### 3. Data reduction — sufficiency, ancillarity, completeness
- `sufficiency`, `neyman_fisher_factorization`, `minimal_sufficiency`,
  `ancillary_statistic`, `completeness_statistic`, `bounded_completeness`,
  `basu_theorem` (complete sufficient ⟂ ancillary).

### 4. Point estimation and its optimality theory
- `estimator`, `bias`, `mean_squared_error`,
  `mse_bias_variance_decomposition` (`MSE = Var + bias²`), `consistency`,
  `asymptotic_normality`, `asymptotic_variance`, `relative_efficiency`,
  `asymptotic_efficiency`;
- `unbiased_estimator`, `umvue`, `cramer_rao_lower_bound` (regularity edged),
  `rao_blackwell_theorem`, `lehmann_scheffe_theorem`,
  `attainment_of_crlb_iff_exponential_family`.

### 5. Methods of estimation
- `method_of_moments`, `plug_in_principle`,
  `maximum_likelihood_estimator`, `mle_invariance`,
  `mle_consistency` (cited — Wald), `mle_asymptotic_normality`
  (`√n(θ̂−θ) ⇒ N(0, I(θ)⁻¹)`, regularity edged),
  `m_estimator`, `estimating_equation`, `sandwich_variance` (stated),
  `bayes_estimator`, `posterior_mean_squared_error_rule`,
  `posterior_median_absolute_error_rule`, `conjugate_prior`,
  `credible_interval`, `bernstein_von_mises` (stated — the Bayes/frequentist
  large-sample bridge).

### 6. Decision-theoretic scaffold
- `loss_function`, `risk_function`, `decision_rule`, `admissibility`,
  `minimax_rule`, `bayes_risk`, `bayes_rule_minimizes_bayes_risk`,
  `complete_class` (stated), `james_stein` (stated `counterexample` — the MLE of
  a ≥3-dim normal mean is inadmissible under squared loss).

### 7. The exact Gaussian core (finite-sample, no asymptotics)
- `chi_squared_distribution`, `students_t_distribution`, `f_distribution` —
  **constructed here** from the probability capsule's normal and gamma
  (`χ²_k = Gamma(k/2, 1/2)`; `t_k = Z/√(V/k)`; `F = (U/d₁)/(V/d₂)`);
- `sample_mean`, `sample_variance`, `bias_of_sample_variance`
  (`E[S²] = σ²` with the `n−1`),
  `normal_sample_mean_variance_independence` (Basu / Cochran),
  `scaled_sample_variance_is_chi_squared` (`(n−1)S²/σ² ~ χ²_{n−1}`),
  `t_statistic_distribution`, `one_sample_t_test`, `two_sample_t_test`,
  `f_test_equality_of_variances`, `cochran_theorem` (quadratic-form
  decomposition), `one_way_anova_identity`.

### 8. Interval estimation
- `confidence_set`, `coverage_probability`, `pivotal_quantity`, `pivot_method`,
  `confidence_set_test_duality`, `wald_interval`, `score_interval`,
  `likelihood_ratio_interval`, `normal_mean_ci_known_variance`,
  `normal_mean_ci_unknown_variance` (the t-interval),
  `normal_variance_ci`, `large_sample_wald_interval`,
  `delta_method_standard_error`.

### 9. Hypothesis testing
- `null_hypothesis`, `alternative_hypothesis`, `test_function`, `size_of_test`,
  `level_of_test`, `power_function`, `type_i_error`, `type_ii_error`,
  `neyman_pearson_lemma` (MP test for simple-vs-simple),
  `monotone_likelihood_ratio`, `karlin_rubin_theorem` (UMP one-sided under
  MLR), `unbiased_test`, `ump_unbiased`, `likelihood_ratio_test`,
  `wilks_theorem` (`−2 log Λ ⇒ χ²`, cited/asymptotic),
  `wald_test`, `score_test`, `three_tests_asymptotically_equivalent`,
  `p_value`, `p_value_uniform_under_null`,
  `pearson_chi_squared_goodness_of_fit` (cited limiting χ²),
  `multiple_testing_fwer`, `bonferroni_correction`,
  `benjamini_hochberg_fdr` (stated).

### 10. Nonparametric / distribution-free glue
- `empirical_cdf`, `glivenko_cantelli` (cited),
  `dvoretzky_kiefer_wolfowitz` (stated finite-sample band),
  `plug_in_estimator`, `bootstrap` (definition + `bootstrap_consistency`
  cited), `kolmogorov_smirnov_statistic` (stated),
  `order_statistic`, `sample_quantile`,
  `kernel_density_estimator` (stated, with the bias–variance / bandwidth
  tradeoff as a `regime` node).

### 11. Linear regression (Gaussian-noise, fixed design)
- `linear_model` (`y = Xβ + ε`, `X` fixed full-rank),
  `ordinary_least_squares`, `normal_equations`,
  `ols_is_projection` (`ŷ = Hy`, `H` the hat matrix),
  `gauss_markov_theorem` (OLS is BLUE under `E[ε]=0`, `Cov(ε)=σ²I`),
  `residual_sum_of_squares`, `unbiased_error_variance_estimator`,
  `ols_distribution_under_normal_errors` (`β̂ ~ N(β, σ²(XᵀX)⁻¹)`),
  `coefficient_t_test`, `overall_f_test`, `r_squared`,
  `partitioned_regression` (Frisch–Waugh–Lovell, stated).

### 12. Principles and boundary nodes (stated, not proved)
- `likelihood_principle` (a `regime`/principle node — stated with the
  Birnbaum theorem as a note), `sufficiency_principle`,
  `conditionality_principle`;
- boundary: `le_cam_lan_theory`, `hajek_convolution_theorem`,
  `local_asymptotic_minimax`, `bahadur_efficiency`, `donsker_theorem`,
  `bootstrap_consistency`, `bernstein_von_mises`, `james_stein`,
  `minimax_rate` — the doorway to Release 0.2 and to nonparametric /
  high-dimensional / semiparametric theory.

## Excluded (out of scope for 0.1)

- **Computation.** MCMC, EM, variational inference, numerical optimization for
  the MLE, the bootstrap as an algorithm to run. Definitions and the
  consistency *statements* only.
- **Experimental design** — randomization, blocking, power *analysis for design*,
  optimal design. That is [`design-of-experiments`](../design-of-experiments/SKILL.md);
  this capsule is inference on data already collected.
- **Causal inference** — potential outcomes, DAGs, IV, propensity scores.
- **Time series, survival analysis, spatial statistics, longitudinal / mixed
  models, GLMs** beyond the Gaussian linear model. Logistic/Poisson regression
  is *mentioned* as an exponential-family + MLE instance, not developed.
- **High-dimensional and post-selection inference** — lasso, ridge as an
  estimator family beyond a mention, sparsity, selective inference,
  concentration of measure in `p ≫ n`.
- **Full empirical-process theory** — Donsker classes, VC dimension, uniform
  entropy. `glivenko_cantelli` and `donsker_theorem` are boundary nodes.
- **Measure-theoretic decision theory and full Le Cam theory** — comparison of
  experiments, deficiency, the general convolution/LAM theorems are boundary
  nodes.
- **Nonparametric Bayes**, Dirichlet processes, Gaussian-process regression.

## Size

**Target ≈ 125–140 nodes.** Statistics at this level carries a high concept
load: the model/likelihood/regularity block, sufficiency–completeness, the
optimality theorems, three parallel test constructions, the exact Gaussian core,
regression, and the nonparametric glue each contribute an irreducible cluster of
dependency-distinct nodes. A release is judged by selection and dependency
clarity, not by hitting a node budget.

## Level and audience

A first rigorous mathematical-statistics course: Casella–Berger *Statistical
Inference* 2e; Lehmann–Casella *Theory of Point Estimation*; Lehmann–Romano
*Testing Statistical Hypotheses*; van der Vaart *Asymptotic Statistics*;
Keener *Theoretical Statistics*; Wasserman *All of Statistics*; Bickel–Doksum
*Mathematical Statistics*. First-year graduate, or a strong senior-undergraduate
course that takes measure-based probability as given.

## Foundational stance

- **ZFC + classical logic**, inherited through `math-probability`. Excluded
  middle is used freely.
- **Probability is the floor.** Every probabilistic object and theorem above is
  a **cited root** — a `bridge` node with `lean_status: cited` and a pointer to
  the exact `math-probability` node. This capsule *uses* the CLT, the SLLN,
  Slutsky, the delta method, conditional expectation; it does not re-prove them.
- **Finite-dimensional linear algebra is cited background** with no capsule (see
  `linear_algebra_background`). This is the one acknowledged gap; a
  `math-linear-algebra` capsule is the natural future floor.
- **The `t`, `χ²`, `F` distributions are constructed, not cited** — they are
  genuine `construction` nodes built from the probability capsule's `normal`
  and `gamma`. Their sampling-distribution roles (`(n−1)S²/σ² ~ χ²_{n−1}`,
  `t`-statistic) are `proved_theorem` with Lean-checked algebraic cores where
  finitary.
- **Regularity conditions are first-class `hypothesis` nodes**, edged into
  every theorem that needs them — Cramér–Rao, MLE asymptotic normality, Wilks,
  the information equality. Using one of these results outside its regularity
  hypotheses must be visible in the graph. This is the analogue of
  `math-probability` making `iid` and `finite_nonzero_variance` first-class.
- **Both paradigms.** Frequentist and Bayesian results both included. A prior is
  a **modeling-input `definition` node**, never an axiom; `bayes_estimator` and
  the frequentist estimators are siblings under `decision_rule`.
- **The Axiom of Choice** enters only through cited probability/measure results.
  No statistical theorem in this release needs AC in its own proof.

## Proof policy

Proofs are **sketched**, with the finitary algebraic / inequality core
**Lean-checked** where feasible:

- `mse_bias_variance_decomposition` (`E[(θ̂−θ)²] = Var(θ̂) + (E θ̂ − θ)²`);
- the **score identity** `E[∂ log f] = ∫ ∂f = ∂∫f = 0` as an
  interchange-of-∂-and-∫ identity, and the **information equality** as the
  algebraic consequence `−E[∂²ℓ] = E[(∂ℓ)²]` given `∫f = 1`;
- `cramer_rao_lower_bound` reduced to Cauchy–Schwarz on `(θ̂, score)`
  (the CS step Lean-checked; the covariance-equals-1 step from the score
  identity);
- `rao_blackwell_theorem` reduced to conditional Jensen / the law of total
  variance (`Var(θ̂) = Var(E[θ̂|T]) + E[Var(θ̂|T)] ≥ Var(E[θ̂|T])`);
- `neyman_fisher_factorization` in the **discrete** case as an identity;
- `neyman_pearson_lemma` via the pointwise `(φ − φ')(f₁ − k f₀) ≥ 0` swap
  (Lean-checked as a sign inequality over a grid + the universal step);
- `bias_of_sample_variance` (`E[Σ(Xᵢ−X̄)²] = (n−1)σ²`) as a finite algebraic
  identity (Lean-checked, `Int` counts);
- `mse_bias_variance_decomposition` for regression / `normal_equations`
  (`XᵀX β̂ = Xᵀy`) and `gauss_markov_theorem` as the projection identity
  `Cov(β̃) − Cov(β̂) = σ² D Dᵀ ⪰ 0` (quadratic-form nonnegativity Lean-checked
  in a fixed small dimension, `decide`);
- `mse_bias_variance_decomposition`, `bayes_rule_minimizes_bayes_risk` under
  squared loss (posterior mean minimizes `E[(θ − a)² | x]`) as the
  complete-the-square identity;
- `t_statistic_distribution` and `chi_squared` degrees-of-freedom algebra
  (`χ²_a + χ²_b = χ²_{a+b}` from `Gamma` additivity) as identities.

Deep asymptotic theorems — `mle_consistency`, `mle_asymptotic_normality`,
`wilks_theorem`, `glivenko_cantelli`, `karlin_rubin_theorem`,
`bootstrap_consistency`, `bernstein_von_mises` — are **cited** with explicit
`lean_status: cited` and a named source. Never labelled `proved_*` beyond what
the kernel or a cited checked proof establishes.

`bc` worksheets carry: the CRLB at named models (Bernoulli `p(1−p)/n`,
Poisson `λ/n`, Normal mean `σ²/n`); the `n−1` correction shown numerically on a
small sample; `t`/`χ²`/`F` critical values and the `t → Normal` convergence;
Neyman–Pearson likelihood-ratio thresholds for a Normal shift; the
Rao–Blackwell variance drop on a worked example; OLS on a 3-point design;
the coverage of a Wald interval by simulation-style enumeration; the
Benjamini–Hochberg step-up on a fixed p-value vector.

## Epistemic-status policy

Every result node carries one status label from the `math-theorem-tree` list.
`definition` / `axiom` / `structure` nodes carry `well_definedness`.
`cited` theorems are labelled `proved_theorem` **with `lean_status: cited`** and
a source. Boundary nodes are `stated_not_proved`.

## The per-result tag: `regime`

The `choice_grade` (sets capsule) / `convergence_mode` (probability capsule)
analogue for this release. Every **inferential** result YAML carries

    regime: one of { exact, asymptotic, distribution_free, bayesian }

- `exact` — the stated sampling distribution / coverage / size holds at every
  finite `n` under the model (the Gaussian core, Neyman–Pearson, Rao–Blackwell,
  Cramér–Rao, Gauss–Markov).
- `asymptotic` — the guarantee is a limit as `n → ∞` (MLE normality, Wald /
  score / LR tests and their intervals, Wilks, the delta-method SE,
  Pearson χ²).
- `distribution_free` — the guarantee holds for **every** distribution in a
  broad nonparametric class (the ECDF, Glivenko–Cantelli, DKW, KS, the
  bootstrap's target, rank-based ideas).
- `bayesian` — the guarantee is a posterior statement, conditional on the prior
  (Bayes estimators, credible intervals, Bernstein–von Mises straddles
  `bayesian` and `asymptotic`).

An index (`indexes/regime-index.md`) lists every result by regime. Reading an
`asymptotic` result as an `exact` finite-sample guarantee is the single most
common misuse in applied statistics — the tag makes it a graph-visible property.
