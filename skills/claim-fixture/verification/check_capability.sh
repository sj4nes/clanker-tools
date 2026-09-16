#!/bin/sh
# Prove a subject environment CAN PRODUCE THE ARTIFACT, before spawning subjects.
#
# The sibling of check_isolation.sh, asking the other question. Isolation asks
# "is this environment clean of the treatment?" Capability asks "can a subject
# here do the thing the measurement reads?" An environment can be perfectly
# clean and completely useless.
#
# WHY THIS EXISTS: b1 run 3 spawned fifteen subjects with no tool permissions.
# Every Write and every `python3` was refused, and `claude -p` is
# non-interactive so no approval flow existed. All fifteen scored NO-HARNESS.
# The isolation probe had passed. Nothing had asked whether an experiment was
# POSSIBLE there.
#
# This is not merely lost data. Where the treatment is an instruction to DO
# something -- "confirm it actually fails against a wrong implementation" -- an
# incapable environment makes the treatment undeliverable, and delta is then
# structurally zero whether or not the claim is true. That is run 2's failure
# with the sign flipped.
#
# Usage:  sh check_capability.sh <probe-cwd> [claude-flags]
#
# The flags must be the SAME ones the subjects will be launched with, or the
# probe is testing a different environment than the one you will use.
#
# The proof is UNFORGEABLE: the subject must report the machine's epoch clock,
# which it cannot know without executing something, into a file it must write.
# Claiming success in prose does not create the file, and guessing the number to
# within ten minutes is not something a transcript can fake after the fact.
set -u
cwd=${1:?usage: check_capability.sh <probe-cwd> [claude-flags]}
flags=${2:-}

[ -d "$cwd" ] || { echo "*** no such directory: $cwd" >&2; exit 2; }
command -v claude >/dev/null || { echo "*** claude CLI not on PATH" >&2; exit 2; }

probe="$cwd/.capability"
rm -rf "$probe"; mkdir -p "$probe"

echo "capability probe"
echo "  probe cwd   : $probe"
echo "  launch flags: ${flags:-<none>}"

before=$(date +%s)
# shellcheck disable=SC2086
out=$(cd "$probe" && timeout 300 claude -p $flags \
  "Run the shell command: date +%s
Then write a file named capability.out in this directory whose entire contents
are that command's output and nothing else. Report what you did." \
  </dev/null 2>&1)
after=$(date +%s)

if [ ! -f "$probe/capability.out" ]; then
    echo "*** FAIL no capability.out was written."
    echo "         The subject could not create a file. Grant tool permissions."
    echo "  probe said: $(printf '%s' "$out" | head -c 300)..."
    echo "  *** DO NOT SPAWN SUBJECTS in this environment."
    exit 1
fi

val=$(tr -cd '0-9' < "$probe/capability.out")
if [ -z "$val" ]; then
    echo "*** FAIL capability.out holds no number: $(head -c 120 "$probe/capability.out")"
    echo "         A file was written but nothing was executed."
    exit 1
fi

# Bounded by the probe's own wall clock, with slack for a slow session.
lo=$((before - 600)); hi=$((after + 600))
if [ "$val" -lt "$lo" ] || [ "$val" -gt "$hi" ]; then
    echo "*** FAIL capability.out holds $val, outside [$lo,$hi]."
    echo "         The number was not produced by running the command here."
    exit 1
fi

echo "    ok   a subject here can write a file AND execute a command"
echo "         (capability.out = $val, inside [$lo,$hi])"
echo "         This proves writing and shell execution only -- a tool the"
echo "         subjects need that this probe does not use is still unchecked."
exit 0
