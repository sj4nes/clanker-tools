#!/bin/sh
# Curated symbol index: for each symbol, the formula nodes whose STATEMENT
# (the text after the em dash on the "## <node> — <formula>" line) uses it as a
# whole token. ptx is the discovery pass; this script is the confirmed result.
set -eu
cd "$(dirname "$0")/.."
f=formulas/thermoacoustics.md
{
  echo "# Symbol index (Release 0.1)"
  echo
  echo "Formula-statement symbol occurrences. Discovery: \`ptx -A -W '[A-Za-z_][A-Za-z0-9_]*' $f\`; results confirmed by whole-token match against each \`## node — statement\` line."
  echo
  for sym in K U E P p J F_net F N W_net W G g k m v a r h x t L A phi mu_k; do
    hits=$(grep -E '^## ' "$f" | sed 's/^## //' | awk -F ' — ' -v s="$sym" '
      NF < 2 { next }
      {
        stmt=$2; gsub(/`/, "", stmt)
        n=split(stmt, toks, /[^A-Za-z0-9_]+/)
        for (i=1;i<=n;i++) if (toks[i]==s) { print "  - `" $1 "` — " $2; next }
      }')
    [ -n "$hits" ] || continue
    printf '### `%s`\n%s\n\n' "$sym" "$hits"
  done
} > indexes/symbol-index.md
echo "wrote indexes/symbol-index.md ($(grep -c '^  - ' indexes/symbol-index.md) entries)"
