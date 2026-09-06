# limsup_liminf

## Type
primitive

## Statement
limsup and liminf of a real sequence (always defined in the extended reals); for a sequence of SETS, limsup A_n = { omega in infinitely many A_n } = intersection_N union_{n>=N} A_n.

## Symbols
- `(a_n)` — a real sequence, type: N -> R
- `(A_n)` — a sequence of events, type: N -> F

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
(root)

## Hypotheses
(none — unconditional within scope)

## Well-definedness
limsup a_n = inf_N sup_{n>=N} a_n exists in [-inf, +inf]; the set versions are countable unions and intersections, hence in any sigma-algebra containing the A_n.

## Type / well-formedness check
for sets, 'A_n infinitely often' (i.o.) is limsup A_n; 'A_n eventually / all but finitely often' is liminf A_n. Both are events (countable operations on F). Discharged from math-real-analysis.

## Specialization / boundary cases
- Borel-Cantelli lemmas are statements about P(limsup A_n)
- a_n -> a iff limsup a_n = liminf a_n = a

## Common misuse
- reading limsup A_n as 'the last A_n' -- it is the i.o. event
- forgetting liminf A_n subset limsup A_n always

## Related nodes (non-prerequisite)
- developed_in: math-real-analysis

## Sources
rudin_principles, billingsley_probability_measure
