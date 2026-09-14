#!/bin/sh
# Thin shim -> shared implementation in the physics-formula-tree skill.
# Canonical source: skills/math-theorem-tree/lib/lean-mutation-check.sh
exec sh "$(dirname "$0")/../../physics-formula-tree/lib/lean-mutation-check.sh" "$(dirname "$0")/.."
