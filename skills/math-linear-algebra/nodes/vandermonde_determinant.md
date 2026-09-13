# vandermonde_determinant

## Type
identity

## Statement
The Vandermonde matrix V with V_{ij} = x_i^{j-1} has det V = prod_{1 <= i < j <= n} (x_j - x_i). It is nonzero exactly when the x_i are pairwise DISTINCT.

## Symbols
- `x_1,...,x_n` — the nodes, type: elements of F
- `V` — type: element of F^{n x n}

## Epistemic status
mathematical_identity  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
determinant, determinant_row_operations, leibniz_formula

## Hypotheses
A square Vandermonde matrix

## Proof provenance
technique: subtract x_1 times each column from the next (an R3-type column operation, which preserves det), factor (x_i - x_1) out of each row, and induct on n
derives_from: determinant_row_operations
lean_status: cited

## Type / well-formedness check
Well-formed over any field. The product has C(n,2) factors.

## Specialization / boundary cases
- n = 2: det[[1,x_1],[1,x_2]] = x_2 - x_1
- n = 3 at x = (1,2,3): det = (2-1)(3-1)(3-2) = 2
- two equal nodes: a repeated row, so det = 0 -- consistent with the product having a zero factor

## Hypothesis-dropped counterexamples
- **distinctness_of_the_nodes**: with a repeated node the matrix is singular, which is exactly the statement that polynomial interpolation at repeated points is not uniquely solvable (one needs derivative data -- Hermite interpolation)

## Common misuse
- using the Vandermonde system to fit a high-degree polynomial numerically: it is notoriously ill-conditioned, with condition number growing exponentially in n. Use orthogonal polynomials or a QR-based fit instead (condition_number, qr_factorisation)

## In the wild
- existence and uniqueness of the Lagrange interpolating polynomial through n distinct points
- the design matrix of polynomial regression is a Vandermonde matrix -- and its ill-conditioning is why centring and orthogonal polynomial bases are standard practice

## Sources
horn_johnson_2e
