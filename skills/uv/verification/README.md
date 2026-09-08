# Verifying the `uv` skill

## What verification means for this skill

`uv` wraps a real CLI, so verification runs the workflow `SKILL.md` prescribes
against the actual `uv` binary in a throwaway directory and asserts each
prescribed check behaves as claimed — including the negative contrast (a stale
lockfile *must* make `uv sync --locked` fail).

## Case

A minimal bare project (`uv init --bare`), one real dependency (`packaging`), one
PEP 723 script, one ephemeral `uvx` tool (`pycowsay`), and two locally available
interpreters (3.11, 3.12). Small, deterministic, no network beyond what `uv`
caches on first run.

## Run

```sh
sh skills/uv/verification/run.sh
```

`uv 0.12.3`, macOS `/bin/sh`, Python 3.11 / 3.12 present. Wall time a few seconds
(longer on the first run while `uv` populates its cache).

## What each step demonstrates

| SKILL step | Prescribed check | Result |
|---|---|---|
| §1 identify + §6 pin | `uv python pin` writes `.python-version` | file contains `3.12` |
| §2 project mode | `uv add` creates `uv.lock`; the dep resolves into it | `name = "packaging"` present |
| §2 / §7 | `uv run` executes in the synced env with no activation; `sys.executable` is under `.venv` | both PASS |
| §2 CI rule | `uv sync --locked` succeeds on a current lockfile | PASS |
| §2 CI rule (negative) | a lockfile diverging from `pyproject.toml` makes `uv sync --locked` **fail** | PASS — the guardrail fires |
| §2 authorized path | `uv lock` + `uv sync --locked` converges after an intended change | PASS |
| §4 script mode | `uv add --script` inserts a `# /// script` block and records the dep; `uv run job.py` runs it | PASS |
| §5 tool mode | `uvx` runs a CLI from a throwaway env and does **not** modify `uv.lock` | PASS — lockfile byte-identical before/after |
| §6 interpreter | `uv run --python 3.11` selects 3.11; without it, `uv run` honours the `.python-version` pin (3.12) | PASS |

## Findings folded back into the skill

- `uv init` sets `requires-python` from the interpreter it is given
  (`>=3.13` under a 3.14 system Python), which then rejects a lower `uv python
  pin`. The verification pins the project's floor explicitly with
  `uv init --bare --python 3.11`. No change needed to the skill body — the SKILL
  already tells the agent to pin the interpreter explicitly and read
  `requires-python` in step 1.
- No correctness fix needed in the skill body. The workflow, the side-effect
  classification, and the `uv sync --locked` gate all held as written.

## The gates are necessary, not sufficient

The run confirms the mechanics (commands exist, flags behave, the lockfile gate
fires). It does not check judgement: whether project vs pip-compat vs script mode
is the right path for a given repo, whether a dependency *should* be added, or
whether a `uv publish` is authorized. Those stay with the agent and the SKILL's
side-effect table.
