#!/bin/sh
# Run 3 of the b1 fixture, end to end. Usage: sh run3.sh <work-dir>
#
# <work-dir> MUST be outside this repository. Subjects are Bash-invoked separate
# `claude` processes, not Agent-tool subagents: a subagent inherits its parent
# session's project skills wherever it does its work, which is what voided run 2.
#
# The order of the steps is the design (design3.md section 5) and is not
# negotiable at runtime:
#
#   1. pre-flight gate      -- refuse to spawn a design that is not ready
#   2. isolation probe      -- refuse to spawn into a contaminated environment
#   3. spawn, interleaved   -- A1 B1 C1 A2 B2 C2 ...
#   4. manipulation check   -- arm A only; ANY hit VOIDS the run
#   5. score                -- only if 4 passed
#
# This script does not interpret the numbers. It prints them; design3.md says
# what they mean, and design3.md was committed before this was ever run.
set -u
here=$(cd "$(dirname "$0")" && pwd)
work=${1:?usage: sh run3.sh <work-dir>   (must be outside the repo)}
N=${N:-5}
FLAGS="--disable-slash-commands"

mkdir -p "$work" || exit 2
work=$(cd "$work" && pwd)
case "$work" in
    "$(cd "$here" && git rev-parse --show-toplevel)"*)
        echo "*** work dir is inside the repository. Subjects would inherit the corpus." >&2
        exit 2 ;;
esac

echo "=== 1. pre-flight ==="
sh "$here/../../../claim-fixture/verification/preflight.sh" "$here" || {
    echo "*** DO NOT SPAWN. Fix the design first." >&2; exit 2; }

echo
echo "=== 2. isolation probe ==="
probe="$work/.probe"; mkdir -p "$probe"
sh "$here/../../../claim-fixture/verification/check_isolation.sh" \
   "$probe" "$here/fingerprints.txt" "$FLAGS" || {
    echo "*** DO NOT SPAWN. The subject environment is not clean." >&2; exit 2; }

echo
echo "=== 3. spawn, interleaved ==="
i=1
while [ "$i" -le "$N" ]; do
    for arm in A B C; do
        d="$work/$arm$i"
        [ -f "$d/.done" ] && { echo "    skip $arm$i (already run)"; continue; }
        rm -rf "$d"; mkdir -p "$d"
        cp "$here/subject3/duration.py" "$here/subject3/SPEC.md" "$d/"
        echo "    spawn $arm$i"
        ( cd "$d" && claude -p $FLAGS "$(cat "$here/task-$arm.md")" </dev/null ) \
            > "$d/.transcript" 2>&1
        echo "$?" > "$d/.done"
    done
    i=$((i+1))
done

echo
echo "=== 4. manipulation check (arm A only) ==="
# Arm B's prompt contains the treatment and arm C's contains the targets, by
# design. A fingerprint in an ARM-A transcript means there was one condition,
# not two -- and that voids the run rather than annotating it.
void=0
i=1
while [ "$i" -le "$N" ]; do
    t="$work/A$i/.transcript"
    if [ ! -f "$t" ]; then
        echo "    A$i  no transcript (attrition)"
    else
        hits=$(grep -vE '^[[:space:]]*(#|$)' "$here/fingerprints.txt" \
               | while IFS= read -r p; do grep -qiF "$p" "$t" && printf '%s; ' "$p"; done)
        if [ -n "$hits" ]; then
            echo "    A$i  *** CONTAMINATED: $hits"; void=1
        else
            echo "    A$i  clean"
        fi
    fi
    i=$((i+1))
done
if [ "$void" -ne 0 ]; then
    echo
    echo "*** RUN VOID. The control arm received the treatment. Do not score,"
    echo "    do not report a delta, and do not write this up as a limitation."
    exit 1
fi

echo
echo "=== 5. score ==="
for arm in A B C; do
    i=1
    while [ "$i" -le "$N" ]; do
        [ -d "$work/$arm$i" ] && sh "$here/score3.sh" "$work/$arm$i"
        i=$((i+1))
    done
done

echo
echo "Kill rates above. design3.md section 5 is the reading, in this order:"
echo "  manipulation check -> positive control (C-A >= +0.20) -> attrition"
echo "  -> ceiling -> the bands. Nothing is read until everything above it passed."
