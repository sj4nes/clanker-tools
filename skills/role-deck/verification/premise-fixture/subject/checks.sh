#!/bin/sh
# Verification harness for the `widget` module.
# Runs the arithmetic checks and fails the build if any check reports a failure.
set -e
cd "$(dirname "$0")"

out=$(sh compute.sh 2>&1)
printf '%s\n' "$out"

# A check that fails prints a line beginning with the marker "*** FAIL".
# Fail the build if the marker appears, or if the pass banner is missing.
if printf '%s\n' "$out" | grep -q '*** FAIL'; then
    echo "harness: FAILED (a check reported failure)" >&2
    exit 1
fi
if ! printf '%s\n' "$out" | grep -q "ALL CHECKS PASSED"; then
    echo "harness: FAILED (no pass banner)" >&2
    exit 1
fi
echo "harness: ok"
