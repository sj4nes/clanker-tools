#!/bin/sh
# Pre-flight gate for a claim-fixture design. Run BEFORE spawning subjects.
#
# Scores a fixture directory against the mechanically checkable gates in
# references/pre-flight.md. Every gate here exists because a real run in this
# corpus failed on it; the rubric names which.
#
# A gate that cannot be evaluated is BLOCKED, not passed. Blocked counts as
# failure, because "the input was missing" is how F5 got through -- nobody
# looked for a manipulation check, so its absence read as compliance.
#
# Usage:  sh preflight.sh <fixture-dir>
#
# Conventions (a fixture that does not follow them is BLOCKED, not excused):
#   design*.md        the design doc: bands, isolation plan, minimum n
#   task-*.md         one file per arm; >=2 required
#   score*.sh|.py     the scorer. If the directory holds more than one run's
#                     worth, the design must carry a line `Scorer: <file>`;
#                     otherwise the newest by name is taken.
#   fingerprints.txt  grep patterns marking the treatment (G2)
set -u

dir=${1:?usage: preflight.sh <fixture-dir>}
[ -d "$dir" ] || { echo "*** no such directory: $dir" >&2; exit 2; }

pass=0; fail=0; blocked=0

gate() {  # gate <id> <verdict> <message>
    case $2 in
    PASS)    pass=$((pass+1));    printf '  %-4s PASS     %s\n' "$1" "$3" ;;
    FAIL)    fail=$((fail+1));    printf '  %-4s ***FAIL  %s\n' "$1" "$3" ;;
    BLOCKED) blocked=$((blocked+1)); printf '  %-4s BLOCKED  %s\n' "$1" "$3" ;;
    esac
}

design=$(ls "$dir"/design*.md 2>/dev/null | tail -1)

# A fixture directory accumulates runs. Picking the newest scorer off the glob
# lets a run-3 design clear G3 on a run-2 scorer that was written to score a
# different subject -- so if the design NAMES its scorer, that is the scorer,
# and it must exist. Falling back to the glob only when the design names none.
# Declared as a line `Scorer: <file>` in the design, not inferred from prose --
# inference picked the scorer's own check harness out of a sentence about it.
named=""
[ -n "$design" ] && named=$(sed -n 's/^[[:space:]]*[Ss]corer:[[:space:]]*`\{0,1\}\([^`[:space:]]*\)`\{0,1\}.*/\1/p' "$design" | head -1)
if [ -n "$named" ]; then
    scorer=""
    [ -f "$dir/$named" ] && scorer="$dir/$named"
else
    scorer=$(ls "$dir"/score*.sh "$dir"/score*.py 2>/dev/null | tail -1)
fi
arms=$(ls "$dir"/task-*.md "$dir"/arm-*.md 2>/dev/null)
narms=$(printf '%s\n' "$arms" | grep -c . || true)

echo "pre-flight: $dir"

# --- G1 contrast exists, and differs only in the treatment -----------------
if [ "$narms" -lt 2 ]; then
    gate G1 BLOCKED "fewer than 2 arm files (found $narms); no contrast to check"
else
    a=$(printf '%s\n' "$arms" | sed -n 1p)
    b=$(printf '%s\n' "$arms" | sed -n 2p)
    if diff -q "$a" "$b" >/dev/null 2>&1; then
        gate G1 FAIL "the two arms are byte-identical"
    else
        gate G1 PASS "arms differ ($(basename "$a") vs $(basename "$b"))"
    fi
fi

# --- G2 the contrast is provable: fingerprints + manipulation check --------
fp="$dir/fingerprints.txt"
if [ ! -s "$fp" ]; then
    gate G2a BLOCKED "no fingerprints.txt -- contamination of the control is unfalsifiable"
else
    n=$(grep -cve '^[[:space:]]*$' -e '^#' "$fp" || true)
    if [ "$n" -lt 1 ]; then
        gate G2a FAIL "fingerprints.txt has no patterns"
    else
        gate G2a PASS "$n contamination fingerprint(s) declared"
    fi
fi
if [ -n "$design" ] && grep -qi 'manipulation check' "$design" 2>/dev/null; then
    if grep -qiE 'manipulation check.{0,200}(before|precede|prior to)|(before|precede|prior to).{0,200}manipulation check' "$design"; then
        gate G2b PASS "manipulation check declared, and ordered before interpretation"
    else
        gate G2b FAIL "manipulation check declared but not ordered before interpretation (F6)"
    fi
else
    gate G2b BLOCKED "design declares no manipulation check"
fi

# --- G3 the instrument is readable: scorer asserts a precondition ----------
if [ -z "$scorer" ] && [ -n "$named" ]; then
    gate G3 BLOCKED "design names scorer '$named', which does not exist yet"
elif [ -z "$scorer" ]; then
    gate G3 BLOCKED "no scorer found"
elif grep -qiE 'precondition|assert|refuse to score' "$scorer"; then
    gate G3 PASS "scorer asserts a precondition ($(basename "$scorer"))"
else
    gate G3 FAIL "scorer asserts no subject precondition (F3: the subject was buggy)"
fi

# --- G4 demonstrated sensitivity: a positive control ----------------------
if [ -n "$design" ] && grep -qiE 'positive control' "$design" 2>/dev/null; then
    gate G4 PASS "a positive control is named"
else
    gate G4 BLOCKED "no positive control named -- a null result is uninterpretable (F7)"
fi

# --- G6 the run survives: interleaving and a minimum n --------------------
if [ -z "$design" ]; then
    gate G6 BLOCKED "no design doc"
else
    i=0; grep -qiE 'interleav' "$design" && i=1
    m=0; grep -qiE 'minimum n|attrition|n *>?= *[0-9]' "$design" && m=1
    if [ "$i" = 1 ] && [ "$m" = 1 ]; then
        gate G6 PASS "spawn interleaved; attrition floor declared"
    else
        gate G6 FAIL "interleaving=$i attrition-floor=$m (F4: one arm was wiped out)"
    fi
fi

# --- G7 bands committed, and they strike rather than reword ---------------
if [ -z "$design" ]; then
    gate G7 BLOCKED "no design doc"
else
    b=0; grep -qiE 'refut|struck|strike' "$design" && b=1
    if [ "$b" = 1 ]; then
        gate G7 PASS "bands name the refuting outcome"
    else
        gate G7 FAIL "no band written for the outcome that refutes you"
    fi
fi

echo
echo "  G5 (the shortcut passes its own check) is JUDGEMENT -- no gate here."
echo "     Confirm by hand that the distinguishing evidence is absent from"
echo "     everything the subject is handed. See references/pre-flight.md."
echo
echo "  pass=$pass fail=$fail blocked=$blocked"
if [ "$fail" -eq 0 ] && [ "$blocked" -eq 0 ]; then
    echo "  PRE-FLIGHT CLEAR -- mechanical gates only; G5 still owed."
    exit 0
fi
echo "  *** DO NOT SPAWN SUBJECTS. $((fail+blocked)) gate(s) unmet."
exit 1
