#!/bin/sh
# Verification run for the `typst` skill: exercises the mechanics SKILL.md
# prescribes against the real `typst` binary in a throwaway directory.
#
#   1. the split-body #include entrypoint compiles to a multi-page PDF
#   2. a broken cross-reference makes `typst compile` FAIL (not silently pass)
#   3. LaTeX math pasted into `$ $` FAILS; the Typst-native form compiles
#   4. a preamble `#show` rule propagates to the heading; inline styling does
#      not (editing the rule changes the show-rule doc's output, not the
#      inline doc's) -- the content/formatting-separation claim
#   5. font resolution is path-dependent: --ignore-system-fonts sees fewer
#      families than the default search
set -e
cd "$(dirname "$0")"
TEMPLATES="$(cd ../templates && pwd)"

command -v typst >/dev/null || { echo "FAIL: typst not on PATH"; exit 1; }
typst --version

WORK=$(mktemp -d)
trap 'rm -rf "$WORK"' EXIT
fail=0
check() { if [ "$1" = "$2" ]; then echo "PASS: $3"; else echo "FAIL: $3 (got [$1] want [$2])"; fail=1; fi; }
ok()    { if [ "$1" -eq 0 ]; then echo "PASS: $2"; else echo "FAIL: $2"; fail=1; fi; }
no()    { if [ "$1" -ne 0 ]; then echo "PASS: $2"; else echo "FAIL: $2 (expected failure)"; fail=1; fi; }
run()   { rc=0; "$@" >"$WORK/cmd.log" 2>&1 || rc=$?; }

echo
echo "=== 1. split-body #include entrypoint compiles to a multi-page PDF ==="
cp -R "$TEMPLATES/." "$WORK/doc/"
cd "$WORK/doc"
mkdir -p build
typst compile --diagnostic-format short manuscript.typ build/out.pdf 2>&1
ok $? "template manuscript.typ compiles"
test -f build/out.pdf && echo "PASS: build/out.pdf exists" || { echo "FAIL: no PDF"; fail=1; }
# rasterise per page to count pages without a PDF library
typst compile manuscript.typ "build/p-{p}.png" --ppi 60 >/dev/null 2>&1
PAGES=$(ls build/p-*.png | wc -l | tr -d ' ')
if [ "$PAGES" -ge 2 ]; then echo "PASS: rendered $PAGES pages (split body + back matter)"; else echo "FAIL: only $PAGES page(s)"; fail=1; fi

echo
echo "=== 2. a broken cross-reference must make compile FAIL ==="
cd "$WORK/doc"
mkdir -p build
printf '\nSee @eq:does-not-exist for the closed form.\n' >> sections/introduction.typ
run typst compile --diagnostic-format short manuscript.typ build/broken.pdf
no $rc "unresolved @eq:does-not-exist is a hard error"
grep -qi 'label\|reference' "$WORK/cmd.log" && echo "PASS: the diagnostic names the reference problem" || echo "NOTE: diagnostic text: $(cat "$WORK/cmd.log")"
cp -R "$TEMPLATES/." "$WORK/doc/"   # restore

echo
echo "=== 3. LaTeX math in \$ \$ fails; native Typst math compiles ==="
cd "$WORK"
cat > latex.typ <<'EOF'
The ratio is $ \frac{a}{b} $ exactly.
EOF
run typst compile --diagnostic-format short latex.typ latex.pdf
no $rc "\$ \\frac{a}{b} \$ (LaTeX) does not compile"
cat > native.typ <<'EOF'
The ratio is $ a / b $ exactly, and also $ frac(a, b) $.
EOF
run typst compile --diagnostic-format short native.typ native.pdf
ok $rc "native a/b and frac(a, b) in dollar-math compile"

echo
echo "=== 4. preamble #show rule propagates; inline styling does not ==="
cd "$WORK"
mkdir showcase && cd showcase
# doc A: semantic heading, styled by a preamble show rule
cat > pre-a.typ <<'EOF'
#let base(body) = { show heading.where(level: 2): set text(size: 13pt); body }
EOF
cat > doc-a.typ <<'EOF'
#import "pre-a.typ": base
#show: base
== Methods
EOF
# doc B: same visual today, but hard-coded inline
cat > doc-b.typ <<'EOF'
#import "pre-a.typ": base
#show: base
#text(size: 13pt, weight: "regular")[Methods]
EOF
typst compile doc-a.typ a1.svg >/dev/null 2>&1
typst compile doc-b.typ b1.svg >/dev/null 2>&1
# now change ONE line in the shared preamble: 13pt -> 22pt
cat > pre-a.typ <<'EOF'
#let base(body) = { show heading.where(level: 2): set text(size: 22pt); body }
EOF
typst compile doc-a.typ a2.svg >/dev/null 2>&1
typst compile doc-b.typ b2.svg >/dev/null 2>&1
if cmp -s a1.svg a2.svg; then echo "FAIL: preamble change did not affect the semantic-heading doc"; fail=1; else echo "PASS: editing the #show rule changed doc-a's output"; fi
if cmp -s b1.svg b2.svg; then echo "PASS: the same edit left the inline-styled doc unchanged (anti-pattern isolates styling from the preamble)"; else echo "FAIL: inline-styled doc unexpectedly changed"; fail=1; fi

echo
echo "=== 5. font resolution is path-dependent ==="
ALL=$(typst fonts | wc -l | tr -d ' ')
BARE=$(typst fonts --ignore-system-fonts | wc -l | tr -d ' ')
echo "system search: $ALL families; embedded-only: $BARE"
if [ "$ALL" -gt "$BARE" ]; then echo "PASS: --ignore-system-fonts resolves fewer families (font set depends on search path)"; else echo "FAIL: font search path made no difference"; fail=1; fi

echo
if [ "$fail" -eq 0 ]; then echo "ALL CHECKS PASSED"; else echo "SOME CHECKS FAILED"; fi
exit $fail
