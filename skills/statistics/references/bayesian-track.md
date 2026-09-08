# Bayesian track and the decision-theory scaffold

Workflow step 8, taken only when a prior is genuinely in play. Nodes are in the
[`math-statistics`](../../math-statistics/SKILL.md) capsule. Computation (MCMC,
variational inference) is out of scope for both the capsule and this skill — the
planned `bayes-bridge` connector will carry the full apparatus.

## Prior specification

State the prior and **why**. Acceptable rationales: a genuine prior study or
elicited expert range; a structural constraint (a rate is non-negative, a
correlation is in `[−1, 1]`); a deliberately weak / reference prior chosen to
let the data dominate. Not acceptable: a prior chosen because it moved the
posterior where you wanted it.

Always report a **prior-sensitivity analysis** — recompute under at least one
alternative prior (a wider one, and a skeptical one centred at the null) and
show the posterior summary for each.

## Conjugacy

`conjugate_prior`: a prior family closed under the likelihood, so the posterior
is the same family with updated hyperparameters — a closed form, no computation.

| Likelihood | Conjugate prior | Posterior |
|---|---|---|
| Bernoulli / Binomial `θ` | Beta(`a`, `b`) | Beta(`a + Σxᵢ`, `b + n − Σxᵢ`) |
| Poisson `λ` | Gamma(`a`, `b`) | Gamma(`a + Σxᵢ`, `b + n`) |
| Normal mean `μ`, known `σ²` | Normal(`μ₀`, `τ²`) | Normal (precision-weighted average of `μ₀` and `x̄`) |
| Normal `μ, σ²` | Normal–Inverse-Gamma | Normal–Inverse-Gamma |
| Exponential / Gamma-rate `λ` | Gamma | Gamma |
| Multinomial `p` | Dirichlet | Dirichlet |

The posterior mean is a weighted average of the prior mean and the MLE, with
weights set by prior precision vs data precision — so a conjugate Bayes
estimator is an explicit **shrinkage** estimator (this is the mechanism behind
`james_stein` and hierarchical models).

## Posterior summaries and intervals

- `posterior_mean_rule` — the posterior mean minimises posterior expected
  **squared-error** loss; `bayes_estimator` under `L₂`.
- `posterior_median_rule` — minimises posterior expected **absolute-error**
  loss; more robust to a skewed posterior.
- `credible_interval` — an interval of posterior probability `1 − α` (either
  equal-tailed, or the highest-posterior-density set). It is a direct
  probability statement about `θ` **given the model and prior** — *not* a
  confidence interval, and it should never be described as one.

## Frequentist agreement is asymptotic only

`bernstein_von_mises`: under the regularity conditions, as `n → ∞` the posterior
is approximately `N(θ̂_MLE, I(θ₀)⁻¹/n)` **regardless of a fixed prior**, so a
credible interval and a Wald confidence interval nearly coincide. At small `n`,
near a boundary (`true_parameter_interior` fails), or with an informative prior,
they can differ substantially — do not lean on this equivalence to report a
credible interval as if it had frequentist coverage.

## The decision-theory scaffold

The capsule frames estimation and testing as decisions:

- `loss_function` `L(θ, a)`; `decision_rule` `δ(x)`; `risk_function`
  `R(θ, δ) = E_θ[L(θ, δ(X))]` — risk is expected loss, as a function of the
  unknown `θ`.
- `admissibility` — `δ` is inadmissible if some `δ′` has `R(θ, δ′) ≤ R(θ, δ)`
  everywhere with strict inequality somewhere. `james_stein` shows the MLE of a
  `≥ 3`-dimensional normal mean is inadmissible under summed squared error.
- `minimax_rule` — minimises the worst-case risk `sup_θ R(θ, δ)`; the
  conservative choice when no prior is defensible.
- `bayes_risk` `∫ R(θ, δ) π(θ) dθ`; `bayes_rule_minimizes_bayes_risk` — the
  Bayes rule for a proper prior is the posterior-expected-loss minimiser, and
  (`complete_class`, stated) under mild conditions every admissible rule is a
  Bayes rule or a limit of them. This is the formal bridge between the Bayesian
  and frequentist accounts.
