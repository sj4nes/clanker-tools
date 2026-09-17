#!/bin/sh
# Freshness gate over the generated parts of the book, in the spirit of
# tools/check-skills.sh.  Asserts what reading the PDF cannot:
#
#   1. tools/typstlib.py's escaping self-test passes
#   2. Part IV (parts/04-catalogue/01-entries.typ) is what gen-catalogue.py
#      produces from skills/*/ RIGHT NOW
#   3. Part V (parts/05-open/01-backlog.typ) is what gen-open.py produces from
#      BACKLOG.md RIGHT NOW
#   4. the book still compiles
#
# Exists because Parts IV and V state ~500 facts that live somewhere else.
# Without this, "generated" degrades to "was generated once", which is a
# hand-written catalogue with a misleading banner on it -- and the book spends
# Part III on checks that had no way of failing.
#
# A failure here is not fixed by editing the generated file.  Either the
# repository changed (re-run the generator and commit the result) or the
# generator changed (same).
#
#   sh docs/book/tools/check-book.sh          gate
#   sh docs/book/tools/check-book.sh --fix    regenerate, then gate
set -e
cd "$(dirname "$0")/.."      # docs/book
fail=0
gates=""

note() { gates="$gates $1"; fail=$((fail + 1)); }

check_generated() {
    part="$1"; committed="$2"; gen="$3"
    if ! python3 "tools/$gen" --stdout > "$TMP/want.typ" 2> "$TMP/gen.txt"; then
        echo "*** FAIL: $gen exited non-zero"
        sed -n '1,6p' "$TMP/gen.txt"
        note "$(basename "$gen" .py)"; return
    fi
    if ! diff -u "$committed" "$TMP/want.typ" > "$TMP/d.txt"; then
        echo "*** FAIL: $part is STALE -- $committed does not match $gen"
        sed -n '3,25p' "$TMP/d.txt"
        echo "    fix: python3 docs/book/tools/$gen   (then commit)"
        note "$4"
    fi
}

TMP=$(mktemp -d)
trap 'rm -rf "$TMP"' EXIT

if [ "$1" = "--fix" ]; then
    python3 tools/gen-catalogue.py
    python3 tools/gen-open.py
fi

if ! python3 tools/typstlib.py; then
    echo "*** FAIL: typstlib self-test"
    note typstlib
fi

check_generated "Part IV" parts/04-catalogue/01-entries.typ gen-catalogue.py part4
check_generated "Part V"  parts/05-open/01-backlog.typ      gen-open.py part5

if ! typst compile book.typ "$TMP/book.pdf" 2> "$TMP/typst.txt"; then
    echo "*** FAIL: typst compile"
    sed -n '1,20p' "$TMP/typst.txt"
    note compile
elif [ -s "$TMP/typst.txt" ]; then
    # A Typst WARNING is how `**bold**` pasted from Markdown renders as two
    # empty bolds -- it compiles, and the text silently disappears.  See
    # README.md, "Defects found by looking at the PDF, not the exit code".
    echo "*** FAIL: typst compiled with warnings"
    sed -n '1,20p' "$TMP/typst.txt"
    note warnings
fi

echo
echo "gates:$gates"
if [ "$fail" -eq 0 ]; then
    echo "ALL BOOK CHECKS PASSED"
else
    echo "*** $fail BOOK CHECK(S) FAILED" >&2
    exit 1
fi
