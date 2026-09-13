# orthogonal_implies_independent

## Type
proposition

## Statement
An orthogonal set of NONZERO vectors is linearly independent. Hence any orthonormal set has at most dim V elements.

## Symbols
- `(v_i)` — an orthogonal family

## Epistemic status
proposition  ·  field_scope: real_or_complex

## Prerequisites (tsort edges into this node)
induced_norm, linear_independence, orthogonality

## Hypotheses
pairwise orthogonal, all vectors nonzero

## Proof provenance
technique: take <., v_j> of a vanishing combination: every term but the j-th dies, leaving a_j ||v_j||^2 = 0, and ||v_j|| != 0 forces a_j = 0
derives_from: linear_independence
lean_status: core — LinAlg.orthogonal_indep_core

## Type / well-formedness check
Well-formed. The nonzero hypothesis is indispensable: 0 is orthogonal to everything.

## Specialization / boundary cases
- an orthonormal set: automatically nonzero, hence independent
- n orthonormal vectors in an n-dimensional space therefore form a BASIS with no further argument

## Hypothesis-dropped counterexamples
- **nonzeroness**: {0, e_1} is orthogonal and dependent
- **positive_definiteness**: the proof divides by ||v_j||^2; over a degenerate form a self-orthogonal nonzero vector makes this step fail, and over F_2 the set {(1,1)} is 'orthogonal' to itself

## Common misuse
- asserting independence of an orthogonal set that contains 0

## Related nodes (non-prerequisite)
- required_by: orthonormal_basis

## Sources
axler_lada_4e
