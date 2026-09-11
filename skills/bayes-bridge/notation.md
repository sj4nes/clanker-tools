# Notation — master symbol list

| Symbol | Meaning | Type | Area |
|---|---|---|---|
| `theta` | parameter under inference | real / vector, per application | inference |
| `x`, `x_1..x_n` | observed data | per application | inference |
| `pi(theta)` | prior density | nonnegative, integrates to 1 | inference |
| `pi(theta\|x)` | posterior density | nonnegative, integrates to 1 | inference |
| `L(theta)` | likelihood function, `x` fixed | nonnegative function of `theta` | inference |
| `p(x)` | marginal likelihood | positive real | model_comparison |
| `a, b` | Beta/Gamma hyperparameters (shape, rate) | positive reals | inference |
| `mu0, tau0^2` | Normal prior mean, variance | real, positive real | inference |
| `mu_n, tau_n^2` | Normal posterior mean, variance | real, positive real | inference |
| `s`, `xbar` | sufficient statistics (sum, sample mean) | matching data type, real | inference |
| `M0, M1` | two candidate models | — | model_comparison |
| `BF_10` | Bayes factor, `p(x\|M1)/p(x\|M0)` | positive real | model_comparison |
| `C(x)` | interval estimate (credible or confidence) | subset of `R` or `[0,1]` | inference |
| `alpha` | miscoverage / significance level | in `(0,1)` | inference |

Fixed throughout: `theta` the parameter, `x` the data, `M0`/`M1` in that
order, `BF_10` never read as `BF_01`. See `conventions.md` for the
reasoning behind each fixed choice.
