# `uv` agent playbooks

Worked end-to-end runs. Companion to [`../SKILL.md`](../SKILL.md). Each names the
side-effect class of every command (see the SKILL's table).

## A. Validate an existing uv project

```sh
# inspect
ls pyproject.toml uv.lock .python-version            # inspect
uv --version                                          # inspect
grep -n 'requires-python' pyproject.toml              # inspect

# converge to the committed state — fails if the lockfile is stale
uv sync --locked                                      # repo-modifying (.venv only)

# verify
uv run python -c "import sys; print(sys.executable)"  # inspect
uv run python --version                               # inspect
uv run python -m pytest                               # inspect
uv run ruff check .                                   # inspect
```

If `uv sync --locked` reports the lockfile is out of date, **stop**. Do not run
`uv lock` to "fix" it inside a validation task — report the divergence. Regenerate
only when the task is explicitly about changing dependencies.

## B. Migrate a requirements-based project

```sh
ls requirements*.txt requirements*.in                 # inspect
uv venv --python 3.12                                 # repo-modifying (.venv)

# if only an unpinned .in exists, compile first
uv pip compile requirements.in --universal -o requirements.txt   # repo-modifying

uv pip sync requirements.txt                          # DESTRUCTIVE (removes unlisted)
.venv/bin/python -m pytest                            # inspect

# optional: adopt project mode
uv init --bare                                        # repo-modifying
# then translate top-level pins into `uv add` calls, and:
uv lock && uv sync                                    # repo-modifying
git diff -- pyproject.toml uv.lock                    # inspect
```

`uv pip sync` is destructive reconciliation: it removes any installed package not
in `requirements.txt`. Run it only in an environment with no hand-managed
packages you need to keep.

## C. Compatibility matrix

```sh
uv python list                                        # inspect
for v in 3.10 3.11 3.12 3.13; do
  echo "=== $v ==="
  uv run --python "$v" python -m pytest || { echo "FAIL on $v"; exit 1; }
done
```

State the versions from `requires-python` or the support policy — not from
"what's installed". `uv` downloads a missing interpreter unless
`--no-managed-python` is set.

## D. Ephemeral tooling (no project mutation)

```sh
uvx ruff check .                                      # inspect
uvx "ruff@0.9.0" check .                              # inspect (pinned)
uvx black --check .                                   # inspect
uvx --from httpie http GET https://example.com        # inspect
uvx mypy src/                                         # inspect
```

If the tool's behavior affects committed code (a formatter that will be
committed, a codegen step), pin the version. If the repo should own the tool
version, make it a dev dependency instead:

```sh
uv add --dev ruff                                     # repo-modifying
uv run ruff check .                                   # inspect
```

## E. Edited `pyproject.toml` by hand → converge

```sh
git diff -- pyproject.toml                            # inspect — confirm your edit
uv lock                                               # repo-modifying (uv.lock)
uv sync                                               # repo-modifying (.venv)
git diff -- uv.lock                                   # inspect — review resolution
uv run python -m pytest                               # inspect
```

Prefer `uv add` / `uv remove` over hand-editing; they keep all three artifacts
(`pyproject.toml`, `uv.lock`, `.venv`) consistent in one step.

## F. Safe release sequence

```sh
uv lock --check                                       # inspect
uv sync --all-groups                                  # repo-modifying (.venv)
uv run ruff check .                                   # inspect
uv run python -m pytest                               # inspect
uv build                                              # repo-modifying (dist/)

ls -l dist/                                           # inspect — name + version
uv venv /tmp/pkg-test --python 3.12                   # repo-modifying (throwaway)
/tmp/pkg-test/bin/python -m pip install dist/*.whl    # inspect
/tmp/pkg-test/bin/python -c "import your_package; print(your_package.__version__)"

# Only after explicit authorization, confirmed version, confirmed index:
uv publish                                            # DESTRUCTIVE / external
```

Checklist before `uv publish`: version not already released; distribution name
correct; target index correct; credentials from `UV_PUBLISH_TOKEN` or trusted
publishing, not a flag. Publishing is irreversible.

## G. One-file script

```sh
uv add --script report.py "requests>=2.32" "rich>=13"   # repo-modifying (the file)
cat report.py                                            # inspect — the PEP 723 block
uv run report.py                                         # inspect

# one-time dep without editing the file:
uv run --with pandas report.py                           # inspect
```

The inline block should carry `requires-python` and constrained dependency
versions. Migrate to a locked project once the script is maintained.
