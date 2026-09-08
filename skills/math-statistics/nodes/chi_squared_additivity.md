# chi_squared_additivity

## Type
identity

## Statement
If U ~ chi^2_a and V ~ chi^2_b are independent, then U + V ~ chi^2_{a+b}: degrees of freedom add.

## Symbols
- `a, b` — degrees of freedom of the summands

## Epistemic status
mathematical_identity  ·  regime: exact

## Prerequisites (tsort edges into this node)
chi_squared_distribution, prob_gamma, prob_mgf

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: multiply the MGFs: (1-2t)^{-a/2} . (1-2t)^{-b/2} = (1-2t)^{-(a+b)/2}, the chi^2_{a+b} MGF; MGF determines the law
derives_from: prob_mgf
lean_status: core — validation/proof-checks.lean Stat.chisq_mgf_add -- the exponent arithmetic -a/2 - b/2 = -(a+b)/2

## Type / well-formedness check
An identity of laws. Immediate from chi^2_k = Gamma(k/2, 1/2) and the fact that independent Gammas with a common rate add in the shape parameter (MGF (1 - 2t)^{-a/2} (1 - 2t)^{-b/2} = (1 - 2t)^{-(a+b)/2}).

## Specialization / boundary cases
- k independent chi^2_1's sum to chi^2_k -- recovers the sum-of-squared-normals definition
- partition the residual sum of squares in a two-factor ANOVA: the component df add to n - 1
- sequential model building: each added block of q predictors contributes an independent chi^2_q to the explained sum of squares (orthogonal design)

## Hypothesis-dropped counterexamples
- **independence**: U and V = c U dependent: U + V = (1+c) U ~ (1+c) chi^2_a, NOT chi^2_{2a} -- df do not add without independence

## Common misuse
- adding df of dependent sums of squares (non-orthogonal designs) -- the cross term is nonzero
- assuming subtraction works unconditionally: chi^2_a - chi^2_b is not chi^2_{a-b} in general (it can be negative); it holds only when the smaller is a component of the larger via an idempotent projection (Cochran)

## Related nodes (non-prerequisite)
- required_by: cochran_theorem, one_way_anova_identity
- uses: chi_squared_distribution

## Sources
casella_berger_2e
