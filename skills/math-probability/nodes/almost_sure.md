# almost_sure

## Type
notation_convention

## Statement
An event A holds almost surely (a.s.) if P(A) = 1, equivalently if its complement is a P-null set. Convergence, equality, and inequalities of random variables are all understood in the a.s. sense unless stated otherwise.

## Symbols
- `A` — an event, type: element of F
- `P` — the probability measure, type: F -> [0,1]

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
null_set, probability_measure

## Hypotheses
(none — unconditional within scope)

## Well-definedness
P(A) = 1 is well-defined; the a.s. quantifier is closed under countable intersection: P(bigcap A_n) = 1 if P(A_n) = 1 for all n (complement is a countable union of null sets).

## Type / well-formedness check
'a.s.' is 'a.e.' for a probability measure. Countably many a.s. events hold simultaneously a.s. (their intersection has probability 1). X = Y a.s. means P(X = Y) = 1; it is an equivalence relation on random variables and is the identification used to define L^p and E[X | G].

## Specialization / boundary cases
- X_n -> X a.s. is the strongest of the four convergence modes
- E[X | G] is defined only up to a.s. equality

## Hypothesis-dropped counterexamples
- **countable_intersection_only**: an uncountable family of a.s. events can have intersection of probability 0: on [0,1] uniform, A_x = { omega != x } has P(A_x) = 1 but bigcap_x A_x = empty

## Common misuse
- reading 'a.s.' as 'always' -- a.s. events can fail on a nonempty (null) set
- intersecting uncountably many a.s. events (e.g. 'X_t continuous in t' needs a separate argument -- separability / a continuous modification)

## Related nodes (non-prerequisite)
- specializes: null_set
- used_by: convergence_almost_sure, strong_law_large_numbers

## Sources
billingsley_probability_measure, durrett_pte
