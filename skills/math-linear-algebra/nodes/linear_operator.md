# linear_operator

## Type
definition

## Statement
A linear operator on V is a linear map T: V -> V. L(V) is an associative unital algebra under composition, with identity I.

## Symbols
- `I` — the identity operator, type: element of L(V)
- `T^k` — the k-fold composite, with T^0 := I

## Epistemic status
definition  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
composition_of_linear_maps, linear_map

## Hypotheses
(none — unconditional within scope)
## Type / well-formedness check
Well-formed. Same domain and codomain is what makes powers T^k, hence polynomials in T, meaningful -- the whole of eigentheory depends on it.

## Specialization / boundary cases
- V = F^n: L(V) is isomorphic to the algebra F^{n x n}
- p(T) for p in F[t] is defined because T^k makes sense -- the map p -> p(T) is the algebra homomorphism whose kernel defines minimal_polynomial

## Hypothesis-dropped counterexamples
- **equal_domain_and_codomain**: for T: V -> W with V != W, T^2 is undefined, so eigenvalues, characteristic polynomials, and diagonalisability are all meaningless. This is why SVD (which handles rectangular A) needs two different bases

## Common misuse
- applying eigenvalue language to a non-square matrix -- use singular_values instead

## Related nodes (non-prerequisite)
- required_by: eigenvalue, invertible_operator, minimal_polynomial

## Sources
axler_lada_4e
