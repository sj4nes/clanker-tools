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
Primary configuration: opus / medium; any other is a labelled replication.
A capability probe runs before subjects are spawned; it must write and execute.
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
printf 'Scorer: score9.sh\n' >> "$T/f/design1.md"
expect "G3  design declares a scorer that is absent" 1 "G3   BLOCKED"

rm -rf "$T/f"; build "$T/f"
printf 'Scorer: score.sh\n' >> "$T/f/design1.md"
expect "G3  design declares the scorer it has"  0 "PRE-FLIGHT CLEAR"

rm -rf "$T/f"; build "$T/f"
sed -i '' '/[Pp]ositive control/d' "$T/f/design1.md"
expect "G4  no positive control"         1 "G4   BLOCKED"

rm -rf "$T/f"; build "$T/f"
sed -i '' '/capability probe/d' "$T/f/design1.md"
expect "G9  no capability probe"         1 "G9   BLOCKED"

rm -rf "$T/f"; build "$T/f"
sed -i '' 's/^A capability probe runs before subjects are spawned.*/A capability probe is performed./' "$T/f/design1.md"
expect "G9  probe declared but unordered" 1 "G9   \*\*\*FAIL"

rm -rf "$T/f"; build "$T/f"
sed -i '' '/Primary configuration:/d' "$T/f/design1.md"
expect "G8  no configuration declared"   1 "G8   BLOCKED"

rm -rf "$T/f"; build "$T/f"
sed -i '' 's/^Primary configuration:.*/Primary configuration:   /' "$T/f/design1.md"
expect "G8  configuration declared empty" 1 "G8   \*\*\*FAIL"

rm -rf "$T/f"; build "$T/f"
sed -i '' '/interleaved/d' "$T/f/design1.md"
expect "G6  no interleaving"             1 "G6   \*\*\*FAIL"

rm -rf "$T/f"; build "$T/f"
sed -i '' '/Bands:/d' "$T/f/design1.md"
expect "G7  no refuting band"            1 "G7   \*\*\*FAIL"

echo
echo "=== 3. against the real fixture, in both of its states ==="
B=../../directed-verification/verification/b1-fixture

# 3a. Run 2's state, reconstructed: the design that was actually used, no
# fingerprint list, no manipulation check, no positive control. The gate has to
# stop THIS -- it is the run that was spent and lost. Reconstructed rather than
# asserted against the live directory, because the live directory has since
# been repaired and now legitimately clears.
rm -rf "$T/r2"; mkdir -p "$T/r2"
cp "$B/design.md" "$B/design2.md" "$B/score.sh" "$B/score2.sh" "$T/r2/"
cp "$B/archive-runs-1-2/task-A.md" "$B/archive-runs-1-2/task-B.md" "$T/r2/"
out=$($PF "$T/r2" 2>&1); got=$?
miss=""
for g in "G2a  BLOCKED" "G2b  BLOCKED" "G4   BLOCKED" "G8   BLOCKED" "G9   BLOCKED"; do
    printf '%s' "$out" | grep -q "$g" || miss="$miss [$g]"
done
if [ "$got" -eq 1 ] && [ -z "$miss" ]; then
    echo "    ok   run 2 as it was actually run is blocked at G2a, G2b, G4, G8 and G9"
else
    echo "*** run 2 should be blocked at G2a/G2b/G4/G8/G9 (exit $got) missing:$miss"
    printf '%s\n' "$out" | sed 's/^/      /'; rc=1
fi

# 3b. The live fixture, repaired for run 3, must now clear -- otherwise 3a only
# proves the gate says no to everything.
out=$($PF "$B" 2>&1); got=$?
if [ "$got" -eq 0 ]; then
    echo "    ok   the repaired fixture clears the gate"
else
    echo "*** the repaired b1 fixture no longer clears (exit $got)"
    printf '%s\n' "$out" | sed 's/^/      /'; rc=1
fi

echo
[ "$rc" -eq 0 ] && echo "ALL PRE-FLIGHT GATE CHECKS PASSED" || echo "*** PRE-FLIGHT GATE CHECKS FAILED"
exit $rc
