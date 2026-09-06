# set_algebra

## Type
primitive

## Statement
The Boolean algebra of subsets of a fixed set: union, intersection, complement, difference, De Morgan's laws, and arbitrary (indexed) unions and intersections.

## Symbols
- `A, B` — subsets of a set Omega, type: element of 2^Omega
- `{A_i}` — an indexed family, type: I -> 2^Omega

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
(root)

## Hypotheses
(none — unconditional within scope)

## Well-definedness
the powerset 2^Omega is a complete Boolean algebra under subset-or-equal; every identity used downstream (De Morgan, distributivity, A = (A cap B) cup (A cap B^c)) holds there.

## Type / well-formedness check
operations are on subsets of one fixed Omega; an indexed intersection needs I nonempty for the usual identities. Discharged from math-sets-functions-cardinality.

## Specialization / boundary cases
- two sets: A cup A^c = Omega, A cap A^c = empty
- indexed: (bigcup_i A_i)^c = bigcap_i A_i^c (De Morgan, arbitrary)

## Common misuse
- intersecting an empty family (gives Omega, not empty)
- assuming a sigma-algebra is closed under ARBITRARY unions -- only countable

## Related nodes (non-prerequisite)
- developed_in: math-sets-functions-cardinality

## Sources
enderton_set_theory, halmos_naive_set_theory
