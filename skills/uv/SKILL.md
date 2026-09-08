---
name: uv
description: >-
  Manage Python interpreters, virtual environments, dependencies, locked
  projects, one-file scripts, and CLI tools with Astral's `uv` as deterministic,
  declarative commands — no manual `venv` activation. Use whenever a task needs
  to install Python packages, run Python code or tests reproducibly, create or
  sync an environment, add or remove a dependency, pin an interpreter, run a
  one-off Python CLI, or build and publish a package. Covers the project vs
  pip-compat vs script vs tool decision, converging with `uv sync` / `uv lock` /
  `uv run` instead of imperative shell, classifying commands by side effect, and
  gating lockfile regeneration, `uv pip sync`, cache clean, and `uv publish`.
version: 1.0.0
author: Simon Janes
tags: [python, uv, packaging, virtualenv, dependencies, terminal, reproducibility]
---

# Python Workflows with `uv`

You are an autonomous terminal agent that uses `uv` to run and set up Python. `uv`
replaces `pip`, `pip-tools`, `virtualenv`, `pyenv`, `pipx`, Poetry/Rye, and Twine
with one tool. Most Python setup and execution can be expressed as deterministic
`uv` commands that **declare a target state and converge toward it**, without
activating an environment.

Your priority is a **reproducible, reviewable result**: the environment matches a
committed lockfile, execution goes through `uv run`, and every command that
changes project metadata or an external registry is inspected first.

Treat Python setup as a controlled process:

    identify repo type → read declared Python → pick least-invasive command → execute with reproducibility controls → verify → report

## Core model

1. **A project** is described by `pyproject.toml`.
2. **Dependencies** resolve into `uv.lock`.
3. **The environment** is materialized, normally as `.venv`.
4. **Commands run through `uv run`** and automatically use that environment.
5. **A global cache** avoids re-downloading or rebuilding identical artifacts.

Favor commands that declare state and converge toward it — `uv sync`, `uv lock`,
`uv run` — over imperative, environment-dependent shell sequences. Never
`source .venv/bin/activate`; activation is shell-specific, easy to forget, and
can silently select the wrong interpreter.

## When to use `uv`

- Installing Python packages or recreating a Python environment.
- Running a Python program, module, or test suite reproducibly.
- Adding, removing, or upgrading a project dependency.
- Regenerating or validating a lockfile.
- Finding, installing, or pinning a Python interpreter.
- Running a one-off Python CLI (formatter, linter, generator) without polluting
  the project.
- Running a self-contained `.py` script with inline dependency metadata.
- Building an sdist/wheel or publishing a package (with explicit authorization).
- Testing a compatibility matrix across interpreter versions.

Do not use `uv` when:

- A different environment manager (Conda, system package manager, Nix, Bazel) is
  authoritative for the repo. Use `uv` only as a diagnostic then.
- The task needs a package index, credential store, or interpreter that policy
  forbids `uv` from reaching, and no cached copy exists.
- You are asked only to read or explain Python source — no environment needed.

## Required operating principles

- **Identify the repo type before running anything.** `pyproject.toml` +
  `uv.lock` → uv project; `pyproject.toml` only → likely uv-compatible, inspect
  it; `requirements*.txt` / `.in` → pip-compat path; a lone `.py` → script path.
- **Prefer `uv run` for all execution.** It locates the project, creates or
  reuses the environment, and runs in that context with no activation.
- **Prefer module invocation:** `uv run python -m pytest`, not `uv run pytest` —
  a bare executable on `PATH` is ambiguous.
- **In any validation or CI path, use `uv sync --locked`.** It fails if
  `pyproject.toml` and `uv.lock` diverge. Never regenerate a lockfile in a
  validation path unless the task explicitly allows a dependency change.
- **Pin the interpreter explicitly** — `.python-version`, `requires-python`, or
  `--python <version>` — never rely on whatever Python the machine happens to
  have.
- **Quote every requirement string** a shell could mangle: characters
  `< > ! [ ] ; ~` and `@`. `uv add "django>=5,<6"`, not `uv add django>=5,<6`.
- **Check local `--help` before relying on a flag.** Subcommands and flags vary
  by `uv` version: `uv --help`, `uv <command> --help`.
- **Treat `pyproject.toml` + `uv.lock` as the source of truth.** A
  `requirements.txt` produced by `uv export` is a compatibility artifact, not a
  second dependency source to hand-maintain.
- **Credentials only from an approved store or injected environment.** Never a
  token in `pyproject.toml`, `uv.toml`, shell history, a committed `.env`, a
  generated requirements file, or tool output. Redact tokens from any output.
- **Review the diff after any metadata-changing command:**
  `git diff -- pyproject.toml uv.lock`. Read a lockfile change as a
  dependency/security change, not incidental noise.
- **A valid command result is not authorization** for a destructive or
  outward-facing action. Classify side effects first (table below).

## Terminology

| Term | Meaning |
|---|---|
| Project | A directory with `pyproject.toml`; `uv` commands operate on it |
| Lockfile | `uv.lock` — the resolved, pinned dependency set |
| Sync | Making `.venv` match the lockfile / project metadata |
| Group | A named optional dependency set (`--dev`, `--group docs`) |
| Extra | An optional feature of a dependency (`pydantic[email]`) |
| Ephemeral tool | A CLI run in a throwaway environment via `uvx` |
| Inline script metadata | A PEP 723 `# /// script` block declaring a script's deps |
| Workspace | Multiple related packages sharing one lockfile |

## Command side-effect classes

| Class | Commands | Policy |
|---|---|---|
| Inspect (non-destructive) | `uv --help`, `uv python list`, `uv python find`, `uv tree`, `uv run python -V`, `uv run python -c ...`, `uvx <linter> check`, `uv lock --check`, `uv export` to stdout | May run after scope review |
| Repo-modifying | `uv init`, `uv add`, `uv remove`, `uv lock`, `uv sync`, `uv add --script`, `uv python pin`, `uv export -o <file>` | Inspect `git status --short` + `pyproject.toml` first; review `git diff` after |
| Destructive / external | `uv pip sync`, `uv cache clean`, `uv tool uninstall`, `uv python uninstall`, `uv publish` | Require explicit confirmation; verify the exact target first |

`uv sync` modifies `.venv`; `uv lock` can modify `uv.lock`; `uv add`/`uv remove`
modify both. `uv pip sync` **removes** packages not in the requirements set.
`uv publish` uploads an immutable release that cannot be replaced.

## Required workflow

### 1. Identify the repo type and declared Python

```sh
ls pyproject.toml uv.lock requirements*.txt requirements*.in .python-version 2>/dev/null
[ -f pyproject.toml ] && grep -n 'requires-python\|^name\|build-system' pyproject.toml
[ -f .python-version ] && cat .python-version
uv --version
```

Decide the path:

| Repo shape | Path |
|---|---|
| `pyproject.toml` + `uv.lock` | Project mode (§2) |
| `pyproject.toml` only | Inspect metadata; usually project mode, run `uv lock` first |
| `requirements*.txt` / `.in` | pip-compat (§3) |
| Lone `.py` | Script (§4) |
| "run this CLI once" | Tool (§5) |

### 2. Project mode (preferred for maintained code)

**Existing project — first choice:**

```sh
uv sync --locked          # fail if lockfile is stale; do not regenerate
uv run python -m pytest
```

If the lockfile is intentionally absent or the task allows regeneration:

```sh
uv lock
uv sync
git diff -- pyproject.toml uv.lock   # review before continuing
```

**New project:**

```sh
uv init my_app && cd my_app
uv python pin 3.12
uv add "fastapi>=0.110"
uv add --dev pytest ruff
uv run ruff check .
uv run python -m pytest
```

**Changing dependencies** (updates `pyproject.toml` + `uv.lock` + `.venv`
coherently — safer than editing metadata by hand):

```sh
uv add "httpx[socks]"
uv add --group docs mkdocs
uv remove requests
git diff -- pyproject.toml uv.lock
```

If you edited `pyproject.toml` directly, converge with `uv lock && uv sync`.

**Sync variants:** `--locked` (lockfile must be current), `--frozen` (use lockfile
as-is, no check), `--no-dev`, `--all-groups`, `--group <name>`. Confirm semantics
against `uv sync --help` for the installed version before adopting a strict CI
policy.

### 3. pip-compat mode (existing requirements project)

```sh
uv venv --python 3.12
uv pip sync requirements.txt          # DESTRUCTIVE: removes anything not listed
.venv/bin/python -m pytest            # invoke the interpreter directly, no activate
```

From an unpinned `requirements.in`:

```sh
uv pip compile requirements.in --universal -o requirements.txt
uv pip sync requirements.txt
```

Use `--universal` for a requirements file meant to resolve across platforms. Do
not run `uv pip sync` in an environment holding manually managed packages you
need to keep. In a project-managed environment prefer `uv remove` over
`uv pip uninstall`.

### 4. Script mode (one-file automation)

```sh
uv add --script cleanup.py "requests>=2.32"   # writes a PEP 723 block into the file
uv run cleanup.py
```

For a one-time dependency without editing the script:

```sh
uv run --with "httpx[socks]" script.py
```

Record `requires-python` in the inline metadata and pin dependency constraints.
When a script becomes a maintained application, migrate it to a locked project.

### 5. Tool mode (Python CLIs)

```sh
uvx ruff check .                 # ephemeral, isolated — the agent-safe default
uvx "ruff@0.9.0" check .         # pin the version when output affects committed code
uvx --from httpie http GET https://example.com   # package name != command name
```

Decision rule:

| Need | Command |
|---|---|
| Run it once | `uvx <tool> …` |
| Version-pinned one-off | `uvx <tool>@<version> …` |
| For the current app | `uv add --dev <tool>` then `uv run <tool> …` |
| Persistently on `PATH` | `uv tool install <tool>` |

Prefer `uvx` for agent execution; it minimizes ambient state. `uv tool install`
is for a human who wants a stable CLI.

### 6. Interpreter management

```sh
uv python list                       # available + installed
uv python find ">=3.11,<3.13"        # actual path for a non-uv subprocess
uv python install 3.12               # pre-provision (often optional; uv auto-downloads)
uv python pin 3.12                   # writes .python-version (project-local, reviewable)
uv run --python 3.10 python -m pytest # one command on a specific interpreter
```

Compatibility matrix — state the versions explicitly, do not assume "all
supported" means "installed here":

```sh
for v in 3.10 3.11 3.12; do uv run --python "$v" python -m pytest || exit 1; done
```

Use `--no-managed-python` when policy forbids downloads and requires the
OS-managed interpreter.

### 7. Verify

```sh
uv run python -c "import sys; print(sys.executable)"   # the expected .venv?
uv run python --version                                 # the pinned version?
uv tree                                                  # explain a transitive dep
uv run python -m pytest
uv run ruff check .
git diff -- pyproject.toml uv.lock                       # after any mutating command
```

A command exiting `0` proves it ran, not that the dependency set is correct or
minimal. Confirm the interpreter, the lockfile state, and the test result
separately.

### 8. Build and publish (gated)

```sh
uv lock --check
uv sync --all-groups
uv run python -m pytest
uv build                             # produces dist/*.tar.gz and dist/*.whl
# inspect dist/ contents
uv venv /tmp/pkg-test --python 3.12
/tmp/pkg-test/bin/python -m pip install dist/*.whl
/tmp/pkg-test/bin/python -c "import your_package"
uv publish                           # ONLY with explicit authorization
```

Before `uv publish`: confirm the distribution name and version, that the version
is not already released, that the target index is correct, and that credentials
come from `UV_PUBLISH_TOKEN` / trusted publishing — never a flag in shell
history. Publishing cannot be undone.

## Cache

```sh
uv cache dir                         # where artifacts live
uv cache prune                       # remove unused entries (safe)
uv cache prune --ci                  # CI post-job size reduction
uv cache clean                       # DESTRUCTIVE: clears all cached content — gate it
UV_CACHE_DIR=/path uv sync           # relocate for sandboxes / quotas
uv --no-cache run python -m pytest   # diagnose a suspected stale-cache issue
```

A `uv.lock` identifies what is needed; it does **not** contain the artifacts. Do
not promise an offline `uv sync` will succeed just because a lockfile exists.

## CI shape

```yaml
- uses: astral-sh/setup-uv@<pinned-commit-sha>   # pin by SHA, not a tag
  with:
    enable-cache: true
- run: uv sync --locked --all-groups
- run: uv run ruff check .
- run: uv run python -m pytest
```

Cache-key invalidation keys on `uv.lock` for project mode, on `requirements.txt`
for `uv pip` flows. Keep build/test jobs separate from any publication job; never
let CI publish silently.

## References

- [`references/command-reference.md`](references/command-reference.md) — the
  command families, flag-by-version caveats, `uv export` / workspace / private
  index details, and the environment-variable list.
- [`references/agent-playbooks.md`](references/agent-playbooks.md) — worked
  end-to-end runs: existing project validation, requirements migration,
  compatibility matrix, ephemeral tooling, a safe release sequence, and the
  cycle of "edited pyproject.toml → converge".

## Completion report

State:

- The repo type identified and the path taken (project / pip-compat / script /
  tool).
- The interpreter version used and how it was selected.
- Each `uv` command run, classified (inspect / repo-modifying / destructive).
- For repo-modifying commands: the `git diff` of `pyproject.toml` and `uv.lock`.
- Verification: which of interpreter check, `uv tree`, and the test/lint command
  passed, failed, or was unavailable.
- Any command that was gated and not run, and why.

Never state that an environment is synced, a lockfile is current, tests pass, or
a package is published unless you verified that result.
