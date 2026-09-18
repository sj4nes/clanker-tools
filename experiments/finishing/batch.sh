#!/bin/sh
# Spawn both arms interleaved: A, B, A, B, ... never as two blocks, so provider
# drift, rate limiting or a model swap mid-run cannot land on one arm (G6).
#
#   sh batch.sh [n]      default n = 12 per arm
set -eu
here=$(cd "$(dirname "$0")" && pwd)
n=${1:-12}
i=1
while [ "$i" -le "$n" ]; do
    for arm in A B; do
        id=$(printf '%s%02d' "$arm" "$i")
        [ -e "$here/runs/$id" ] && { echo "skip $id (exists)"; continue; }
        echo "--- $id"
        sh "$here/run.sh" "$id" "$here/task-$arm.md" >/dev/null 2>&1 || echo "  run failed: $id"
    done
    i=$((i + 1))
done
echo "done: $(ls -d "$here"/runs/[AB]* 2>/dev/null | wc -l | tr -d ' ') runs"
