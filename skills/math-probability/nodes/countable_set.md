# countable_set

## Type
primitive

## Statement
A set is countable if it injects into the natural numbers. Finite sets are countable; a countable union of countable sets is countable (using countable choice); N x N is countable.

## Symbols
- `A` — a set, type: set
- `N` — the natural numbers, type: set

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
(root)

## Hypotheses
(none — unconditional within scope)

## Well-definedness
injectivity into N is a well-defined property; the Cantor pairing N x N -> N is an explicit bijection (see instance-checks in the sibling capsule).

## Type / well-formedness check
'countable' includes finite here. A countable union of countable sets needs the axiom of countable choice (noted, not used elsewhere in this capsule). Discharged from math-sets-functions-cardinality.

## Specialization / boundary cases
- Q is countable; the algebraic numbers are countable
- a sigma-algebra is closed under countable unions, so it is the natural domain for a countably additive measure

## Hypothesis-dropped counterexamples
- **countable_choice**: without countable choice it is consistent that a countable union of countable sets of reals is uncountable (Feferman-Levy)

## Common misuse
- assuming R or 2^N is countable (Cantor's diagonal argument: they are not)
- confusing 'countable union' with 'arbitrary union'

## Related nodes (non-prerequisite)
- developed_in: math-sets-functions-cardinality

## Sources
enderton_set_theory, halmos_naive_set_theory
