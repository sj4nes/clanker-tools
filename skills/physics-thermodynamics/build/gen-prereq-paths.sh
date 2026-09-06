#!/bin/sh
# Minimal prerequisite paths for the core results: transitive closure of the
# prerequisite graph, presented in tsort order. Derived from the graph, not the
# flat tsort list.
set -eu
cd "$(dirname "$0")/.."
python3 - <<'EOF'
import collections
pre = collections.defaultdict(set)
for l in open('build/dependencies.sorted.edges'):
    a, b = l.split()
    pre[b].add(a)
order = [x.strip() for x in open('indexes/tsort-order.txt')]
pos = {n: i for i, n in enumerate(order)}
asm = set()
for l in open('nodes/nodes.tsv'):
    f = l.rstrip('\n').split('\t')
    if len(f) > 1 and f[1] in ('assumption', 'regime_limit'):
        asm.add(f[0])

def close(n):
    seen, stk = set(), list(pre[n])
    while stk:
        x = stk.pop()
        if x in seen:
            continue
        seen.add(x)
        stk += list(pre[x])
    return seen

cores = ['ideal_gas_law', 'first_law_thermodynamics', 'carnot_efficiency',
         'entropy', 'entropy_ideal_gas', 'adiabatic_reversible_ideal_gas',
         'maxwell_relations', 'gibbs_free_energy']
out = ["# Minimal prerequisite paths (Release 0.1)", "",
       "Transitive closure of `edges/dependencies.edges`, not the flat `tsort`",
       "order. Each list is the set of nodes to understand first, in `tsort`",
       "order. `[A]` marks an assumption / regime node -- required, but not a",
       "concept to \"learn\".", ""]
for c in cores:
    deps = sorted(close(c), key=lambda x: pos.get(x, 0))
    s = " · ".join(f"[{d}]" if d in asm else d for d in deps)
    out += [f"## {c}  ({len(deps)} prerequisites)", s, ""]
open('indexes/prerequisite-paths.md', 'w').write("\n".join(out))
print("wrote indexes/prerequisite-paths.md")
EOF
