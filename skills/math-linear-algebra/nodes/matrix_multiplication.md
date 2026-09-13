# matrix_multiplication

## Type
definition

## Statement
For A in F^{m x n} and B in F^{n x p}, (AB)_{ij} = sum_{k=1}^n A_{ik} B_{kj}, giving AB in F^{m x p}. Defined only when the INNER shapes agree.

## Symbols
- `k` — the summation index, ranging over the shared inner dimension

## Epistemic status
definition  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
index_convention, matrix

## Hypotheses
inner shapes conformable
## Type / well-formedness check
Well-formed exactly when the inner dimensions match. The rule looks arbitrary as a formula and is forced as soon as one asks that it represent composition -- see matrix_mult_is_composition.

## Specialization / boundary cases
- B a column vector: Ab is the combination of the columns of A with coefficients b, the reading that drives column_space
- A a row vector and B a column: a 1x1 product, the scalar a^T b
- A = I: IB = B

## Hypothesis-dropped counterexamples
- **conformability**: ill-typed otherwise
- **commutativity_is_absent**: see matrix_mult_noncommutative

## Common misuse
- cancelling a common factor: AB = AC does not give B = C unless A is injective (has a left inverse)
- assuming (AB)^k = A^k B^k, which needs AB = BA

## In the wild
- the composition of linear layers in a neural network; the transition-matrix product in a Markov chain; the design-matrix products X^T X and X^T y in least squares

## Related nodes (non-prerequisite)
- required_by: matrix_mult_is_composition, invertible_matrix, trace_cyclic

## Sources
hoffman_kunze_2e, strang_5e
