# nullity

## Type
definition

## Statement
nullity T = dim(ker T), the dimension of the solution space of the homogeneous equation T(v) = 0.

## Symbols
- `nullity T` — type: natural number, at most dim V

## Epistemic status
definition  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
dimension, kernel

## Hypotheses
(none — unconditional within scope)
## Type / well-formedness check
Well-formed when ker T is finite-dimensional, automatic if V is.

## Specialization / boundary cases
- T injective: nullity 0
- T = 0 on V: nullity = dim V

## Hypothesis-dropped counterexamples
- **none_all_hypotheses_essential**: a definition; the content is entirely in rank_nullity

## Common misuse
- reading nullity as a count of SOLUTIONS rather than a DIMENSION: over an infinite field a one-dimensional kernel already contains infinitely many solutions (over F_q it contains exactly q)

## Sources
hoffman_kunze_2e
