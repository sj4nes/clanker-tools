#!/bin/sh
# Thin shim -> shared implementation in the physics-formula-tree skill.
# Canonical source: skills/math-theorem-tree/lib/mutation-check.sh
exec sh "$(dirname "$0")/../../physics-formula-tree/lib/mutation-check.sh" "$(dirname "$0")/.."
