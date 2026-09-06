# probability_measure

## Type
definition

## Statement
A probability measure is a measure P on (Omega, F) with P(Omega) = 1. So P: F -> [0,1], P(empty) = 0, and P is countably additive.

## Symbols
- `P` — the probability measure, type: F -> [0,1]
- `(Omega, F)` — a measurable space, type: measurable space

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
kolmogorov_axioms, measure

## Hypotheses
(none — unconditional within scope)

## Well-definedness
a measure with P(Omega) = 1 exists on any measurable space (e.g. a Dirac point mass); the constraint is consistent and non-vacuous.

## Type / well-formedness check
the only change from a general measure is the normalization P(Omega) = 1, which forces P <= 1 everywhere and removes every finiteness caveat (continuity from above always holds).

## Specialization / boundary cases
- Omega finite: P given by a pmf on Omega
- P = lambda restricted to [0,1]: the uniform model space

## Hypothesis-dropped counterexamples
- **normalization**: drop P(Omega)=1 and expectations are no longer weighted averages; Bayes' normalizing constant is meaningless

## Common misuse
- forgetting P is countably (not just finitely) additive
- assuming P(A) > 0 for every nonempty A

## Related nodes (non-prerequisite)
- specializes: measure
- used_by: probability_space, kolmogorov_axioms

## Sources
billingsley_probability_measure, durrett_pte
