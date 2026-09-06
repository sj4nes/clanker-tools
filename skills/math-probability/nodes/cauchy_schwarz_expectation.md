# cauchy_schwarz_expectation

## Type
theorem

## Statement
(E[XY])^2 <= E[X^2] E[Y^2] for X, Y in L^2(P). Equality iff X and Y are a.s. linearly dependent.

## Symbols
- `X, Y` — random variables in L^2(P), type: L^2(P)

## Epistemic status
proved_theorem

## Prerequisites (tsort edges into this node)
expectation, expectation_linearity, expectation_monotonicity

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: nonnegative quadratic in t has discriminant (2 E[XY])^2 - 4 E[Y^2] E[X^2] <= 0; if E[Y^2] = 0 then Y = 0 a.s. and both sides are 0
derives_from: expectation_monotonicity
lean_status: core — validation/proof-checks.lean Prob.corr_bound_iff + the 2-point CS/Jensen decide grid; full universal CS over Z is a real-number fact (cited)

## Type / well-formedness check
the L^2(P) inner-product Cauchy-Schwarz: the quadratic t |-> E[(X + tY)^2] = E[X^2] + 2t E[XY] + t^2 E[Y^2] is nonnegative for all real t, so its discriminant is <= 0.

## Specialization / boundary cases
- Y = 1: (E[X])^2 <= E[X^2], i.e. Var(X) >= 0
- centered X, Y: (Cov(X,Y))^2 <= Var(X) Var(Y), hence |rho| <= 1 (correlation)
- Y = X^{p-1} style: a route to Holder / the moment ladder

## Hypothesis-dropped counterexamples
- **finite_second_moments**: X ~ Cauchy, Y = 1: E[X^2] = inf and E[XY] = E[X] does not exist -- the inequality is between undefined quantities
- **equality_needs_linear_dependence**: if X, Y are not proportional a.s. the inequality is strict

## Common misuse
- applying it to variables not in L^2
- forgetting equality characterizes a.s. linear dependence

## Related nodes (non-prerequisite)
- special_case_of: holder_inequality (p = q = 2)
- used_by: correlation, covariance

## Sources
boucheron_lugosi_massart, durrett_pte
