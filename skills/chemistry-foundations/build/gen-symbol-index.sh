#!/bin/sh
# Symbol-index DISCOVERY pass. The formula statements are Unicode-heavy
# (subscripts, Greek, primed symbols), so unlike physics-newtonian this index is
# NOT mechanically generated — `indexes/symbol-index.md` is hand-curated and
# hand-confirmed against each `## <node> — <statement>` line. This script only
# runs the ptx discovery pass the curator starts from; confirm every lead with
# `rg` per the `ptx` skill before trusting it.
set -eu
cd "$(dirname "$0")/.."
f=formulas/chemistry-foundations.md
echo "ptx discovery over $f (leads only — confirm with rg, then edit the index by hand):"
echo
ptx -A -W '[A-Za-z_][A-Za-z0-9_]*' "$f" 2>/dev/null | grep -E ' (K_a|K_b|K_w|K_c|K_p|N_A|A_r|pH|pOH|pK_a) ' || true
echo
echo "The curated result is committed at indexes/symbol-index.md."
