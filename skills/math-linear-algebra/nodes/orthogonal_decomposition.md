# orthogonal_decomposition

## Type
theorem

## Statement
If U is a FINITE-DIMENSIONAL subspace of an inner product space V then V = U (+) U^perp, and (U^perp)^perp = U. Every v decomposes uniquely as v = P_U v + (v - P_U v).

## Symbols
- `P_U` — the orthogonal projection onto U

## Epistemic status
proved_theorem  ·  field_scope: real_or_complex

## Prerequisites (tsort edges into this node)
dimension_formula_sum, direct_sum, finite_dimensional, gram_schmidt, orthogonal_complement, orthogonal_projection

## Hypotheses
U finite-dimensional

## Proof provenance
technique: take an orthonormal basis of U by gram_schmidt and set P_U v = sum <v,e_i> e_i; then v - P_U v is orthogonal to each e_i hence to U. The intersection is trivial because a vector in both is orthogonal to itself, hence 0 by positive definiteness
derives_from: orthogonal_projection
lean_status: cited

## Type / well-formedness check
Well-formed. The hypothesis is on U (finite-dimensional), NOT on V -- the theorem holds for a finite-dimensional subspace of an infinite-dimensional space, which is what makes least squares work in function spaces.

## Specialization / boundary cases
- U = {0}: V = {0} (+) V
- U = V: V = V (+) {0}
- U = col(A) in F^m: gives the least-squares decomposition of b into fitted values plus residual

## Hypothesis-dropped counterexamples
- **finite_dimensionality_of_U**: in an incomplete inner product space, a NON-CLOSED infinite-dimensional subspace can have U^perp = {0} while U != V -- then V != U + U^perp and (U^perp)^perp = V != U. The standard witness is the space of finitely-supported sequences inside l^2. In a complete space (Hilbert) closedness of U is the right hypothesis
- **positive_definiteness**: a degenerate form allows a nonzero vector in U ∩ U^perp

## Common misuse
- applying it to an arbitrary subspace of an infinite-dimensional space without a closedness or finite-dimensionality hypothesis
- assuming the complement is unique among ALL complements: it is unique among ORTHOGONAL ones, which is the point (see direct_sum)

## Related nodes (non-prerequisite)
- required_by: projection_matrix_characterisation, best_approximation, spectral_theorem_symmetric

## Sources
axler_lada_4e
