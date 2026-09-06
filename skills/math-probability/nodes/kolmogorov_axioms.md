# kolmogorov_axioms

## Type
axiom

## Statement
P(A) >= 0 ; P(Omega) = 1 ; countable additivity on disjoint events. See results/kolmogorov_axioms.yaml.

## Symbols
- `P` — a probability measure, type: F -> [0,1]

## Epistemic status
axiom

## Prerequisites (tsort edges into this node)
countable_set, measure, set_algebra, sigma_algebra

## Hypotheses
(none — unconditional within scope)
## Type / well-formedness check
see the hand-written results/kolmogorov_axioms.yaml for the full treatment.

## Specialization / boundary cases
- Omega finite: P is a pmf

## Hypothesis-dropped counterexamples
- **countable_additivity**: finite-additive density on N is not a probability measure

## Common misuse
- assuming only finite additivity

## Related nodes (non-prerequisite)
- full_entry: results/kolmogorov_axioms.yaml

## Sources
billingsley_probability_measure, durrett_pte
