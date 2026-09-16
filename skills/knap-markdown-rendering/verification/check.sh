#!/bin/sh
# Mutation check for run.sh. Each guard is broken ALONE, in a scratch copy, and
# asserted to be the one that fires.
#
# Guards mask each other. A guard only ever seen to fail alongside another has
# not been tested -- which in this corpus is how a dead marker grep survived in
# eight of nine harnesses. Here G-render and G-semantic both watch case c03, so
# each must be shown to fire with the other satisfied.
set -u
here=$(cd "$(dirname "$0")" && pwd)
T=$(mktemp -d); trap 'rm -rf "$T"' EXIT INT HUP
rc=0

scratch() { rm -rf "$T/v"; cp -R "$here" "$T/v"; }

fires() {  # fires <label> <pattern>
    out=$(sh "$T/v/run.sh" 2>&1); got=$?
    if [ "$got" -ne 0 ] && printf '%s' "$out" | grep -qF "$2"; then
        echo "    ok   $1"
    else
        echo "*** $1 (exit $got, expected the guard to fire)"
        printf '%s\n' "$out" | sed 's/^/      /' | tail -12
        rc=1
    fi
}

echo "=== each guard fires on its own defect ==="

# G-render alone: output drifts, exit status and semantics untouched.
scratch
sed -i '' 's/^> A hacker/> A HACKER/' "$T/v/cases/c01-blockquote.expected"
fires "G-render  a case whose output drifts" "c01-blockquote: output differs"

# G-exit alone: the render succeeds and matches, but the expected status is wrong.
scratch
printf '0\n' > "$T/v/cases/c06-unknown-filter.rc"
fires "G-exit    a case whose exit status is wrong" "c06-unknown-filter: exit 1, want 0"

# G-semantic alone: the fence reverts to *** AND its .expected is updated to
# match, so section 1 passes completely. Only the semantic guard can see it.
# This is the exact shape of the 1.0.0 defect.
scratch
printf -- '***\nyear: {{ year }}\n{{ directors | wikilink | yaml_property:"directors" }}\n***\n\n# {{ title }}\n' \
    > "$T/v/cases/c03-frontmatter.knap"
sed -i '' 's/^---$/***/' "$T/v/cases/c03-frontmatter.expected"
out=$(sh "$T/v/run.sh" 2>&1)
if printf '%s' "$out" | grep -qF "ok   c03-frontmatter" \
   && printf '%s' "$out" | grep -qF "front matter is NOT parseable"; then
    echo "    ok   G-semantic fires while G-render is fully SATISFIED"
else
    echo "*** G-semantic should fire with section 1 green (the 1.0.0 defect shape)"
    printf '%s\n' "$out" | sed 's/^/      /' | tail -12
    rc=1
fi

# The harness must refuse rather than pass when the tool is absent.
# A PATH that still has a shell and coreutils, but no knap. Emptying PATH
# entirely tests nothing -- `sh` itself becomes unfindable and the 127 comes
# from the caller, not from the guard.
scratch
out=$(PATH=/usr/bin:/bin /bin/sh "$T/v/run.sh" 2>&1); got=$?
if [ "$got" -eq 2 ]; then
    echo "    ok   absent knap is refused (exit 2), not reported as passing"
else
    echo "*** absent knap gave exit $got, want 2"; rc=1
fi

echo
[ "$rc" -eq 0 ] && echo "ALL GUARD MUTATIONS CAUGHT" || echo "*** GUARD MUTATION FAILURES"
exit $rc
