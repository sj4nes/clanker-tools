#!/usr/bin/env python3
"""physics-formula-atlas -- minimal graphviz map of the cross-capsule edges.

Not a map of all 289 nodes: a map of exactly the nodes that participate in
a cross-capsule edge (source or target), one cluster per capsule, colored
by capsule. This is the atlas's actual content, rendered.

Usage: python3 build/gen-capsule-map.py > indexes/capsule-map.dot
       dot -Tsvg indexes/capsule-map.dot -o indexes/capsule-map.svg
"""
import pathlib

ATLAS_ROOT = pathlib.Path(__file__).resolve().parents[1]

CAPSULE_COLOR = {
    "physics-newtonian": "#dbeafe",
    "physics-thermodynamics": "#fef3c7",
    "physics-thermoacoustics": "#fee2e2",
    "physics-acoustics": "#dcfce7",
}
CAPSULE_LABEL = {
    "physics-newtonian": "physics-newtonian",
    "physics-thermodynamics": "physics-thermodynamics",
    "physics-thermoacoustics": "physics-thermoacoustics",
    "physics-acoustics": "physics-acoustics",
}


def load_edges():
    path = ATLAS_ROOT / "edges" / "cross-capsule.plan"
    edges = []
    for line in open(path, encoding="utf-8"):
        line = line.split("#", 1)[0].strip()
        if not line:
            continue
        parts = line.split()
        if len(parts) != 2:
            continue
        edges.append(tuple(parts))
    return edges


def qid(node):
    """capsule:node -> a graphviz-safe node id"""
    return node.replace(":", "__").replace("-", "_")


def main():
    edges = load_edges()
    nodes_by_capsule = {}
    for src, dst in edges:
        for n in (src, dst):
            capsule, _, nid = n.partition(":")
            nodes_by_capsule.setdefault(capsule, set()).add(nid)

    print("digraph physics_formula_atlas {")
    print('  rankdir=LR;')
    print('  fontname="Helvetica"; node [fontname="Helvetica", fontsize=11, shape=box, style="rounded,filled"];')
    print('  edge [fontname="Helvetica", fontsize=9, color="#555555"];')
    print('  labelloc="t"; label="physics-formula-atlas -- cross-capsule discharge map (28 edges, the nodes that carry them)";')
    print()

    order = ["physics-newtonian", "physics-thermodynamics", "physics-thermoacoustics", "physics-acoustics"]
    for capsule in order:
        nids = sorted(nodes_by_capsule.get(capsule, []))
        if not nids:
            continue
        print(f'  subgraph "cluster_{capsule.replace("-", "_")}" {{')
        print(f'    label="{CAPSULE_LABEL[capsule]}"; style=filled; fillcolor="#f8fafc"; color="#94a3b8";')
        for nid in nids:
            full = f"{capsule}:{nid}"
            print(f'    "{qid(full)}" [label="{nid}", fillcolor="{CAPSULE_COLOR[capsule]}"];')
        print("  }")
        print()

    for src, dst in edges:
        print(f'  "{qid(src)}" -> "{qid(dst)}";')

    print("}")


if __name__ == "__main__":
    main()
