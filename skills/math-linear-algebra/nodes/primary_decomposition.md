# primary_decomposition

## Type
theorem

## Statement
If p_T splits over F then V is the DIRECT SUM of the generalised eigenspaces, V = (+)_lambda G_lambda, each is T-invariant, and T acts on G_lambda as lambda I + N with N nilpotent. (Equivalently: T = D + N with D diagonalisable, N nilpotent, DN = ND -- the Jordan-Chevalley decomposition.)

## Symbols
- `D` — the diagonalisable (semisimple) part
- `N` — the nilpotent part

## Epistemic status
proved_theorem  ·  field_scope: algebraically_closed

## Prerequisites (tsort edges into this node)
algebraically_closed_field, direct_sum, generalised_eigenspace, invariant_subspace, minimal_polynomial, nilpotent_operator

## Hypotheses
p_T splits over F, V finite-dimensional

## Proof provenance
technique: write p_T = prod (t - lambda_i)^{a_i}; the factors are pairwise coprime, so by the Chinese remainder theorem in F[t] the projections onto ker((T - lambda_i)^{a_i}) are polynomials in T, summing to I and annihilating each other
derives_from: generalised_eigenspace
lean_status: cited

## Type / well-formedness check
Well-formed given splitting. The uniqueness of the D + N decomposition subject to commuting is part of the content and is what makes 'the semisimple part' well-defined.

## Specialization / boundary cases
- T diagonalisable: every N_lambda = 0 and the decomposition is into eigenspaces
- T nilpotent: one generalised eigenspace G_0 = V, with D = 0
- refining each nilpotent part into cyclic blocks gives jordan_normal_form -- the step NOT taken in this release

## Hypothesis-dropped counterexamples
- **splitting**: over R the rotation has no eigenvalues, so no generalised eigenspaces and no decomposition. The RATIONAL canonical form is the field-independent substitute and is out of scope
- **commutativity_of_D_and_N**: without requiring DN = ND the decomposition into a diagonalisable plus a nilpotent part is NOT unique -- any matrix can be written as a sum of a diagonalisable and a nilpotent one in many ways

## Common misuse
- quoting the Jordan-Chevalley decomposition without the commuting condition, losing uniqueness
- applying it over R without checking that the spectrum is real

## Related nodes (non-prerequisite)
- required_by: jordan_normal_form, smith_normal_form_boundary

## Sources
hoffman_kunze_2e, axler_lada_4e
