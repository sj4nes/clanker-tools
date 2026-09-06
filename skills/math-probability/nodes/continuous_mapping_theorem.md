# continuous_mapping_theorem

## Type
theorem

## Statement
If X_n -> X (a.s., or in probability, or in distribution) and g is measurable with P(X in D_g) = 0 where D_g is g's discontinuity set, then g(X_n) -> g(X) in the same mode.

## Symbols
- `g` — a measurable function continuous P_X-a.e., type: R -> R^k
- `D_g` — the set of discontinuities of g, type: Borel set

## Epistemic status
proved_theorem

## Prerequisites (tsort edges into this node)
convergence_almost_sure, convergence_in_distribution, convergence_in_probability, portmanteau_theorem

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: a.s.: X_n(omega) -> X(omega) and g continuous at X(omega) (a.e.) => g(X_n(omega)) -> g(X(omega)). p: via the subsequence principle. d: portmanteau -- for bounded continuous h, h o g is bounded and continuous P_X-a.e.
derives_from: portmanteau_theorem
lean_status: cited — Billingsley CPM Thm 2.7; Durrett Thm 3.2.10

## Type / well-formedness check
for a.s. and in-probability, pointwise/along-subsequence continuity carries the limit through; for in-distribution, use the portmanteau form (bounded continuous test functions compose with g to bounded a.e.-continuous functions).

## Specialization / boundary cases
- g(x) = x^2: X_n -> X in distribution => X_n^2 -> X^2 in distribution (e.g. sqrt(n) Xbar -> N(0, sigma^2) gives n Xbar^2 -> sigma^2 chi-squared_1)
- g continuous everywhere: the a.e. hypothesis is automatic
- combined with Slutsky to build asymptotic distributions of test statistics (t-statistic, Wald statistic)

## Hypothesis-dropped counterexamples
- **P_X_gives_the_discontinuity_set_measure_zero**: g(x) = 1_{x >= 0}, X_n = -1/n -> 0, but g(X_n) = 0 for all n while g(0) = 1 -- g is discontinuous exactly at the limit point, which here has full mass
- **same_mode_out**: if the input is only in distribution, the output is only in distribution -- you cannot upgrade

## Common misuse
- applying it across a discontinuity that the limit law charges
- expecting the output mode to be stronger than the input mode

## Related nodes (non-prerequisite)
- uses: portmanteau_theorem
- pairs_with: slutsky_theorem, delta_method

## Sources
billingsley_probability_measure, durrett_pte
