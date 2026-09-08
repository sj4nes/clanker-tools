# `uv` command reference

Companion to [`../SKILL.md`](../SKILL.md). The installed `uv` version is the
authority — run `uv <command> --help` before relying on any flag below.

## Command families

```
uv init        Create a project or script scaffold
uv add         Add a dependency (updates pyproject.toml + uv.lock + .venv)
uv remove      Remove a dependency (same three, coherently)
uv lock        Resolve / update uv.lock without necessarily installing
uv sync        Make .venv match the lockfile / project metadata
uv run         Run a command or script in the project environment
uv tree        Inspect the resolved dependency graph
uv export      Export dependencies to another format (requirements-txt, ...)

uv python ...  Manage interpreters (list, find, install, pin, upgrade, uninstall)
uv venv        Create a plain virtual environment (pip-compat path)
uv pip ...     Pip / pip-tools / virtualenv-compatible operations

uv tool ...    Install / list / upgrade / uninstall durable CLI tools
uvx ...        Alias for `uv tool run` — ephemeral isolated tool run

uv build       Build sdist + wheel
uv publish     Upload distributions to an index (immutable; gate it)

uv cache ...   dir / prune / prune --ci / clean
uv auth ...    Manage package-index credentials
uv self ...    Update / manage uv itself
```

`uv help` and `uv help <command>` are part of the official reference workflow.

## Flags that vary by version — check `--help` first

| Area | Flag | Note |
|---|---|---|
| `uv sync` | `--locked` | Do not change the lockfile; fail if it is out of date. Use in CI/validation. |
| `uv sync` | `--frozen` | Use the existing lockfile without the normal freshness check. |
| `uv sync` | `--no-dev`, `--all-groups`, `--group <n>`, `--no-default-groups` | Select which optional sets install. Names and defaults have shifted between releases. |
| `uv lock` | `--check` (a.k.a. `--locked` on some versions) | Validate that `uv.lock` is current without rewriting it. |
| `uv pip compile` | `--universal` | Resolve across supported platforms rather than pinning to the current machine. |
| `uv pip install` | `--system` / `UV_SYSTEM_PYTHON=1` | Install into the system interpreter — generally wrong; only for containers/CI that intend it. |
| `uv run` | `--python <ver>`, `--with <pkg>`, `--no-project`, `--no-managed-python` | Per-command interpreter, ephemeral dep, ignore surrounding project, forbid downloads. |
| `uv python install` | `--reinstall`, version ranges, `pypy@x` | CPython, PyPy, Pyodide distributions; downloadable CPython from `python-build-standalone`. |

## `uv export` — interoperability, not a second source

```sh
uv export --format requirements-txt -o requirements.txt
uv export --format requirements-txt --no-hashes --no-dev -o requirements.txt
```

Generated requirement files are compatibility artifacts for deployment systems
that demand them. `pyproject.toml` + `uv.lock` remain the source of truth; do not
hand-edit an exported file.

## Requirement string forms (always quote)

```sh
uv add "fastapi>=0.110"
uv add "pydantic[email]"
uv add "django>=5,<6"
uv add "httpx[socks]"
uv add "git+https://github.com/org/repo.git"
uv add "git+https://github.com/org/repo.git@v1.4.0"
uv add "../local-package"
uv add --dev pytest ruff
uv add --group docs mkdocs
```

## Interpreter selection precedence

`uv` selects an interpreter from, roughly: an explicit `--python`; the active
`VIRTUAL_ENV`; a `.python-version` file; `requires-python` in `pyproject.toml`; a
compatible system Python; a uv-managed download. Pin explicitly so the choice is
visible to other developers and agents:

```sh
uv python pin 3.12          # writes ./.python-version
uv python pin --global 3.12 # user-level default (prefer project-local)
```

## Workspaces (monorepos)

Configured by a `[tool.uv.workspace]` table in the root `pyproject.toml` listing
member paths; one root `uv.lock` resolves the shared graph.

```sh
uv sync --all-packages
uv run --package api python -m api
uv build --package shared_library
```

- Run workspace commands from the root unless targeting a known member.
- Use `--package <name>` when command ownership matters.
- Add a dependency to the member that needs it, not the root.
- Commit the root `uv.lock`.

## Build backend

A package needs `[build-system]` in `pyproject.toml`. `uv` ships its own backend:

```toml
[build-system]
requires = ["uv_build>=0.0.0"]
build-backend = "uv_build"
```

Use the version appropriate to the installed `uv` — do not paste an old pin into
a new project. A project **with** `[build-system]` is treated as a package to
build and install into its own environment; **without** one it is an
application / dependency container.

## Environment variables

| Variable | Purpose |
|---|---|
| `UV_CACHE_DIR` | Cache location (sandboxes, quotas, CI). |
| `UV_SYSTEM_PYTHON` | Allow `uv pip` to target the system interpreter. |
| `UV_PYTHON` | Default interpreter request. |
| `UV_INDEX_URL` / `UV_EXTRA_INDEX_URL` | Package index endpoints. |
| `UV_PUBLISH_TOKEN` / `UV_PUBLISH_USERNAME` / `UV_PUBLISH_PASSWORD` / `UV_PUBLISH_URL` / `UV_PUBLISH_INDEX` | Publishing auth and target. |
| `UV_CREDENTIALS_DIR` | Override the credentials directory (`uv auth`). |
| `UV_NO_CACHE` | Disable the persistent cache. |

Read secrets only from an approved store or injected environment. Never commit
them, echo them, or leave them in generated files or logs. Prefer short-lived CI
trusted-publisher federation over stored long-lived tokens.

## Private indexes

Configure the index endpoint in `uv.toml` / `pyproject.toml` (non-secret) and
pass credentials via `uv auth` or environment variables (secret). Keep tokens out
of `pyproject.toml`, shell history, CI logs, committed `.env` files, and exported
requirements files.
