# partitioned_regression

## Type
theorem

## Statement
Frisch-Waugh-Lovell: partition X = [X_1 | X_2]. The OLS coefficient beta_hat_2 on X_2 in the full regression of y on [X_1, X_2] equals the OLS coefficient from regressing the X_1-residuals of y on the X_1-residuals of X_2: beta_hat_2 = ( X_2_tilde^T X_2_tilde )^{-1} X_2_tilde^T y_tilde, where tilde denotes residuals from projecting out X_1 (i.e. M_1 = I - H_1 applied).

## Symbols
- `M_1 = I - X_1(X_1^T X_1)^{-1} X_1^T` — the residual-maker for X_1
- `'partialling out' X_1` — regressing both y and X_2 on X_1 and taking residuals

## Epistemic status
proved_theorem  ·  regime: exact

## Prerequisites (tsort edges into this node)
ols_is_projection, ordinary_least_squares

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: block form of the normal equations [X_1^T X_1, X_1^T X_2; X_2^T X_1, X_2^T X_2][b_1; b_2] = [X_1^T y; X_2^T y]; eliminate b_1 to get (X_2^T M_1 X_2) b_2 = X_2^T M_1 y
derives_from: ols_is_projection
lean_status: cited — the block-elimination identity is proof-checks.lean Stat.fwl_block_elimination for a fixed integer design via decide

## Type / well-formedness check
An exact algebraic identity. It formalizes 'controlling for X_1': a multiple-regression coefficient is a SIMPLE regression coefficient on the parts of y and x_2 that X_1 cannot explain. Proof: block normal equations, solve the X_1 block, substitute.

## Specialization / boundary cases
- time-series regression with a trend: 'detrend y and x, then regress' gives the same slope as including the trend
- fixed-effects panel estimator = regress the within-group-demeaned y on the within-group-demeaned x (X_1 = the group dummies)
- the residuals from the full regression equal the residuals from the partialled-out simple regression

## Hypothesis-dropped counterexamples
- **X_1_and_X_2_not_collinear**: if X_2 lies in the span of X_1 then M_1 X_2 = 0 and beta_hat_2 is not identified -- 'controlling for X_1' has removed all variation in X_2

## Common misuse
- interpreting a partialled-out coefficient as causal without an identification argument (FWL is algebra, not identification)
- expecting the SE of beta_hat_2 to come out right from the two-step regression without the correct residual df (n - p, not n - dim(X_2))

## In the wild
- the workhorse identity behind fixed-effects / within estimators, added-variable (partial-regression) plots, and double/debiased machine learning (regress out nuisance predictions, then regress residuals)

## Related nodes (non-prerequisite)
- uses: ordinary_least_squares, ols_is_projection
- historically_precedes: 

## Sources
frisch_waugh_1933, lovell_1963, seber_lee_linear_regression
