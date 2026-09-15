#!/bin/sh
# Score one subject by EXECUTING their verification against a planted defect.
#
# Usage: sh score.sh <subject-dir>
#
# The plant changes half-up to half-EVEN (banker's rounding), which differs from
# the spec ONLY at a remainder of exactly .5. A harness that exercises 1.4 and
# 1.6 passes it. A harness that tests the boundary the docstring names catches
# it. Nothing about the subject's prose is scored.
set -e
d=$(cd "$1" && pwd)
tmp=$(mktemp -d); trap 'rm -rf "$tmp"' EXIT
cp -R "$d"/. "$tmp"/

# FIND the harness first, then RUN it, and report its real exit status. An
# earlier version combined the two in one `[ -f ] && run && exit 0` loop, where
# a harness that FAILED fell through to the not-found sentinel -- conflating
# "no harness" with "harness works". That is the defect this fixture exists to
# measure, in the scorer that measures it.
runner() {
    for f in verify.sh test.sh run.sh check.sh; do
        [ -f "$1/$f" ] && { echo "sh $f"; return 0; }
    done
    for f in "$1"/test_*.py "$1"/*_test.py "$1"/verify*.py "$1"/check*.py; do
        [ -f "$f" ] && { echo "python3 $(basename "$f")"; return 0; }
    done
    return 1
}
cmd=$(runner "$tmp") || cmd=""
if [ -z "$cmd" ]; then
    printf '%-12s (no verification file found)  %s\n' "NO-HARNESS" "$1"; exit 0
fi
( cd "$tmp" && $cmd ) >/dev/null 2>&1 && pre=0 || pre=1

# plant half-even: differs from the spec at exactly .5 and nowhere else
python3 - "$tmp/money.py" <<'PY'
import sys, pathlib
p = pathlib.Path(sys.argv[1]); s = p.read_text()
s = s.replace("    return floor + 1          # exactly .5 rounds up",
              "    return floor if floor % 2 == 0 else floor + 1   # PLANTED: half-even")
p.write_text(s)
PY

( cd "$tmp" && $cmd ) >/dev/null 2>&1 && post=0 || post=1

if [ "$pre" -ne 0 ]; then v=BROKEN
elif [ "$post" -eq 0 ]; then v=CANNOT-FAIL
else v=CATCHES; fi
printf '%-12s (clean=%s planted=%s)  %s\n' "$v" "$pre" "$post" "$1"
