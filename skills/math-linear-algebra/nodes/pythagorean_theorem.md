# pythagorean_theorem

## Type
proposition

## Statement
If u perp v then ||u+v||^2 = ||u||^2 + ||v||^2. Over R the converse holds; over C the converse gives only Re<u,v> = 0.

## Symbols
- `Re<u,v>` — the real part

## Epistemic status
proposition  ·  field_scope: real_or_complex

## Prerequisites (tsort edges into this node)
induced_norm, orthogonality

## Hypotheses
u perp v for the forward direction

## Proof provenance
technique: expand <u+v, u+v> using linearity and conjugate-symmetry; the cross terms sum to 2 Re<u,v>
derives_from: induced_norm
lean_status: dim_core — LinAlg.pythagoras (n = 2)

## Type / well-formedness check
Well-formed. The asymmetry between R and C is genuine: expanding gives ||u+v||^2 = ||u||^2 + 2Re<u,v> + ||v||^2, and only the REAL PART appears.

## Specialization / boundary cases
- extends by induction to any finite orthogonal family: ||sum v_i||^2 = sum ||v_i||^2
- with u = P_U v and v - P_U v, it gives ||v||^2 = ||P_U v||^2 + ||v - P_U v||^2 -- the decomposition behind best_approximation and behind the ANOVA sum-of-squares identity

## Hypothesis-dropped counterexamples
- **the_complex_converse**: in C^1 take u = 1 and v = i: <u,v> = conj(i) = -i, so Re<u,v> = 0 and ||u+v||^2 = |1+i|^2 = 2 = 1 + 1. Pythagoras holds, yet <u,v> != 0 so the vectors are NOT orthogonal

## Common misuse
- inferring orthogonality from the Pythagorean identity over C

## Related nodes (non-prerequisite)
- required_by: bessel_inequality, best_approximation

## Sources
axler_lada_4e
