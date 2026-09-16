#!/bin/sh
# Verification for knap-markdown-rendering (tool-fact).
#
# A tool-fact skill owes reference material, and reference material is only
# worth anything if it is TRUE OF THE INSTALLED TOOL. So every documented
# template in references/ has a case here, and each case is RENDERED BY THE
# REAL knap and diffed against expected output captured from it. A claim in the
# prose that no case covers is a claim nobody checked.
#
# Three independent guards, each broken alone in check.sh:
#   G-render   a case's output differs from its .expected
#   G-exit     a case's exit status differs from its .rc (default 0)
#   G-semantic a property the prose asserts that diffing cannot see
#
# G-semantic exists because of the defect that prompted this rebuild. Version
# 1.0.0 documented `***` as a YAML front-matter fence. Every render of it
# matched its own expected output perfectly -- it is stable, deterministic, and
# unparseable by any front-matter consumer. A diff harness alone would have
# certified it forever.
set -u
cd "$(dirname "$0")"
rc=0

command -v knap >/dev/null 2>&1 || { echo "*** knap is not on PATH"; exit 2; }
VER=$(knap --version 2>&1 | tr -d ' ')
echo "knap $VER"
case "$VER" in
    0.6.*) ;;
    *) echo "    note: these cases were captured against 0.6.0; $VER may differ" ;;
esac

echo
echo "=== 1. every documented template renders as documented ==="
for t in cases/*.knap; do
    name=$(basename "$t" .knap)
    want_rc=0
    [ -f "cases/$name.rc" ] && want_rc=$(cat "cases/$name.rc")
    got=$(knap render "$t" -d cases/movie.json 2>&1); got_rc=$?

    if [ "$got_rc" -ne "$want_rc" ]; then
        echo "*** $name: exit $got_rc, want $want_rc"          # G-exit
        rc=1
        continue
    fi
    if ! printf '%s\n' "$got" | diff -u "cases/$name.expected" - > "/tmp/knap-$name.diff" 2>&1; then
        echo "*** $name: output differs from cases/$name.expected"   # G-render
        sed 's/^/      /' "/tmp/knap-$name.diff" | head -20
        rc=1
        continue
    fi
    echo "    ok   $name"
done

echo
echo "=== 2. semantics a diff cannot see ==="

# The fence must actually BE front matter. `***` renders stably and is not.
fm=$(knap render cases/c03-frontmatter.knap -d cases/movie.json 2>&1)
if printf '%s\n' "$fm" | python3 -c 'import re,sys; sys.exit(0 if re.match(r"\A---\n.*?\n---\n", sys.stdin.read(), re.S) else 1)'; then
    echo "    ok   c03 front matter is delimited by --- and parses as front matter"
else
    echo "*** c03 front matter is NOT parseable: the fence is not ---"
    printf '%s\n' "$fm" | head -3 | sed 's/^/      /'
    rc=1
fi

# A missing variable renders empty AND exits 0. This is the fact most likely to
# ruin a document silently, so the skill states it and this pins it.
out=$(knap render cases/c04-missing-is-silent.knap -d cases/movie.json 2>&1); st=$?
if [ "$st" -eq 0 ] && [ "$out" = "A[]B[]C" ]; then
    echo "    ok   c04 a missing variable renders empty and exits 0 (still true)"
else
    echo "*** c04 missing-variable behaviour changed: exit $st, output '$out'"
    echo "      references/failure-modes.md is now wrong; fix the doc, not this."
    rc=1
fi

# validate is a STATIC check. The skill says so; this proves it still is.
knap validate -t '{% if a %}x' >/dev/null 2>&1 && { echo "*** validate accepted an unclosed tag"; rc=1; } \
    || echo "    ok   validate rejects a syntax error"
if knap validate -t '{{ definitely_not_in_any_data }}' >/dev/null 2>&1; then
    echo "    ok   validate ACCEPTS an undefined variable (static only, as documented)"
else
    echo "*** validate now checks runtime values; references/failure-modes.md is wrong"
    rc=1
fi

echo
[ "$rc" -eq 0 ] && echo "ALL KNAP CHECKS PASSED" || echo "*** KNAP CHECKS FAILED"
exit $rc
