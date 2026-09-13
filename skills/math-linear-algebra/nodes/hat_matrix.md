# hat_matrix

## Type
construction

## Statement
For A of full column rank, H = A(A^TA)^{-1}A^T is the orthogonal projection onto col(A). It is symmetric, idempotent, of rank = rank A, and tr(H) = rank A. The residual maker is M = I - H, also an orthogonal projection, onto col(A)^perp, with tr(M) = m - rank A.

## Symbols
- `H` — the hat matrix, type: element of R^{m x m}
- `M = I - H` — the residual maker

## Epistemic status
constructive_result  ·  field_scope: real_or_complex

## Prerequisites (tsort edges into this node)
invertible_matrix, least_squares, matrix_rank, projection_matrix_characterisation, trace

## Hypotheses
rank A = n (full column rank)

## Proof provenance
technique: symmetry and idempotence by direct computation; H a = a for a in col(A) and Hb = 0 for b in col(A)^perp identify it as the projection; tr(H) = tr(A(A^TA)^{-1}A^T) = tr((A^TA)^{-1}A^TA) = tr(I_n) = n by trace_cyclic
derives_from: projection_matrix_characterisation
lean_status: instance — LinAlg.idempotent_trace_eq_rank_both

## Type / well-formedness check
Well-formed when A^TA is invertible, i.e. when A has full column rank -- which by psd_characterisations is exactly when the Gram matrix is positive DEFINITE rather than merely semidefinite.

## Specialization / boundary cases
- A a single column a: H = aa^T/(a^Ta), the rank-one projection onto its span
- A = I_m: H = I, tr = m
- the diagonal entries h_ii are the LEVERAGES in regression, with sum equal to the number of parameters

## Hypothesis-dropped counterexamples
- **full_column_rank**: if A is rank deficient, A^TA is singular and H is undefined by this formula. The projection onto col(A) still exists -- use AA^+ with the pseudoinverse
- **orthogonality_needs_symmetry**: a weighted fit uses H_W = A(A^TW A)^{-1}A^TW, which is idempotent but NOT symmetric: an OBLIQUE projection. Quoting tr H = rank still works, but the Pythagorean decomposition of sums of squares does not

## Common misuse
- applying the unweighted formula and the orthogonal sum-of-squares decomposition to a weighted or GLS fit
- computing H explicitly for large m: it is m x m, while the fit needs only Ax

## In the wild
- THE object of linear regression diagnostics: leverages h_ii, Cook's distance, and tr(M) = n - p as the residual degrees of freedom that make s^2 = RSS/(n-p) unbiased -- this is exactly what math-statistics' unbiased_error_variance_estimator cites

## Related nodes (non-prerequisite)
- special_case_of: orthogonal_projection

## Sources
strang_5e, rao_linear_statistical_inference
