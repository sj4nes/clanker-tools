#!/bin/sh
# Full pipeline for the physics-thermodynamics capsule (Release 0.1).
set -eu
cd "$(dirname "$0")/.."

echo "=== graph-check + tsort + reverse deps ==="
sh build/build-tree.sh

echo
echo "=== views ==="
sh build/gen-topic-index.sh
sh build/gen-assumption-index.sh
sh build/gen-prereq-paths.sh

echo
echo "=== dimensional checks (bc, [M L T Theta N]) ==="
# `bc`'s `quit` ALWAYS exits 0, so neither $? nor `set -e` can catch a failed
# check -- the OUTPUT must be inspected.  Both conditions below are needed:
# the banner alone would be satisfied by a file that never reached its later
# sections, the absence of FAIL alone by one that crashed before printing.
# See docs/bc-verification-audit.md.
bcout=$(bc -q -l validation/dimensional-checks.bc)
printf '%s\n' "$bcout"
if ! printf '%s\n' "$bcout" | grep -q "ALL BC CHECKS PASSED" \
   || printf '%s\n' "$bcout" | grep -qF '*** FAIL'; then
    echo "bc checks FAILED" >&2
    exit 1
fi

echo
echo "=== derivation algebra (lean, instance checks) ==="
if command -v lean >/dev/null 2>&1; then
  lean validation/derivation-checks.lean && echo "lean: all instance checks pass (exit 0)"
else
  echo "lean not found -- skipping (checks are documented in validation/derivation-checks.lean)"
fi

echo
echo "run.sh: ok"
