#!/bin/sh
# Verification for the local-first-backup skill.
set -e
here=$(dirname "$0")

echo "== reference model: backup / restore / retention / credential properties =="
python3 "$here/runner.py"

echo
echo "== templates parse as text and contain their required sections =="
python3 "$here/check_templates.py"

echo
echo "All local-first-backup verification checks passed."
