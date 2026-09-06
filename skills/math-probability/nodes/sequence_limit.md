# sequence_limit

## Type
primitive

## Statement
Convergence of a real sequence in the epsilon-N sense, with uniqueness of limits, the algebra of limits, the squeeze theorem, and monotone convergence.

## Symbols
- `(x_n)` — a real sequence, type: N -> R
- `L` — the limit, type: real

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
(root)

## Hypotheses
(none — unconditional within scope)

## Well-definedness
limits are unique (a Hausdorff fact for R); the algebra of limits (sum, product, quotient with nonzero denominator) is standard.

## Type / well-formedness check
the quantifier order is 'for all eps EXISTS N' (N may depend on eps); the uniform form ('exists N for all eps') is a different, stronger statement -- relevant to the difference between the convergence modes downstream. Discharged from math-real-analysis.

## Specialization / boundary cases
- P(A_n) -> P(A) statements (continuity of probability) are sequence limits in [0,1]
- convergence of a series is convergence of its partial-sum sequence

## Common misuse
- swapping the eps and N quantifiers (that is uniform convergence)
- assuming a bounded sequence converges (it has a convergent SUBSEQUENCE -- Bolzano-Weierstrass)

## Related nodes (non-prerequisite)
- developed_in: math-real-analysis

## Sources
rudin_principles, tao_analysis_I
