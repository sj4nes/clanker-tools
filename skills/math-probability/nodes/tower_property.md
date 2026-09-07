# tower_property

## Type
theorem

## Statement
If H subset G subset F then E[E[X | G] | H] = E[X | H]. In particular E[E[X | G]] = E[X] (the law of total expectation / iterated expectation).

## Symbols
- `X` — an integrable random variable, type: L^1(P)
- `H, G` — nested sub-sigma-algebras H subset G subset F, type: sigma-algebra

## Epistemic status
proved_theorem

## Prerequisites (tsort edges into this node)
conditional_expectation_abstract, conditional_expectation_existence, expectation_linearity

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: for A in H subset G: integral_A E[E[X|G]|H] = integral_A E[X|G] = integral_A X = integral_A E[X|H]; both outer terms are H-measurable with equal integrals on all H-sets, so equal a.s.
derives_from: conditional_expectation_existence
lean_status: core — validation/proof-checks.lean -- linearity core; the tower is the defining-property chase

## Type / well-formedness check
the smaller sigma-algebra wins: conditioning on more then less information equals conditioning on less. Proof: E[X | H] is H-measurable (hence G-measurable) and its integral matches X on H-sets; check that E[X|G] has the same integrals on H-sets (it does, since H subset G).

## Specialization / boundary cases
- H = { empty, Omega }: E[E[X | G]] = E[X] -- compute a mean by conditioning (first-step analysis, LOTUS for expectations)
- E[X] = sum_i E[X | B_i] P(B_i) for a partition -- the law-of-total-probability analogue
- martingale: E[X_{n+1} | F_n] = X_n gives E[X_m | F_n] = X_n for m > n by iterating

## Hypothesis-dropped counterexamples
- **nesting_H_subset_G**: if H and G are not nested, E[E[X | G] | H] need NOT equal E[X | H]: with X, G, H chosen so G and H are independent and both informative about X, iterating loses information both ways and the two sides differ
- **integrability**: needs X in L^1 for all the conditional expectations to exist

## Common misuse
- applying it to non-nested conditioning sigma-algebras
- writing E[E[X|G]|H] = E[X|G] (wrong -- the OUTER, smaller one wins)

## In the wild
- the law of total expectation E[X] = E[E[X | Y]] is 'first-step analysis' -- computing an expected hitting time, a gambler's-ruin probability, an expected number of comparisons in a randomized algorithm, by conditioning on the first step
- credit and actuarial models: expected loss = E[ E[loss | default scenario] ] -- iterate the conditioning over rating states, macro scenarios
- the martingale property E[X_{n+1} | F_n] = X_n plus the tower gives E[X_m | F_n] = X_n for all m > n -- the backbone of optional-stopping and derivative pricing

## Related nodes (non-prerequisite)
- generalizes: law_of_total_probability
- used_by: law_of_total_variance, martingale

## Sources
williams_probability_martingales, durrett_pte
