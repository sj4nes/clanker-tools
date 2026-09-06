#!/bin/sh
set -eu
cd "$(dirname "$0")/.."
PTX=$(command -v ptx || echo /opt/homebrew/opt/coreutils/libexec/gnubin/ptx)
# ptx 9.x errors on some multi-file / blank-line inputs; feed it one clean stream.
grep -h -v '^[[:space:]]*$' results/*.yaml notation.md > build/_corpus.txt
"$PTX" -A -W '[A-Za-z_][A-Za-z0-9_]*' build/_corpus.txt > build/_ptx.raw 2>/dev/null || true
{
  echo "# Symbol / keyword index (ptx discovery + rg confirmation)"
  echo
  echo "ptx -A -W over a cleaned concatenation of results/*.yaml + notation.md"
  echo "(\`build/_ptx.raw\`, $(wc -l < build/_ptx.raw | tr -d ' ') rotations). Per the ptx skill this is a"
  echo "DISCOVERY aid only; each list below is rg-CONFIRMED result nodes."
  echo
  for kw in sup inf limsup liminf Cauchy compact uniform derivative integrable \
            antiderivative partition closure subsequence monotone continuity \
            epsilon completeness bounded convex; do
    printf '## %s\n' "$kw"
    hits=$(rg -l -i -- "$kw" results/*.yaml 2>/dev/null | sed 's#results/##;s#\.yaml##' | sort || true)
    if [ -n "$hits" ]; then echo "$hits" | sed 's/^/- /'; else echo "- (no result YAML; see nodes/ and notation.md)"; fi
    echo
  done
} > indexes/symbol-index.md
echo "gen-symbol-index: ok ($(wc -l < indexes/symbol-index.md | tr -d ' ') lines, $(wc -l < build/_ptx.raw | tr -d ' ') ptx rotations)"
