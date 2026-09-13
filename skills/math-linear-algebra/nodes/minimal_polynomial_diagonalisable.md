# minimal_polynomial_diagonalisable

## Type
theorem

## Statement
T is diagonalisable if and only if m_T splits over F into DISTINCT linear factors (i.e. m_T is squarefree and splits).

## Symbols
- `k` — the number of DISTINCT eigenvalues, equal to deg m_T here

## Epistemic status
proved_theorem  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
cayley_hamilton, diagonalisability_criterion, direct_sum, minimal_polynomial

## Hypotheses
V finite-dimensional

## Proof provenance
technique: if diagonalisable, prod(T - lambda_i I) kills every basis eigenvector so annihilates T, and no proper divisor does. Conversely if m_T = prod(t - lambda_i) with distinct roots, the polynomials prod_{j != i}(t - lambda_j)/prod_{j != i}(lambda_i - lambda_j) give a partition of unity, whose images are projections onto the eigenspaces summing to I
derives_from: diagonalisability_criterion
lean_status: cited

## Type / well-formedness check
Well-formed. The criterion is often the most practical one because m_T is smaller than p_T and squarefreeness is checkable by gcd(m, m') without factoring.

## Specialization / boundary cases
- T a projection: T^2 = T so m_T divides t^2 - t = t(t-1), squarefree -- every projection is diagonalisable
- T an involution with char F != 2: m_T divides t^2 - 1 = (t-1)(t+1), squarefree -- diagonalisable
- J = [[1,1],[0,1]]: m_J = (t-1)^2, not squarefree -- not diagonalisable

## Hypothesis-dropped counterexamples
- **squarefreeness**: the Jordan block above
- **splitting**: the real rotation has m_T = t^2 + 1, squarefree but not split over R -- not diagonalisable over R, diagonalisable over C
- **characteristic_two**: an involution over F_2 has m_T dividing t^2 - 1 = (t-1)^2, which is NOT squarefree there. Indeed [[1,1],[0,1]] over F_2 is an involution and is not diagonalisable -- the char_not_2 subtlety is real

## Common misuse
- checking p_T for repeated roots instead of m_T: I_n has p = (t-1)^n with repeated roots yet is diagonal

## Related nodes (non-prerequisite)
- equivalent_to: diagonalisability_criterion

## Sources
hoffman_kunze_2e
