# eigenspace

## Type
definition

## Statement
E_lambda = ker(T - lambda I) = {v : Tv = lambda v}, a subspace of V consisting of 0 together with all eigenvectors for lambda. It is T-invariant.

## Symbols
- `E_lambda` — type: subspace of V
- `dim E_lambda` — the GEOMETRIC multiplicity of lambda

## Epistemic status
definition  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
eigenvalue, kernel, subspace

## Hypotheses
lambda in F

## Proof provenance
technique: kernel of the linear map T - lambda I; invariance because T commutes with T - lambda I
derives_from: kernel
lean_status: cited

## Type / well-formedness check
Well-formed as a kernel, hence a subspace. Including 0 is what makes it a subspace -- the set of eigenvectors alone is not.

## Specialization / boundary cases
- lambda not an eigenvalue: E_lambda = {0}, dimension 0
- T = lambda I: E_lambda = V

## Hypothesis-dropped counterexamples
- **including_zero**: the eigenvectors alone do not form a subspace (they miss 0), which is why every statement about 'the space of eigenvectors' must mean E_lambda
- **distinct_lambdas**: E_lambda ∩ E_mu = {0} for lambda != mu, since a nonzero common element would give lambda v = mu v

## Common misuse
- adding eigenvectors for DIFFERENT eigenvalues and expecting an eigenvector: the sum is generally not one, which is exactly distinct_eigenvalues_independent

## Related nodes (non-prerequisite)
- required_by: algebraic_geometric_multiplicity, diagonalisability_criterion, generalised_eigenspace

## Sources
axler_lada_4e
