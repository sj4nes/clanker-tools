# normal_affine_closure

## Type
proposition

## Statement
If X ~ N(mu, sigma^2) then aX + b ~ N(a mu + b, a^2 sigma^2) for a != 0. If X ~ N(mu_1, s_1^2), Y ~ N(mu_2, s_2^2) are independent, then X + Y ~ N(mu_1 + mu_2, s_1^2 + s_2^2).

## Symbols
- `X, Y` — normal random variables, type: Omega -> R
- `a, b` — constants, a != 0, type: real

## Epistemic status
proposition

## Prerequisites (tsort edges into this node)
characteristic_function, convolution_formula, normal_distribution, standard_normal, transformation_univariate

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: affine: change of variables on the density. Sum: mgf_sum_independent then mgf_uniqueness -- the exponents add
derives_from: mgf_sum_independent
lean_status: core

## Type / well-formedness check
affine closure by transformation_univariate; the sum by multiplying MGFs: exp(mu_1 t + s_1^2 t^2/2) exp(mu_2 t + s_2^2 t^2/2) = exp((mu_1+mu_2) t + (s_1^2 + s_2^2) t^2/2), then mgf_uniqueness.

## Specialization / boundary cases
- standardization Z = (X - mu)/sigma ~ N(0,1) is the a = 1/sigma, b = -mu/sigma case
- sample mean of n iid N(mu, sigma^2) is exactly N(mu, sigma^2/n) -- the CLT holds with no error for normal data
- any linear combination sum a_i X_i of jointly normal X_i is normal -- the definition of a Gaussian vector

## Hypothesis-dropped counterexamples
- **independence_for_the_sum**: X ~ N(0,1), Y = -X ~ N(0,1): X + Y = 0, a point mass, NOT N(0, 2) -- the sum rule needs independence (or joint normality with the right covariance)
- **joint_normality_for_linear_combos**: X ~ N(0,1) and Y = X if |X| < 1 else -X: each is N(0,1) but X + Y is not normal -- marginal normality is not joint normality

## Common misuse
- adding variances of dependent normals
- assuming a sum of normal marginals is normal without joint normality

## Related nodes (non-prerequisite)
- defines: the Gaussian vector / multivariate normal
- uses: mgf_sum_independent, mgf_uniqueness

## Sources
billingsley_probability_measure, durrett_pte
