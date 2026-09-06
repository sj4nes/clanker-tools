# conditional_expectation_l2_projection

## Type
theorem

## Statement
For X in L^2(P), E[X | G] is the orthogonal projection of X onto the closed subspace L^2(Omega, G, P): it is the G-measurable random variable minimizing E[(X - Z)^2] over all G-measurable Z in L^2.

## Symbols
- `X` — a square-integrable random variable, type: L^2(P)
- `G` — a sub-sigma-algebra, type: sigma-algebra subset F

## Epistemic status
proved_theorem

## Prerequisites (tsort edges into this node)
conditional_expectation_abstract, conditional_expectation_existence, lp_space

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: L^2(G) is a closed subspace of the Hilbert space L^2(P); the projection theorem gives a unique closest point Z*, characterized by X - Z* orthogonal to L^2(G), i.e. E[(X - Z*) 1_A] = 0 for all A in G -- exactly the defining property of E[X | G]
derives_from: conditional_expectation_existence
lean_status: core — validation/proof-checks.lean Prob.jensen_sq (the L^2 convexity core)

## Type / well-formedness check
the geometric meaning of conditioning: E[X | G] is the BEST PREDICTOR of X using only G-information, in mean-square. The residual X - E[X | G] is orthogonal to every G-measurable function (E[(X - E[X|G]) W] = 0 for W in L^2(G)).

## Specialization / boundary cases
- G = sigma(Y): E[X | Y] = argmin_{g measurable} E[(X - g(Y))^2] -- nonparametric regression is estimating this
- restricting Z to AFFINE functions of Y gives the best LINEAR predictor mu_X + (Cov(X,Y)/Var Y)(Y - mu_Y) -- equals E[X|Y] iff (X,Y) jointly normal
- the Pythagorean identity: E[X^2] = E[(E[X|G])^2] + E[(X - E[X|G])^2]

## Hypothesis-dropped counterexamples
- **finite_second_moment**: the projection picture needs X in L^2; for X in L^1 only, E[X | G] still exists (conditional_expectation_existence) but is not a projection and is not a mean-square minimizer
- **G_measurable_predictors_only**: allowing Z to depend on more than G lets Z = X drive the error to 0 -- the constraint Z in L^2(G) is the whole point

## Common misuse
- assuming the best predictor is linear (only for jointly Gaussian)
- using the L^2 characterization when X is not square-integrable

## Related nodes (non-prerequisite)
- uses: lp_space, conditional_expectation_existence
- special_case: linear regression / best linear predictor
- gives: the Pythagorean / ANOVA identity

## Sources
williams_probability_martingales, durrett_pte
