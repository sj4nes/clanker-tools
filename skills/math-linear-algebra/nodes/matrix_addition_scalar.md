# matrix_addition_scalar

## Type
definition

## Statement
Matrices of the same shape add entrywise and scale entrywise, making F^{m x n} a vector space of dimension mn with basis the matrix units E_{ij}.

## Symbols
- `E_{ij}` — the matrix unit with 1 in position (i,j) and 0 elsewhere

## Epistemic status
definition  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
dimension, matrix, vector_space

## Hypotheses
equal shapes

## Proof provenance
technique: the axioms hold entrywise; the E_{ij} clearly span and are independent
derives_from: vector_space
lean_status: cited

## Type / well-formedness check
Well-formed only for matrices of EQUAL shape; unlike multiplication, addition has no conformability rule beyond equality.

## Specialization / boundary cases
- m = n = 1 recovers F itself
- F^{n x 1} = F^n, so column vectors are the n x 1 case

## Hypothesis-dropped counterexamples
- **equal_shapes**: adding a 2x3 and a 3x2 matrix is ill-typed, not merely false

## Common misuse
- assuming multiplication is also entrywise -- that is the Hadamard product, a different operation which does NOT represent composition

## Sources
hoffman_kunze_2e
