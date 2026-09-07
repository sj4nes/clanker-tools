# hoeffding_lemma

## Type
lemma

## Statement
If X is a random variable with a <= X <= b a.s. and E[X] = 0, then M_X(t) = E[e^{tX}] <= exp(t^2 (b - a)^2 / 8) for all real t. (X is sub-Gaussian with parameter (b-a)/2.)

## Symbols
- `X` — a bounded centered random variable, type: Omega -> [a, b]
- `t` — a real parameter, type: real

## Epistemic status
proved_lemma

## Prerequisites (tsort edges into this node)
convex_function, expectation, jensen_inequality, mgf

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: convex bound of e^{tx} by its chord on [a,b]; take E; the log of the bound has second derivative <= (b-a)^2/4 (it is the variance of a tilted [a,b]-valued law); integrate twice from psi(0) = psi'(0) = 0
derives_from: convex_function
lean_status: cited — Hoeffding 1963 Lemma; Boucheron-Lugosi-Massart Lemma 2.2

## Type / well-formedness check
by convexity of x |-> e^{tx} on [a, b], e^{tX} <= (b - X)/(b - a) e^{ta} + (X - a)/(b - a) e^{tb}; take expectations (E[X] = 0), define psi(t) = log of the result, and show psi''(t) <= (b - a)^2 / 4 by a variance argument, so psi(t) <= t^2 (b-a)^2 / 8.

## Specialization / boundary cases
- X ~ Uniform{-c, c} (or any symmetric law on [-c, c]): recovers the sub-Gaussian bound e^{c^2 t^2 / 2}
- the (b - a)^2 / 8 constant is sharp for the two-point law at a, b with mean 0

## Hypothesis-dropped counterexamples
- **boundedness**: an unbounded centered X (e.g. centered exponential) is not sub-Gaussian -- its MGF grows faster than any e^{ct^2}, only e^{c|t|} for small t (sub-exponential); Hoeffding's inequality is replaced by Bernstein's
- **E_X_eq_0**: without centering, M_X(t) has an extra e^{t E[X]} factor -- the lemma is stated for the centered variable

## Common misuse
- applying it to unbounded variables
- forgetting to center first

## In the wild
- the single ingredient between Chernoff and Hoeffding's inequality: it says a bounded random variable is sub-Gaussian, which is the hypothesis of essentially all of high-dimensional statistics and the analysis of stochastic optimisation (Wainwright 2019; Boucheron-Lugosi-Massart 2013)

## Related nodes (non-prerequisite)
- requires: convex_function, mgf
- used_by: hoeffding_inequality
- generalizes_to: sub-Gaussian / Bernstein / sub-exponential concentration

## Sources
boucheron_lugosi_massart, durrett_pte
