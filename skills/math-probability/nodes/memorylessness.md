# memorylessness

## Type
proposition

## Statement
P(X > s + t | X > s) = P(X > t) for all s, t >= 0. Among distributions on [0, inf) this holds iff X is exponential; among distributions on {1, 2, ...} iff X is geometric.

## Symbols
- `X` — a nonnegative random variable, type: Omega -> [0, inf) or {1,2,...}
- `s, t` — nonnegative reals/integers

## Epistemic status
proposition

## Prerequisites (tsort edges into this node)
cdf, conditional_probability

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: P(X > s+t | X > s) = G(s+t)/G(s) = G(t) means G(s+t) = G(s)G(t); with G monotone and G(0) = 1, G(x) = G(1)^x = e^{-lambda x}
derives_from: cdf
lean_status: cited — Grimmett-Stirzaker 4.8; Feller I.XIII

## Type / well-formedness check
the survival function G(x) = P(X > x) satisfies G(s + t) = G(s) G(t) (Cauchy's functional equation); the only monotone solutions are G(x) = e^{-lambda x} (continuous) or G(k) = (1-p)^k (discrete).

## Specialization / boundary cases
- the residual lifetime of an exponential component is exactly a fresh exponential -- no 'aging'
- a geometric number of coin flips: given the first m were failures, the additional flips to a success is again Geometric(p)

## Hypothesis-dropped counterexamples
- **the_characterization_is_exact**: gamma with shape 2: P(X > s + t | X > s) DECREASES in s -- it 'remembers' (positive aging). Weibull with shape > 1 likewise. Pareto: negative aging.

## Common misuse
- assuming any 'waiting time' is memoryless
- using memorylessness to justify ignoring elapsed time for a non-exponential process

## Related nodes (non-prerequisite)
- characterizes: exponential_distribution, geometric_distribution
- fails_for: gamma, Weibull, lognormal, Pareto

## Sources
grimmett_stirzaker, durrett_pte
