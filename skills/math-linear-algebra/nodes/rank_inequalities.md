# rank_inequalities

## Type
theorem

## Statement
rank(AB) <= min(rank A, rank B); rank(A + B) <= rank A + rank B; and Sylvester's inequality rank(AB) >= rank A + rank B - n for A in F^{m x n}, B in F^{n x p}.

## Symbols
- `n` — the INNER dimension of the product, the one Sylvester's bound uses

## Epistemic status
proved_theorem  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
column_space, matrix_multiplication, matrix_rank, rank_nullity

## Hypotheses
shapes conformable

## Proof provenance
technique: col(AB) subset col(A) gives one half, row(AB) subset row(B) the other; subadditivity because col(A+B) subset col(A) + col(B); Sylvester by applying rank_nullity to B restricted to null(AB)
derives_from: rank_nullity
lean_status: core — LinAlg.rank_bounds_consistent

## Type / well-formedness check
Well-formed; note Sylvester's lower bound involves the inner dimension n, not m or p, and can be negative (in which case it is vacuous).

## Specialization / boundary cases
- B invertible: rank(AB) = rank A -- multiplying by an invertible matrix never changes rank, the fact behind similarity invariance
- A = B = I_n: Sylvester gives n >= n + n - n, tight
- A, B nonzero with AB = 0 (the pair from matrix_mult_noncommutative squared): rank(AB) = 0 while both factors have rank 1, and Sylvester gives 0 >= 1 + 1 - 2 = 0, again tight

## Hypothesis-dropped counterexamples
- **upper_bound_is_not_equality**: rank(AB) < min(rank A, rank B) happens whenever col(B) meets null(A) nontrivially: A = [[1,0],[0,0]], B = [[0,0],[0,1]] both have rank 1 and AB = 0
- **conformability**: otherwise ill-typed

## Common misuse
- assuming rank(AB) = rank(A) when B is merely square -- it needs B INVERTIBLE
- assuming rank(A+B) >= |rank A - rank B| as an equality

## In the wild
- the low-rank bottleneck in factored models: a product of thin matrices cannot have rank above the inner dimension, which is exactly what low-rank adaptation and latent-factor models exploit

## Sources
horn_johnson_2e
