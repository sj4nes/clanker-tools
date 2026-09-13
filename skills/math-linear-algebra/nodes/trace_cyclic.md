# trace_cyclic

## Type
proposition

## Statement
tr(AB) = tr(BA) whenever both products are defined (A in F^{m x n}, B in F^{n x m}), hence tr(P^{-1}AP) = tr(A). Trace is a SIMILARITY INVARIANT and therefore a property of the operator, not of the basis.

## Symbols
- `P` — an invertible change-of-basis matrix

## Epistemic status
proposition  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
matrix_multiplication, similarity, trace

## Hypotheses
shapes conformable

## Proof provenance
technique: tr(AB) = sum_i sum_k A_{ik}B_{ki} = sum_k sum_i B_{ki}A_{ik} = tr(BA), just exchanging the order of summation
derives_from: matrix_multiplication
lean_status: dim_core — LinAlg.trace_mul_comm (n = 2)

## Type / well-formedness check
Well-formed; note AB and BA need not even be the same SIZE (m x m versus n x n), yet their traces agree. The cyclic property permits cyclic rotation only -- NOT arbitrary permutation.

## Specialization / boundary cases
- P^{-1}(AP) and (AP)P^{-1} = A: the similarity invariance is the cyclic identity applied once
- tr(xy^T) = y^T x for column vectors: the rank-one case, used constantly in matrix calculus

## Hypothesis-dropped counterexamples
- **cyclic_not_arbitrary**: tr(ABC) = tr(ACB) is FALSE in general. Take A = I and the noncommuting B, C of matrix_mult_noncommutative: tr(BC) = 1 while tr(CB) = 1 here, but with a third factor the identity genuinely breaks -- only CYCLIC rotations are valid
- **conformability**: otherwise ill-typed

## Common misuse
- permuting factors arbitrarily under a trace (only cyclic rotation is allowed)
- concluding AB = BA from tr(AB) = tr(BA), which always holds

## In the wild
- tr(H) = p as the effective number of parameters of a linear smoother, hence the degrees-of-freedom term in AIC/Cp and in residual variance estimation
- the trace trick in matrix calculus: d tr(AX)/dX = A^T

## Related nodes (non-prerequisite)
- required_by: similar_invariants, char_poly_coefficients

## Sources
hoffman_kunze_2e, horn_johnson_2e
