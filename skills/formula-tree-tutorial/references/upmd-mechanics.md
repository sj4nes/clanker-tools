# upmd mechanics

[`upmd`](https://upmd.dev) (`github.com/rezigned/upmd`) runs named fenced code
blocks in a Markdown file as a dependency-aware workflow, in a real terminal.
Verified against **upmd 0.2.3**.

## Install

```sh
curl --proto '=https' --tlsv1.2 -LsSf \
  https://github.com/rezigned/upmd/releases/latest/download/upmd-installer.sh | sh
# or: brew install upmd   (if available on the platform)
upmd --version
```

## Running

| Command | Effect |
|---|---|
| `upmd tutorial.md` | interactive TUI — navigate blocks, run on demand (needs a real TTY) |
| `upmd tutorial.md --cli` | interactive, no TUI (plain terminal) |
| `upmd --ci --all tutorial.md` | run **every** block non-interactively (`--ci` = `--cli --yes`); the CI / verification gate |
| `upmd --ci -b capstone tutorial.md` | run the block named `capstone` and its full `deps:` chain, non-interactively |
| `upmd tutorial.md --all` | auto-advance through all blocks (prompts unless `--yes`) |
| `upmd -d DIR tutorial.md` | set the working directory for code execution |

After a run, `upmd` prints `Shell cwd was reset to <cwd>` — each invocation
starts from the current directory.

## Code-block attributes

Attributes go in `[ ... ]` on the fence info line, after the language:

````markdown
```bash [name:setup]
export G=9.81
echo "g = $G m/s^2"
```

```bash [name:chk_period, deps:setup]
echo "T = 2*pi*sqrt(1.0/$G):"
echo "scale=4; 8*a(1) * sqrt(1.0/$G)" | bc -l
```
````

| Attribute | Meaning |
|---|---|
| `name:x` | names the block (target for `-b x`, referent in `deps:`) |
| `deps:a` | run `a` (and its deps) before this block |
| `deps:"a, b"` | `a` then `b` as **sequential** stages, both before this block |
| `deps:"a \| b"` | `a` and `b` in the **same** stage (order-independent / parallel) |
| `bin:zsh` | override the interpreter for this block |

`deps:` grammar: comma `,` separates sequential stages; pipe `|` groups members
of one stage. For a linear tutorial (minimal-path form) each check just
`deps:` the previous check. For a branching path, list the real prerequisites
with `|`: `deps:"setup | chk_velocity | chk_force"`.

## State between blocks

- **Shell blocks** (`bash`, `sh`, `zsh`): successful blocks pass **exported
  environment variables** and **working-directory changes** to later blocks.
  Non-exported shell variables do **not** carry — always `export` a value another
  block needs.
- Each block otherwise starts fresh: no aliases, functions, or `set` options
  persist. Re-establish what you need, or put it in `setup`.
- **Other languages** (Python, Go, Rust, TypeScript): only with
  `upmd --capture-state` (experimental). Do not rely on it for a shipped
  tutorial — keep cross-block state in exported shell env, and have non-shell
  blocks read from `$ENV`.

## Writing calculation blocks

- Use `bash` calling `bc`. For `sqrt`, `s()`, `c()`, `a()` (atan), `l()`, `e()`,
  or `pi` via `4*a(1)`, invoke **`bc -l`**.
- `bc` truncates; it does not round. Set `scale=` explicitly. See the `bc` skill.
- Prefer a here-string (`bc -l <<< "..."`) or heredoc for multi-line `bc`; keep
  the physics expression readable.
- Every check prints a **labelled** result: a dimensional check prints the
  zero-vector (`0 0 0` / `0 0 0 0`); a limiting case prints the value with
  `(want <x>)`; a worked number prints units.
- Blocks must be **idempotent** — running twice gives the same output — and must
  not depend on any block not in their `deps:`.
- Exit non-zero on a real failure so `--ci --all` catches it. A bare `bc`
  mismatch will not fail the block on its own; add a guard when the value matters:

  ```bash
  got=$(echo "scale=0; (2^2)" | bc); [ "$got" = 4 ] || { echo "FAIL: $got != 4"; exit 1; }
  ```

## Gotchas

- **`upmd` treats every fenced code block as a task.** A fence with no language,
  or an unsupported one (`text`, `math`), prints `Language not supported` /
  `failed to start`. It does not fail `--ci --all` (exit stays 0) but it is
  noise. So in a tutorial: **no non-runnable code fences and no 4-space indented
  code blocks.** Show formulas inline in prose (`` **`T = 2 pi sqrt(L/g)`** ``);
  give run instructions as inline `code` in a sentence, never in a ` ```bash `
  block (it would run `upmd` recursively). Every fence in the file is a real
  `bash`/`lean`/… block with a `name`.
- **uppercase and leading-`_` identifiers break `bc`** (same as the `bc` skill):
  `A`, `Pr`, `_x` fail; `amp`, `pr`, `x_1` are fine.
- **No comment syntax in `bc` input** — strip `#` lines if you pipe a `.bc` file
  in; or keep comments in the surrounding Markdown prose, not the code.
- **`upmd` reruns from scratch** each `--ci --all`; there is no cache. Keep
  blocks fast.
- **cwd**: if a block `cd`s, later blocks inherit it (shell state) but the next
  `upmd` invocation resets. Use absolute paths or `cd` in `setup`.
- **Reusing a capsule's `.bc` file**: `bc -l capsule/validation/dimensional-checks.bc`
  works as a single block, but for a *tutorial* split it so each concept's lines
  live in that concept's section — the reader should see one idea per check.
- **Unicode in `bc`**: keep block code ASCII (`delta_kappa`, not `δ_κ`); put the
  pretty symbols in the prose.
