# matrix_mult_noncommutative

## Type
counterexample

## Statement
AB != BA in general. Minimal witness: A = [[0,1],[0,0]], B = [[0,0],[1,0]] give AB = [[1,0],[0,0]] and BA = [[0,0],[0,1]] -- not equal, and with DIFFERENT eigenvalue positions though the same spectrum {0,1}.

## Symbols
- `A, B` — 2x2 nilpotent matrices over any field

## Epistemic status
counterexample  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
matrix_multiplication

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: direct computation
derives_from: matrix_multiplication
lean_status: instance — LinAlg.ab_ne_ba, LinAlg.noncomm_but_trace_and_det_agree

## Type / well-formedness check
Well-formed over any field; the entries are 0 and 1, so the witness works even over F_2.

## Specialization / boundary cases
- tr(AB) = tr(BA) = 1 nevertheless -- the trace IS cyclic even though the product is not commutative (trace_cyclic)
- det(AB) = det(BA) = 0, likewise: determinant is multiplicative hence commutative on products

## Hypothesis-dropped counterexamples
- **none_all_hypotheses_essential**: this IS a counterexample node; it exists to block the scalar-algebra habit

## Common misuse
- writing (A+B)^2 = A^2 + 2AB + B^2 (correct only if AB = BA)
- writing e^{A}e^{B} = e^{A+B} (the Baker-Campbell-Hausdorff correction is exactly the failure of commutativity)
- writing (AB)^{-1} = A^{-1}B^{-1} instead of B^{-1}A^{-1}

## Related nodes (non-prerequisite)
- illustrated_by: 

## Sources
horn_johnson_2e
