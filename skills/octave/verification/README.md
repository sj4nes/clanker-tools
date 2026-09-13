# Verifying the `octave` skill

## What verification means for this skill

The skill prescribes a method — *independent routes, derived tolerances, n large
enough for the claim to have content, negative contrasts* — so verification
applies that method to **real claims from the `math-linear-algebra` capsule**
and asserts the results, including the cases that must fail.

The capsule's own checks reach only 2×2 (`bc`) and n = 2 (Mathlib-free Lean,
`dim_core`). These reach n = 4–5, rectangular, and rank-deficient — which is
the gap the skill exists to close.

## Case

Eight sections, 27 assertions:

| § | capsule claim | independent routes |
|---|---|---|
| 1 | `spectral_theorem_symmetric` | `eig` vs `roots(poly(A))`; `QQ' = I`; **negative:** a rotation has complex eigenvalues |
| 2 | `psd_characterisations` | eigenvalues, Sylvester minors, Cholesky, full-rank factor — all four must agree; **negative:** `diag(0,−1)` fails all four |
| 3 | `char_poly_coefficients`, `cayley_hamilton` | `poly()` vs `trace`/`det`; Horner evaluation of `p_A(A)` |
| 4 | `rank_nullity`, `four_subspaces`, `row_rank_equals_column_rank` | `rank` vs `null` dimension; `rank(X)` vs `rank(X')`; `null(X) ⟂ orth(X')` |
| 5 | `least_squares`, `hat_matrix` | backslash vs normal equations; residual orthogonality; stated `H` vs a QR route; **negative:** an oblique projection has `P² = P` and `tr = rank` but `P' ≠ P` |
| 6 | `singular_values`, `eckart_young`, `condition_number`, `matrix_norms` | `svd` vs `sqrt(eig(A'A))`; truncated-SVD error vs `σ_{k+1}`; Frobenius three ways |
| 7 | `sylvester_law_of_inertia` | signs of `eig(C)` vs `eig(P'CP)` preserved, while the eigenvalues themselves are not |
| 8 | the method's own guardrail | `assert()` must reject a deliberately false claim |

## Result

`sh run.sh` exits 0. Negative-contrast tested twice — corrupting the spectral
reconstruction tolerance and corrupting a rank claim each make it exit 1.

No output-grepping is required: Octave exits 1 on a failed assert, so `set -e`
suffices. This is the one respect in which Octave is a strictly better check
runner than `bc` (see `docs/bc-verification-audit.md`).

## Findings folded back into the skill

Writing these checks surfaced four things, all now in the references:

1. **A rank claim I asserted was wrong.** I built a 5×3 matrix and *assumed* it
   was rank 2; it was rank 3. The assertion caught it — which is the argument
   for asserting rather than printing, made against my own work.
2. **`eig` vs `roots(poly(A))` passes with a margin of only 1.3×** under a
   backward-stable tolerance. That is not a tolerance problem, it is the
   capsule's own `char_poly_roots_are_eigenvalues` warning: root-finding on a
   characteristic polynomial is ill-conditioned and loses half the digits. The
   defensible bound for that route is `sqrt(eps)·‖A‖`, which leaves ~9×10⁵.
   Recorded in `references/tolerance-and-conditioning.md`.
3. **`sqrt(eig(B'B))` returns a NEGATIVE eigenvalue** (−5.34e-14) for a matrix
   that is positive semidefinite in exact arithmetic, so its square root is
   complex — while `svd` returns a real 9.85e-16. Forming `A'A` squares the
   condition number, which is the capsule's own `least_squares` warning,
   measured. The check now asserts this *breakdown* rather than asserting a
   false agreement.
4. **Naming a file `diag.m` shadowed the built-in `diag`**, which `roots` calls
   internally, breaking an unrelated computation. Confirms the filename-shadowing
   trap in `references/octave-gotchas.md` with a concrete instance.

## Standing limitations

Verified at n = 2–5 over ℝ, square and rectangular. This says nothing about
other fields, about larger n, or about claims whose hypotheses only bite
asymptotically. **None of it is a proof** — that is `lean`'s job, and the
capsule's Lean cores remain the universal evidence. Exact and
arbitrary-precision work stays in `bc`, which Octave's doubles cannot follow.
