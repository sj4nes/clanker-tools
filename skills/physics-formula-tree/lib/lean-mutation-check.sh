#!/bin/sh
# Re-export of the canonical Lean mutation check.
# Canonical source: skills/math-theorem-tree/lib/lean-mutation-check.sh
exec sh "$(dirname "$0")/../../math-theorem-tree/lib/lean-mutation-check.sh" "$@"
