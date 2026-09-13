# Notation — math-linear-algebra Release 0.1

Every symbol used in `results/*.yaml`, with one meaning, one type, one scope.
Convention-sensitive entries link to their `notation_convention` node.

## Scalars and fields

| symbol | meaning | type |
|---|---|---|
| `F` | an arbitrary field | field |
| `R`, `C` | the real and complex fields | field (cited) |
| `F_p`, `F_2` | the finite field with p (resp. 2) elements | field |
| `a, b, c` | scalars | elements of `F` |
| `char F` | the characteristic: least `n > 0` with `n*1 = 0`, else 0 | 0 or a prime |
| `conj(a)`, `a-bar` | complex conjugation | field automorphism of `C` |
| `\|a\|` | modulus of a scalar | nonnegative real |
| `F[t]` | polynomials in one indeterminate over `F` | commutative ring (a PID) |
| `delta_{ij}` | the Kronecker delta: 1 if `i = j`, else 0 | element of `F` |

## Spaces and vectors

| symbol | meaning | type |
|---|---|---|
| `V, W, X` | vector spaces over `F` | vector space |
| `U` | usually a subspace of `V` | subspace |
| `u, v, w` | vectors | elements of `V` |
| `0` | overloaded: zero scalar, zero vector, zero matrix | resolved by position; every node's `symbols` block types it |
| `F^n` | column vectors of length `n` | vector space of dimension `n` |
| `e_i` | the `i`-th standard basis column | element of `F^n` |
| `span(S)` | finite linear combinations of `S`; `span(empty) = {0}` | subspace |
| `dim V`, `dim_F V` | dimension over `F` | natural number (or cardinal) |
| `U + W`, `U (+) W` | sum, direct sum | subspace |
| `U ∩ W` | intersection | subspace |
| `V/U` | quotient space | vector space of cosets |
| `V^*`, `V^**` | dual, double dual | vector space |
| `U^0` | annihilator of `U`, inside `V^*` | subspace of `V^*` |
| `U^perp` | orthogonal complement of `U`, inside `V` | subspace of `V` |

`U^0` and `U^perp` are **different objects in different spaces**: the
annihilator needs no inner product and lives in the dual; the orthogonal
complement needs one and lives in `V`. See `annihilator`.

## Maps

| symbol | meaning | type |
|---|---|---|
| `T, S` | linear maps | elements of `L(V,W)` |
| `L(V,W)`, `L(V)` | the space of linear maps; operators on `V` | vector space; unital algebra |
| `I` | the identity operator or matrix | element of `L(V)` / `F^{n x n}` |
| `ker T`, `im T` | kernel (in `V`), image (in `W`) | subspaces |
| `rank T`, `nullity T` | `dim(im T)`, `dim(ker T)` | natural numbers |
| `T^t` | the DUAL map `W^* -> V^*`, no inner product | linear map |
| `T^*` | the ADJOINT `W -> V`, needs an inner product, conjugates over `C` | linear map |
| `T\|_U` | restriction to an invariant subspace | element of `L(U)` |
| `p(T)` | a polynomial evaluated at an operator | element of `L(V)` |
| `[v]_B` | coordinates of `v` in the ordered basis `B` | element of `F^n` |
| `[T]_{C<-B}` | matrix of `T` from basis `B` to basis `C` | element of `F^{m x n}` |

`T^t` and `T^*` are distinguished deliberately (`dual_map` vs
`adjoint_operator`); they agree over `R` under the Riesz identification only.

## Matrices — see `index_convention`, `transpose_convention`

| symbol | meaning | type |
|---|---|---|
| `A in F^{m x n}` | `m` rows, `n` columns | matrix |
| `A_{ij}` | entry in row `i`, column `j`; **indices from 1** | element of `F` |
| `A_{i.}`, `A_{.j}` | the `i`-th row, the `j`-th column | element of `F^n` / `F^m` |
| `A^T` | transpose, `(A^T)_{ij} = A_{ji}` | element of `F^{n x m}` |
| `A^*` | conjugate transpose, `(A^*)_{ij} = conj(A_{ji})` | element of `C^{n x m}` |
| `A^{-1}`, `A^+` | inverse; Moore–Penrose pseudoinverse | matrix |
| `adj(A)` | the ADJUGATE (transposed cofactor matrix) — unrelated to `A^*` | element of `F^{n x n}` |
| `I_n` | identity of size `n` | element of `F^{n x n}` |
| `E_{ij}` | the matrix unit | element of `F^{m x n}` |
| `tr(A)`, `det A` | trace, determinant | elements of `F` |
| `M_{ij}`, `C_{ij}` | the `(i,j)` minor; the cofactor `(-1)^{i+j} M_{ij}` | elements of `F` |
| `row(A)`, `col(A)`, `null(A)` | row space, column space, null space | subspaces |
| `rank A` | `dim col(A) = dim row(A)` | natural number |
| `rref(A)` | the unique reduced row echelon form | matrix |
| `~_r`, `~`, `~_c` | row equivalence; similarity; congruence | equivalence relations |
| `M/A` | Schur complement `D - CA^{-1}B` | matrix |

`adj(A)` (adjugate) and `A^*` (adjoint) are unrelated despite the shared name
"adjoint" in older texts. This capsule always writes `adj` for the former.

## Inner products, norms — see `inner_product_convention`

| symbol | meaning | type |
|---|---|---|
| `<u,v>` | inner product, **linear in the FIRST slot** | element of `F` |
| `\|\|v\|\|` | induced norm `sqrt(<v,v>)` | nonnegative real |
| `u perp v` | `<u,v> = 0` | relation |
| `P_U` | orthogonal projection onto `U` | element of `L(V)` |
| `H`, `M = I - H` | hat matrix; residual maker | matrices |
| `\|\|A\|\|_2`, `\|\|A\|\|_F` | spectral (operator) norm; Frobenius norm | nonnegative reals |
| `kappa_2(A)` | condition number `sigma_1/sigma_n` | real `>= 1` |

## Spectral

| symbol | meaning | type |
|---|---|---|
| `lambda`, `mu` | eigenvalues | elements of `F` |
| `E_lambda`, `G_lambda` | eigenspace; generalised eigenspace | subspaces |
| `alg(lambda)`, `geom(lambda)` | algebraic, geometric multiplicity | positive integers |
| `p_A(t)` | characteristic polynomial `det(tI - A)`, **monic** | element of `F[t]` |
| `m_T` | minimal polynomial, **monic** | element of `F[t]` |
| `rho(A)` | spectral radius `max \|lambda_i\|` | nonnegative real |
| `R_A(x)` | Rayleigh quotient `<Ax,x>/<x,x>` | real (for self-adjoint `A`) |
| `sigma_1 >= ... >= sigma_p` | singular values | nonnegative reals |
| `U Sigma V^*` | the SVD | matrices |
| `A > 0`, `A >= 0` | positive definite, positive semidefinite (Loewner) | relation on symmetric matrices |
| `(n_+, n_-, n_0)` | inertia | triple of natural numbers |
| `J_k(lambda)` | the `k x k` Jordan block | matrix |
| `S_n`, `sgn(sigma)` | symmetric group; sign homomorphism | group; `{+1,-1}` |

## Deliberate omissions

- No `\|A\|` without a subscript: the matrix norm is always named, because
  `condition_number` and `spectral_radius` depend on which one is meant.
- No `A >= B` entrywise: `>=` on matrices is always the **Loewner** (PSD)
  ordering in this capsule.
- No `x . y` dot-product notation: written `<x,y>` or `y^* x` throughout, so the
  conjugation convention stays visible.
