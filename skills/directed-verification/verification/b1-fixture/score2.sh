#!/bin/sh
# Score one subject by EXECUTING their verification. Rerun of a fixture whose
# first version was invalid.
#
# Usage: sh score2.sh <subject-dir>
#
# THE PRECONDITION THAT FAILED LAST TIME IS NOW ASSERTED, not assumed. Run 1's
# subject carried real bugs, so a GOOD harness failed on the clean file and was
# scored BROKEN -- the measurement inverted quality for the best subjects. This
# scorer refuses to run unless the pristine subject is verified correct against
# an independent oracle first.
set -e
here=$(cd "$(dirname "$0")" && pwd)
d=$(cd "$1" && pwd)

# --- precondition: the pristine subject is correct -------------------------
python3 - "$here/subject2/rounding.py" <<'PY' || { echo "*** PRECONDITION FAILED: subject is not correct" >&2; exit 2; }
import sys, math, importlib.util
from fractions import Fraction
sp = importlib.util.spec_from_file_location("s", sys.argv[1])
m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m)
def oracle(n, d):
    x = Fraction(n, d); s = -1 if x < 0 else 1
    return s * math.floor(abs(x) + Fraction(1, 2))
bad = sum(1 for dd in range(1, 25) for n in range(-600, 601)
          if m.round_half_away(n, dd) != oracle(n, dd))
sys.exit(1 if bad else 0)
PY

tmp=$(mktemp -d); trap 'rm -rf "$tmp"' EXIT
cp -R "$d"/. "$tmp"/
cp "$here/subject2/rounding.py" "$tmp/rounding.py"   # pristine, in case they edited it

# find the harness, THEN run it, so a failing harness is not read as a missing one
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
[ -z "$cmd" ] && { printf '%-12s (nothing runnable)  %s\n' NO-HARNESS "$1"; exit 0; }

( cd "$tmp" && $cmd ) >/dev/null 2>&1 && pre=0 || pre=1
python3 "$here/plant.py" "$tmp/rounding.py"
( cd "$tmp" && $cmd ) >/dev/null 2>&1 && post=0 || post=1

if   [ "$pre"  -ne 0 ]; then v=BROKEN        # fails on a VERIFIED-correct subject
elif [ "$post" -eq 0 ]; then v=CANNOT-FAIL   # passes the planted defect
else                        v=CATCHES; fi
printf '%-12s (clean=%s planted=%s)  %s\n' "$v" "$pre" "$post" "$1"
