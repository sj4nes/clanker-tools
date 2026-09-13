---
name: octave
description: >-
  Verify matrix and linear-algebra claims numerically with GNU Octave: check a
  stated formula against an independently computed reference, at realistic
  dimension, with a tolerance derived from conditioning rather than guessed.
  Use when a claim is about matrices, vectors, or floating-point numerics —
  eigenvalues and the spectral theorem, SVD and low-rank approximation, rank
  and the four subspaces, determinants and characteristic polynomials,
  positive-definiteness and Cholesky, least squares and projection,
  factorisations, conditioning, matrix norms — and the existing `bc` or
  Mathlib-free Lean checks can only reach 2x2 toy cases. NOT a replacement for
  `bc` (which keeps exact and arbitrary-precision decimal work, where Octave's
  doubles are structurally unable to follow), not a proof tool (that is `lean`),
  and not a general scripting or plotting environment.
version: 1.0.0
author: Simon Janes
tags: [verification, octave, linear-algebra, matrices, numerics, tolerance, conditioning]
---

# Matrix verification with GNU Octave

You are verifying a **stated mathematical claim** about matrices by computing
it numerically. The deliverable is an executable `.m` file that **exits
nonzero when the claim is false**, at a dimension large enough for the claim to
have content, with every tolerance justified.

This skill exists because two existing tools cannot reach matrix-level claims:
Mathlib-free Lean caps at a fixed small dimension (`dim_core`, n = 2), and `bc`
has no matrices at all. It does **not** displace either. See
[`docs/bc-verification-audit.md`](../../docs/bc-verification-audit.md) for why
`bc` keeps its territory.

## The transaction

    state the claim → choose an INDEPENDENT route → pick n → derive the tolerance
    → assert → negative-contrast → report what was and was not covered

## Operating principles

1. **Never check a built-in against itself.** `[Q,D] = eig(A); assert(Q*D*Q', A)`
   passes at 3e-15 and tests *Octave*, not your claim — no error in the source
   being verified could make it fail. This is the single most common way a
   matrix "check" becomes worthless. See
   [`references/independence.md`](references/independence.md).

2. **Verify the claim as STATED, by a different route than the claim uses.**
   If the source says "positive definite iff all leading principal minors are
   positive", compute the minors with `det` on submatrices *and* the
   eigenvalues with `eig` *and* attempt `chol`, then require all three to
   agree. Agreement across genuinely different computations is the evidence;
   one built-in call is not.

3. **Derive every tolerance; never guess one.** A residual and a solution error
   have different scales, and both depend on the matrix. Fixed tolerances are
   wrong in both directions — demonstrably so, see
   [`references/tolerance-and-conditioning.md`](references/tolerance-and-conditioning.md).

       residual  ||Ax - b|| / ||b||     ~ n * eps          (backward stable)
       solution  ||x - x*|| / ||x*||    ~ cond(A) * eps    (forward error)

   A small residual **never** certifies an accurate solution.

4. **Pick n so the claim has content.** n = 2 makes most linear-algebra claims
   degenerate: every 2x2 symmetric matrix is diagonalisable, rank is 0/1/2,
   and a repeated eigenvalue is the only way to be defective. Use n >= 4 for
   structural claims, and include a rectangular case for anything about rank,
   SVD, or the four subspaces.

5. **Assert; do not print and eyeball.** Octave has `assert` and exits 1 on an
   uncaught error. Unlike `bc`, no output-grepping protocol is required. Print
   values *in addition to* asserting them, never instead.

6. **Include the negative case.** A check that only ever sees a true instance
   proves nothing about the check. Every claim of the form "X iff Y" needs a
   witness where both fail, and every "must hold" needs a nearby case where it
   does not.

7. **Seed every random matrix.** `rand("seed", N)` and `randn("seed", N)` are
   reproducible; an unseeded test that fails once a week is worse than no test.

8. **State what was NOT covered.** A numerical check at n = 5 over the reals is
   evidence about n = 5 over the reals. It is not a proof, it says nothing
   about other fields, and it cannot see a hypothesis that only bites at larger
   n. Say so in the report.

## Scope boundary

| task | tool |
|---|---|
| matrix identities, factorisations, spectra, rank, conditioning | **this skill** |
| exact decimal, arbitrary precision, integer/number-theoretic work | [`bc`](../bc/SKILL.md) — Octave's doubles **cannot** follow; one existing capsule check brackets a quantity to 1e-25, which is inexpressible in double |
| proving a universal statement | [`lean`](../lean/SKILL.md) |
| the dependency graph of a capsule | [`math-theorem-tree`](../math-theorem-tree/SKILL.md) |
| statistical workflow on data | [`statistics`](../statistics/SKILL.md) |
| Monte Carlo, simulation | [`simulation`](../simulation/SKILL.md) — stdlib Python is already in those harnesses |

**Do not migrate working `bc` checks to Octave.** The 24 harnesses audited in
`docs/bc-verification-audit.md` assert correctly and are negative-contrast
tested. Add Octave where the *dimension* is the limitation, not as a rewrite.

## Running

```sh
octave --no-gui --quiet checks.m          # exit 0 pass, 1 on a failed assert
```

`--no-gui --quiet` suppresses the banner; an uncaught `error` or a failed
`assert` exits **1**; `exit(N)` sets a status deliberately. No output parsing.

In a `run.sh`, that means the ordinary shell idiom is finally correct:

```sh
octave --no-gui --quiet checks.m          # under `set -e` this is sufficient
```

## File skeleton

```matlab
% <claim> -- numerical verification
% Source: <capsule>/<node>.  Claim as stated: <quote it>
1;                                   % script, not a function file

tol = @(A) 20 * rows(A) * eps * norm(A, 2);   % derived, see references/

A = [...];                                     % n >= 4, or seeded random
assert(issymmetric(A));                        % the claim's HYPOTHESIS, checked

% route 1: the claim as stated
% route 2: an independent computation
assert(route1, route2, -1e-10);                % NEGATIVE tol = RELATIVE

% negative contrast: the claim must FAIL here
B = [...];
assert(!<claim holds for B>);

printf("PASS: <claim> at n=%d\n", rows(A));
```

## References

- [`references/independence.md`](references/independence.md) — the trap, and
  the catalogue of independent routes per claim type.
- [`references/tolerance-and-conditioning.md`](references/tolerance-and-conditioning.md)
  — deriving tolerances; residual vs forward error; when `cond` makes a claim
  uncheckable.
- [`references/octave-gotchas.md`](references/octave-gotchas.md) — the language
  and CLI traps an agent hits: `'` vs `.'`, `^` vs `.^`, 1-based indexing,
  filename shadowing, `isequal` on floats.
- [`verification/`](verification/) — this skill verified against real
  `math-linear-algebra` claims, with negative contrasts.
