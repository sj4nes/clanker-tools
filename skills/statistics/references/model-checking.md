# Model checking and robustness

Workflow step 7. A conclusion that survives only under the strongest assumption
set is a fragile conclusion. Nodes are in the
[`math-statistics`](../../math-statistics/SKILL.md) capsule.

## What to check, by assumption

| Assumption | Diagnostic | If it fails |
|---|---|---|
| distributional form (normality, family membership) | QQ plot of residuals; `pearson_chi_squared_gof` on binned data (watch cells with expected count < 5 — the limiting `χ²` is asymptotic); Kolmogorov–Smirnov / Anderson–Darling against `dvoretzky_kiefer_wolfowitz` intuition | switch to the exact small-sample method for another family, a GLM with the right family, or a distribution-free procedure |
| independence of errors / rows | residual autocorrelation (Durbin–Watson, ACF) for ordered data; intraclass correlation for grouped data; residuals vs cluster id | mixed model or `sandwich_variance` with cluster-robust SE; block / cluster bootstrap; the true `n` is the number of clusters |
| homoscedasticity | residual-vs-fitted plot; scale-location plot; Breusch–Pagan / White | heteroscedasticity-consistent (`sandwich_variance`) SE; weighted least squares; a variance-stabilising transform |
| functional form / linearity / link | residual-vs-predictor plots; added-variable plots (`partitioned_regression`); component-plus-residual plots | add terms (polynomial, spline, interaction); change the link; transform the predictor |
| no influential points driving the fit | leverage `hᵢᵢ` (hat matrix, `ols_is_projection`); Cook's distance; DFBETAS | report the fit with and without; never delete a point without a mechanism |
| missingness is ignorable (MAR) | **not testable** — compare complete-case to imputed estimates; pattern-mixture sensitivity | multiple imputation / IPW under MAR; MNAR sensitivity analysis with a stated deviation parameter |
| correct specification overall | the robustness comparison below | report the range across specifications |

## The regression assumption ladder

`gauss_markov_theorem`: OLS is the best **linear unbiased** estimator using only
`E[ε | X] = 0` and `Var(ε | X) = σ²I` — **no normality needed** for
unbiasedness, consistency, or BLUE-ness.

The **exact** finite-sample `t` and `F` tests (`coefficient_t_test`,
`overall_f_test`, `ols_distribution_under_normal_errors`, `r_squared`)
additionally need `ε | X ~ N(0, σ²I)`. Without normality those tests are only
asymptotically valid — and if homoscedasticity or independence also fails, even
the asymptotic version needs a `sandwich_variance`.

`partitioned_regression` (Frisch–Waugh–Lovell): the coefficient on `X₁` in a
multiple regression equals the slope from regressing (residuals of `Y` on the
other regressors) on (residuals of `X₁` on the other regressors) — this is what
"adjusted for" means, and the basis for added-variable diagnostic plots.

## The robustness comparison — always run it

Re-do the headline inference under weaker assumptions and report whether the
conclusion moves:

1. model-based SE **vs** `sandwich_variance` (mis-specification-robust);
2. parametric interval **vs** `bootstrap` interval (distribution-free) — noting
   the bootstrap's failure modes (`references/interval-estimation.md`);
3. the primary model **vs** one alternative reasonable specification
   (different covariate set, different link, different outlier rule stated by
   mechanism);
4. complete-case **vs** an imputation / IPW analysis if data are missing.

If the effect estimate and its interval are stable across (1)–(4), say so — that
is a strong statement. If they move, the sensitivity **is** the finding: report
the range and what drives it, and do not present the most favourable
specification as the result.
