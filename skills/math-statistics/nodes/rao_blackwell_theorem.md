# rao_blackwell_theorem

## Type
theorem

## Statement
If theta_hat is an estimator of g(theta) with finite variance and T is sufficient for theta, then theta_hat_RB = E[theta_hat | T] is a statistic, has the same bias as theta_hat, and satisfies Var_theta(theta_hat_RB) <= Var_theta(theta_hat) for every theta (strictly, unless theta_hat was already a function of T).

## Symbols
- `theta_hat_RB = E[theta_hat | T]` — the Rao-Blackwellized estimator -- a statistic BECAUSE T is sufficient (the conditional expectation does not depend on theta)
- `T` — a sufficient statistic

## Epistemic status
proved_theorem  ·  regime: exact

## Prerequisites (tsort edges into this node)
prob_conditional_expectation, prob_jensen_ineq, prob_law_total_variance, sufficiency, unbiased_estimator

## Hypotheses
sufficiency, unbiased_estimator

## Proof provenance
technique: law of total variance: Var(theta_hat) = E[Var(theta_hat|T)] + Var(E[theta_hat|T]); the first term is >= 0
derives_from: prob_law_total_variance
lean_status: core — validation/proof-checks.lean Stat.rao_blackwell_var -- Var(X) = E[Var(X|T)] + Var(E[X|T]) instantiated so Var(E[X|T]) <= Var(X); the finitary total-variance identity

## Type / well-formedness check
Sufficiency is exactly what makes E[theta_hat | T] a legal estimator (theta-free). Proof of the variance drop: law of total variance, Var(theta_hat) = E[Var(theta_hat | T)] + Var(E[theta_hat | T]) >= Var(E[theta_hat | T]) = Var(theta_hat_RB). Same mean: tower property.

## Specialization / boundary cases
- Bernoulli, estimating p^2: start with theta_hat = X_1 X_2 (unbiased, crude); condition on T = sum X_i to get theta_hat_RB = [T(T-1)] / [n(n-1)], the UMVUE
- estimating P(X_1 <= c) in a normal model: start with 1{X_1 <= c}, condition on (Xbar, S^2)
- if theta_hat is already a function of T, Rao-Blackwell returns it unchanged

## Hypothesis-dropped counterexamples
- **sufficiency**: condition on a NON-sufficient statistic T and E[theta_hat | T] depends on theta -- it is not a usable estimator. The variance would still drop, but you cannot compute the thing.
- **finite_variance**: if Var(theta_hat) = inf the inequality is vacuous

## Common misuse
- Rao-Blackwellizing on a sufficient-but-not-complete statistic and calling the result 'the UMVUE' -- you need completeness (Lehmann-Scheffe) for uniqueness/optimality
- expecting a strict improvement when the starting estimator already depends only on T

## In the wild
- Rao-Blackwellized particle filters in robotics / target tracking: analytically marginalize the linear-Gaussian substructure (condition on it) and only sample the nonlinear part -- large variance reduction per particle
- Monte Carlo: replacing a sampled indicator by its conditional expectation ('conditional Monte Carlo') is Rao-Blackwellization and always reduces estimator variance

## Related nodes (non-prerequisite)
- required_by: lehmann_scheffe_theorem
- uses: sufficiency, prob_jensen_ineq

## Sources
casella_berger_2e, lehmann_casella_tpe
