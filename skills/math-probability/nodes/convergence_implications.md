# convergence_implications

## Type
theorem

## Statement
The lattice of modes: (a.s.) => (in probability); (L^p) => (in probability); (in probability) => (in distribution); (in probability) => (a.s. along a subsequence); (in distribution to a CONSTANT) => (in probability). No other implication holds in general.

## Symbols
- `X_n, X` — random variables on a common space (except the d-only statements), type: N -> (Omega -> R)

## Epistemic status
proved_theorem

## Prerequisites (tsort edges into this node)
borel_cantelli_first, convergence_almost_sure, convergence_in_distribution, convergence_in_lp, convergence_in_probability, markov_inequality, portmanteau_theorem

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: a.s.=>p: dominated convergence of indicators / continuity of P. L^p=>p: Markov on |X_n - X|^p. p=>d: portmanteau via a bounded-Lipschitz test function. p=>a.s. subsequence: pick n_k with P(|X_{n_k} - X| > 2^{-k}) < 2^{-k}, apply Borel-Cantelli 1. d-to-constant=>p: F of a constant is a step, so F_{X_n} -> it everywhere but the jump.
derives_from: portmanteau_theorem
lean_status: core — validation/proof-checks.lean Prob.markov_finite + Prob.union_bound (the Boole/BC1 step)

## Type / well-formedness check
each arrow is a short proof; the content is equally in the NON-arrows, witnessed by standard counterexamples (the typewriter sequence, escaping mass, a symmetric two-point law).

## Specialization / boundary cases
- finite-dimensional summary: a.s. and L^p each imply p; p implies d; that is all
- Scheffe's lemma: if densities converge a.e. then L^1 (hence p, hence d) convergence follows -- a bridge that skips the counterexamples
- if X_n -> X in distribution and X_n -> Y in probability then X = Y in distribution

## Hypothesis-dropped counterexamples
- **a_s_does_not_imply_L_p**: X_n = n 1_{(0,1/n]}: X_n -> 0 a.s. but E|X_n| = 1 (escaping mass)
- **L_p_does_not_imply_a_s**: the typewriter sequence (indicators of [j/2^k, (j+1)/2^k] in order): -> 0 in every L^p but converges a.s. for NO omega
- **p_does_not_imply_a_s**: same typewriter sequence -- in probability but not a.s.
- **d_does_not_imply_p**: X ~ N(0,1), X_n = (-1)^n X: each X_n ~ N(0,1) so X_n -> N(0,1) in distribution, but |X_n - X_{n+1}| = 2|X| does not -> 0, so not in probability
- **d_to_a_nonconstant_does_not_imply_p**: the same example -- the limit must be a CONSTANT for the reverse arrow

## Common misuse
- assuming convergence in distribution says anything about the variables jointly
- assuming a.s. => L^p (needs uniform integrability / a dominator)
- using 'converges in probability' as if it gave an a.s. limit

## Related nodes (non-prerequisite)
- organizes: convergence_almost_sure, convergence_in_probability, convergence_in_lp, convergence_in_distribution
- uses: markov_inequality, borel_cantelli_first

## Sources
durrett_pte, williams_probability_martingales
