# Deriving tolerances; residual vs forward error

A guessed tolerance is a defect. It fails in both directions: too tight and a
correct computation reports failure; too loose and a genuinely wrong result
passes. For matrices the right value is **derived from the matrix**, and the
derivation differs depending on what is being asserted.

## The two quantities, which are not interchangeable

Measured on Hilbert matrices (`hilb(n)`), which are deliberately
ill-conditioned:

```
hilb( 4): cond = 1.55e+04 | residual = 2.54e-15 | solution error = 2.57e-13
hilb( 8): cond = 1.53e+10 | residual = 1.73e-12 | solution error = 3.84e-08
hilb(12): cond = 1.61e+16 | residual = 1.92e-09 | solution error = 1.98e-02
```

A fixed `tol = 1e-10` would have:

- passed the residual at n = 8 while the solution was wrong in the 8th digit;
- passed the residual at n = 4 and 8 but failed it at n = 12;
- failed the solution at n = 8 and 12 *for a correct, backward-stable solver*.

**A small residual never certifies an accurate solution.** `A\b` is backward
stable: it returns the exact solution of a *nearby* problem. How far that is
from the exact solution of *your* problem is governed by conditioning.

## The two rules

```matlab
% BACKWARD / residual: is this the exact answer to a nearby problem?
tol_resid = @(A) 20 * rows(A) * eps * norm(A, 2);

% FORWARD / solution: how far is it from the true answer?
tol_forward = @(A) 20 * cond(A) * eps;
```

The constant (10–100) absorbs the implementation's growth factor; `rows(A)`
absorbs accumulation over the elimination; `eps` is 2.22e-16. Verified: the
forward bound held at every Hilbert size tested, including n = 12 where the
predicted error was 3.58 and the actual was 1.98e-2.

## Which to use

| asserting | tolerance |
|---|---|
| a factorisation reassembles (`QDQ'`, `USV'`, `L'L`) | residual |
| an identity between expressions in the same matrices | residual |
| a computed solution matches a known exact solution | **forward** |
| eigenvalues of a **symmetric** matrix match known values | residual — symmetric eigenvalues are perfectly conditioned (Weyl) |
| eigenvalues of a **non-symmetric** matrix | see "uncheckable" below |
| singular values | residual — always well conditioned |
| a rank or an integer count | **no tolerance** — but see the threshold problem |

## Use RELATIVE tolerance: a negative third argument

Octave's `assert` treats a negative tolerance as **relative**. This matters
enormously at scale:

```matlab
assert(1000.0001, 1000.0,  1e-6);   % FAILS -- absolute, too tight at this magnitude
assert(1000.0001, 1000.0, -1e-6);   % passes -- relative, which is what you meant
```

Default to a negative (relative) tolerance for anything whose magnitude is not
O(1). Use absolute only when the expected value is zero or near it — a relative
tolerance against zero is meaningless.

## Rank is a threshold, not a computation

`rank(A)` counts singular values above `max(size(A)) * eps * s(1)`. That is a
**choice**, not a fact about the matrix. A matrix can be exactly rank-deficient
in theory and numerically full rank, or the reverse.

So: never assert a rank for a matrix constructed near the boundary, and when
asserting rank, also assert the **gap** that makes the threshold safe:

```matlab
s = svd(A);
r = rank(A);
assert(r == expected_rank);
assert(s(r) / s(r+1) > 1e6);   % the gap is decisive, not marginal
```

If the gap is not decisive, the rank claim is not checkable at that matrix, and
the honest move is to say so rather than tighten the tolerance until it passes.

## Two routes that are NOT equally accurate (worked cases)

A margin near 1x is the signal that the tolerance does not match the
computation. Both of these were found by the skill's own verification run.

**`eig(A)` vs `roots(poly(A))`, n = 5 symmetric.** Discrepancy 1.51e-13 against
a backward-stable tolerance of 1.97e-13 — margin 1.3x. The poly route is not
backward stable: root-finding on a characteristic polynomial is ill-conditioned
(the Wilkinson problem), and loses roughly half the available digits. The
defensible bound is `sqrt(eps) * norm(A,2)` = 1.32e-07, margin ~9e5.

This is `math-linear-algebra`'s own `char_poly_roots_are_eigenvalues` misuse
note, measured: *never compute eigenvalues via the characteristic polynomial
numerically.*

**`svd(B)` vs `sqrt(eig(B'*B))`, 5x4.** Forming `B'B` squares the condition
number (measured: `cond(B)` = 4.12e16 → `cond(B'B)` = 8.84e16). The three
largest singular values still agree to ~1e-15. The smallest does not merely
lose accuracy — `eig(B'*B)` returns **−5.34e-14**, a negative eigenvalue of a
matrix that is positive semidefinite in exact arithmetic, so its square root is
complex, while `svd` returns a real 9.85e-16.

The honest check asserts agreement on the singular values the squared route can
carry, **and asserts the breakdown of the rest** — not a blanket agreement that
would be false. This is the capsule's `least_squares` warning about the normal
equations, measured.

## When a claim is uncheckable at a given matrix

Some claims cannot be verified numerically on some inputs, and recognising that
is part of the method:

- **Non-symmetric eigenvalues near a defective matrix.** A Jordan block
  perturbed by `epsilon` moves its eigenvalues by `epsilon^(1/n)` — at n = 5
  and `epsilon = 1e-16` that is 1e-3.2. No tolerance is both meaningful and
  passable. Verify defectiveness structurally (rank of `A - lambda I`) rather
  than by eigenvalue proximity.
- **`cond(A) * eps > 1`.** The forward bound exceeds the quantity itself;
  nothing about the solution is determined. `hilb(12)` above is past this line.
- **Jordan form, and anything discontinuous in the entries.** Never compute it
  numerically; it is not a continuous function of the matrix.

State these as *excluded*, the way a capsule node states a dropped hypothesis.
Do not paper over them with a loose tolerance.

## Reporting

Print the derived tolerance and the achieved residual next to each other, so a
reader can see the margin rather than trusting a pass:

```matlab
r = norm(Q*D*Q' - A, 2);
t = tol_resid(A);
printf("  spectral reconstruction: resid %.2e vs tol %.2e (margin %.0fx)\n", r, t, t/r);
assert(r < t);
```

A check that passes with a margin of 1.2x is telling you the tolerance is
guessed. A margin of 1e3–1e6 is typical for a correct backward-stable result.
