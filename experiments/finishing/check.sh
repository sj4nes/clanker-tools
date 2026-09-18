#!/bin/sh
# Validity gate 1: the manipulation check. Runs BEFORE any band is consulted.
# A hit voids the run rather than annotating it.
set -eu
here=$(cd "$(dirname "$0")" && pwd)
run=${1:?usage: check.sh <run-dir>}
hits=0
while IFS= read -r pattern; do
    case "$pattern" in ''|\#*) continue ;; esac
    if grep -qiF "$pattern" "$run/events.jsonl" 2>/dev/null; then
        echo "*** CONTAMINATED: '$pattern' present in $run/events.jsonl"
        hits=$((hits + 1))
    fi
done < "$here/fingerprints.txt"
[ "$hits" -eq 0 ] && echo "manipulation check: clean ($run)"
exit "$hits"
