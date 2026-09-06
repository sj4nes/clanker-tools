# portmanteau_theorem

## Type
theorem

## Statement
The following are equivalent to X_n -> X in distribution: (i) E[g(X_n)] -> E[g(X)] for all bounded continuous g; (ii) for all bounded Lipschitz g; (iii) limsup P(X_n in C) <= P(X in C) for all closed C; (iv) liminf P(X_n in U) >= P(X in U) for all open U; (v) P(X_n in A) -> P(X in A) for all A with P(X in boundary A) = 0.

## Symbols
- `g` — a test function, type: R -> R bounded and continuous
- `C, U, A` — closed / open / continuity Borel sets, type: element of B(R)

## Epistemic status
proved_theorem

## Prerequisites (tsort edges into this node)
cdf_properties, convergence_in_distribution, expectation

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: CDF => (i) by approximating 1_{(-inf,x]} by Lipschitz functions and using continuity points; (i) => (iii) by g_k decreasing to 1_C; (iii) <=> (iv) by complements; (v) from both one-sided bounds when the boundary is null; (i) => CDF by (v) with A = (-inf, x]
derives_from: convergence_in_distribution
lean_status: cited — Billingsley Convergence of Probability Measures Thm 2.1; Durrett Thm 3.2.5

## Type / well-formedness check
the CDF definition is the special case A = (-inf, x] with P(X = x) = 0. Form (i) is the working definition of weak convergence on general metric spaces; forms (iii)-(v) are what make it a topology on laws.

## Specialization / boundary cases
- A = (-inf, x], P(X = x) = 0: the CDF form
- g bounded uniformly continuous is enough (form ii) -- the class can be shrunk
- the Levy metric / bounded-Lipschitz metric metrizes this convergence on laws over R

## Hypothesis-dropped counterexamples
- **boundedness_of_g**: g(x) = x is continuous but unbounded: E[X_n] -> E[X] can FAIL under X_n -> X in distribution (escaping mass) -- convergence of unbounded moments needs uniform integrability
- **continuity_of_g**: g = 1_{(-inf, 0]} (discontinuous): P(X_n <= 0) -> P(X <= 0) fails when X has an atom at 0
- **P_of_boundary_zero_in_(v)**: A = {0}, X ~ N(0,1) (so P(X in bd A) = P(X = 0) = 0) is fine; A = {0}, X = 0 constant is not

## Common misuse
- applying form (i) to an unbounded g (moments)
- using P(X_n in A) -> P(X in A) for a set whose boundary carries mass

## Related nodes (non-prerequisite)
- characterizes: convergence_in_distribution
- used_by: continuous_mapping_theorem, slutsky_theorem

## Sources
billingsley_probability_measure, durrett_pte
