#!/bin/sh
# Re-export of the canonical graph mutation check.
# Canonical source: skills/math-theorem-tree/lib/mutation-check.sh
exec sh "$(dirname "$0")/../../math-theorem-tree/lib/mutation-check.sh" "$@"
