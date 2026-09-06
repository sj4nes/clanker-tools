# null_set

## Type
definition

## Statement
A null set (mu-null set) is a set N in F with mu(N) = 0. A property holds mu-almost everywhere (a.e.) if the set where it fails is contained in a null set.

## Symbols
- `N` — a null set, type: element of F with measure 0
- `mu` — the ambient measure, type: measure

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
measure

## Hypotheses
(none — unconditional within scope)

## Well-definedness
mu(N) = 0 is well-defined; the a.e. quantifier is closed under countable conjunction: if P_n holds a.e. for each n, then all P_n hold simultaneously a.e.

## Type / well-formedness check
a countable union of null sets is null (countable subadditivity) -- this is why 'a.e.' statements can be combined countably. A measure is complete if every subset of a null set is measurable (Lebesgue measure's completion adds exactly these).

## Specialization / boundary cases
- mu = P: a P-null set is the complement of an almost-sure event; 'a.e.' becomes 'almost surely'
- Lebesgue: Q is null, so 'x irrational' holds Lebesgue-a.e.

## Hypothesis-dropped counterexamples
- **countability_of_the_union**: an UNCOUNTABLE union of null sets need not be null: R = bigcup_{x} {x}, each {x} Lebesgue-null, but lambda(R) = inf

## Common misuse
- combining uncountably many a.e. statements
- assuming a null set is empty or countable (the Cantor set is uncountable and Lebesgue-null)

## Related nodes (non-prerequisite)
- used_by: almost_sure, expectation_monotonicity, conditional_expectation_abstract

## Sources
billingsley_probability_measure, folland_real_analysis
