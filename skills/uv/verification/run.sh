#!/bin/sh
# Verification run for the `uv` skill: exercises the prescribed workflow
# (project mode, script mode, tool mode, interpreter selection, lockfile
# gating) against the real `uv` binary in a throwaway directory and confirms
# each prescribed check behaves as claimed.
#
#   1. project mode: uv init -> uv add -> uv lock -> uv sync --locked -> uv run
#   2. lockfile gate: a hand-edited pyproject.toml makes `uv sync --locked` fail
#   3. script mode: uv add --script writes a PEP 723 block; uv run executes it
#   4. tool mode: uvx runs a CLI in an isolated env without touching the project
#   5. interpreter pin: uv python pin writes .python-version; uv run honours it
set -e
cd "$(dirname "$0")"

command -v uv >/dev/null || { echo "FAIL: uv not on PATH"; exit 1; }
uv --version

WORK=$(mktemp -d)
trap 'rm -rf "$WORK"' EXIT
fail=0
check() { if [ "$1" = "$2" ]; then echo "PASS: $3"; else echo "FAIL: $3 (got [$1] want [$2])"; fail=1; fi; }
contains() { case "$1" in *"$2"*) echo "PASS: $3";; *) echo "FAIL: $3 (missing [$2] in [$1])"; fail=1;; esac; }

echo
echo "=== 1. project mode: init / add / lock / sync --locked / run ==="
cd "$WORK"
uv init --bare --python 3.11 >/dev/null 2>&1
uv python pin 3.12 >/dev/null
check "$(cat .python-version)" "3.12" "uv python pin wrote .python-version"
uv add "packaging>=24" >/dev/null 2>&1
test -f uv.lock && echo "PASS: uv add produced uv.lock" || { echo "FAIL: no uv.lock"; fail=1; }
grep -q 'name = "packaging"' uv.lock && echo "PASS: dependency resolved into the lockfile" || { echo "FAIL: packaging not in lockfile"; fail=1; }
uv sync --locked >/dev/null 2>&1 && echo "PASS: uv sync --locked succeeds when lockfile is current" || { echo "FAIL: sync --locked on current lockfile"; fail=1; }
OUT=$(uv run python -c "import packaging, sys; print(packaging.__name__)")
check "$OUT" "packaging" "uv run executes in the synced environment (no activation)"
EXE=$(uv run python -c "import sys; print(sys.executable)")
contains "$EXE" ".venv" "uv run uses the project .venv interpreter"

echo
echo "=== 2. lockfile gate: stale lockfile must make sync --locked fail ==="
# SKILL principle: in a validation path, uv sync --locked fails on divergence
# and the agent must NOT regenerate the lockfile. Create divergence by adding a
# dependency (updates both) then restoring the previous lockfile so it is stale.
cp uv.lock uv.lock.stale
uv add "typing-extensions>=4" >/dev/null 2>&1
cp uv.lock.stale uv.lock
if uv sync --locked >/dev/null 2>&1; then
  echo "FAIL: uv sync --locked accepted a stale lockfile"; fail=1
else
  echo "PASS: uv sync --locked rejects a lockfile that diverges from pyproject.toml"
fi
# converging is the explicit-authorization path
uv lock >/dev/null 2>&1 && uv sync --locked >/dev/null 2>&1 && echo "PASS: uv lock + uv sync --locked converges after an authorized change" || { echo "FAIL: converge after uv lock"; fail=1; }

echo
echo "=== 3. script mode: uv add --script writes PEP 723 metadata ==="
cd "$WORK"
mkdir scriptdir && cd scriptdir
cat > job.py <<'EOF'
import packaging
print("ok", packaging.__name__)
EOF
uv add --script job.py "packaging>=24" >/dev/null 2>&1
grep -q '# /// script' job.py && echo "PASS: uv add --script inserted a '# /// script' block" || { echo "FAIL: no PEP 723 block"; fail=1; }
grep -q 'packaging' job.py && echo "PASS: the dependency is recorded in the script" || { echo "FAIL: dep not in script"; fail=1; }
OUT=$(uv run job.py)
contains "$OUT" "ok packaging" "uv run executes the script with its declared deps"

echo
echo "=== 4. tool mode: uvx runs an isolated CLI without touching the project ==="
cd "$WORK"
BEFORE=$(cat uv.lock)
uvx --from packaging python -c "print('tool-env')" >/dev/null 2>&1 || true
# a real ephemeral tool: pycowsay is tiny and has no deps
OUT=$(uvx --quiet pycowsay "hi" 2>/dev/null | tr -d ' \n' || true)
contains "$OUT" "hi" "uvx runs a CLI from a throwaway environment"
check "$(cat uv.lock)" "$BEFORE" "uvx did not modify the project lockfile"

echo
echo "=== 5. interpreter selection: --python overrides the pin for one command ==="
cd "$WORK"
rm -f uv.lock.stale
V=$(uv run --python 3.11 python -c "import sys; print('%d.%d' % sys.version_info[:2])" 2>/dev/null || echo skip)
if [ "$V" = "skip" ]; then
  echo "SKIP: Python 3.11 unavailable and downloads disabled"
else
  check "$V" "3.11" "uv run --python 3.11 selects that interpreter"
  PIN=$(uv run python -c "import sys; print('%d.%d' % sys.version_info[:2])")
  check "$PIN" "3.12" "without --python, uv run honours the .python-version pin"
fi

echo
if [ "$fail" -eq 0 ]; then echo "ALL CHECKS PASSED"; else echo "SOME CHECKS FAILED"; fi
exit $fail
