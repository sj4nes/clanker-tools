# levy_continuity_theorem

## Type
theorem

## Statement
If phi_{X_n}(t) -> phi(t) for every t and phi is continuous at t = 0, then phi is the characteristic function of some random variable X and X_n -> X in distribution. Conversely X_n -> X in distribution implies phi_{X_n} -> phi_X pointwise.

## Symbols
- `phi_{X_n}` — characteristic functions, type: R -> C
- `phi` — the pointwise limit, type: R -> C

## Epistemic status
proved_theorem

## Prerequisites (tsort edges into this node)
cf_properties, characteristic_function, convergence_in_distribution

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: continuity of phi at 0 gives tightness of (X_n) (a CF-tail bound); every subsequential distributional limit has CF phi (by the converse direction + the pointwise convergence); phi determines the limit uniquely, so the whole sequence converges
derives_from: cf_properties
lean_status: cited — Billingsley Thm 26.3; Durrett Thm 3.3.6

## Type / well-formedness check
the workhorse for proving convergence in distribution: reduce to a pointwise limit of characteristic functions (which factor over sums). The continuity of phi at 0 rules out mass escaping to infinity (tightness).

## Specialization / boundary cases
- CLT: phi_{S_n}(t) = phi_{X_1}(t/sqrt n)^n -> e^{-t^2/2}, continuous at 0, hence S_n -> N(0,1)
- Poisson limit: (1 + (lambda/n)(e^{it} - 1))^n -> exp(lambda(e^{it} - 1))

## Hypothesis-dropped counterexamples
- **continuity_of_the_limit_phi_at_0**: X_n ~ N(0, n): phi_{X_n}(t) = e^{-n t^2/2} -> 1_{t = 0}, which is NOT continuous at 0 -- and indeed X_n has no distributional limit (mass escapes to +-inf). The continuity condition is exactly the tightness check.
- **pointwise_convergence_for_all_t**: convergence of phi_{X_n}(t) on a bounded interval of t is not enough in general

## Common misuse
- skipping the continuity-at-0 check (it is where tightness lives)
- concluding convergence from CF agreement on a finite set of t

## Related nodes (non-prerequisite)
- uses: characteristic_function, cf_properties
- used_by: central_limit_theorem, poisson_limit_theorem

## Sources
billingsley_probability_measure, durrett_pte
