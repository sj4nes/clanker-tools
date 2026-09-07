# upmd mechanics (for theorem-tree tutorials)

[`upmd`](https://upmd.dev) (`github.com/rezigned/upmd`) runs named fenced code
blocks in a Markdown file as a dependency-aware workflow in a real terminal.
Verified against **upmd 0.2.3**. The block grammar and state model are identical
to the physics case; the addition here is **§ Lean beats**.

## Install

```sh
curl --proto '=https' --tlsv1.2 -LsSf \
  https://github.com/rezigned/upmd/releases/latest/download/upmd-installer.sh | sh
# or: brew install upmd
upmd --version
```

## Running

| Command | Effect |
|---|---|
| `upmd tutorial.md` | interactive TUI (needs a real TTY) |
| `upmd tutorial.md --cli` | interactive, no TUI |
| `upmd --ci --all tutorial.md` | run **every** block non-interactively (`--ci` = `--cli --yes`); the verification gate |
| `upmd --ci -b capstone tutorial.md` | run `capstone` and its full `deps:` chain, non-interactively |
| `upmd -d DIR tutorial.md` | set the working directory for code execution |

Each invocation starts from the current directory; `upmd` prints
`Shell cwd was reset to <cwd>` after a run.

## Code-block attributes

Attributes go in `[ ... ]` on the fence info line, after the language:

````markdown
```bash [name:setup]
export SEED=2
echo "seed loaded"
```

```bash [name:chk_supremum, deps:setup]
echo "scale=20; ..." | bc -l
```
````

| Attribute | Meaning |
|---|---|
| `name:x` | names the block (target for `-b x`, referent in `deps:`) |
| `deps:a` | run `a` (and its deps) before this block |
| `deps:"a, b"` | `a` then `b` as **sequential** stages, both before this block |
| `deps:"a \| b"` | `a` and `b` in the **same** stage (order-independent) |
| `bin:zsh` | override the interpreter for this block |

`deps:` grammar: comma `,` separates sequential stages; pipe `|` groups members
of one stage. For a minimal-path tutorial each `chk_` block usually just
`deps:` the previous one; a theorem that draws on two earlier results lists both
with `|` — mirror `edges/dependencies.plan` for that node, restricted to nodes
that have a block.

## State between blocks

- **Shell blocks** (`bash`, `sh`, `zsh`): successful blocks pass **exported
  environment variables** and **cwd changes** to later blocks. Non-exported
  variables do not carry — always `export` a value another block needs.
- Each block otherwise starts fresh: no aliases, functions, or `set` options
  persist. Put shared state in `setup`.
- **Other languages** (Python, Lean, …): no state capture. A Lean beat is
  self-contained — it writes its own temp file and needs nothing from earlier
  blocks except env vars it reads from `$…`.

## Writing `bc` calculation blocks

- Use `bash` calling `bc`. For `sqrt`, `s()`, `c()`, `a()` (atan), `l()`,
  `e()`, or `pi` via `4*a(1)`, invoke **`bc -l`**.
- `bc` truncates; it does not round. Set `scale=` explicitly. See the `bc` skill.
- **Probabilities and rationals: work in integer counts ("k out of N"), not
  decimals.** `echo "scale=6; 1/6" | bc` gives `.166666`, and `6 * .166666`
  gives `.999996` — an equality guard against `1` then fails. This is the same
  "k out of N" convention the capsule's Lean file uses (`P(A)` as an integer
  numerator over a fixed `N`). Compare numerators with bash `$(( ))` or
  `[ "$a" -le "$b" ]`; show the fraction (`$n/6`) only in the echo text. Reach
  for `bc` decimals only where the quantity is genuinely irrational (a `√2`
  bisection, a normal-CDF value) — and then compare with a tolerance, never `=`.
- **uppercase and leading-`_` identifiers break `bc`**: `A`, `Pr`, `_x` fail;
  `amp`, `pr`, `x_1` are fine. Keep block code ASCII — `delta_kappa`, not `δ_κ`;
  put pretty symbols in the prose.
- **No `#` comments in `bc` input.** Comments live in the surrounding Markdown.
- Every check prints a **labelled** result. For math:
  - a **definition instance** prints the concrete object (`pi(2,1) = 8`; the
    class `[3] = {3, 8, 13, …}`);
  - an **identity check** prints both sides and their difference (`want 0`);
  - a **specialization** prints the value with `(want <x>)`;
  - a **brute counterexample search** prints a count with `(want 0)` when the
    theorem forbids one, or the witness it found when a hypothesis is dropped.
- Blocks must be **idempotent** and must not depend on any block outside their
  `deps:`.
- A bare `bc` mismatch does **not** fail the block. Guard the values that matter:

  ```bash
  got=$(echo "scale=0; 2*5*3" | bc); [ "$got" = 30 ] || { echo "FAIL: $got"; exit 1; }
  ```

## Lean beats

`upmd` has **no native Lean runner** (`bin:lean` gives `Language not supported`).
Run Lean from a `bash` block instead. The pattern, from
`skills/math-real-analysis/tutorial/hole-in-the-rationals.md`:

````markdown
```bash [name:lean_triangle_inequality, deps:setup]
command -v lean >/dev/null || { echo "SKIP: lean not on PATH"; exit 0; }
d=$(mktemp -d)
cat > "$d/tri.lean" <<'LEAN'
-- <capsule>/validation/proof-checks.lean, section 1
-- triangle inequality, UNIVERSAL over the integers (genuine, not an instance)
theorem tri3 (a b c : Int) :
    (a - c).natAbs <= (a - b).natAbs + (b - c).natAbs := by omega
LEAN
if lean "$d/tri.lean" 2>/dev/null; then
  echo "kernel accepted, for ALL integers a, b, c:  |a - c| <= |a - b| + |b - c|"
  echo "this is the whole of 'convergent => Cauchy'."
else
  echo "FAIL: lean rejected the triangle inequality"; rm -rf "$d"; exit 1
fi
rm -rf "$d"
```
````

Rules for a Lean beat:

1. **`command -v lean` guard first**, `echo "SKIP: …"; exit 0` if absent. The
   tutorial must go green on a machine without Lean. Say so in the preamble.
2. **Heredoc the capsule's exact snippet** — copy from
   `validation/proof-checks.lean`, do not retype the proof. Keep the capsule's
   own comment lines; add a `-- <capsule>/validation/proof-checks.lean, §N`
   provenance line.
3. **No Mathlib.** The capsules are Mathlib-free (Lean 4.33 core: `omega`,
   `decide`, `grind`, `simp`, structural tactics). A snippet that needs `ring` /
   `linarith` / `nlinarith` / `positivity` is not in the capsule and does not
   belong in the tutorial.
4. **State exactly what the kernel verified**, matching the capsule's
   `proof-checks.md` wording:
   - *genuine / universal* — "proved for all `a, b : Int` by `omega`" /
     "universal in the scalars by list induction + `grind`";
   - *instance* — "an instance at `a = 5, b = 3` by `decide` — kernel evaluation
     of a closed proposition, **not** a proof of the general theorem";
   - *cited* — do not run it; one sentence: "the general theorem is cited to
     <source> and not formalised in the capsule."
5. **`mktemp -d` and clean up** on every exit path (`rm -rf "$d"` before
   `exit 1` too).
6. **Check the exit code, not stdout.** `lean file.lean` exits 0 iff the file
   elaborates with no errors and no `sorry`. Redirect `2>/dev/null` unless you
   want the reader to see Lean's own diagnostics on failure.
7. One Lean beat per node with `lean_status: core`. Skip `cited` nodes (mention
   in prose). Do not batch several capsule sections into one Lean file — one
   idea per block.
8. **Read the snippet the `lean_ref` points to before you feature it.** Some
   capsule cores are near-vacuous — an identity of the shape
   `(h : s = f a b) ⊢ s = f a b` proves nothing mathematical, it just
   type-checks. (In `math-probability`, `Prob.incl_excl_2/3` are like this.) If
   the `lean_ref` is not substantive, give that node a `bc` + counterexample
   treatment instead and note it in the completion report — it may be a capsule
   fix (a weak core, or a `lean_ref` that should point elsewhere). A *substantive*
   core has real hypotheses doing work (`Prob.union_bound`:
   `0 ≤ pAB ⊢ pA + pB - pAB ≤ pA + pB`).

`lean_<id>` blocks usually `deps:setup` only (they are self-contained). Wire a
`deps:` to an earlier `lean_` or `chk_` block only when the prose genuinely
builds on it.

## Gotchas

- **`upmd` treats every fenced code block as a task.** A fence with no language,
  or `text` / `math` / `lean`, prints `Language not supported` / `failed to
  start` — it does not fail `--ci --all` (exit stays 0) but it is noise. So:
  **no non-runnable code fences, no 4-space-indented code blocks.** Show
  statements and formulas inline (`` **`∀ε>0 ∃N …`** ``); give run commands as
  inline `code` in a sentence, never in a ` ```bash ` block (it would run `upmd`
  recursively). Every fence is a real `bash` block with a `name`.
- **`upmd` reruns from scratch** each `--ci --all`; no cache. Keep blocks fast —
  a Lean elaboration is ~1–3 s, a bounded `bc` search should be well under a
  second. Cap loop counts (`[ "$n" -gt 100 ] && exit 1`).
- **cwd**: a block that `cd`s is inherited by later blocks in the same run, but
  the next `upmd` invocation resets. Use absolute paths or `cd` in `setup`.
- **Reusing a capsule's `.bc` file wholesale** (`bc -l capsule/validation/instance-checks.bc`)
  works as one block, but for a tutorial split it so each concept's lines live
  in that concept's section — one idea per check.
- **`bc`'s `n % 2` is scale-dependent** (from the `math-theorem-tree` fixes): at
  `scale > 0` it is not integer parity. Use a sign-flip variable or `scale=0`
  for parity.
- **`bc` multiplication truncates *intermediate* products to `scale`.** A chain
  like `2 * eps * eps` at `scale=0` collapses: `2 * 0.02 = 0.04`, then
  `0.04 * 0.02 = 0.0008` truncated to scale 2 gives `0.00` → a later divide is
  a divide-by-zero. This bites the `app_<id>` blocks (real formulas with small
  parameters like `eps = 0.02`). Compute the whole expression at a high scale,
  then truncate the final answer:
  `echo "scale=8; x = ln($h/$delta) / (2 * $eps * $eps); scale=0; x/1 + 1" | bc -l`.
  `l()`, `e()`, `sqrt()` also need `scale > 0` to produce anything.
- **`awk` is available** and is the right tool for a counterexample that needs a
  real loop with floats (e.g. scanning `sin n`), as in `hole-in-the-rationals`
  §9 — `bash`+`bc` in a `while` is fine for bisection but slow for `10^6`
  iterations.
