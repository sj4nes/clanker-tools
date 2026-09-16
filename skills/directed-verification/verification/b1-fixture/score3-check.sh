#!/bin/sh
# Negative contrast for score3.sh -- the instrument's own positive control.
#
# A scorer that returns a number for everything is not a measurement. This
# builds four subjects whose verdicts are known in advance and asserts the
# scorer separates them: a suite that checks nothing scores near 0, an
# oracle-based suite scores 20/20, a suite that fails on the verified-correct
# subject is BROKEN rather than a low score, and an empty directory is
# NO-HARNESS rather than 0 killed.
#
# 0-killed and NO-HARNESS mean opposite things; run 1 of this fixture was
# ruined by a scorer that conflated a good suite with a broken one.
set -u
here=$(cd "$(dirname "$0")" && pwd)
T=$(mktemp -d); trap 'rm -rf "$T"' EXIT INT HUP
rc=0

seed() { mkdir -p "$T/$1"; cp "$here/subject3/duration.py" "$here/subject3/SPEC.md" "$T/$1/"; }

expect() {   # expect <dir> <pattern> <label>
    out=$(sh "$here/score3.sh" "$T/$1" 2>&1)
    if printf '%s' "$out" | grep -q "$2"; then
        echo "    ok   $3"
        echo "         $out" | sed 's/  */ /g'
    else
        echo "*** $3"; printf '%s\n' "$out" | sed 's/^/      /'; rc=1
    fi
}

seed empty
rm "$T/empty/duration.py" "$T/empty/SPEC.md"
expect empty 'NO-HARNESS' "an empty directory is NO-HARNESS, not 0 killed"

seed weak
cat > "$T/weak/test_weak.py" <<'PY'
from duration import parse_duration, format_duration
assert parse_duration("1h 30m") == 5400
assert format_duration(5400) == "1h 30m"
print("ok")
PY
expect weak 'kill=  [0-5]/20' "a suite that checks two happy paths kills at most 5"

seed strong
cat > "$T/strong/test_strong.py" <<'PY'
import re
from duration import parse_duration, format_duration
C = re.compile(r"\A(0|[1-9][0-9]*)([hms])\Z", re.ASCII)
SZ = {"h": 3600, "m": 60, "s": 1}

def ref_parse(t):
    if type(t) is not str: raise ValueError
    ps = t.split(" ")
    if not 1 <= len(ps) <= 3: raise ValueError
    us, vs = [], []
    for p in ps:
        m = C.match(p)
        if m is None: raise ValueError
        vs.append(int(m.group(1))); us.append(m.group(2))
    rk = ["hms".index(u) for u in us]
    if rk != sorted(set(rk)): raise ValueError
    for i, (u, v) in enumerate(zip(us, vs)):
        if i and u in "ms" and v > 59: raise ValueError
    tot = sum(SZ[u] * v for u, v in zip(us, vs))
    if tot >= 360000: raise ValueError
    return tot

def ref_fmt(n):
    if type(n) is not int: raise TypeError
    if not 0 <= n < 360000: raise ValueError
    if n == 0: return "0s"
    h, r = divmod(n, 3600); m, s = divmod(r, 60)
    return " ".join(f"{v}{u}" for v, u in ((h,"h"),(m,"m"),(s,"s")) if v)

def outcome(fn, x):
    try: return ("v", fn(x))
    except Exception as e: return ("e", type(e).__name__)

probes = [ref_fmt(n) for n in range(0, 360000, 13)] + [
    "", " ", "01s", "1h 1h", "1s 1m", "1h 60m", "1H", "1h  1m", " 1s", "1s ",
    "100h", "360000s", "1.5s", "-1s", "１s", "1", "90m", "0h 0m 0s", "99h 3599s",
    5, None, 1.0, True]
for p in probes:
    assert outcome(parse_duration, p) == outcome(ref_parse, p), p
for n in list(range(0, 360000, 11)) + [-1, 360000, 1.0, "5", None, True, False]:
    assert outcome(format_duration, n) == outcome(ref_fmt, n), n
print("ok")
PY
expect strong 'kill= 20/20' "an oracle-based suite kills all 20"

seed broken
cat > "$T/broken/test_broken.py" <<'PY'
from duration import format_duration
assert format_duration(0) == ""     # false of the verified-correct subject
PY
expect broken 'BROKEN' "a suite failing on the correct subject is BROKEN"


# --- and the preconditions themselves must be able to fire -----------------
# P1/P3 are the load-bearing parts of this design. A precondition that cannot
# fail is not a precondition, so each is broken in a scratch COPY of the
# fixture and asserted to refuse to score.
fixture() {  # fixture <name> -- a throwaway copy of the fixture directory
    cp -R "$here" "$T/$1"
    rm -rf "$T/$1/subject" "$T/$1/subject2" "$T/$1/__pycache__"
}
refuses() {  # refuses <fixture> <pattern> <label>
    out=$(sh "$T/$1/score3.sh" "$T/strong" 2>&1); got=$?
    if [ "$got" -eq 2 ] && printf '%s' "$out" | grep -q "$2"; then
        echo "    ok   $3"
    else
        echo "*** $3 (exit $got)"; printf '%s\n' "$out" | sed 's/^/      /'; rc=1
    fi
}

fixture fx1
sed -i '' 's/    if total >= _MAX:/    if total > _MAX:/' "$T/fx1/subject3/duration.py"
refuses fx1 'P1 FAILED' "P1 fires when the reference drifts from the oracle"

fixture fx3
cp "$T/fx3/subject3/duration.py" "$T/fx3/mutants3/m05.py"
refuses fx3 'P3 FAILED' "P3 fires on a mutant equivalent to the reference"

fixture fx4
printf '\n# hand-edited\n' >> "$T/fx4/mutants3/m07.py"
out=$(sh "$T/fx4/score3.sh" "$T/strong" 2>&1); got=$?
if [ "$got" -eq 2 ] && printf '%s' "$out" | grep -q 'P4 FAILED'; then
    echo "    ok   P4 fires when a mutant file drifts from its generator"
else
    echo "*** P4 should fire on a hand-edited mutant (exit $got)"; rc=1
fi

echo
[ "$rc" -eq 0 ] && echo "SCORER CONTRAST PASSED -- the instrument separates weak from strong" \
                || echo "*** SCORER CONTRAST FAILED"
exit $rc
