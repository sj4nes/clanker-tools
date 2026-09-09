#!/bin/sh
# Verification for the unattended-automation skill.
set -e
here=$(dirname "$0")

echo "== reference runner: failure-scenario matrix =="
python3 "$here/runner.py"

echo
echo "== audit-event schema is valid JSON =="
python3 -c "import json; json.load(open('$here/../templates/audit-event.schema.json')); print('  ok: audit-event.schema.json parses')"

echo
echo "== job-skeleton.sh is syntactically valid POSIX sh =="
sh -n "$here/../templates/job-skeleton.sh" && echo "  ok: job-skeleton.sh parses"

echo
echo "All unattended-automation verification checks passed."
