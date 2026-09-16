#!/bin/sh
# Negative-contrast harness for preflight.sh.
#
# A gate that only ever fails is as useless as one that only ever passes. This
# builds a COMPLIANT fixture, asserts the gate clears it, then breaks one gate
# at a time and asserts the gate that fires is the SPECIFIC one broken -- not
# merely a nonzero exit.
#
# That is G4 (demonstrated sensitivity) applied to the pre-flight gate itself,
# which is the check claim-fixture has never run on its own method.
set -u
cd "$(dirname "$0")"
PF="sh ./preflight.sh"
T=$(mktemp -d)
trap 'rm -rf "$T"' EXIT INT HUP
rc=0

build() {  # build <dir> -- a fixture that should clear every mechanical gate
    d=$1; mkdir -p "$d"
    cat > "$d/design1.md" <<'EOD'
# Design
Bands: Δ>=+3 supported; 0 REFUTED, and the claim is struck rather than reworded.
Spawn order is interleaved A1 B1 A2 B2 so truncation costs both arms equally.
Minimum n = 5 per arm; below that the run is void. Attrition reported.
A manipulation check runs BEFORE the outcome is interpreted; failure voids it.
Positive control: a subject handed the answer must score CATCHES, confirming
the instrument can detect an effect it knows is there.
EOD
    printf 'Do the task.\n'                      > "$d/task-A.md"
    printf 'Do the task. It must be able to fail.\n' > "$d/task-B.md"
    printf 'Name the risky area first\ntest-writing\n' > "$d/fingerprints.txt"
    printf '#!/bin/sh\n# assert precondition before scoring\nexit 0\n' > "$d/score.sh"
}

expect() {  # expect <label> <want-exit> <want-token>
    lbl=$1; want=$2; tok=$3
    out=$($PF "$T/f" 2>&1); got=$?
    if [ "$got" -ne "$want" ]; then
        echo "*** $lbl: exit $got, want $want"; echo "$out" | sed 's/^/      /'; rc=1; return
    fi
    if [ -n "$tok" ] && ! printf '%s' "$out" | grep -q "$tok"; then
        echo "*** $lbl: expected gate '$tok' to fire"; echo "$out" | sed 's/^/      /'; rc=1; return
    fi
    echo "    ok   $lbl"
}

echo "=== 1. the gate clears a compliant design (positive control) ==="
rm -rf "$T/f"; build "$T/f"
expect "compliant fixture clears all mechanical gates" 0 "PRE-FLIGHT CLEAR"

echo
echo "=== 2. each gate fires on its OWN defect ==="

rm -rf "$T/f"; build "$T/f"; cp "$T/f/task-A.md" "$T/f/task-B.md"
expect "G1  identical arms"              1 "G1   \*\*\*FAIL"

rm -rf "$T/f"; build "$T/f"; rm "$T/f/fingerprints.txt"
expect "G2a no fingerprint list"         1 "G2a  BLOCKED"

rm -rf "$T/f"; build "$T/f"; : > "$T/f/fingerprints.txt"
expect "G2a empty fingerprint list"      1 "G2a  BLOCKED"

rm -rf "$T/f"; build "$T/f"
sed -i '' 's/A manipulation check runs BEFORE the outcome is interpreted; failure voids it./A manipulation check is performed./' "$T/f/design1.md"
expect "G2b check declared but unordered" 1 "G2b  \*\*\*FAIL"

rm -rf "$T/f"; build "$T/f"
sed -i '' '/manipulation check/d' "$T/f/design1.md"
expect "G2b no manipulation check"       1 "G2b  BLOCKED"

rm -rf "$T/f"; build "$T/f"
printf '#!/bin/sh\nexit 0\n' > "$T/f/score.sh"
expect "G3  scorer without precondition" 1 "G3   \*\*\*FAIL"

rm -rf "$T/f"; build "$T/f"
sed -i '' '/[Pp]ositive control/d' "$T/f/design1.md"
expect "G4  no positive control"         1 "G4   BLOCKED"

rm -rf "$T/f"; build "$T/f"
sed -i '' '/interleaved/d' "$T/f/design1.md"
expect "G6  no interleaving"             1 "G6   \*\*\*FAIL"

rm -rf "$T/f"; build "$T/f"
sed -i '' '/Bands:/d' "$T/f/design1.md"
expect "G7  no refuting band"            1 "G7   \*\*\*FAIL"

echo
echo "=== 3. the gate blocks the run that actually failed ==="
B=../../directed-verification/verification/b1-fixture
# The b1 fixture is a live artifact: as it is repaired, the gate that stops it
# moves. What must hold is that it is STILL BLOCKED -- never that a specific
# gate fires -- so this asserts the block and NAMES the gate, so a change in
# which one is visible in the output rather than a stale assertion.
out=$($PF "$B" 2>&1); got=$?
unmet=$(printf '%s' "$out" | grep -E 'BLOCKED|\*\*\*FAIL' | sed 's/^ *//' | cut -d' ' -f1 | tr '\n' ' ')
if [ "$got" -eq 1 ] && [ -n "$unmet" ]; then
    echo "    ok   b1-fixture run 2 is still blocked, at: ${unmet%% }"
else
    echo "*** b1-fixture should be blocked but was not (exit $got)"
    printf '%s\n' "$out" | sed 's/^/      /'; rc=1
fi

echo
[ "$rc" -eq 0 ] && echo "ALL PRE-FLIGHT GATE CHECKS PASSED" || echo "*** PRE-FLIGHT GATE CHECKS FAILED"
exit $rc
