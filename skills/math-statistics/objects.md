# The type vocabulary

Which sets / spaces / structures the objects in this capsule inhabit, and the
well-formedness rules used in the `type_check_status` field of each result YAML.

## Base objects (from the cited roots)

- **Sample space** `(X, A)` — a measurable space; observations are `A`-measurable
  random elements. Usually `X = R` or `R^k`.
- **Parameter** `theta` — a point of `Theta subset R^d` (parametric model). `d`
  fixed and finite. A **prior** is a probability measure on `(Theta, B(Theta))`.
- **The model** `P = { P_theta : theta in Theta }` — a family of probability
  measures on `(X, A)`, indexed by `Theta`.
- **Density** `f(.; theta)` — a nonnegative `A`-measurable function with
  `int f dmu = 1`, for a common sigma-finite `mu` (dominated model).

## Derived objects and their types

| Object | Type | Well-formedness check |
|---|---|---|
| statistic `T` | measurable `X^n -> Y` | no `theta` in its definition; measurable |
| estimator `theta_hat` | statistic valued in `Theta` (or the range of the estimand `g`) | takes values in the target space; measurable |
| likelihood `L(.)` | function `Theta -> [0, inf)` | data fixed, `theta` free; needs the dominated-model condition |
| score `U(.)` | random function `Theta -> R^d` | `log f(x; .)` differentiable in `theta` |
| Fisher information `I(theta)` | symmetric PSD `d x d` matrix (scalar `>= 0` if `d = 1`) | finite; PD is the separate hypothesis node |
| test function `phi` | measurable `X^n -> [0, 1]` | `[0,1]`-valued; `1` = reject |
| power / coverage function | `Theta -> [0, 1]` | it is `theta -> E_theta[phi]` resp. `P_theta(theta in C)` |
| confidence set `C(X)` | random subset of `Theta` | `{ (x, theta) : theta in C(x) }` measurable |
| pivot `Q(X, theta)` | `X^n x Theta -> R` | its law under `P_theta` is the same for all `theta` |
| loss `L(theta, a)` | `Theta x A -> [0, inf)` | nonnegative |
| risk `R(., delta)` | `Theta -> [0, inf)` | `= E_theta[L(theta, delta(X))]`, expectation exists |
| decision rule `delta` | `X^n -> A` (or `-> P(A)` randomized) | measurable |
| exponential-family natural parameter `eta` | point of the convex set `H subset R^k` | `int h e^{eta.T} dmu < inf` |
| empirical CDF `F_hat_n` | random element of the cadlag functions `R -> [0,1]` | nondecreasing step function with jumps `1/n` |
| empirical measure `P_hat_n` | random probability measure on `(X, A)` | mass `1/n` at each `X_i` |
| kernel density estimate `f_hat_h` | random element of `L^1(R)` (a density if `K` is) | `h > 0`, `K` a symmetric density |
| design matrix `X` | fixed real `n x p` matrix | full column rank `p < n` |
| hat matrix `H` | real symmetric idempotent `n x n` matrix | `H = H^T = H^2`, `rank H = p` |
| sampling law `chi^2_k` / `t_k` / `F_{d1,d2}` | probability measure on `(0, inf)` resp. `R` | `k, d1, d2 > 0` |

## Recurring well-formedness pitfalls (checked in `validation/type-checks.md`)

- A quantity called a **statistic** must not contain `theta` (e.g.
  `sum (X_i - mu)^2` with the true `mu` is not a statistic).
- A **pivot** contains `theta` and is *not* a statistic; its defining property
  is a `theta`-free law.
- **Per-observation vs sample** Fisher information: `I(theta)` vs `n I(theta)` —
  a factor-of-`n` type error.
- **Degrees of freedom**: `n - 1` (one-sample `S^2`), `n - p` (regression),
  `k - 1 - d` (goodness-of-fit) — each stated explicitly per node.
- A **credible** level is a posterior probability (`theta` random); a
  **confidence** level is a coverage frequency (`C(X)` random). Different types.
- **Matrix vs scalar**: `I(theta)^{-1}` requires PD (linear_algebra_background);
  the scalar case just needs `I(theta) > 0`.
