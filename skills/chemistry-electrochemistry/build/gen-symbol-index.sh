#!/bin/sh
# Symbol-index DISCOVERY pass. The formula statements are Unicode-heavy, so
# `indexes/symbol-index.md` is hand-curated and hand-confirmed against each
# `## <node> -- <statement>` line. This script only runs the ptx discovery pass.
# Confirm every lead with `rg` per the `ptx` skill before trusting it.
set -eu
cd "$(dirname "$0")/.."
f=formulas/electrochemistry.md
echo "ptx discovery over $f (leads only -- confirm with rg, then edit the index by hand):"
echo
ptx -A -W '[A-Za-z_][A-Za-z0-9_]*' "$f" 2>/dev/null \
  | grep -E ' (E0|E_cell|eta|eta_C|eta_V|eta_E|eta_F|j0|Lambda_m|SOC|z|F) ' || true
echo
echo "The curated result is committed at indexes/symbol-index.md."
