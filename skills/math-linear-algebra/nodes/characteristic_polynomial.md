# characteristic_polynomial

## Type
definition

## Statement
p_A(t) = det(tI - A) in F[t], MONIC of degree n. It is a similarity invariant, so p_T is well-defined for an operator T by taking any matrix representation.

## Symbols
- `p_A` — type: monic element of F[t] of degree n
- `t` — the indeterminate

## Epistemic status
definition  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
characteristic_polynomial_convention, determinant, determinant_similarity_invariant, matrix_of_linear_map, polynomial_ring

## Hypotheses
A square

## Proof provenance
technique: similarity invariance: det(tI - P^{-1}AP) = det(P^{-1}(tI - A)P) = det(tI - A) by determinant_similarity_invariant applied over F[t]
derives_from: determinant_similarity_invariant
lean_status: dim_core — LinAlg.charpoly_2 (n = 2, universal in t)

## Type / well-formedness check
Well-formed: tI - A is a matrix over the commutative ring F[t], and the determinant of a matrix over a commutative ring is defined by the same Leibniz formula. Monicity of degree n follows because the identity permutation contributes prod(t - A_{ii}).

## Specialization / boundary cases
- n = 1: p(t) = t - a
- n = 2: p(t) = t^2 - tr(A) t + det(A)
- A triangular: p(t) = prod_i (t - A_{ii}), by determinant_triangular

## Hypothesis-dropped counterexamples
- **the_sign_convention**: under det(A - tI) the polynomial is (-1)^n p_A, with the same roots but different coefficient signs -- see characteristic_polynomial_convention
- **does_not_determine_similarity**: [[1,1],[0,1]] and I_2 share p(t) = (t-1)^2 but are not similar. The characteristic polynomial is an invariant, not a complete one (similar_invariants)

## Common misuse
- computing p_A by expanding det(tI - A) symbolically for large n: use the eigenvalues if known, or an algorithm like Faddeev-LeVerrier
- treating p_A as determining A up to similarity

## Related nodes (non-prerequisite)
- required_by: char_poly_roots_are_eigenvalues, cayley_hamilton, algebraic_geometric_multiplicity

## Sources
hoffman_kunze_2e, horn_johnson_2e
