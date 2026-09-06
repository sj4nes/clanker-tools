# chebyshev_inequality

## Type
theorem

## Statement
Var(X) < inf, k > 0 => P(|X - E[X]| >= k) <= Var(X)/k^2. See results/chebyshev_inequality.yaml.

## Symbols
- `X` — a random variable with finite variance, type: L^2(P)

## Epistemic status
proved_theorem

## Prerequisites (tsort edges into this node)
markov_inequality, variance, variance_computational

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: Markov applied to (X - EX)^2 with threshold k^2
derives_from: markov_inequality
lean_status: core — validation/proof-checks.lean Prob.chebyshev_reduction

## Type / well-formedness check
see the hand-written results/chebyshev_inequality.yaml for the full treatment.

## Specialization / boundary cases
- k = c sd(X): P(|X - EX| >= c sd) <= 1/c^2
- sample mean: gives the WLLN

## Hypothesis-dropped counterexamples
- **finite_variance**: Cauchy has 1/k tails, not 1/k^2 -- no variance bound

## Common misuse
- using it when Chernoff/Hoeffding apply

## Related nodes (non-prerequisite)
- full_entry: results/chebyshev_inequality.yaml

## Sources
billingsley_probability_measure, durrett_pte
