#!/bin/sh
# Score one run-3 subject: the fraction of a frozen 20-mutant set that their
# verification KILLS. Usage: sh score3.sh <subject-dir>
#
# Preconditions are asserted, never assumed. Each one is here because its
# absence ruined an earlier run of this fixture:
#
#   P1  the reference agrees with an independently written oracle on every
#       probe          -- run 1 assumed a correct subject; it was buggy, and
#                         good suites were scored BROKEN for failing on it.
#   P2  the probe corpus's own VALID/INVALID labels are honest
#                      -- this one caught a mislabelled probe while it was
#                         being written.
#   P3  every mutant differs from the reference somewhere in the probe domain
#                      -- an equivalent mutant is unkillable and silently
#                         depresses every subject's rate in both arms. One of
#                         the first twenty was equivalent.
#   P4  the committed mutant files still match their generator.
#
# Nothing in the subject's prose is read. The score is an execution.
set -e
here=$(cd "$(dirname "$0")" && pwd)
d=$(cd "$1" && pwd)
export PYTHONDONTWRITEBYTECODE=1   # single-byte mutants written within one
                                   # second otherwise reuse a stale .pyc

# --- P1..P4 ---------------------------------------------------------------
( cd "$here" && python3 - <<'PY'
import sys
import domain3

ref = domain3._reference()
oracle = domain3.load("oracle3.py")

bad = [(a, b) for a, b in zip(domain3.outcomes(ref), domain3.outcomes(oracle)) if a != b]
if bad:
    print(f"*** P1 FAILED: reference disagrees with the oracle on {len(bad)} probe(s)")
    for a, b in bad[:5]:
        print(f"      {a[0]}({a[1]}) ref={a[2]!r} oracle={b[2]!r}")
    sys.exit(2)

label = []
for s in domain3.VALID_NONCANONICAL:
    try:
        ref.parse_duration(s)
    except Exception as e:                                     # noqa: BLE001
        label.append(f"{s!r} labelled valid but raised {type(e).__name__}")
for s in domain3.INVALID:
    try:
        label.append(f"{s!r} labelled invalid but parsed to {ref.parse_duration(s)}")
    except ValueError:
        pass
    except Exception as e:                                     # noqa: BLE001
        label.append(f"{s!r} labelled invalid but raised {type(e).__name__}")
if label:
    print("*** P2 FAILED: the probe corpus lies about its own labels")
    for m in label:
        print("      " + m)
    sys.exit(2)

base = domain3.outcomes(ref)
equiv = []
for n in range(1, 21):
    m = domain3.outcomes(domain3.load(f"mutants3/m{n:02d}.py"))
    diff = [(a, b) for a, b in zip(base, m) if a != b]
    if not diff:
        equiv.append(f"m{n:02d}")
if equiv:
    print("*** P3 FAILED: unkillable mutant(s): " + " ".join(equiv))
    sys.exit(2)
PY
) || { echo "*** PRECONDITION FAILED -- refusing to score" >&2; exit 2; }

( cd "$here" && python3 make_mutants3.py --check >/dev/null ) \
    || { echo "*** P4 FAILED: mutants3/ has drifted from its generator" >&2; exit 2; }

# --- the subject's suite, in a scratch copy --------------------------------
tmp=$(mktemp -d); trap 'rm -rf "$tmp"' EXIT
cp -R "$d"/. "$tmp"/
rm -rf "$tmp"/__pycache__
cp "$here/subject3/duration.py" "$tmp/duration.py"   # pristine, in case they edited it
cp "$here/subject3/SPEC.md"     "$tmp/SPEC.md"

# Find the harness, THEN run it, so a FAILING harness is never read as a
# MISSING one -- the distinction is the difference between 0 killed and
# NO-HARNESS, and they mean opposite things.
cmd=""
for f in verify.sh test.sh run.sh check.sh; do
    [ -f "$tmp/$f" ] && { cmd="sh $f"; break; }
done
if [ -z "$cmd" ]; then
    pys=$(cd "$tmp" && ls test_*.py *_test.py verify*.py check*.py 2>/dev/null || true)
    if [ -n "$pys" ]; then
        if grep -lq 'import pytest\|from pytest' $(cd "$tmp" && echo $pys | tr ' ' '\n' | sed "s|^|$tmp/|") 2>/dev/null; then
            python3 -c 'import pytest' 2>/dev/null \
                || { echo "*** the subject wrote pytest tests and pytest is absent" >&2; exit 2; }
            cmd="python3 -m pytest -q"
        elif grep -l 'unittest' $(echo "$pys" | sed "s|^|$tmp/|") >/dev/null 2>&1 \
             && ! grep -l 'unittest.main()' $(echo "$pys" | sed "s|^|$tmp/|") >/dev/null 2>&1; then
            cmd="python3 -m unittest discover -q"
        else
            cmd=$(printf 'for f in %s; do python3 "$f" || exit 1; done' "$(echo $pys)")
        fi
    fi
fi
[ -z "$cmd" ] && { printf '%-11s kill=  -/20  (nothing runnable)  %s\n' NO-HARNESS "$1"; exit 0; }

# The command is written to a file rather than eval'd inline: a multi-file
# suite expands to a shell loop, and `timeout <loop>` is not a command.
printf '%s\n' "$cmd" > "$tmp/.harness.sh"
TO=""
command -v timeout  >/dev/null 2>&1 && TO="timeout 120"
command -v gtimeout >/dev/null 2>&1 && TO="gtimeout 120"

run() { ( cd "$tmp" && rm -rf __pycache__ && $TO sh .harness.sh ) >/dev/null 2>&1; }

if run; then :; else
    printf '%-11s kill=  -/20  (fails on the verified-correct subject)  %s\n' BROKEN "$1"
    exit 0
fi

killed=0; survivors=""
for n in 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20; do
    cp "$here/mutants3/m$n.py" "$tmp/duration.py"
    if run; then survivors="$survivors m$n"; else killed=$((killed+1)); fi
    cp "$here/subject3/duration.py" "$tmp/duration.py"
done

printf '%-11s kill=%3d/20  survived:%s  %s\n' SCORED "$killed" "${survivors:- none}" "$1"
