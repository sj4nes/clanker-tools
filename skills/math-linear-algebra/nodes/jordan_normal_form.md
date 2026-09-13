# jordan_normal_form

## Type
theorem

## Statement
Over an algebraically closed field, every operator has a basis in which its matrix is block diagonal with Jordan blocks J_k(lambda) (lambda on the diagonal, 1s on the superdiagonal), unique up to the ORDER of the blocks. STATED, NOT PROVED in Release 0.1 -- the cyclic-subspace construction of a basis for a nilpotent operator is deferred to 0.2.

## Symbols
- `J_k(lambda)` — the k x k Jordan block
- `r` — the number of blocks, = sum of the geometric multiplicities

## Epistemic status
proved_theorem  ·  field_scope: algebraically_closed

## Prerequisites (tsort edges into this node)
algebraically_closed_field, nilpotent_operator, primary_decomposition

## Hypotheses
F algebraically closed, V finite-dimensional

## Proof provenance
technique: primary_decomposition reduces to the nilpotent case; the remaining step -- decomposing a nilpotent operator into cyclic subspaces -- is NOT carried out here. Cited
derives_from: primary_decomposition
lean_status: stated_not_proved

## Type / well-formedness check
Well-formed. The block multiset is a COMPLETE similarity invariant, which is the sense in which Jordan form solves the classification problem that characteristic and minimal polynomials only partially solve.

## Specialization / boundary cases
- all blocks 1x1: the diagonalisable case
- one block of size n: the cyclic (non-derogatory) case, where m_T = p_T
- the number of blocks for lambda is geom(lambda); their sizes sum to alg(lambda)

## Hypothesis-dropped counterexamples
- **algebraic_closedness**: no Jordan form over R for the rotation matrix; the real analogue uses 2x2 rotation blocks
- **numerical_instability**: the Jordan form is DISCONTINUOUS in the entries: an arbitrarily small perturbation of a Jordan block has distinct eigenvalues and is diagonalisable. It is therefore never computed numerically -- Schur form is used instead

## Common misuse
- computing a Jordan form in floating point
- treating the block ORDER as meaningful: only the multiset is an invariant

## Related nodes (non-prerequisite)
- generalizes: primary_decomposition

## Sources
horn_johnson_2e, hoffman_kunze_2e
