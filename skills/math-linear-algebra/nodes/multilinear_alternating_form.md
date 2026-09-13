# multilinear_alternating_form

## Type
definition

## Statement
D: (F^n)^n -> F is multilinear if it is linear in each column separately with the others fixed, and ALTERNATING if D(...) = 0 whenever two columns are EQUAL. Alternating implies sign-change under a swap; the converse needs char F != 2.

## Symbols
- `D` — type: function (F^n)^n -> F
- `the n arguments` — the COLUMNS of a matrix, type: elements of F^n

## Epistemic status
definition  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
field, index_convention, matrix

## Hypotheses
D multilinear

## Proof provenance
technique: vanishing implies antisymmetry: expand D(u+v, u+v) = 0 by multilinearity and cancel the two vanishing terms
derives_from: matrix
lean_status: cited

## Type / well-formedness check
Well-formed. Defining alternating by VANISHING rather than by sign change is deliberate and is what makes the theory characteristic-independent (see permutation_sign's counterexample).

## Specialization / boundary cases
- n = 1: the multilinear alternating forms on F^1 are exactly the scalar multiples of the identity, D(a) = ca
- n = 2: D([a,c],[b,d]) = ad - bc up to a scalar

## Hypothesis-dropped counterexamples
- **the_vanishing_definition**: over F_2, 'D changes sign under a swap' is satisfied by the PERMANENT (which never changes sign, and -1 = 1), yet the permanent is not the determinant. The vanishing definition excludes it
- **multilinearity**: a form that is merely additive in each slot, without homogeneity, does not pin down D even with alternation

## Common misuse
- treating 'alternating' and 'antisymmetric' as synonyms in characteristic 2

## Related nodes (non-prerequisite)
- required_by: determinant_existence_uniqueness, determinant

## Sources
hoffman_kunze_2e, lang_algebra_3e
