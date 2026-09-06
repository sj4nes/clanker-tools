# law_of_total_variance

## Type
theorem

## Statement
For X in L^2 and a sub-sigma-algebra G: Var(X) = E[Var(X | G)] + Var(E[X | G]), where Var(X | G) = E[(X - E[X|G])^2 | G].

## Symbols
- `X` — a square-integrable random variable, type: L^2(P)
- `G` — a sub-sigma-algebra, type: sigma-algebra subset F

## Epistemic status
proved_theorem

## Prerequisites (tsort edges into this node)
conditional_expectation_abstract, tower_property, variance, variance_computational

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: E[Var(X|G)] = E[E[X^2|G]] - E[(E[X|G])^2] = E[X^2] - E[(E[X|G])^2] (tower); Var(E[X|G]) = E[(E[X|G])^2] - (E X)^2; add -- the middle terms cancel
derives_from: tower_property
lean_status: core — validation/proof-checks.lean Prob.centid + Prob.expectation_linearity (GENUINE)

## Type / well-formedness check
'within-group + between-group variance'. Decomposes total variability into the average conditional (unexplained) variance plus the variance of the conditional means (explained). Proof: apply variance_computational and the tower property.

## Specialization / boundary cases
- G = sigma(Y): Var(X) = E[Var(X | Y)] + Var(E[X | Y]) -- the ANOVA / random-effects decomposition; R^2 = Var(E[X|Y])/Var(X) is the fraction 'explained' by Y
- hierarchical models: total variance = measurement variance + between-unit variance
- compound distributions: Var(sum_{i=1}^N Y_i) = E[N] Var(Y) + Var(N) (E Y)^2 for N ⟂ iid Y_i

## Hypothesis-dropped counterexamples
- **finite_second_moment**: X must be in L^2 for all three variances to be finite
- **both_terms_nonnegative**: E[Var(X|G)] >= 0 and Var(E[X|G]) >= 0, so conditioning can only REDUCE expected variance: E[Var(X|G)] <= Var(X)

## Common misuse
- forgetting the Var(E[X|G]) term (assuming Var(X) = E[Var(X|G)])
- using it with X not in L^2

## Related nodes (non-prerequisite)
- uses: tower_property, variance_computational
- decomposes: variance
- analogue: law of total expectation

## Sources
williams_probability_martingales, grimmett_stirzaker
