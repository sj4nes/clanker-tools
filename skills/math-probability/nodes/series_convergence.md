# series_convergence

## Type
primitive

## Statement
Convergence of an infinite series of reals via its partial sums; the comparison, ratio, and root tests; absolute convergence; the fact that a series of nonnegative terms either converges or diverges to +inf.

## Symbols
- `(a_n)` — the terms, type: N -> R
- `sum a_n` — the sum, type: real or +inf

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
(root)

## Hypotheses
(none — unconditional within scope)

## Well-definedness
the sum is the limit of the monotone (for nonnegative terms) partial-sum sequence; rearrangement is safe for absolutely convergent series only.

## Type / well-formedness check
a series of NONNEGATIVE terms always has a sum in [0, +inf] (monotone partial sums) -- this is what makes countable additivity of a measure well-posed. Discharged from math-real-analysis.

## Specialization / boundary cases
- countable additivity: P(bigcup A_n) = sum P(A_n) is a convergent series bounded by 1
- sum P(A_n) < inf is the hypothesis of the first Borel-Cantelli lemma

## Common misuse
- rearranging a conditionally convergent series (Riemann rearrangement theorem)
- assuming a_n -> 0 implies sum a_n converges (harmonic series)

## Related nodes (non-prerequisite)
- developed_in: math-real-analysis

## Sources
rudin_principles, tao_analysis_I
