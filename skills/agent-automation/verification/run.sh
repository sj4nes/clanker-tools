#!/bin/sh
# Verification for the agent-automation skill.
# Runs the reference executor wrapper through its test suite and validates the
# audit-event JSON schema is well-formed.
set -e
here=$(dirname "$0")

echo "== executor wrapper test suite =="
python3 "$here/executor.py"

echo
echo "== audit-event schema is valid JSON =="
python3 -c "import json,sys; json.load(open('$here/../templates/audit-event.schema.json')); print('  ok: audit-event.schema.json parses')"

echo
echo "All agent-automation verification checks passed."
