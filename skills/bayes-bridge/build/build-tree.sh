#!/bin/sh
# Thin shim -> shared implementation in the math-theorem-tree skill.
# Canonical source: skills/math-theorem-tree/lib/build-tree.sh
exec sh "$(dirname "$0")/../../math-theorem-tree/lib/build-tree.sh" "$(dirname "$0")/.."
