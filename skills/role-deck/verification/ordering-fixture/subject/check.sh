#!/bin/sh
# Build gate: fails the build when any test in the suite fails.
set -e
cd "$(dirname "$0")"

out=$(sh suite.sh)
printf '%s\n' "$out"

if printf '%s\n' "$out" | grep -q '^FAIL'; then
    echo "check: FAILED (a test failed)" >&2
    exit 1
fi
echo "check: ok"
