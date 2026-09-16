#!/bin/sh
# Prove a subject environment is clean of the treatment BEFORE spawning subjects.
#
# G1 says assume contamination and prove its absence. This is the proof. It
# launches a throwaway session in the intended subject environment and asks it
# which skills it has, then greps that list against the fixture's fingerprints.
#
# WHY THIS EXISTS: b1 run 2 ran its subjects in a directory outside the repo and
# was contaminated anyway. Working directory is NOT the isolation boundary --
# the SESSION is. A subagent spawned by the Agent tool inherits the parent
# session's project skills no matter where it does its work. Only a separate
# `claude` process, launched with a cwd outside the project, drops them.
#
# Usage:  sh check_isolation.sh <subject-cwd> <fingerprints-file> [claude-flags]
#
# The third argument must be the SAME flags the subjects will be launched with,
# or the probe is testing a different environment than the one you will use.
# Verified clean on 2026-09-15: a cwd outside the repo plus
# `--disable-slash-commands` yields a subject with ZERO skills.
set -u
cwd=${1:?usage: check_isolation.sh <subject-cwd> <fingerprints-file> [claude-flags]}
fp=${2:?usage: check_isolation.sh <subject-cwd> <fingerprints-file> [claude-flags]}
flags=${3:-}

[ -d "$cwd" ] || { echo "*** no such directory: $cwd" >&2; exit 2; }
[ -s "$fp"  ] || { echo "*** fingerprints file missing or empty: $fp" >&2; exit 2; }

command -v claude >/dev/null || { echo "*** claude CLI not on PATH" >&2; exit 2; }

echo "isolation probe"
echo "  subject cwd : $cwd"
echo "  fingerprints: $fp"

# A project root inside the repo means project skills load regardless of cwd.
root=$(cd "$cwd" && git rev-parse --show-toplevel 2>/dev/null || true)
if [ -n "$root" ] && [ -d "$root/.claude/skills" ]; then
    echo "*** FAIL subject cwd resolves to a git root with .claude/skills:"
    echo "         $root/.claude/skills ($(ls "$root/.claude/skills" | wc -l | tr -d ' ') skills)"
    echo "         Subjects here inherit the corpus. Move outside the repo."
    exit 1
fi

echo "  launch flags: ${flags:-<none>}"
# shellcheck disable=SC2086
out=$(cd "$cwd" && timeout 180 claude -p $flags \
  "List the names of every skill available to you, comma-separated. If you have none, output exactly NONE." </dev/null 2>&1)
[ -n "$out" ] || { echo "*** FAIL probe returned nothing"; exit 1; }

echo "  probe saw   : $(printf '%s' "$out" | head -c 200)..."

bad=0
while IFS= read -r pat; do
    case "$pat" in ''|'#'*) continue ;; esac
    if printf '%s' "$out" | grep -qiF "$pat"; then
        echo "*** FAIL contaminant present in subject environment: '$pat'"
        bad=1
    fi
done < "$fp"

if [ "$bad" -eq 0 ]; then
    echo "    ok   no fingerprint from '$fp' is visible to a subject here"
    echo "         (this proves absence of the NAMED contaminants only --"
    echo "          a fingerprint you did not think of is still unchecked)"
    exit 0
fi
echo "  *** DO NOT SPAWN SUBJECTS in this environment."
exit 1
