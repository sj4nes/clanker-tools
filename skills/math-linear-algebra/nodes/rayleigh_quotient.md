# rayleigh_quotient

## Type
definition

## Statement
R_A(x) = <Ax,x>/<x,x> for x != 0. A DEFINITION ONLY at this point in the graph: that its extrema over the unit sphere are the extreme eigenvalues is proved downstream (courant_fischer), which is what lets it be used inside the spectral theorem's own proof without circularity (edges/cycles.md).

## Symbols
- `R_A` — type: function V\{0} -> R when A is self-adjoint (real-valued by self_adjoint)

## Epistemic status
definition  ·  field_scope: real_or_complex

## Prerequisites (tsort edges into this node)
induced_norm, inner_product, self_adjoint

## Hypotheses
A self-adjoint for real-valuedness, x != 0
## Type / well-formedness check
Well-formed and REAL-VALUED when A is self-adjoint, by the realness of <Ax,x>. Scale-invariance means it is really a function on the projective space, equivalently on the unit sphere -- which is what makes compactness applicable.

## Specialization / boundary cases
- x an eigenvector for lambda: R_A(x) = lambda exactly
- A = I: R_A is constantly 1
- the range of R_A over all x != 0 is the interval [lambda_min, lambda_max] for self-adjoint A (the numerical range)

## Hypothesis-dropped counterexamples
- **self_adjointness**: for a non-self-adjoint A, R_A is complex-valued and its range is a REGION of C (the numerical range / field of values), not an interval. The extremal characterisation fails entirely -- [[0,-1],[1,0]] has R_A identically 0 on real vectors while having no real eigenvalue
- **x_nonzero**: the quotient is undefined at 0

## Common misuse
- reading R_A's maximum as an eigenvalue for a non-symmetric matrix
- quoting the extremal property before courant_fischer -- in this capsule that ordering is deliberate

## In the wild
- the power-iteration convergence estimate; the variational principle for the ground-state energy in quantum mechanics and for the fundamental frequency in vibration analysis

## Related nodes (non-prerequisite)
- required_by: spectral_theorem_symmetric, courant_fischer

## Sources
horn_johnson_2e, axler_lada_4e
