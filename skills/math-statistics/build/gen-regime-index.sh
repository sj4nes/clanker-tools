#!/bin/sh
set -eu
cd "$(dirname "$0")/.."
out=indexes/regime-index.md
echo "# Regime index (generated)" > $out
echo >> $out
echo "Every result YAML carrying a \`regime:\` tag, grouped. See scope.md." >> $out
echo >> $out
for r in exact asymptotic distribution_free bayesian; do
  echo "## $r" >> $out
  grep -l "^regime: $r\$" results/*.yaml | sed 's#results/##;s#\.yaml##;s/^/- /' | sort >> $out
  echo >> $out
done
echo "gen-regime-index: ok"
