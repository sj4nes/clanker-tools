# Conventions, foundational stance, and cycle resolutions

## Foundational stance (what is primitive for this release)

`math-statistics` Release 0.1 is **not self-contained**. It sits on
[`math-probability`](../math-probability/SKILL.md) Release 0.1 and takes an
explicit, enumerated set of objects and theorems as **cited primitives** — the
`prob_*`, `ra_*`, and `linear_algebra_background` nodes in `nodes/nodes.tsv`.
Each such node is `type: bridge`, `lean_status: cited`, and its
`primary_statement` ends with `-- <capsule>:<node>` naming the exact upstream
node it stands in for. These are the graph roots (no incoming edges).

| Layer | Primitive here | Where it is actually built |
|---|---|---|
| Probability space, random variables, laws, CDF/pmf/pdf | cited | `math-probability` |
| Expectation, variance, covariance, moments, MGF, CF | cited | `math-probability` |
| Independence, i.i.d., conditional expectation, tower / total variance | cited | `math-probability` |
| The distribution families used as models | cited | `math-probability` |
| The four convergence modes; WLLN, SLLN, CLT, Slutsky, CMT, delta method, Lévy | cited | `math-probability` |
| Markov / Chebyshev / Jensen / Cauchy–Schwarz / Hoeffding inequalities | cited | `math-probability` |
| Continuity, differentiability, Taylor, MVT, compactness, convexity, ∂-under-∫ | cited | `math-real-analysis` |
| **Finite-dimensional linear algebra** (rank, PSD, spectral theorem, projections, quadratic forms) | **cited, NO capsule** | `linear_algebra_background` — the one acknowledged gap |

**The `t`, `χ²`, `F` distributions are the exception** — they are `construction`
nodes *built here* from `prob_normal` and `prob_gamma`, not cited.

**ZFC + classical logic**, inherited. Excluded middle used freely. The Axiom of
Choice enters only through cited measure-theory results; no statistical theorem
in this release invokes AC in its own proof.

## Regularity conditions are first-class hypothesis nodes

The analogue of `math-probability` making `iid` and `finite_nonzero_variance`
first-class. Six `hypothesis` nodes —
`support_independent_of_theta`, `interchange_derivative_integral`,
`true_parameter_interior`, `fisher_information_positive_definite`,
`log_likelihood_smooth`, `identifiability` — carry a prerequisite edge into
every theorem that needs them (`score_identity`, `information_equality`,
`cramer_rao_lower_bound`, `mle_score_equation`, `mle_consistency`,
`mle_asymptotic_normality`, `wilks_theorem`). Applying one of those results
outside its regularity hypotheses is therefore a graph-visible defect.

## The per-result `regime` tag

Every inferential result YAML carries `regime: { exact | asymptotic |
distribution_free | bayesian }` — see `scope.md` §"The per-result tag". Indexed
in `indexes/regime-index.md`.

## Notation

| Symbol | Meaning | Notes |
|---|---|---|
| `theta`, `Theta` | parameter, parameter space | `theta_0` is the *true* value |
| `P_theta`, `E_theta`, `Var_theta` | probability / expectation / variance under `P_theta` | subscript never dropped in a multi-parameter context |
| `X_1, ..., X_n` | the sample; `X = (X_1,...,X_n)` | `n` = sample size throughout |
| `X_(1) <= ... <= X_(n)` | order statistics | parentheses on the index |
| `Xbar`, `Xbar_n` | sample mean `(1/n) sum X_i` | |
| `S^2` | sample variance with the **`n − 1`** divisor | `S^2 = (n-1)^{-1} sum (X_i - Xbar)^2` |
| `L(theta)`, `ell(theta)` | likelihood, log-likelihood | functions of `theta` for fixed data |
| `U(theta)` | score `d ell / d theta` | vector-valued in the multiparameter case |
| `I(theta)` | Fisher information (scalar) or matrix | **per observation**; the sample information is `n I(theta)` |
| `theta_hat` | a generic estimator; `theta_hat_MLE` when the method matters | |
| `b(theta)` | bias `E_theta[theta_hat] - theta` | |
| `phi`, `phi(x)` | test function, `phi: data -> [0,1]` | `phi = 1` means "reject `H0`" |
| `alpha` | the nominal size / 1 − confidence level | `z_{1-alpha/2}`, `t_{n-1,1-alpha/2}` are upper quantiles |
| `beta(theta)` | power function `E_theta[phi]` | not to be confused with a regression coefficient `beta` |
| `Lambda` | likelihood-ratio statistic `sup_{Theta_0} L / sup_Theta L` | `Lambda in [0,1]`; reject for small `Lambda` |
| `Phi`, `phi` (lower, in a density context) | standard-normal CDF, pdf | context disambiguates from a test function |
| `chi^2_k`, `t_k`, `F_{d1,d2}` | the sampling distributions | `k`, `d1`, `d2` are degrees of freedom |
| `F_hat_n` | empirical CDF | `F` without hat is the population CDF |
| `X` (regression) | the `n x p` design matrix | fixed, full column rank `p < n` |
| `H` | the hat matrix `X(X^T X)^{-1} X^T` | symmetric, idempotent, `rank p` |
| `pi`, `pi(theta | x)` | prior, posterior | a prior is a modeling input, never an axiom |

**Degrees of freedom.** `S^2` uses `n − 1`; regression error variance uses
`n − p`; a chi-squared goodness-of-fit with `d` estimated parameters uses
`k − 1 − d`. Every such count is stated explicitly in the node.

**One-sided vs two-sided.** Quantile subscripts are always written out
(`z_{1-alpha}` vs `z_{1-alpha/2}`); "the `alpha` level" alone is never used to
imply a side.

**`argmax`.** `theta_hat = argmax_theta ell(theta)` denotes *a* maximizer;
existence needs `ra_compactness` + `ra_continuity` and uniqueness is a separate
claim (edged where used).

## Cycle resolutions

None required in Release 0.1. Five *potential* cycles avoided by modeling choice
are recorded in [`edges/cycles.md`](edges/cycles.md).

## `tsort` order is not proof order and not teaching order

`indexes/tsort-order.txt` is one linearization of the DAG. Independent nodes
(e.g. the distribution families, the three regularity hypotheses) may land in
any relative order; do not read adjacency as logical necessity. The abstract
`decision_rule` node is emitted *after* `estimator` and `test_function` because
those are its prerequisites in this graph — that is the opposite of how a course
would introduce them.
