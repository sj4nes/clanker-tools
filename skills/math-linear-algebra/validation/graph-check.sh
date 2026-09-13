#!/bin/sh
# Thin shim -> shared implementation in the math-theorem-tree skill.
# Canonical source: skills/math-theorem-tree/lib/graph-check.sh
exec sh "$(dirname "$0")/../../math-theorem-tree/lib/graph-check.sh" "$(dirname "$0")/.."
