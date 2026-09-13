# generalised_eigenspace

## Type
definition

## Statement
G_lambda = ker((T - lambda I)^{dim V}). It is T-invariant, contains E_lambda, and dim G_lambda = alg(lambda) -- the ALGEBRAIC multiplicity, unlike E_lambda which realises the geometric one.

## Symbols
- `G_lambda` — type: T-invariant subspace of V

## Epistemic status
definition  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
algebraic_geometric_multiplicity, eigenspace, kernel, nilpotent_operator

## Hypotheses
V finite-dimensional

## Proof provenance
technique: the kernel chain stabilises because dimensions cannot increase indefinitely; the dimension count dim G_lambda = alg(lambda) follows from the block triangular form in a basis adapted to the chain
derives_from: algebraic_geometric_multiplicity
lean_status: cited

## Type / well-formedness check
Well-formed. The exponent dim V is a safe uniform choice: the kernels ker((T - lambda I)^k) increase and stabilise by k = dim V at the latest, so no smaller universal exponent works and no larger one helps.

## Specialization / boundary cases
- T diagonalisable: G_lambda = E_lambda for every lambda -- the two multiplicities agree
- J = [[1,1],[0,1]]: E_1 is one-dimensional but G_1 = F^2, of dimension 2 = alg(1)
- (T - lambda I) restricted to G_lambda is NILPOTENT, which is the content primary_decomposition exploits

## Hypothesis-dropped counterexamples
- **the_exponent**: using exponent 1 gives E_lambda, which is too small; the whole point is to take a high enough power to capture the full algebraic multiplicity
- **finite_dimensionality**: the chain need not stabilise otherwise

## Common misuse
- confusing G_lambda with E_lambda when quoting multiplicities

## Related nodes (non-prerequisite)
- required_by: primary_decomposition

## Sources
axler_lada_4e
