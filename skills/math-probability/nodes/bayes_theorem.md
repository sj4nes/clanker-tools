# bayes_theorem

## Type
theorem

## Statement
P(B_j | A) = P(A | B_j) P(B_j) / sum_i P(A | B_i) P(B_i). See results/bayes_theorem.yaml.

## Symbols
- `{B_i}` — a partition with positive priors, type: family in F

## Epistemic status
proved_theorem

## Prerequisites (tsort edges into this node)
conditional_probability, law_of_total_probability, multiplication_rule

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: definition of P(B_j|A) with the law of total probability in the denominator
derives_from: law_of_total_probability
lean_status: core — validation/proof-checks.lean Prob.bayes_denominator

## Type / well-formedness check
see the hand-written results/bayes_theorem.yaml for the full treatment.

## Specialization / boundary cases
- two hypotheses: odds form, posterior odds = likelihood ratio x prior odds

## Hypothesis-dropped counterexamples
- **partition_of_Omega**: a non-exhaustive partition loses probability mass

## Common misuse
- confusing P(A|B) with P(B|A)

## Related nodes (non-prerequisite)
- full_entry: results/bayes_theorem.yaml

## Sources
billingsley_probability_measure, durrett_pte
