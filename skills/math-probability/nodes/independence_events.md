# independence_events

## Type
definition

## Statement
Events A_1, ..., A_n are (mutually) independent if for EVERY subset S of indices, P(bigcap_{i in S} A_i) = prod_{i in S} P(A_i). An infinite family is independent if every finite subfamily is.

## Symbols
- `A_i` — events, type: element of F
- `S` — any subset of the index set, type: index set

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
finite_additivity, probability_measure

## Hypotheses
(none — unconditional within scope)

## Well-definedness
the condition is a finite conjunction of numeric identities per subset; it is preserved under complementation of any subset of the A_i.

## Type / well-formedness check
defined by FACTORIZATION, not by conditioning -- this keeps independence available for null events and sigma-algebras, and avoids the independence <-> conditional-probability circularity (see edges/cycles.md). 'P(A|B) = P(A)' is then a theorem, valid when P(B) > 0.

## Specialization / boundary cases
- two events: independence is the single equation P(A cap B) = P(A) P(B)
- A with P(A) in {0, 1}: A is independent of every event
- pairwise independence: only the |S| = 2 equations -- strictly weaker (pairwise_not_mutual)

## Hypothesis-dropped counterexamples
- **all_subsets_not_just_pairs**: pairwise_not_mutual: X, Y iid fair bits, Z = X XOR Y -- each pair independent, but P(X=Y=Z=0) = 1/4 != 1/8
- **the_empty_and_singleton_S_are_trivial**: the content is in |S| >= 2

## Common misuse
- checking only pairwise independence
- confusing independence with disjointness (disjoint events with positive probability are DEPENDENT: P(A cap B) = 0 != P(A)P(B))

## Related nodes (non-prerequisite)
- generalizes_to: independence_sigma_algebras, independence_random_variables
- equivalent_to: P(A|B) = P(A) when P(B) > 0

## Sources
billingsley_probability_measure, durrett_pte
