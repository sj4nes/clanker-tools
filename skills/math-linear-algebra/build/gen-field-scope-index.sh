#!/bin/sh
set -eu
cd "$(dirname "$0")/.."
out=indexes/field-scope-index.md
{
echo "# Field-scope and choice-grade index (generated)"
echo
echo "Which field a result actually needs, and which form of choice it uses."
echo "See scope.md for the tag vocabulary. A result tagged \`any_field\` holds"
echo "over every field; anything stronger names what it is buying."
echo
echo "## By field_scope"
echo
for r in any_field char_not_2 ordered_field real_or_complex algebraically_closed; do
  echo "### $r"
  grep -l "^field_scope: $r\$" results/*.yaml 2>/dev/null | sed 's#results/##;s#\.yaml##;s/^/- /' | sort || echo "- (none)"
  echo
done
echo "### (untagged — cited roots and conventions)"
grep -L "^field_scope:" results/*.yaml 2>/dev/null | sed 's#results/##;s#\.yaml##;s/^/- /' | sort
echo
echo "## By choice_grade"
echo
for c in choice_free needs_countable_choice needs_full_AC; do
  echo "### $c"
  grep -l "^choice_grade: $c\$" results/*.yaml 2>/dev/null | sed 's#results/##;s#\.yaml##;s/^/- /' | sort || echo "- (none)"
  echo
done
} > $out
echo "gen-field-scope-index: ok"
