# r_squared

## Type
definition

## Statement
The coefficient of determination is R^2 = 1 - RSS/TSS, where TSS = sum_i (y_i - ybar)^2; it is the fraction of the response's variance 'explained' by the fitted model, and equals the squared correlation between y and y_hat.

## Symbols
- `TSS` — total sum of squares (RSS of the intercept-only model)
- `adjusted R^2 = 1 - (RSS/(n-p)) / (TSS/(n-1))` — penalizes added predictors

## Epistemic status
definition  ·  regime: exact

## Prerequisites (tsort edges into this node)
prob_correlation, residual_sum_of_squares, sample_variance

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: Pythagorean identity TSS = (explained SS) + RSS (from ols_is_projection, since y - ybar 1 decomposes orthogonally); R^2 = explained/total
derives_from: sample_variance
lean_status: core

## Type / well-formedness check
A descriptive statistic in [0,1] (for a model with an intercept). NOT a goodness-of-fit test, NOT a measure of correct specification, and NOT comparable across different response variables or transformations. R^2 never decreases when a predictor is added -- hence adjusted R^2.

## Specialization / boundary cases
- simple regression: R^2 = (sample correlation of x and y)^2
- R^2 = 0: the model does no better than ybar; R^2 = 1: exact fit (residuals all 0)
- in-sample R^2 vs cross-validated / out-of-sample R^2 -- the gap measures overfitting

## Hypothesis-dropped counterexamples
- **model_has_an_intercept**: without an intercept the identity TSS = explained + RSS fails and 'R^2' can be negative or > 1 depending on the software's convention -- it is not interpretable
- **same_response_and_no_transformation**: R^2 for a model of y and a model of log y are not comparable; a high R^2 can accompany a badly misspecified model and a low R^2 a correct one (just noisy)

## Common misuse
- treating a high R^2 as evidence the model is correct or useful for prediction (could be overfitting; could be a spurious trend)
- comparing R^2 across models with different y transformations or different samples
- adding predictors to chase R^2 without adjusted R^2 or out-of-sample validation

## In the wild
- ubiquitous as a headline fit summary -- and correspondingly misused; econometrics emphasizes that a low R^2 does not invalidate a well-identified causal estimate

## Related nodes (non-prerequisite)
- uses: residual_sum_of_squares, sample_variance
- related_to: overall_f_test

## Sources
weisberg_applied_linear_regression, seber_lee_linear_regression
