#!/bin/sh
# Thin shim -> shared implementation in the physics-formula-tree skill.
# Canonical source: skills/math-theorem-tree/lib/build-tree.sh
exec sh "$(dirname "$0")/../../physics-formula-tree/lib/build-tree.sh" "$(dirname "$0")/.."
