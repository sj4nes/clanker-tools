# Hypothesis testing and multiplicity

Workflow step 6. Test **only pre-specified hypotheses**. Nodes are in the
[`math-statistics`](../../math-statistics/SKILL.md) capsule.

## The frame

- `null_hypothesis` `H₀`, `alternative_hypothesis` `H₁`; a `test_function`
  `φ(x) ∈ {0, 1}` (reject / not).
- `size_of_test` `α = sup_{θ ∈ H₀} E_θ[φ]`; the *level* is any upper bound on
  the size. `type_i_error` = reject a true `H₀`; a **type II error** is failing
  to reject a false one (`1 − power`).
- `power_function` `β(θ) = E_θ[φ]`. **Compute the power at the minimum
  meaningful effect before running the test** — a test with 30 % power there
  cannot produce an informative "not significant".

## Choosing the test from optimality theory

| Situation | Optimal test | Node |
|---|---|---|
| simple `H₀: θ = θ₀` vs simple `H₁: θ = θ₁` | reject when the likelihood ratio `L(θ₁)/L(θ₀)` exceeds a threshold set to give size `α` | `neyman_pearson_lemma` (most powerful) |
| one-sided `H₀: θ ≤ θ₀` vs `H₁: θ > θ₀`, family has a monotone likelihood ratio in a statistic `T` | reject for large `T` | `monotone_likelihood_ratio` → `karlin_rubin_theorem` (uniformly most powerful) |
| two-sided or nuisance parameters present | no UMP test in general; use the likelihood-ratio test, optionally restricting to unbiased tests (power ≥ size everywhere) | `likelihood_ratio_test` |
| composite / multi-parameter, large sample | `−2 log Λ ⇒ χ²_r`, `r` = number of restrictions | `wilks_theorem` (**cited, asymptotic**) |

The three large-sample tests (`three_tests_asymptotically_equivalent`):

- **LRT** — needs both the null and the full fit; parametrization-invariant.
- **Wald** (`wald_test`) — needs only the full fit; **not** invariant to
  reparametrization; unreliable near a boundary.
- **Score / Lagrange multiplier** (`score_test`) — needs only the **null** fit;
  useful when the alternative is hard to fit.

They agree as `n → ∞` but can disagree materially at finite `n`; when they do,
trust the LRT / score over Wald.

Other named tests: `pearson_chi_squared_gof` (goodness of fit to a family;
limiting `χ²` is **asymptotic** — needs expected cell counts of roughly ≥ 5),
`one_sample_t_test` / `two_sample_t_test` (exact under normality),
`overall_f_test` and `one_way_anova_identity` (exact under normal errors, via
`cochran_theorem`'s quadratic-form decomposition).

## The p-value

`p_value`: the smallest `α` at which `H₀` is rejected, i.e. the probability
under `H₀` of a test statistic at least as extreme as observed.
`p_value_uniform_under_null`: for a continuous test statistic, the p-value is
`Uniform(0, 1)` under `H₀` — this is why it can be combined and calibrated, and
why "`p = 0.06`" and "`p = 0.6`" are very different pieces of evidence.

**A large p-value is not evidence for `H₀`.** "Fail to reject" with low power is
uninformative — report the interval and the effect sizes it still admits. To
make a positive claim of "no meaningful difference" you need an **equivalence
test**: pre-specify a margin `δ` and run two one-sided tests (TOST) of
`H₀: |θ| ≥ δ`; rejecting both concludes equivalence within `δ`. This is the
`confidence_set_test_duality` statement that the whole `1 − 2α` interval lies
inside `(−δ, δ)`.

## Multiplicity

Testing `m` hypotheses each at level `α` inflates the chance of **some** false
positive (`multiple_testing_fwer`) to roughly `1 − (1 − α)^m` under
independence — `≈ 0.64` for `m = 20, α = 0.05` (verified in
[`../verification/checks.bc`](../verification/checks.bc) and
[`infer_sim.py`](../verification/infer_sim.py) `fwer_multiplicity`).

| Goal | Procedure | Rule | Node |
|---|---|---|---|
| control the **family-wise error rate** (any false positive is costly) | Bonferroni | reject `Hᵢ` if `pᵢ ≤ α/m` | `bonferroni_correction` |
| " (less conservative, still FWER) | Holm step-down | order `p_{(1)} ≤ … ≤ p_{(m)}`; reject while `p_{(k)} ≤ α/(m − k + 1)` | — |
| " (exact under independence) | Šidák | `pᵢ ≤ 1 − (1 − α)^{1/m}` | `checks.bc` |
| control the **false discovery rate** (a known fraction of false positives among rejections is acceptable — screening) | Benjamini–Hochberg step-up | largest `k` with `p_{(k)} ≤ k q / m`; reject `H_{(1)} … H_{(k)}` | `benjamini_hochberg_fdr` |

FWER control ⇒ FDR control, not the reverse. Under positive dependence BH still
controls the FDR; under arbitrary dependence use the BY correction (divide `q`
by `Σ 1/i`). **Report both adjusted and unadjusted results**, and state which
hypotheses were pre-specified — anything chosen after seeing the data is
exploratory and its nominal level is meaningless.
