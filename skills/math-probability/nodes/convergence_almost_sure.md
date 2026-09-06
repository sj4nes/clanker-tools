# convergence_almost_sure

## Type
definition

## Statement
X_n -> X almost surely if P({omega : X_n(omega) -> X(omega)}) = 1.

## Symbols
- `(X_n)` — a sequence of random variables on one probability space, type: N -> (Omega -> R)
- `X` — the limit random variable (or law), type: Omega -> R (or a law)

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
almost_sure, probability_measure, random_variable, sequence_limit

## Hypotheses
(none — unconditional within scope)
## Type / well-formedness check
the convergence set { omega : X_n(omega) -> X(omega) } is an event (a countable combination of { |X_n - X| < 1/k }); a.s. convergence requires it to have probability 1. This is the strongest of the four modes together with L^p.

## Specialization / boundary cases
- the SLLN delivers this mode: sample mean -> E[X_1] a.s.
- a.s. convergence is preserved by continuous functions (continuous_mapping_theorem) and is equivalent to P(sup_{m >= n} |X_m - X| > eps) -> 0 for all eps

## Hypothesis-dropped counterexamples
- **common_probability_space**: a.s. convergence is meaningless for X_n and X defined on different spaces -- only the WEAKER convergence in distribution makes sense then

## Common misuse
- confusing 'X_n -> X a.s.' with 'P(X_n -> X) can be computed pointwise' -- it needs the whole trajectory
- assuming a.s. convergence from convergence in probability (only a SUBSEQUENCE converges a.s.)

## Related nodes (non-prerequisite)
- implies: convergence_in_probability
- delivered_by: strong_law_large_numbers
- tag: a.s. -- the choice_grade analogue

## Sources
durrett_pte, billingsley_probability_measure
