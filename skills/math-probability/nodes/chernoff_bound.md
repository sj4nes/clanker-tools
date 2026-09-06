# chernoff_bound

## Type
theorem

## Statement
For any random variable X with an MGF and any a: P(X >= a) <= inf_{t > 0} e^{-ta} M_X(t). Symmetrically P(X <= a) <= inf_{t < 0} e^{-ta} M_X(t).

## Symbols
- `X` — a random variable with M_X(t) < inf for some t > 0, type: Omega -> R
- `a` — a threshold, type: real

## Epistemic status
proved_theorem

## Prerequisites (tsort edges into this node)
markov_inequality, mgf

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: Markov on e^{tX} with threshold e^{ta}, then take the infimum over t > 0
derives_from: markov_inequality
lean_status: core — validation/proof-checks.lean Prob.markov_finite (Markov core; e^{tX} transform is one line)

## Type / well-formedness check
for fixed t > 0, { X >= a } = { e^{tX} >= e^{ta} }; apply Markov to the nonnegative variable e^{tX}: P(X >= a) <= E[e^{tX}]/e^{ta} = e^{-ta} M_X(t). Then optimize over t.

## Specialization / boundary cases
- X ~ N(0, sigma^2): optimizing gives P(X >= a) <= e^{-a^2 / (2 sigma^2)} -- the Gaussian tail
- X = sum of n iid: M_X(t) = M_{X_1}(t)^n, so the bound is exponentially small in n -- the large-deviations rate function I(a) = sup_t (ta - log M_{X_1}(t))
- X ~ Poisson(lambda), a = lambda(1 + delta): the multiplicative Chernoff bound e^{-lambda delta^2/(2+delta)}

## Hypothesis-dropped counterexamples
- **existence_of_the_MGF_for_some_t_gt_0**: heavy-tailed X (Cauchy, power law): M_X(t) = inf for all t > 0, the bound is vacuous -- only polynomial (Markov/Chebyshev/moment) bounds apply

## Common misuse
- forgetting to optimize over t (a single t gives a valid but loose bound)
- applying it when the MGF does not exist
- using t <= 0 for an upper-tail bound

## Related nodes (non-prerequisite)
- derives_from: markov_inequality
- sharpens: chebyshev_inequality
- used_by: hoeffding_inequality
- dual_of: Cramer's large-deviations theorem

## Sources
boucheron_lugosi_massart, durrett_pte
