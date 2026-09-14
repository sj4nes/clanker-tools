#!/bin/sh
# Re-export of the single canonical capsule-graph implementation, so physics and
# chemistry capsules point at their own method skill's lib/ rather than at the
# math one.  Canonical source: skills/math-theorem-tree/lib/graph-check.sh
exec sh "$(dirname "$0")/../../math-theorem-tree/lib/graph-check.sh" "$@"
