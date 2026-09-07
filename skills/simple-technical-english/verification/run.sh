#!/bin/sh
# ste-check -- advisory Simplified Technical English checker.
# Wraps ste-check.awk. One file per awk invocation so line hints and the
# per-document synonym-drift summary stay correct.
#
# Usage:
#   ./run.sh [--strict] [--max N] [--hard N] [--canon "v,v"] FILE [FILE...]
#
# Exit status: 0 normally; with --strict, 1 if any file produced a finding.

set -eu

here=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
strict=0
max=20
hard=25
canon=""

while [ $# -gt 0 ]; do
  case "$1" in
    --strict) strict=1; shift ;;
    --max)    max=$2; shift 2 ;;
    --hard)   hard=$2; shift 2 ;;
    --canon)  canon=$2; shift 2 ;;
    --)       shift; break ;;
    -h|--help)
      sed -n '2,11p' "$0"; exit 0 ;;
    -*) echo "ste-check: unknown option: $1" >&2; exit 2 ;;
    *)  break ;;
  esac
done

[ $# -ge 1 ] || { echo "usage: $0 [--strict] [--max N] [--hard N] [--canon v,v] FILE..." >&2; exit 2; }

rc=0
for f in "$@"; do
  [ -f "$f" ] || { echo "ste-check: not a file: $f" >&2; rc=2; continue; }
  echo "=== $f ==="
  awk -v max="$max" -v hard="$hard" -v strict="$strict" -v canon="$canon" \
      -f "$here/ste-check.awk" "$f" || rc=$?
  echo
done
exit $rc
