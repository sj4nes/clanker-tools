# probability_integral_transform

## Type
theorem

## Statement
If F_X is continuous, then F_X(X) ~ Uniform(0,1). Conversely, for any CDF F and U ~ Uniform(0,1), the variable F^{-1}(U) has CDF F.

## Symbols
- `X` — a random variable with continuous CDF, type: Omega -> R
- `U` — a uniform variable, type: Omega -> (0,1)
- `F` — any target CDF, type: R -> [0,1]

## Epistemic status
proved_theorem

## Prerequisites (tsort edges into this node)
cdf, cdf_properties, continuous_uniform_distribution, distribution_pushforward, quantile_function

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: inverse: P(F^{-1}(U) <= x) = P(U <= F(x)) = F(x) by the Galois connection F^{-1}(u) <= x iff u <= F(x). Forward: if F_X continuous, P(F_X(X) <= u) = P(X <= F_X^{-1}(u)) = F_X(F_X^{-1}(u)) = u
derives_from: quantile_function
lean_status: cited — Durrett Thm 1.2.2; Devroye Non-Uniform Random Variate Generation ch. 2

## Type / well-formedness check
the inverse direction (F^{-1}(U) ~ F) needs NO continuity and is the basis of simulation: to sample any distribution, sample a uniform and apply the quantile function.

## Specialization / boundary cases
- F(x) = 1 - e^{-lambda x} (exponential): F^{-1}(u) = -ln(1-u)/lambda -- inversion sampling for the exponential
- F discrete: F^{-1}(U) picks value x_k when U falls in (F(x_{k-1}), F(x_k)] -- the alias/CDF method
- goodness-of-fit: if the model F is right, the transformed data F(x_i) should look Uniform(0,1) (the basis of PP-plots and the Kolmogorov-Smirnov test)

## Hypothesis-dropped counterexamples
- **continuity_of_F_X_for_the_forward_direction**: X ~ Bernoulli(1/2): F_X(X) takes only the values 1/2 and 1, not Uniform(0,1) -- atoms in F_X break the forward transform (the inverse direction still works)

## Common misuse
- applying the forward direction to a discrete or mixed X
- forgetting to use the generalized inverse for non-invertible F

## Related nodes (non-prerequisite)
- used_by: simulation (inversion sampling)
- requires: quantile_function

## Sources
durrett_pte, grimmett_stirzaker
