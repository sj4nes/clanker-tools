# gram_matrix

## Type
construction

## Statement
For vectors v_1,...,v_k in an inner product space, G_{ij} = <v_j, v_i> (equivalently G = A^*A with A the matrix of columns). G is Hermitian positive SEMIdefinite, rank G = dim span(v_i), and G is positive DEFINITE iff the v_i are linearly independent.

## Symbols
- `G` — the Gram matrix, type: k x k Hermitian PSD
- `det G` — the Gram determinant, the squared volume of the parallelepiped

## Epistemic status
constructive_result  ·  field_scope: real_or_complex

## Prerequisites (tsort edges into this node)
inner_product, linear_independence, matrix_rank, positive_definite

## Hypotheses
an inner product space

## Proof provenance
technique: x^*Gx = ||Ax||^2 >= 0, with equality iff Ax = 0; so G is definite iff null(A) = {0} iff the columns are independent. rank G = rank A because null(A^*A) = null(A)
derives_from: positive_definite
lean_status: dim_core — LinAlg.gram_psd, LinAlg.gram_psd_nonneg, LinAlg.gram_symmetric (n = 2)

## Type / well-formedness check
Well-formed; Hermitian because (A^*A)^* = A^*A, and PSD because x^*A^*Ax = ||Ax||^2 >= 0. Both facts are one line and are the reason PSD matrices are ubiquitous.

## Specialization / boundary cases
- k = 1: G = [||v_1||^2]
- the v_i orthonormal: G = I
- A^TA in the normal equations IS a Gram matrix, which is why least_squares has a unique solution exactly under full column rank
- det G is the squared volume of the parallelepiped spanned by the v_i -- zero iff they are dependent

## Hypothesis-dropped counterexamples
- **independence_for_definiteness**: with a repeated vector G is singular; in regression this is exact collinearity, and near-collinearity makes G nearly singular and the fit ill-conditioned (condition_number)
- **null(A^*A) = null(A) needs the CONJUGATE**: over C with A^TA instead, A = [[1, i]] gives a singular A^TA despite full rank -- see conjugate_transpose

## Common misuse
- forming the Gram matrix to solve least squares (it squares the condition number -- see least_squares)
- using A^TA over C

## In the wild
- kernel matrices in machine learning ARE Gram matrices, which is why Mercer's condition is positive semidefiniteness
- the covariance matrix of a random vector is the Gram matrix of the centred variables under the E[XY] inner product

## Related nodes (non-prerequisite)
- required_by: psd_characterisations, singular_values

## Sources
horn_johnson_2e
