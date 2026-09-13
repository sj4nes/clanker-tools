# condition_number

## Type
diagnostic

## Statement
kappa_2(A) = sigma_1/sigma_n = ||A||_2 ||A^{-1}||_2 for invertible A. It bounds the relative error amplification: ||dx||/||x|| <= kappa(A) (||db||/||b|| + ||dA||/||A||) to first order. LARGE kappa means ILL-CONDITIONED, which is NOT the same as singular.

## Symbols
- `kappa_2(A)` — type: real >= 1
- `dx, db` — perturbations

## Epistemic status
definition  ·  field_scope: real_or_complex

## Prerequisites (tsort edges into this node)
invertibility_equivalences, linear_system, matrix_norms, singular_values

## Hypotheses
A invertible

## Proof provenance
technique: from ||A||_2 = sigma_1 and ||A^{-1}||_2 = 1/sigma_n; the perturbation bound by expanding (A+dA)(x+dx) = b+db and using submultiplicativity. The floating-point interpretation (roughly log10(kappa) digits lost) is a CITED numerical-analysis heuristic
derives_from: matrix_norms
lean_status: core — LinAlg.condition_ge_one

## Type / well-formedness check
Well-formed for invertible A; for singular A, kappa = infinity by convention, and for rectangular A one uses sigma_1/sigma_r. Note kappa is SCALE-INVARIANT: kappa(cA) = kappa(A), unlike the determinant.

## Specialization / boundary cases
- A orthogonal: kappa = 1, the best possible -- which is why orthogonal transformations are the building block of stable algorithms
- A = diag(1, 1e-10): kappa = 1e10, so about 10 digits are lost
- kappa(A^TA) = kappa(A)^2 -- the reason the normal equations are avoided (least_squares)
- the Hilbert matrix H_n has kappa growing like e^{3.5n}: catastrophic by n = 12

## Hypothesis-dropped counterexamples
- **determinant_is_not_conditioning**: A = 1e-5 * I_{10} has det = 1e-50, vanishingly small, yet kappa = 1 -- perfectly conditioned. Conversely diag(1, 1e-10) has det = 1e-10 and kappa = 1e10. The determinant is scale-sensitive and conditioning is not; the two carry entirely different information. This is the single most important practical point in the node
- **conditioning_is_a_property_of_the_PROBLEM**: kappa bounds what ANY algorithm can achieve on this data; a backward-stable algorithm achieves it, an unstable one does worse. Conditioning and stability are different notions

## Common misuse
- using a small determinant as a near-singularity test (see above)
- treating a large kappa as an algorithm's fault: it is a property of the problem, and the remedy is reformulation (regularisation, scaling, a better basis), not a better solver

## In the wild
- the standard diagnostic for whether a linear system or regression is trustworthy; variance inflation factors in regression are a condition-number statement about the design matrix
- the reason centring and scaling predictors, and using orthogonal polynomial bases, materially improve a fit

## Related nodes (non-prerequisite)
- contrasts_with: determinant_invertible_iff
- approximates: linear_system

## Sources
trefethen_bau, higham_asna_2e
