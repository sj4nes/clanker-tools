# fundamental_theorem_of_algebra

## Type
bridge

## Statement
Every nonconstant polynomial in C[t] has a root in C; equivalently every such polynomial splits into linear factors. C is algebraically closed. CITED, NOT PROVED -- every known proof needs analysis or topology that no capsule in this stack develops.

## Symbols
- `p` — a polynomial, type: element of C[t]
- `z` — a root, type: element of C

## Epistemic status
proved_theorem  ·  field_scope: algebraically_closed

## Prerequisites (tsort edges into this node)
complex_number

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: cited; standard proofs use Liouville's theorem, the argument principle, or a minimum-modulus/compactness argument, none available in this stack
lean_status: cited

## Type / well-formedness check
Well-formed. Note the statement is about C specifically, not about fields in general -- most fields are not algebraically closed.

## Specialization / boundary cases
- degree 2 over R: t^2 + 1 has no real root but factors over C, which is the minimal instance of why R is not algebraically closed

## Hypothesis-dropped counterexamples
- **the_field_being_C**: over R the theorem is false: t^2 + 1 is irreducible. This is precisely the hypothesis that eigenvalue_existence_closed needs, and why a real rotation matrix can have no real eigenvalue
- **nonconstant**: a nonzero constant polynomial has no root; the degree >= 1 hypothesis is not decorative

## Common misuse
- citing FTA to claim a REAL matrix has real eigenvalues -- it gives complex ones, and realness for symmetric matrices is a separate theorem (self_adjoint_real_eigenvalues)
- treating this capsule's use of it as proved: it is the capsule's single largest cited gap

## Related nodes (non-prerequisite)
- required_by: schur_triangularisation, spectral_theorem_normal

## Sources
hoffman_kunze_2e, horn_johnson_2e
