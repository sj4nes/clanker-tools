# Octave traps an agent will hit

All verified on GNU Octave 11.3.0.

## Language

| trap | why | do |
|---|---|---|
| **`'` is the CONJUGATE transpose** | `[1+2i]'` is `1-2i`. Over the reals they coincide, so this bites only in complex work — exactly where it matters most (Hermitian vs complex-symmetric). | `.'` for a plain transpose; `'` when you mean the adjoint. Say which in a comment. |
| **`^` is MATRIX power, `.^` is elementwise** | `A^2` is `A*A`; `A.^2` squares each entry. Both are valid, silently different. | Elementwise needs the dot. Every operator has a dotted form: `.*`, `./`, `.^`. |
| **1-based indexing** | `A(1,1)` is the first element; `A(0,1)` errors. | Matches the `math-linear-algebra` `index_convention` node, which also starts at 1 — no translation needed. |
| **`isequal` on floats is exact** | `isequal(0.1+0.2, 0.3)` is `0`. | Never use it for numerics. Use `assert(a, b, tol)`. It IS right for integers, ranks, sizes, and logical flags. |
| **`A\b` not `inv(A)*b`** | The explicit inverse is slower and less accurate. | `\` always. `inv` only when the inverse itself is the object under test. |
| **Automatic broadcasting** | `[1 2 3] + [1; 2; 3]` silently produces a 3x3 matrix, not an error. | Assert shapes: `assert(size(x), [3 1])`. |
| **`sum`/`mean` default to columns** | On a row vector they reduce to a scalar; on a matrix they return a row. | Pass the dimension explicitly: `sum(A, 1)`, `sum(A, 2)`. |
| **integer division is not integer** | `5/2` is `2.5`. | `idivide`, `floor`, or `fix` — and say which rounding you meant. |

## Files and invocation

| trap | why | do |
|---|---|---|
| **A script filename shadows built-ins** | Not just a warning — it BREAKS unrelated code. While building this skill, a scratch file named `diag.m` shadowed the built-in `diag`, which `roots` calls internally, so an eigenvalue computation failed with `invalid call to script`. A file named `fail.m` likewise shadows `fail`. | Name check files distinctively: `checks.m`, `verify-<claim>.m`. Never `test.m`, `diag.m`, `fail.m`, `rank.m`, `norm.m`. |
| **A bare `.m` may be parsed as a function file** | A file whose first statement looks like a definition can be treated as a function. | Start script files with `1;`. |
| **`--quiet` still prints warnings** | e.g. `matrix singular to machine precision`. | That warning is often *information* — a near-singular matrix means the claim may be uncheckable. Do not suppress it; read it. |
| **Startup is ~1.7s** | Against `bc` at ~0.2s. Across many harnesses this adds up. | One `.m` per capsule, not per claim. Batch the checks. |

## Exit status — the good news

Unlike `bc`, Octave signals failure properly:

| event | exit |
|---|---|
| clean run | 0 |
| failed `assert` | 1 |
| uncaught `error(...)` | 1 |
| `exit(N)` | N |

So the ordinary shell idiom is correct, and **no output-grepping protocol is
needed**:

```sh
set -e
octave --no-gui --quiet checks.m        # aborts the run on any failed assert
```

This is the one place Octave is strictly better than `bc` as a check runner.
It does not make Octave a `bc` replacement — see the scope table in
[`../SKILL.md`](../SKILL.md).

## Reproducibility

```matlab
rand("seed", 42);      % verified reproducible across runs
randn("seed", 7);
```

Seed **every** random matrix. An unseeded check that fails intermittently is
worse than no check: it trains the reader to ignore failures.

Prefer a fixed, written-out matrix when the claim is about a specific
structure. Use seeded random matrices when the claim is generic and you want
coverage over many instances — and then loop, so one unlucky draw is not the
whole evidence.

## Precision — the hard boundary

Octave is IEEE double: ~15–16 significant digits, `eps = 2.22e-16`.

Some existing `bc` checks in this repo are **not expressible** here. The
`math-number-systems` incompleteness witness brackets 2 to within 1e-25:

```
x = 1.4142135623730950488
x^2         = 2.00000000000000044409   -- already ABOVE 2 in double
x^2 < 2 ?     0                        -- the witness collapses
x + 1e-25 distinguishable from x ?  0
```

There is no tolerance that repairs this; the quantity being demonstrated is
smaller than the representable gap. Such checks stay in `bc`.
