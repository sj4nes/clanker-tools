# moment_ladder

## Type
theorem

## Statement
On a probability space, if 1 <= q <= p then ||X||_q <= ||X||_p, so L^p(P) subset L^q(P): a finite p-th moment implies finite q-th moments for all q <= p.

## Symbols
- `X` — a random variable, type: Omega -> R
- `p, q` — exponents with 1 <= q <= p, type: real

## Epistemic status
proved_theorem

## Prerequisites (tsort edges into this node)
jensen_inequality, lp_space, moment

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: Jensen with phi(u) = u^{p/q} (convex, p/q >= 1) applied to |X|^q; take the (1/p)-th power
derives_from: jensen_inequality
lean_status: core — validation/proof-checks.lean Prob.jensen_sq (GENUINE, universal in t,x,y,n) is the p/q = 2 core

## Type / well-formedness check
apply Jensen's inequality to the convex function phi(u) = |u|^{p/q} and the variable |X|^q: E[|X|^q]^{p/q} = phi(E[|X|^q]) <= E[phi(|X|^q)] = E[|X|^p]. Uses P(Omega) = 1 crucially.

## Specialization / boundary cases
- p = 2, q = 1: E[|X|] <= sqrt(E[X^2]) -- finite variance implies finite mean, so Var and E both exist together
- the sequence ||X||_q is nondecreasing in q, converging to ||X||_inf

## Hypothesis-dropped counterexamples
- **finite_total_measure**: on an infinite measure space the inclusion reverses partially and can fail entirely -- the ladder is a probability-space phenomenon (P(Omega) = 1 is the hidden hypothesis)

## Common misuse
- assuming a finite mean implies a finite variance (the ladder only goes DOWN: high moments control low, not vice versa)
- using it on a non-probability measure

## Related nodes (non-prerequisite)
- derives_from: jensen_inequality
- orders: lp_space
- special_case_of: Lyapunov's inequality

## Sources
williams_probability_martingales, durrett_pte
