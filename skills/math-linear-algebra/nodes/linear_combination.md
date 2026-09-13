# linear_combination

## Type
definition

## Statement
A linear combination of a family (v_i)_{i in I} is a finite sum sum_{i in J} a_i v_i with J a FINITE subset of I and a_i in F.

## Symbols
- `J` — a finite index subset, type: finite subset of I
- `a_i` — coefficients, type: elements of F

## Epistemic status
definition  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
indexed_family, vector_space

## Hypotheses
J finite
## Type / well-formedness check
Well-formed. FINITENESS of J is essential and is not a technicality: a vector space has no topology, so an infinite sum has no meaning. This is what keeps span, independence, and basis purely algebraic.

## Specialization / boundary cases
- J empty: the empty sum is 0 by convention, which is why span(empty) = {0}
- |J| = 1: the combinations of a single v are the scalar multiples of v

## Hypothesis-dropped counterexamples
- **finiteness**: allowing infinite sums requires convergence, hence a topology and completeness -- that is Hilbert space theory, not linear algebra. Under the algebraic definition, the standard basis of the space of ALL sequences does NOT span it: (1,1,1,...) is not a finite combination of the e_i. This single point is why a Hamel basis of an infinite-dimensional space is enormous and unusable

## Common misuse
- writing 'v = sum_{i=1}^infinity a_i e_i' inside a vector-space argument -- that is a limit statement and needs a norm

## Related nodes (non-prerequisite)
- required_by: span, linear_independence

## Sources
axler_lada_4e, hoffman_kunze_2e
