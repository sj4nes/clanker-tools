# matrix_mult_is_composition

## Type
theorem

## Statement
[S o T]_{D<-B} = [S]_{D<-C} [T]_{C<-B}. Matrix multiplication represents composition; associativity of the product follows from associativity of composition, with no index computation.

## Symbols
- `B, C, D` — ordered bases of the three spaces involved

## Epistemic status
proved_theorem  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
composition_of_linear_maps, matrix_multiplication, matrix_of_linear_map

## Hypotheses
all spaces finite-dimensional, bases fixed

## Proof provenance
technique: compute the j-th column of both sides: both equal the D-coordinates of S(T(b_j))
derives_from: matrix_of_linear_map
lean_status: dim_core — LinAlg.mul_assoc2, LinAlg.mul_one2 (n = 2)

## Type / well-formedness check
Well-formed: the middle basis C must be THE SAME on both factors, which is the conceptual content of the conformability rule.

## Specialization / boundary cases
- S = I: recovers [T] = [T]
- all spaces equal with one basis: L(V) is isomorphic to F^{n x n} as an algebra

## Hypothesis-dropped counterexamples
- **same_middle_basis**: using different bases for the codomain of T and the domain of S silently inserts a change-of-basis matrix; this is the most common source of wrong products in applied work
- **finite_dimensionality**: no matrix representation exists otherwise

## Common misuse
- proving associativity of matrix multiplication by a triple-sum index manipulation and treating that as the explanation: the real reason is that function composition is associative

## Related nodes (non-prerequisite)
- required_by: change_of_basis

## Sources
hoffman_kunze_2e, axler_lada_4e
