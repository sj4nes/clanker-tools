# multiplication_rule

## Type
identity

## Statement
P(A cap B) = P(A | B) P(B) = P(B | A) P(A). Chain rule: P(A_1 cap ... cap A_n) = P(A_1) P(A_2 | A_1) P(A_3 | A_1 cap A_2) ... (each conditioning event having positive probability).

## Symbols
- `A_i` — events with the running intersections of positive probability, type: element of F

## Epistemic status
mathematical_identity

## Prerequisites (tsort edges into this node)
conditional_probability

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: P(A|B) P(B) = [P(A cap B)/P(B)] P(B) = P(A cap B); induct for the n-fold version
derives_from: conditional_probability
lean_status: core

## Type / well-formedness check
a rearrangement of the definition of conditional probability, iterated. The order of the A_i can be permuted; each requires its predecessor-intersection to have positive probability.

## Specialization / boundary cases
- independent A, B: P(A cap B) = P(A) P(B)
- drawing without replacement: P(both aces) = (4/52)(3/51) -- the chain rule computes sequential-sampling probabilities
- P(A_1 cap ... cap A_n) for a Markov chain telescopes to P(A_1) prod P(A_{i+1} | A_i)

## Hypothesis-dropped counterexamples
- **positive_probability_of_the_conditioning_events**: if some prefix intersection has probability 0, that conditional factor is undefined -- but then the whole intersection also has probability 0, so the identity is read as 0 = 0

## Common misuse
- assuming P(A cap B) = P(A) P(B) without independence
- chain-rule factors in an order where a conditioning event has probability 0

## Related nodes (non-prerequisite)
- derives_from: conditional_probability
- used_by: law_of_total_probability, bayes_theorem

## Sources
billingsley_probability_measure, durrett_pte
