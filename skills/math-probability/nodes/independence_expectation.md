# independence_expectation

## Type
theorem

## Statement
If X, Y are independent and both integrable, then XY is integrable and E[XY] = E[X] E[Y]. Consequently Cov(X, Y) = 0: independent random variables are uncorrelated.

## Symbols
- `X, Y` — independent integrable random variables, type: L^1(P)

## Epistemic status
proved_theorem

## Prerequisites (tsort edges into this node)
covariance, expectation, fubini_tonelli, independence_random_variables, lotus

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: LOTUS on the product law + Fubini-Tonelli: true for indicators of rectangles, extend by linearity and MCT; integrability of XY from E|XY| = E|X| E|Y| < inf
derives_from: fubini_tonelli
lean_status: cited — Billingsley Thm 21.2; Durrett Thm 2.1.9

## Type / well-formedness check
the joint law is the product P_X tensor P_Y; E[XY] = integral integral xy dP_X dP_Y = (integral x dP_X)(integral y dP_Y) by Fubini-Tonelli (applicable since the product |x||y| integrates).

## Specialization / boundary cases
- more generally E[g(X) h(Y)] = E[g(X)] E[h(Y)] for measurable g, h with the products integrable
- Var(X + Y) = Var(X) + Var(Y) for independent X, Y
- the MGF and CF of a sum of independents factor (mgf_sum_independent)

## Hypothesis-dropped counterexamples
- **independence_not_merely_uncorrelated**: X ~ Uniform(-1,1), Y = X^2: E[XY] = E[X^3] = 0 = E[X] E[Y], so uncorrelated, but X, Y are strongly dependent -- the converse is FALSE (uncorrelated_not_independent)
- **integrability**: independent Cauchy X, Y: E[XY] does not exist even though E[X], E[Y] individually fail too

## Common misuse
- using E[XY] = E[X]E[Y] to CONCLUDE independence
- applying it to non-integrable variables

## Related nodes (non-prerequisite)
- one_way_only: uncorrelated_not_independent is the failed converse
- requires: independence_random_variables
- used_by: variance_of_sum, mgf_sum_independent

## Sources
billingsley_probability_measure, durrett_pte
