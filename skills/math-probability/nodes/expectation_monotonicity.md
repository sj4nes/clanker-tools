# expectation_monotonicity

## Type
proposition

## Statement
If X <= Y almost surely then E[X] <= E[Y] (when both exist). Also |E[X]| <= E[|X|], and X >= 0 a.s. with E[X] = 0 implies X = 0 a.s.

## Symbols
- `X, Y` — integrable random variables, type: L^1(P)

## Epistemic status
proposition

## Prerequisites (tsort edges into this node)
abstract_integral, almost_sure, expectation

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: integral of a nonnegative function is >= 0; apply to Y - X; the triangle inequality |E X| <= E|X| from -|X| <= X <= |X|
derives_from: abstract_integral
lean_status: core

## Type / well-formedness check
monotonicity of the Lebesgue integral: Y - X >= 0 a.s. so E[Y - X] = integral (Y-X) dP >= 0, then linearity. The a.s. qualifier is enough (null sets do not affect the integral).

## Specialization / boundary cases
- X = 1_A <= 1_B = Y when A subset B: recovers P(A) <= P(B)
- E[X] = 0 with X >= 0 a.s.: X = 0 a.s. -- the 'no negative mass' rigidity used in L^p norms

## Hypothesis-dropped counterexamples
- **a_s_inequality**: X <= Y on a null set only is not enough to compare -- but changing X, Y on a null set changes neither expectation, so 'a.s.' is exactly the right hypothesis
- **existence_of_both_expectations**: if E[Y] = +inf and E[X] = -inf the inequality is vacuous/ill-posed

## Common misuse
- concluding X <= Y a.s. from E[X] <= E[Y] (false -- expectation loses the pointwise order)
- using strict monotonicity without a strict a.s. inequality on a positive-probability set

## Related nodes (non-prerequisite)
- used_by: markov_inequality, jensen_inequality, cauchy_schwarz_expectation

## Sources
billingsley_probability_measure, durrett_pte
