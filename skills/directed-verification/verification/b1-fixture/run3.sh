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

# The subject configuration is a PARAMETER, and it is recorded. RESULT2.md does
# not say which model produced its transcripts, so run 2 is not reproducible
# even if it had been valid. A result that does not name its configuration is a
# claim about nothing in particular.
#
# Whether a configuration is also a FACTOR -- more than one, compared -- is a
# design question, not a runtime one. See design3.md section 8.
MODEL=${MODEL:-opus}
EFFORT=${EFFORT:-medium}
CONFIG="$MODEL-$EFFORT"
# An explicit, identical toolset for every arm. Run 3 granted none, so no
# subject could write or execute, and arm B's treatment -- which IS an
# instruction to execute -- was undeliverable. See RESULT3.md.
TOOLS=${TOOLS:-"Read Write Edit Bash Glob Grep"}
FLAGS="--disable-slash-commands --model $MODEL --effort $EFFORT --allowedTools $TOOLS"

mkdir -p "$work" || exit 2
work=$(cd "$work" && pwd)
case "$work" in
    "$(cd "$here" && git rev-parse --show-toplevel)"*)
        echo "*** work dir is inside the repository. Subjects would inherit the corpus." >&2
        exit 2 ;;
esac

echo "run 3 / config $CONFIG"
echo "  model  : $MODEL"
echo "  effort : $EFFORT"
echo "  n      : $N per arm, 3 arms"
echo "  work   : $work"
echo

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
echo "=== 2b. capability probe ==="
sh "$here/../../../claim-fixture/verification/check_capability.sh" "$probe" "$FLAGS" || {
    echo "*** DO NOT SPAWN. A subject here cannot produce the artifact." >&2; exit 2; }

echo
echo "=== 3. spawn, interleaved ==="
TO=""
command -v timeout  >/dev/null 2>&1 && TO=timeout
command -v gtimeout >/dev/null 2>&1 && TO=gtimeout
[ -z "$TO" ] && { echo "*** no timeout(1); a hung subject would stall the run" >&2; exit 2; }
i=1
while [ "$i" -le "$N" ]; do
    for arm in A B C; do
        d="$work/$CONFIG/$arm$i"
        [ -f "$d/.done" ] && { echo "    skip $arm$i (already run)"; continue; }
        rm -rf "$d"; mkdir -p "$d"
        cp "$here/subject3/duration.py" "$here/subject3/SPEC.md" "$d/"
        # The manifest travels with the subject, so a transcript can never be
        # read later without knowing what produced it.
        printf 'arm=%s\nindex=%s\nmodel=%s\neffort=%s\nflags=%s\nspawned=%s\nfixture=%s\n' \
            "$arm" "$i" "$MODEL" "$EFFORT" "$FLAGS" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
            "$(git -C "$here" rev-parse HEAD)" > "$d/.manifest"
        echo "    spawn $arm$i"
        # A hung subject must cost one cell, not the run. A non-zero .done is
        # attrition and is reported as such; design3.md section 5 has the floor.
        SUBJECT_TIMEOUT=${SUBJECT_TIMEOUT:-1800}
        ( cd "$d" && $TO $SUBJECT_TIMEOUT claude -p $FLAGS \
              "$(cat "$here/task-$arm.md")" </dev/null ) \
            > "$d/.transcript" 2>&1
        st=$?
        # Attrition is NOT completion. A session-limit stub used to be written
        # with a .done, so a resumed run SKIPPED the subjects that never ran.
        if [ "$st" -ne 0 ] || [ ! -s "$d/.transcript" ] \
           || grep -qi 'hit your session limit' "$d/.transcript"; then
            echo "    ---- $arm$i did not complete (status $st); left for a resumed run"
            rm -f "$d/.done"
        else
            echo "$st" > "$d/.done"
        fi
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
    t="$work/$CONFIG/A$i/.transcript"
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
        [ -d "$work/$CONFIG/$arm$i" ] && sh "$here/score3.sh" "$work/$CONFIG/$arm$i"
        i=$((i+1))
    done
done

echo
echo "Kill rates above, for config $CONFIG ONLY. A kill rate carries its"
echo "configuration or it carries nothing."
echo
echo "design3.md section 5 is the reading, in this order:"
echo "  manipulation check -> positive control (C-A >= +0.20) -> attrition"
echo "  -> ceiling -> the bands. Nothing is read until everything above it passed."
