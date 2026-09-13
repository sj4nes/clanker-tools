# The independence trap, and the routes that avoid it

## The trap

```matlab
[Q, D] = eig(A);
assert(norm(Q*D*Q' - A) < 1e-12);      % passes at 3e-15
```

This is not a check of anything you wrote. `eig` produced `Q` and `D`; matrix
multiplication reassembled them. Both are LAPACK. **No error in the source
being verified could make this fail**, because the source never entered the
computation.

The same shape appears whenever a single built-in both produces and validates
the answer:

| looks like a check | actually tests |
|---|---|
| `[Q,D]=eig(A); assert(Q*D*Q',A)` | LAPACK's `eig` against LAPACK's `*` |
| `[U,S,V]=svd(A); assert(U*S*V',A)` | LAPACK's `svd` against LAPACK's `*` |
| `L=chol(A); assert(L'*L,A)` | LAPACK's `chol` against LAPACK's `*` |
| `x=A\b; assert(A*x,b)` | the solver's own residual (see tolerance ref: this is a *backward* check and is genuinely weak) |
| `assert(rank(A), rank(A))` | nothing |

These reconstruction identities are not *worthless* — they would catch a
catastrophically broken install — but they are not evidence about a stated
claim, and must never be the only check.

## The pattern that works

**The source states N things that are equivalent, or one thing computable N
ways. Compute each by its own route. Require agreement.**

The agreement is the evidence: a wrong claim in the source has to survive every
route simultaneously, and the routes share no code path.

```matlab
% math-linear-algebra: psd_characterisations claims FOUR equivalent conditions
r1 = all(eig(A) > 0);                                  % spectral
r2 = all(arrayfun(@(k) det(A(1:k,1:k)) > 0, 1:rows(A)));  % Sylvester's minors
[~, p] = chol(A); r3 = (p == 0);                       % Cholesky existence
r4 = (rank(chol(A)) == columns(A));                    % A = B'B, full col rank
assert(isequal(r1, r2, r3, r4));                       % they must AGREE

% ...and on a matrix that is NOT positive definite, all four must agree in
% the other direction, or the check is one-sided and proves nothing
M = [0 0; 0 -1];
n1 = all(eig(M) > 0);
n2 = (det(M(1,1)) > 0) && (det(M) > 0);
[~, q] = chol(M); n3 = (q == 0);
assert(!(n1 || n2 || n3));
```

## Route catalogue

For each claim type, at least two genuinely different computations.

| claim | route A | route B (independent) |
|---|---|---|
| eigenvalues of a symmetric matrix are real | `isreal(eig(A))` | roots of `poly(A)` have zero imaginary part; or the n=2 discriminant `(a-d)^2 + 4b^2 >= 0` in closed form |
| characteristic polynomial coefficients | `poly(A)` (built from eigenvalues) | `trace(A)` and `det(A)` computed directly; compare to the stated `t^n - tr t^{n-1} + ... + (-1)^n det` |
| Cayley–Hamilton | evaluate `p_A(A)` by Horner from `poly(A)` | must equal the zero matrix — the *matrix* evaluation is the independent step |
| rank | `rank(A)` (SVD-based) | count pivots from `rref(A)`; or `columns(A) - columns(null(A))` |
| rank–nullity | `rank(A)` | `size(null(A), 2)`; assert the sum equals `columns(A)` |
| row rank = column rank | `rank(A)` | `rank(A')` |
| four subspaces orthogonality | `null(A)` | `orth(A')`; assert `norm(null(A)' * orth(A')) ~ 0` |
| determinant | `det(A)` | product of `eig(A)`; or product of `diag(U)` from `[L,U,P]=lu(A)` with the permutation sign |
| positive definiteness | `eig` | leading principal minors; Cholesky success; `x'Ax > 0` on many seeded random `x` |
| Sylvester's law of inertia | signs of `eig(A)` | signs of `eig(P'*A*P)` for a random invertible `P` — must match *as a multiset of signs*, while the eigenvalues themselves must **not** match |
| SVD singular values | `svd(A)` | `sqrt(eig(A'*A))` sorted descending |
| Eckart–Young | `norm(A - A_k, 2)` from the truncated SVD | `s(k+1)` directly |
| least squares | `A\b` | `(A'*A) \ (A'*b)`; and assert the residual is orthogonal to `col(A)`: `norm(A' * (b - A*x)) ~ 0` |
| projection matrix | `H = A*inv(A'*A)*A'` | assert `H^2 = H`, `H' = H`, `trace(H) = rank(A)` — three independent properties |
| condition number | `cond(A)` | `max(svd(A)) / min(svd(A))` |
| matrix norms | `norm(A,2)` | `max(svd(A))`; `norm(A,'fro')` vs `sqrt(trace(A'*A))` vs `sqrt(sum(svd(A).^2))` |

## Verifying a *formula* rather than a property

When the source states a closed form, code the formula **literally as written**
and compare it to the built-in. That is the one case where calling a built-in
*is* the independent route — because the formula, not the built-in, is what is
under test.

```matlab
% the source's stated formula for the hat matrix
H_stated = X * inv(X' * X) * X';
% an independent route to the same projection
[Q, ~] = qr(X, 0);
H_ref = Q * Q';
assert(H_stated, H_ref, -1e-10);
```

If you find yourself unable to name what the two routes are, you do not yet
have a check.

## Degenerate dimensions

At n = 2 most structural claims are vacuous:

- every 2x2 symmetric matrix is diagonalisable;
- rank is 0, 1, or 2, so rank claims have almost no room to fail;
- there is exactly one way to be defective (a single Jordan block);
- "all leading principal minors" is two numbers.

Use **n >= 4** for structural claims, and a **rectangular** case (e.g. 5x3 and
3x5) for anything about rank, SVD, the four subspaces, or least squares.
Include at least one **rank-deficient** case where the claim's hypothesis fails.
