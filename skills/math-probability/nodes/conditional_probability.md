# conditional_probability

## Type
definition

## Statement
For events A, B with P(B) > 0, the conditional probability of A given B is P(A | B) = P(A cap B) / P(B). For fixed B, P(. | B) is itself a probability measure on F.

## Symbols
- `A, B` — events, type: element of F
- `P(. | B)` — the conditioned measure, type: F -> [0,1]

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
complement_rule, probability_measure

## Hypotheses
(none — unconditional within scope)

## Well-definedness
P(. | B) satisfies the Kolmogorov axioms: nonnegative, P(Omega | B) = P(B)/P(B) = 1, countably additive (inherited from P). So all earlier results apply to it.

## Type / well-formedness check
the positivity P(B) > 0 is a genuine precondition; conditioning on probability-zero events needs conditional_expectation_abstract. P(. | B) restricts and renormalizes P to B.

## Specialization / boundary cases
- B = Omega: P(A | Omega) = P(A)
- A subset B: P(A | B) = P(A)/P(B) >= P(A)
- A, B disjoint: P(A | B) = 0

## Hypothesis-dropped counterexamples
- **positivity_of_P_B**: P(B) = 0 makes the ratio 0/0 -- the Borel-Kolmogorov paradox shows the 'limit' answer depends on the approximating sequence of positive-probability events

## Common misuse
- confusing P(A|B) with P(B|A) (base-rate / prosecutor's fallacy)
- conditioning on a measure-zero event without the abstract machinery
- assuming P(A|B) >= P(A) (only when A, B positively associated)

## Related nodes (non-prerequisite)
- used_by: multiplication_rule, bayes_theorem, law_of_total_probability
- generalizes_to: conditional_expectation_abstract

## Sources
billingsley_probability_measure, durrett_pte
