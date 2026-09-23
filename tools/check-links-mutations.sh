#!/bin/sh
# Can check-links.py fail?  It reports ALL LINK CHECKS PASSED over 1493 links,
# and a checker only ever run against a clean corpus has demonstrated nothing.
#
# Each mutant is planted in a scratch file inside the repository (so `git
# ls-files` sees it), checked, and removed.  One defect per mutant.
set -e
cd "$(dirname "$0")/.."
PY=python3
scratch="docs/_linkcheck_mutant.md"
fail=0

cleanup() { rm -f "$scratch"; }
trap cleanup EXIT INT TERM

probe() {                      # probe <label> <expect-substring> <body>
    printf '%s\n' "$3" > "$scratch"
    git add -N "$scratch" >/dev/null 2>&1 || true
    out=$($PY tools/check-links.py 2>&1) && status=0 || status=$?
    if [ "$status" -eq 0 ]; then
        echo "*** FAIL $1: DEAD GUARD, mutant passed"; fail=$((fail + 1))
    elif ! printf '%s\n' "$out" | grep -qF "$2"; then
        echo "*** FAIL $1: failed, but not for the stated reason"
        printf '%s\n' "$out" | grep FAIL; fail=$((fail + 1))
    else
        echo "PASS $1"
    fi
    rm -f "$scratch"
    git rm --cached -q "$scratch" >/dev/null 2>&1 || true
}

echo "=== negative control: the corpus is clean ==="
$PY tools/check-links.py >/dev/null || { echo "*** FAIL: corpus is not clean"; exit 1; }
echo "PASS negative control"
echo

echo "=== mutants ==="
probe "broken-path      " "[file]" "# M
[x](./nope-does-not-exist.md)"

probe "broken-anchor    " "[anchor]" "# M
[x](verifying-skills.md#no-such-heading-anywhere)"

probe "good-anchor-lives" "[file]" "# M
A live anchor must NOT fire, so this mutant pairs it with a broken path:
[ok](verifying-skills.md#8-checklist-before-marking-a-skill-verified)
[bad](./nope.md)"

# A link inside a fence, and inside an inline span, must both stay invisible:
# if either fires, the masking regressed and every skeleton and every typst
# migration row becomes a false positive again.
printf '%s\n' "# M
\`\`\`markdown
[fenced](./not-real-at-all.md)
\`\`\`
An inline example: \`[t](u)\` and \`![a](img.png)\`." > "$scratch"
git add -N "$scratch" >/dev/null 2>&1 || true
if $PY tools/check-links.py >/dev/null 2>&1; then
    echo "PASS code-is-not-a-link  (fenced + inline examples stay invisible)"
else
    echo "*** FAIL code-is-not-a-link: a link inside code was reported"
    $PY tools/check-links.py 2>&1 | grep FAIL; fail=$((fail + 1))
fi
rm -f "$scratch"; git rm --cached -q "$scratch" >/dev/null 2>&1 || true

echo
if [ "$fail" -eq 0 ]; then
    echo "ALL LINK MUTATION CHECKS PASSED"
else
    echo "*** $fail LINK MUTATION CHECK(S) FAILED" >&2; exit 1
fi
