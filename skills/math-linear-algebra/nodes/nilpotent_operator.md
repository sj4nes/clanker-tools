# nilpotent_operator

## Type
definition

## Statement
N in L(V) is nilpotent if N^k = 0 for some k >= 1. Then its only eigenvalue is 0, m_N = t^{k_0} for the least such k_0, and N^{dim V} = 0.

## Symbols
- `k_0` — the index of nilpotency, = deg m_N, at most dim V

## Epistemic status
definition  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
eigenvalue, linear_operator, minimal_polynomial

## Hypotheses
V finite-dimensional

## Proof provenance
technique: if Nv = lambda v with v != 0 then 0 = N^k v = lambda^k v forces lambda = 0; then p_N = t^n and Cayley-Hamilton gives N^n = 0
derives_from: minimal_polynomial
lean_status: cited

## Type / well-formedness check
Well-formed. The bound k_0 <= dim V follows from Cayley-Hamilton (p_N = t^n) and is sharp for a single Jordan block.

## Specialization / boundary cases
- N = 0: nilpotent with k_0 = 1
- the strictly upper triangular shift on F^n: k_0 = n, the extreme case
- N = J - I for the Jordan block J: nilpotent of index 2

## Hypothesis-dropped counterexamples
- **nilpotence_versus_zero_spectrum**: over a NON-algebraically-closed field an operator can have empty spectrum without being nilpotent -- the real rotation has no real eigenvalue and is invertible, hence not nilpotent. 'Only eigenvalue 0' characterises nilpotence only when p splits
- **finite_dimensionality**: on F[t] the differentiation operator is locally nilpotent (every element is killed by some power) but no single power annihilates everything

## Common misuse
- concluding nilpotence from 'all eigenvalues are 0' over R without checking that p splits
- assuming a nilpotent matrix is 0: it is 0 only if k_0 = 1

## Related nodes (non-prerequisite)
- required_by: generalised_eigenspace, primary_decomposition, jordan_normal_form

## Sources
axler_lada_4e, hoffman_kunze_2e
