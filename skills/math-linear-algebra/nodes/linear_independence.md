# linear_independence

## Type
definition

## Statement
A family (v_i)_{i in I} is linearly independent if the only finite linear combination of its members equal to 0 is the one with all coefficients 0. Otherwise it is dependent.

## Symbols
- `(v_i)` — a FAMILY (repetition allowed), type: indexed family in V

## Epistemic status
definition  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
indexed_family, linear_combination

## Hypotheses
(none — unconditional within scope)
## Type / well-formedness check
Well-formed. Independence is a property of the indexed FAMILY, not of the underlying set: a family with a repeated vector is dependent even though its image set may be independent. The capsule uses families throughout for this reason.

## Specialization / boundary cases
- the empty family is independent vacuously
- a single vector v is independent iff v != 0
- any family containing 0 is dependent (take that coefficient 1, the rest 0)
- two vectors are independent iff neither is a scalar multiple of the other

## Hypothesis-dropped counterexamples
- **all_coefficients_zero**: requiring only SOME coefficient to be nonzero would make every family dependent; the quantifier is over ALL representations of 0
- **the_field**: over F_2 the vectors (1,1) and (1,1) are dependent, but independence is also field-sensitive in subtler ways: (1, sqrt 2) and (1, 1) are independent over Q as a Q-vector space and dependent over R in R^2 only if proportional -- always check which field

## Common misuse
- checking independence of n vectors in F^n by 'they look different' rather than by rank or determinant
- treating independence as a property of a SET when the family has repeats

## Related nodes (non-prerequisite)
- required_by: basis, dependence_lemma

## Sources
axler_lada_4e, hoffman_kunze_2e
