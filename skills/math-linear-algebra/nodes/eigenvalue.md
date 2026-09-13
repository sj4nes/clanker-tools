# eigenvalue

## Type
definition

## Statement
lambda in F is an eigenvalue of T in L(V) if Tv = lambda v for some v != 0; such a v is an eigenvector for lambda. DEFINED WITHOUT THE DETERMINANT (edges/cycles.md, cycle 1).

## Symbols
- `lambda` — an eigenvalue, type: element of F
- `v` — an eigenvector, type: NONZERO element of V

## Epistemic status
definition  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
linear_operator, vector_space

## Hypotheses
T in L(V), v != 0
## Type / well-formedness check
Well-formed for an OPERATOR (same domain and codomain), since Tv and lambda v must live in the same space. The requirement v != 0 is essential: T0 = lambda 0 holds for every lambda.

## Specialization / boundary cases
- lambda = 0 is an eigenvalue iff T is not injective, i.e. iff ker T != {0}
- T = lambda I: every nonzero vector is an eigenvector
- a projection has eigenvalues in {0,1}; a reflection in {1,-1} (when char F != 2)

## Hypothesis-dropped counterexamples
- **v_nonzero**: without it every scalar would be an eigenvalue of every operator, and the notion would be empty
- **the_field**: the real rotation [[0,-1],[1,0]] has NO real eigenvalue but two complex ones (+-i). Eigenvalues are field-relative, which is why eigenvalue_existence_closed carries the algebraically_closed_field hypothesis
- **squareness**: a rectangular matrix has no eigenvalues; the correct analogue is singular_values

## Common misuse
- saying 'the eigenvalues of A' without naming the field
- assuming eigenvectors for a single eigenvalue are unique: the eigenspace is a SUBSPACE, and any nonzero element of it is an eigenvector

## In the wild
- the modes of a linear dynamical system x' = Ax: stability is governed by the signs of the real parts of the eigenvalues
- PageRank is the eigenvector of the Google matrix for eigenvalue 1; PCA uses the eigenvectors of a covariance matrix

## Related nodes (non-prerequisite)
- required_by: eigenspace, char_poly_roots_are_eigenvalues, singular_values

## Sources
axler_lada_4e, horn_johnson_2e
