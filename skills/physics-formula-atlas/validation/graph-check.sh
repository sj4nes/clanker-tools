#!/bin/sh
# physics-formula-atlas -- checks the *combined* graph (three capsules'
# native edges + this atlas's cross-capsule edges) stays acyclic, and that
# every cross-capsule edge endpoint actually exists in its named capsule's
# registry.
set -eu
cd "$(dirname "$0")/.."
mkdir -p build

python3 - <<'PYEOF'
import importlib.util
spec = importlib.util.spec_from_file_location("prereq_path", "build/prereq-path.py")
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

graph, node_ids = m.build_graph()

# every cross-capsule edge endpoint must exist in its capsule's registry
bad = []
for dst, srcs in m.load_cross_capsule_edges().items():
    for node in [dst] + srcs:
        capsule, _, nid = node.partition(":")
        if capsule not in node_ids or nid not in node_ids[capsule]:
            bad.append(node)
if bad:
    print("cross-capsule edges reference unregistered nodes:", bad)
    raise SystemExit(1)

with open("build/combined.edges", "w") as f:
    for dst, srcs in graph.items():
        for s in srcs:
            f.write(f"{s}\t{dst}\n")

n_edges = sum(len(v) for v in graph.values())
n_nodes = sum(len(v) for v in node_ids.values())
print(f"graph-check: ok ({n_edges} combined edges, {n_nodes} nodes across 3 capsules, 0 unregistered cross-capsule endpoints)")
PYEOF

TSORT_ERR=$(mktemp)
tsort build/combined.edges > build/combined-tsort-order.txt 2>"$TSORT_ERR"
if [ -s "$TSORT_ERR" ]; then
  echo "tsort reported a cycle in the combined graph:" >&2
  cat "$TSORT_ERR" >&2
  rm -f "$TSORT_ERR"
  exit 1
fi
rm -f "$TSORT_ERR"
echo "tsort: ok ($(wc -l < build/combined-tsort-order.txt | tr -d ' ') nodes, acyclic)"
