#!/bin/sh
# Mutation check: does this capsule's graph harness actually CATCH a broken graph?
#
# The bc audit (docs/bc-verification-audit.md) found 20 of 24 harnesses that
# could not fail: `quit` always exits 0, so a false claim was reported as a pass.
# The graph layer had the same shape of hole -- `graph-check.sh` and
# `build-tree.sh` check the emitted order against the edge list they were handed,
# so a SPURIOUS edge and a MISSING edge both passed silently. That was found by
# planting them, not by reading the scripts.
#
# So this file plants them on every run. Each mutation is applied to a COPY of
# the capsule under a temp root, the gates are run, and the harness asserts a
# non-zero exit. A mutation that survives is reported as a hole in the checks --
# the checks are the thing under test here, not the capsule.
#
#   Usage: sh mutation-check.sh <capsule-root>
#
# CANONICAL SOURCE: skills/math-theorem-tree/lib/mutation-check.sh
# See docs/verifying-skills.md §5.
set -eu
lib=$(cd "$(dirname "$0")" && pwd)
cap=$(cd "${1:?usage: mutation-check.sh <capsule-root>}" && pwd)
name=$(basename "$cap")

work=$(mktemp -d)
trap 'rm -rf "$work"' EXIT INT TERM

# Gates under test, run against the mutated copy. Deliberately NOT all.sh: the
# lean/bc/octave layers are slow and are not what this file is testing.
gates() {
    r=$1
    sh "$lib/build-tree.sh" "$r" >/dev/null 2>&1 || return 1
    python3 "$lib/check-edge-evidence.py" "$r" >/dev/null 2>&1 || return 1
    return 0
}

reset() {
    rm -rf "$work/cap"
    mkdir -p "$work/cap"
    # everything the gates read; build/ is regenerated
    for d in nodes edges results formulas validation indexes sources; do
        [ -e "$cap/$d" ] && cp -R "$cap/$d" "$work/cap/" || true
    done
    mkdir -p "$work/cap/build"
}

fails=0
planted=0
expect_caught() {
    label=$1
    planted=$((planted + 1))
    if gates "$work/cap"; then
        echo "*** SURVIVED: $label -- the gates reported success on a broken graph" >&2
        fails=$((fails + 1))
    else
        echo "  caught: $label"
    fi
}

plan="$work/cap/edges/dependencies.plan"

# A baseline that does NOT pass means the mutations prove nothing.
reset
if ! gates "$work/cap"; then
    echo "*** baseline FAILED: the unmutated copy does not pass the gates" >&2
    gates_out=$(sh "$lib/build-tree.sh" "$work/cap" 2>&1 || true)
    printf '%s\n' "$gates_out" >&2
    python3 "$lib/check-edge-evidence.py" "$work/cap" >&2 || true
    exit 1
fi
echo "mutation-check ($name): baseline passes; planting defects"

# The first real edge, used as the subject of the hygiene mutations (M1-M3),
# which are blind to whether the node carries text.
first=$(grep -Ev '^[[:space:]]*(#|$)' "$plan" | sed -E 's/[[:space:]]*#.*$//' | head -1)
a=$(echo "$first" | awk '{print $1}')
b=$(echo "$first" | awk '{print $2}')

# M4 and M5 are caught only by the node TEXT, so they must be planted on a node
# that HAS text -- otherwise the harness reports a hole in the gates when the
# real gap is coverage. Coverage is reported separately, below, because it is a
# genuine limit: on a node with no entry, the graph is unfalsifiable.
covered=$(ls "$work/cap/results"/*.yaml 2>/dev/null | sed 's|.*/||; s|\.yaml$||' || true)
if [ -z "$covered" ] && [ -d "$work/cap/formulas" ]; then
  covered=$(grep -h '^## ' "$work/cap/formulas"/*.md 2>/dev/null \
            | sed -E 's/^## `?([A-Za-z0-9_]+).*/\1/' || true)
fi
printf '%s\n' "$covered" | grep -v '^$' | LC_ALL=C sort -u > "$work/covered.txt"
covered_edge=$(grep -Ev '^[[:space:]]*(#|$)' "$plan" | sed -E 's/[[:space:]]*#.*$//' \
  | awk 'NR==FNR { cov[$1]=1; next } NF==2 && ($2 in cov) { print; exit }' \
        "$work/covered.txt" -)
if [ -z "$covered_edge" ]; then
  echo "*** mutation-check ($name): SKIP M4/M5 -- no edge whose target carries text;" >&2
  echo "    the graph of this capsule is not falsifiable by any check yet." >&2
fi
ca=$(echo "$covered_edge" | awk '{print $1}')
cb=$(echo "$covered_edge" | awk '{print $2}')

# M1 -- a cycle. BSD tsort exits 0 on one, so this tests the stderr guard.
reset; echo "$b $a" >> "$plan"
expect_caught "M1 cycle ($b -> $a reverses an existing edge)"

# M2 -- an edge endpoint that is not a registered node.
reset; echo "nosuchnode_planted $b" >> "$plan"
expect_caught "M2 unregistered endpoint (nosuchnode_planted)"

# M3 -- a self-edge.
reset; echo "$a $a" >> "$plan"
expect_caught "M3 self-edge ($a)"

# M4 -- a REAL edge deleted. Hygiene cannot see this: the remaining graph is
# perfectly well-formed. Only the node text still claiming the dependency can.
if [ -n "$covered_edge" ]; then
  reset
  # match on the two FIELDS, not the whole line: plan lines may carry a trailing
  # "# evidence" comment, and a literal-line grep silently deletes nothing --
  # which reports itself as a surviving mutation. (Found exactly that way.)
  awk -v A="$ca" -v B="$cb" '!($1 == A && $2 == B)' "$plan" > "$plan.tmp" \
    && mv "$plan.tmp" "$plan"
  expect_caught "M4 deleted edge ($ca -> $cb), graph still well-formed"
fi

# M5 -- a SPURIOUS edge between two registered nodes, chosen so it cannot make a
# cycle. Hygiene cannot see this either; only the node text not claiming it can.
if [ -n "$covered_edge" ]; then
reset
sh "$lib/build-tree.sh" "$work/cap" >/dev/null 2>&1   # need the built graph to pick one
src=$(python3 - "$work/cap" "$cb" <<'PY'
import sys, collections
root = sys.argv[1]
par = collections.defaultdict(set)
nodes = []
for line in open(root + "/build/dependencies.sorted.edges"):
    p = line.split()
    if len(p) == 2:
        par[p[1]].add(p[0]); nodes += p
def anc(n):
    out, st = set(), list(par[n])
    while st:
        x = st.pop()
        if x not in out:
            out.add(x); st.extend(par[x])
    return out
# a source whose ancestors do not include the target, and which is not already
# a parent of it -- so the new edge is both novel and acyclic
order = [l.strip() for l in open(root + "/indexes/tsort-order.txt")]
tgt = sys.argv[2]
for cand in order:
    if cand != tgt and cand not in par[tgt] and tgt not in anc(cand):
        print(cand, tgt); break
PY
)
echo "$src" >> "$plan"
expect_caught "M5 spurious edge ($src), acyclic and well-formed"
fi

ncov=$(printf '%s\n' "$covered" | grep -c . || true)
nreg=$(($(wc -l < "$cap/nodes/nodes.tsv") - 1))
echo
echo "falsifiable coverage: $ncov of $nreg registered nodes carry text a mutation could contradict"
if [ "$fails" -gt 0 ]; then
    echo "*** mutation-check ($name): $fails of $planted mutations SURVIVED -- the gates have a hole" >&2
    exit 1
fi
echo "mutation-check ($name): ok ($planted/$planted planted defects caught)"
