# transpose_convention

## Type
notation_convention

## Statement
A^T is the TRANSPOSE (A^T)_{ij} = A_{ji}; A^* is the CONJUGATE TRANSPOSE (A^*)_{ij} = conj(A_{ji}). They coincide over R. Every Hermitian statement in this capsule says which one it means.

## Symbols
- `A^T` — transpose, type: F^{m x n} -> F^{n x m}
- `A^*` — conjugate transpose, type: C^{m x n} -> C^{n x m}

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
(root — cited, see conventions.md)

## Hypotheses
(none — unconditional within scope)
## Type / well-formedness check
A convention. The substantive point is that the ADJOINT with respect to an inner product is A^*, not A^T, over C -- adjoint_operator proves this, and getting it wrong makes the complex spectral theorem false.

## Specialization / boundary cases
- over R the two coincide, which is why the statistics-facing half of the capsule can be written entirely with A^T

## Hypothesis-dropped counterexamples
- **none_all_hypotheses_essential**: a convention; the failure mode is using A^T over C, under which A^T A need not be positive semidefinite -- take A = [[1, i]], where A^T A has a zero eigenvalue direction while A^* A does not

## Common misuse
- defining a complex symmetric matrix as A^T = A and expecting real eigenvalues: that is the HERMITIAN condition A^* = A, and complex-symmetric matrices can have any spectrum

## Related nodes (non-prerequisite)
- dual_of: dual_map

## Sources
horn_johnson_2e
