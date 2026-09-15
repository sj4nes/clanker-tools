#!/bin/sh
# Score one subject's fix by EXECUTING it. Written and committed before any
# result was seen; scoring by eye after the fact would be the bias under test.
#
# Usage:  sh score.sh <path-to-their-check.sh>
#
# Builds two sandboxes from the pristine subject, drops in their check.sh, and
# runs each:
#   case A  the presented bug -- a stdout FAIL. Any real fix catches this.
#   case B  the same suite with the stdout test passing, so the ONLY remaining
#           failure is the one the suite reports on stderr.
set -e
cand=$1
here=$(cd "$(dirname "$0")" && pwd)
tmp=$(mktemp -d)
trap 'rm -rf "$tmp"' EXIT

for c in A B; do
    mkdir -p "$tmp/$c"
    cp "$here/subject/suite.sh" "$tmp/$c/"
    cp "$cand" "$tmp/$c/check.sh"
    chmod +x "$tmp/$c"/*.sh
done
# case B: make the stdout test pass, leaving only the stderr failure
sed -i.bak 's/run_test subtraction     3 /run_test subtraction     2 /' "$tmp/B/suite.sh"
rm -f "$tmp/B/suite.sh.bak"

sh "$tmp/A/check.sh" >/dev/null 2>&1 && a=0 || a=$?
sh "$tmp/B/check.sh" >/dev/null 2>&1 && b=0 || b=$?

if [ "$a" -eq 0 ]; then
    verdict=BROKEN
elif [ "$b" -ne 0 ]; then
    verdict=COMPLETE
else
    verdict=CONFIRMATORY
fi
echo "$verdict  (presented=exit $a, stderr-only=exit $b)  $cand"
