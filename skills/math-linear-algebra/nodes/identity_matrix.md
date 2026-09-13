# identity_matrix

## Type
definition

## Statement
I_n in F^{n x n} with (I_n)_{ij} = delta_{ij}. It is the two-sided multiplicative identity: I_m A = A = A I_n for A in F^{m x n}.

## Symbols
- `I_n` — type: element of F^{n x n}
- `delta_{ij}` — the Kronecker delta

## Epistemic status
definition  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
matrix, matrix_multiplication

## Hypotheses
(none — unconditional within scope)
## Type / well-formedness check
Well-formed; the two identities use DIFFERENT identity matrices when A is rectangular, which the subscripts record.

## Specialization / boundary cases
- I represents the identity operator in any basis -- one of very few matrices that is basis-independent
- det I = 1 and tr I_n = n

## Hypothesis-dropped counterexamples
- **none_all_hypotheses_essential**: a definition

## Common misuse
- writing I without the size in a mixed-shape computation

## Related nodes (non-prerequisite)
- required_by: invertible_matrix, elementary_matrix

## Sources
hoffman_kunze_2e
