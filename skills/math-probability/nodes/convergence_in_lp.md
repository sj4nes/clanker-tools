# convergence_in_lp

## Type
definition

## Statement
X_n -> X in L^p (p >= 1) if E[|X_n - X|^p] -> 0, i.e. ||X_n - X||_p -> 0.

## Symbols
- `(X_n)` — a sequence of random variables on one probability space, type: N -> (Omega -> R)
- `X` — the limit random variable (or law), type: Omega -> R (or a law)

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
lp_space, random_variable, sequence_limit

## Hypotheses
(none — unconditional within scope)
## Type / well-formedness check
convergence in the L^p(P) norm; requires X_n, X in L^p. By Markov's inequality (applied to |X_n - X|^p) it implies convergence in probability; the converse needs uniform integrability.

## Specialization / boundary cases
- L^2 convergence of the sample mean under finite variance (a one-line Chebyshev bound), giving the L^2 WLLN
- in a Hilbert space (L^2) it is convergence in norm; Cauchy sequences converge (Riesz-Fischer)

## Hypothesis-dropped counterexamples
- **uniform_integrability_for_the_converse**: X_n = n 1_{(0, 1/n]} on ([0,1], lambda): X_n -> 0 in probability and a.s., but E[|X_n|] = 1 not -> 0 -- convergence in probability does NOT imply L^1 without a dominating / uniformly integrable family

## Common misuse
- forgetting the p (L^1 and L^2 convergence are different)
- assuming L^p convergence from a.s. convergence (needs domination -- DCT)

## Related nodes (non-prerequisite)
- implies: convergence_in_probability
- via: markov_inequality
- strongest_with: convergence_almost_sure
- tag: L^p

## Sources
durrett_pte, billingsley_probability_measure
