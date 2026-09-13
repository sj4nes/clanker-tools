# simultaneous_diagonalisation

## Type
theorem

## Statement
Two real symmetric matrices A, B with B POSITIVE DEFINITE are simultaneously diagonalisable by CONGRUENCE: some invertible P gives P^TBP = I and P^TAP diagonal. Separately, two NORMAL matrices are simultaneously UNITARILY diagonalisable if and only if they COMMUTE.

## Symbols
- `P` — invertible (congruence case) or unitary (commuting case)

## Epistemic status
proved_theorem  ·  field_scope: real_or_complex

## Prerequisites (tsort edges into this node)
cholesky_factorisation, congruence, diagonalisability_criterion, positive_definite, spectral_theorem_normal, spectral_theorem_symmetric

## Hypotheses
A, B symmetric with B positive definite; OR A, B normal and commuting

## Proof provenance
technique: congruence case: take the Cholesky factor B = LL^T, set C = L^{-1}AL^{-T} which is symmetric, diagonalise it orthogonally as C = QDQ^T, and put P = L^{-T}Q. Commuting case: each eigenspace of A is B-invariant, so diagonalise B within each
derives_from: cholesky_factorisation
lean_status: cited

## Type / well-formedness check
Well-formed. TWO distinct theorems sharing a name, with different hypotheses and different transformation laws -- congruence in the first, unitary similarity in the second. Conflating them is the standard confusion.

## Specialization / boundary cases
- B = I: the congruence case reduces to the ordinary spectral theorem
- A, B commuting Hermitian: BOTH theorems apply and give the same answer
- the generalised eigenproblem Ax = lambda Bx is exactly the congruence case, and its solutions are the diagonal entries

## Hypothesis-dropped counterexamples
- **positive_definiteness_of_B**: A = [[0,1],[1,0]] and B = [[1,0],[0,-1]] are both symmetric with B indefinite, and no congruence diagonalises both. Definiteness of ONE of the pair is essential
- **commutativity_in_the_normal_case**: the two Pauli-like matrices [[0,1],[1,0]] and [[1,0],[0,-1]] are Hermitian and do NOT commute; no single unitary diagonalises both. This is the linear-algebra core of the uncertainty principle
- **congruence_is_not_similarity**: the first theorem's P is not orthogonal, so the diagonal entries of P^TAP are NOT the eigenvalues of A -- they are the generalised eigenvalues of (A,B)

## Common misuse
- reading the diagonal of P^TAP as eigenvalues of A in the congruence case
- assuming any two symmetric matrices can be simultaneously diagonalised

## In the wild
- the generalised eigenproblem of structural vibration (stiffness and mass matrices, with mass positive definite); linear discriminant analysis (between- and within-class scatter)
- whitening followed by PCA is exactly this construction

## Sources
horn_johnson_2e, golub_van_loan_4e
