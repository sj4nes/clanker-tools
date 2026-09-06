# convergence_in_probability

## Type
definition

## Statement
X_n -> X in probability if for every eps > 0, P(|X_n - X| > eps) -> 0 as n -> inf.

## Symbols
- `(X_n)` — a sequence of random variables on one probability space, type: N -> (Omega -> R)
- `X` — the limit random variable (or law), type: Omega -> R (or a law)

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
probability_measure, random_variable, sequence_limit

## Hypotheses
(none — unconditional within scope)
## Type / well-formedness check
a statement about the MARGINAL of |X_n - X| for each n -- no joint trajectory needed beyond a common space. Weaker than a.s. (which controls the whole tail at once) and than L^p (Markov), stronger than in distribution.

## Specialization / boundary cases
- the WLLN delivers this mode: sample mean -> E[X_1] in probability
- X_n -> X in probability iff every subsequence has a further subsequence converging a.s. -- the 'subsequence principle'
- X_n -> c (a constant) in probability <=> X_n -> c in distribution

## Hypothesis-dropped counterexamples
- **eps_quantifier**: P(|X_n - X| > eps) -> 0 for ONE eps is not enough; it must hold for every eps > 0

## Common misuse
- reading it as a.s. convergence (typewriter sequence: converges in probability, not a.s.)
- assuming a rate -- convergence in probability alone gives no n at which P(|X_n - X| > eps) < delta

## Related nodes (non-prerequisite)
- implied_by: convergence_almost_sure, convergence_in_lp
- implies: convergence_in_distribution
- delivered_by: weak_law_large_numbers
- tag: p

## Sources
durrett_pte, billingsley_probability_measure
