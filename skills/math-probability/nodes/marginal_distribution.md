# marginal_distribution

## Type
definition

## Statement
A marginal distribution is the law of a subvector of (X_1,...,X_n), obtained by integrating (or summing) the joint density (pmf) over the remaining coordinates: f_{X_1}(x_1) = integral f_{X_1,X_2}(x_1, x_2) dx_2.

## Symbols
- `f_X` — the joint density, type: R^n -> [0, inf)
- `f_{X_i}` — a marginal density, type: R -> [0, inf)

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
abstract_integral, fubini_tonelli, joint_distribution

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: P(X_1 in B) = P(X in B x R^{n-1}) = integral_B integral_{R^{n-1}} f_X dx_{-1} dx_1 by Tonelli
derives_from: fubini_tonelli
lean_status: cited — Billingsley Thm 18.3

## Type / well-formedness check
marginalization is projection of the joint law; it discards all dependence information. Fubini-Tonelli justifies the integration (nonnegative integrand).

## Specialization / boundary cases
- joint uniform on the unit disk: each marginal has a semicircular density, not uniform
- bivariate normal: marginals are normal (but normal marginals do not imply joint normal)

## Hypothesis-dropped counterexamples
- **none_well_defined_always**: the marginal always exists; the caution is that MANY joints share it

## Common misuse
- thinking equal marginals implies equal joints
- assuming joint normality from normal marginals

## Related nodes (non-prerequisite)
- projection_of: joint_distribution
- used_by: conditional_distribution, independence_factorization

## Sources
billingsley_probability_measure, durrett_pte
