# law_of_total_probability

## Type
theorem

## Statement
If {B_i} is a countable partition of Omega with P(B_i) > 0, then for any event A: P(A) = sum_i P(A | B_i) P(B_i).

## Symbols
- `A` — an event, type: element of F
- `{B_i}` — a countable measurable partition of Omega, type: family in F

## Epistemic status
proved_theorem

## Prerequisites (tsort edges into this node)
conditional_probability, finite_additivity, multiplication_rule, set_algebra

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: A = bigsqcup_i (A cap B_i); P(A) = sum_i P(A cap B_i) = sum_i P(A | B_i) P(B_i) by countable additivity and the multiplication rule
derives_from: finite_additivity
lean_status: core — validation/proof-checks.lean Prob.bayes_denominator

## Type / well-formedness check
A is the disjoint union of A cap B_i; apply countable additivity, then the multiplication rule to each term.

## Specialization / boundary cases
- two-part partition {B, B^c}: P(A) = P(A|B) P(B) + P(A|B^c) P(B^c)
- the denominator of Bayes' theorem is exactly this expansion
- first-step analysis: P(gambler ruin) = p P(ruin | up) + (1-p) P(ruin | down)

## Hypothesis-dropped counterexamples
- **the_B_i_partition_Omega**: if the B_i do not cover Omega, sum_i P(A|B_i) P(B_i) = P(A cap bigcup B_i) < P(A) -- you undercount the part of A outside the B_i

## Common misuse
- using events that overlap or fail to cover Omega
- forgetting a case (a non-exhaustive partition silently loses probability)

## Related nodes (non-prerequisite)
- used_by: bayes_theorem
- expectation_analogue: tower_property / law of total expectation

## Sources
billingsley_probability_measure, durrett_pte
