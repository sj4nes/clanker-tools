# best_approximation

## Type
theorem

## Statement
For a finite-dimensional subspace U, P_U v is the UNIQUE closest point of U to v: ||v - P_U v|| < ||v - u|| for every u in U with u != P_U v.

## Symbols
- `P_U v` — the orthogonal projection, here characterised variationally

## Epistemic status
proved_theorem  ·  field_scope: real_or_complex

## Prerequisites (tsort edges into this node)
induced_norm, orthogonal_decomposition, orthogonal_projection, pythagorean_theorem

## Hypotheses
U finite-dimensional

## Proof provenance
technique: write v - u = (v - P_U v) + (P_U v - u) with the two terms orthogonal (the first is in U^perp, the second in U); Pythagoras gives ||v-u||^2 = ||v - P_U v||^2 + ||P_U v - u||^2, strictly larger unless u = P_U v
derives_from: pythagorean_theorem
lean_status: cited

## Type / well-formedness check
Well-formed, with a STRICT inequality -- uniqueness of the minimiser is part of the statement, and it is what makes least squares a well-posed problem.

## Specialization / boundary cases
- U = span(e): the closest point on a line, the elementary projection formula
- U = col(A): the least-squares problem, giving least_squares

## Hypothesis-dropped counterexamples
- **finite_dimensionality_or_closedness_of_U**: for a non-closed subspace the infimum need not be ATTAINED -- there is a nearest-point sequence but no nearest point. The same witness as orthogonal_decomposition (finitely-supported sequences in l^2)
- **the_norm_being_induced**: in a general normed space the nearest point need not be unique: in R^2 with the infinity-norm, the nearest point on a line to an off-line point can be a whole segment. Uniqueness comes from strict convexity of the Euclidean ball, i.e. from the inner product

## Common misuse
- assuming a unique best approximation in an L^1 or L^infinity sense -- that is a different (and generally non-unique) problem

## In the wild
- least squares in every form: regression, curve fitting, Fourier truncation (the partial sum is the best L^2 approximation), and conditional expectation

## Related nodes (non-prerequisite)
- required_by: least_squares

## Sources
axler_lada_4e
