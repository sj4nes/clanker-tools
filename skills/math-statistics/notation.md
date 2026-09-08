# Master symbol list

See [`conventions.md`](conventions.md) for usage rules (degrees of freedom,
one- vs two-sided quantiles, `argmax` existence). This file is the flat
symbol -> meaning -> area reference; the generated
[`indexes/symbol-index.md`](indexes/symbol-index.md) is the KWIC view over the
node corpus.

| Symbol | Meaning | Area |
|---|---|---|
| `theta`, `Theta`, `theta_0` | parameter, parameter space, true parameter value | model |
| `P_theta`, `E_theta`, `Var_theta` | probability / expectation / variance under the law `P_theta` | model |
| `f(x; theta)` | model density (likelihood contribution of one observation) | model |
| `X_1,...,X_n`, `X` | the sample; `X` also the regression design matrix (context) | model / regression |
| `X_(1) <= ... <= X_(n)` | order statistics | nonparametric |
| `Xbar`, `Xbar_n` | sample mean `(1/n) sum X_i` | gaussian_core |
| `S^2`, `S` | sample variance (divisor `n - 1`), sample SD | gaussian_core |
| `T`, `T(X)` | a statistic; the sufficient statistic where context fixes it | sufficiency |
| `L(theta)`, `ell(theta)` | likelihood, log-likelihood | model |
| `U(theta)` | score `grad ell(theta)` | model |
| `I(theta)`, `n I(theta)` | per-observation Fisher information; sample information | model |
| `theta_hat`, `theta_hat_MLE` | a generic estimator; the MLE when the method matters | estimation |
| `b(theta)` | bias `E_theta[theta_hat] - theta` | estimation |
| `MSE(theta)`, `AVar` | mean squared error; asymptotic variance | estimation |
| `phi`, `phi(x)` | test function, `X^n -> [0,1]`; `phi = 1` means reject `H0` | testing |
| `alpha`, `1 - alpha` | test size / significance level; confidence or credible level | testing / intervals |
| `beta(theta)`, `beta_phi(theta)` | power function `E_theta[phi]` (not a regression coefficient) | testing |
| `Lambda` | likelihood-ratio statistic `sup_{Theta_0} L / sup_Theta L`, in `[0,1]` | testing |
| `W`, `S` (score-test) | Wald statistic; score statistic | testing |
| `p(x)`, `p-value` | the observed significance level | testing |
| `z_p`, `t_{k,p}`, `chi^2_{k,p}`, `F_{d1,d2,p}` | upper-`p` quantiles of the named laws | gaussian_core |
| `chi^2_k`, `t_k`, `F_{d1,d2}` | the sampling distributions (constructed here) | gaussian_core |
| `C(X)`, `C(x)` | confidence set (random) / realized interval | intervals |
| `Q(X, theta)` | a pivotal quantity | intervals |
| `pi(theta)`, `pi(theta | x)` | prior; posterior | methods |
| `delta`, `delta_pi` | decision rule; Bayes rule | decision_theory |
| `L(theta, a)`, `R(theta, delta)`, `r(pi, delta)` | loss, risk, Bayes risk | decision_theory |
| `F`, `F_hat_n` | population CDF; empirical CDF | nonparametric |
| `P_hat_n` | empirical measure | nonparametric |
| `f_hat_h`, `h`, `K` | kernel density estimate, bandwidth, kernel | nonparametric |
| `y`, `X`, `beta`, `eps` | regression response, design, coefficients, errors | regression |
| `beta_hat`, `y_hat`, `e` | OLS estimator, fitted values, residuals | regression |
| `H`, `I - H` | hat matrix `X(X^T X)^{-1} X^T`; residual-maker | regression |
| `RSS`, `TSS`, `R^2` | residual / total sum of squares; coefficient of determination | regression |
| `sigma_hat^2` | `RSS/(n-p)`, unbiased error-variance estimate | regression |
| `n - p`, `n - 1`, `k - 1 - d` | residual df in regression / one-sample / goodness-of-fit | (all) |
| `eta`, `T(x)`, `A(eta)`, `h(x)` | exponential-family natural parameter, statistic, cumulant function, carrier | exponential_family |
| `IF(x)` | influence function of a functional | nonparametric |
| `h/sqrt(n)`, `Delta_n` | LAN local parameter; central sequence | principles |
| `FWER`, `FDR` | family-wise error rate; false discovery rate | testing |
