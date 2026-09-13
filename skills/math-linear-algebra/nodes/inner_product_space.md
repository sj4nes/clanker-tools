# inner_product_space

## Type
structure

## Statement
A vector space over R or C together with a chosen inner product. Finite-dimensional real ones are Euclidean spaces; complete infinite-dimensional ones are Hilbert spaces (OUT OF SCOPE).

## Symbols
- `(V, <.,.>)` — the structure; the inner product is DATA, not intrinsic to V

## Epistemic status
definition  ·  field_scope: real_or_complex

## Prerequisites (tsort edges into this node)
inner_product, vector_space

## Hypotheses
F = R or C
## Type / well-formedness check
Well-formed. The inner product is extra structure: the same V carries many, and results about 'the' orthogonal complement or 'the' adjoint are relative to the chosen one.

## Specialization / boundary cases
- R^n with the dot product: Euclidean n-space
- C^n with y^*x: unitary space
- F^{m x n} with <A,B> = tr(B^*A): the Frobenius inner product, which is what matrix_norms uses

## Hypothesis-dropped counterexamples
- **completeness_is_NOT_assumed**: finite-dimensional inner product spaces are automatically complete; infinite-dimensional ones need not be, and every theorem here that uses orthogonal_decomposition fails for a non-closed subspace of an incomplete space. That is the Hilbert-space boundary this capsule does not cross

## Common misuse
- treating orthogonality as intrinsic to V: it depends entirely on the chosen inner product, and a change of inner product is a change of geometry

## Related nodes (non-prerequisite)
- required_by: cauchy_schwarz, orthogonality

## Sources
axler_lada_4e
