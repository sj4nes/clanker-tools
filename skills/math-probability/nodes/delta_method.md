# delta_method

## Type
theorem

## Statement
If sqrt(n)(T_n - theta) -> N(0, sigma^2) in distribution and g is differentiable at theta with g'(theta) != 0, then sqrt(n)(g(T_n) - g(theta)) -> N(0, g'(theta)^2 sigma^2).

## Symbols
- `T_n` — an asymptotically normal estimator, type: N -> (Omega -> R)
- `g` — a transformation differentiable at theta, type: R -> R
- `theta` — the true parameter, type: real

## Epistemic status
proved_theorem

## Prerequisites (tsort edges into this node)
central_limit_theorem, continuous_mapping_theorem, convergence_in_distribution, slutsky_theorem

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: Taylor with remainder: g(T_n) - g(theta) = g'(xi_n)(T_n - theta) with xi_n between; T_n -> theta in probability so g'(xi_n) -> g'(theta) in probability; Slutsky gives the product limit
derives_from: slutsky_theorem
lean_status: cited — Durrett; van der Vaart Asymptotic Statistics Thm 3.1

## Type / well-formedness check
a first-order Taylor expansion g(T_n) approx g(theta) + g'(theta)(T_n - theta), made rigorous by Slutsky: sqrt(n)(g(T_n) - g(theta)) = [g'(theta) + o_p(1)] sqrt(n)(T_n - theta).

## Specialization / boundary cases
- g(x) = x^2 at theta: asymptotic variance 4 theta^2 sigma^2 (degenerate at theta = 0 -- then a chi-squared limit at rate n, the SECOND-order delta method)
- g = log: stabilizes a variance that scales with the mean (log-transform for count / ratio data)
- the asymptotic variance of a sample correlation, an odds ratio, an R^2 -- all standard delta-method calculations

## Hypothesis-dropped counterexamples
- **g_prime_theta_nonzero**: g(x) = x^2 at theta = 0: g'(0) = 0, the first-order limit is degenerate; n(g(T_n) - g(theta)) -> sigma^2 chi-squared_1 instead (a different rate AND a non-normal limit)
- **differentiability_at_theta**: g with a kink at theta (e.g. |x - theta|): no single derivative, the limit is a folded normal

## Common misuse
- applying it where g'(theta) = 0 (wrong rate and wrong limit shape)
- using it far from the asymptotic regime (the linearization error dominates in small samples)

## Related nodes (non-prerequisite)
- uses: slutsky_theorem, central_limit_theorem
- second_order: when g'(theta) = 0

## Sources
durrett_pte, grimmett_stirzaker
