# matrix_of_linear_map

## Type
construction

## Statement
For T: V -> W with ordered bases B of V and C of W, [T]_{C<-B} is the matrix whose j-th COLUMN is [T(b_j)]_C. Then [T(v)]_C = [T]_{C<-B} [v]_B.

## Symbols
- `[T]_{C<-B}` — type: element of F^{m x n} where n = dim V, m = dim W

## Epistemic status
constructive_result  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
index_convention, linear_map, linear_map_determined_by_basis, matrix, ordered_basis

## Hypotheses
V, W finite-dimensional, bases fixed and ORDERED

## Proof provenance
technique: existence and uniqueness from linear_map_determined_by_basis; the action formula by expanding v in the basis
derives_from: ordered_basis
lean_status: cited

## Type / well-formedness check
Well-formed and unique by linear_map_determined_by_basis. The COLUMNS-are-images convention is what makes composition correspond to the product in the order [S][T]; the opposite convention transposes everything.

## Specialization / boundary cases
- V = W = F^n with standard bases: [T] is the matrix A with T(x) = Ax
- T = I with B != C: [I]_{C<-B} is the change-of-basis matrix, which is generally NOT the identity matrix

## Hypothesis-dropped counterexamples
- **finite_dimensionality**: no matrix exists otherwise
- **the_bases_being_recorded**: the SAME operator has different matrices in different bases; conversely the same matrix represents different operators. Dropping the subscripts is how sign and transposition errors enter

## Common misuse
- saying 'the matrix of T' without naming bases
- confusing [T]_{C<-B} with [T]_{B<-C}: they are related by inversion, not transposition

## Related nodes (non-prerequisite)
- required_by: change_of_basis, characteristic_polynomial

## Sources
hoffman_kunze_2e, axler_lada_4e
