# cauchy_schwarz

## Type
theorem

## Statement
|<u,v>| <= ||u|| ||v||, with EQUALITY if and only if u and v are linearly dependent.

## Symbols
- `|<u,v>|` — the modulus of the inner product

## Epistemic status
proved_theorem  ·  field_scope: real_or_complex

## Prerequisites (tsort edges into this node)
induced_norm, inner_product, inner_product_space

## Hypotheses
<.,.> an inner product (positive definite)

## Proof provenance
technique: for v != 0, expand 0 <= ||u - (<u,v>/||v||^2) v||^2 -- i.e. the squared norm of u minus its projection onto v -- and rearrange. Equality holds iff that vector is 0, i.e. u is a multiple of v
derives_from: induced_norm
lean_status: dim_core — LinAlg.lagrange_identity2/3 and LinAlg.cauchy_schwarz2/3 (Int coefficients, n = 2 and 3; the defect is exhibited as a sum of squares). The REAL-coefficient statement is cited

## Type / well-formedness check
Well-formed. The equality clause is part of the theorem, not an afterthought: it is what makes Cauchy-Schwarz a rigidity statement and what gives the correlation bound its interpretation.

## Specialization / boundary cases
- u = v: equality, both sides ||v||^2
- v = 0: both sides 0, equality with the pair trivially dependent
- F^n standard: (sum |x_i y_i|)^2 <= (sum |x_i|^2)(sum |y_i|^2), the classical inequality
- random variables with <X,Y> = E[XY]: |E[XY]| <= sqrt(E[X^2]E[Y^2]), hence |corr| <= 1

## Hypothesis-dropped counterexamples
- **positive_definiteness**: for the Minkowski form on R^2 the inequality REVERSES on timelike vectors -- the reverse Cauchy-Schwarz inequality of special relativity. So it is definiteness, not bilinearity, that gives the direction
- **the_proof_needs_only_nonnegativity**: positive SEMI-definiteness suffices for the inequality; strict definiteness is needed only for the equality clause

## Common misuse
- stating it as <u,v> <= ||u|| ||v|| without the modulus (false when the inner product is negative)
- using it in a normed space with no inner product

## In the wild
- the correlation coefficient bound |corr(X,Y)| <= 1 and its equality case (perfect linear dependence) -- the inequality statistics rests on
- the Cramer-Rao bound in math-statistics is Cauchy-Schwarz applied to the score and the estimator

## Related nodes (non-prerequisite)
- required_by: triangle_inequality, isometry_characterisation

## Sources
axler_lada_4e, steele_cauchy_schwarz
