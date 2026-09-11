#!/usr/bin/env python3
"""physics-formula-atlas -- cross-capsule prerequisite-path walker.

Given a qualified node id `capsule:node_id`, walks backward through:
  - each capsule's own edges/dependencies.edges (native, in-capsule edges)
  - this atlas's edges/cross-capsule.edges (the bridge edges)
and prints the full DAG of prerequisites down to every root (a node with no
further predecessors: a primitive, axiom, assumption, or convention),
labelling which capsule each node lives in and marking exactly where a
cross-capsule edge was crossed.

Usage:
    python3 build/prereq-path.py physics-thermoacoustics:specific_heat_cv
    python3 build/prereq-path.py --all-roots physics-newtonian:newton_second_law
"""
import argparse
import pathlib
import sys

REPO_ROOT = pathlib.Path(__file__).resolve().parents[3]
ATLAS_ROOT = pathlib.Path(__file__).resolve().parents[1]

CAPSULES = ["physics-newtonian", "physics-thermodynamics", "physics-thermoacoustics", "physics-acoustics"]


def load_node_ids(capsule):
    path = REPO_ROOT / "skills" / capsule / "nodes" / "nodes.tsv"
    ids = set()
    with open(path, encoding="utf-8") as f:
        next(f)  # header
        for line in f:
            if not line.strip():
                continue
            ids.add(line.split("\t", 1)[0])
    return ids


def load_native_edges(capsule):
    """Returns {node_id: [prereq_id, ...]} within one capsule, qualified
    with the capsule prefix on both ends so it merges cleanly with the
    cross-capsule edge set."""
    path = REPO_ROOT / "skills" / capsule / "edges" / "dependencies.plan"
    edges = {}
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.split("#", 1)[0].strip()
            if not line:
                continue
            # physics-formula-tree capsules use whitespace-separated edges
            # (unlike the math-theorem-tree capsules' tab-separated files).
            parts = line.split()
            if len(parts) != 2:
                continue
            src, dst = parts
            dst_q = f"{capsule}:{dst}"
            src_q = f"{capsule}:{src}"
            edges.setdefault(dst_q, []).append(src_q)
    return edges


def load_cross_capsule_edges():
    path = ATLAS_ROOT / "edges" / "cross-capsule.plan"
    edges = {}
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.split("#", 1)[0].strip()
            if not line:
                continue
            parts = line.split()
            if len(parts) != 2:
                continue
            src, dst = parts
            edges.setdefault(dst, []).append(src)
    return edges


def build_graph():
    graph = {}
    node_ids = {}
    for capsule in CAPSULES:
        node_ids[capsule] = load_node_ids(capsule)
        for dst, srcs in load_native_edges(capsule).items():
            graph.setdefault(dst, []).extend(srcs)
    for dst, srcs in load_cross_capsule_edges().items():
        graph.setdefault(dst, []).extend(srcs)
    return graph, node_ids


def qualify(raw, node_ids):
    if ":" in raw:
        return raw
    hits = [c for c in CAPSULES if raw in node_ids[c]]
    if len(hits) == 1:
        return f"{hits[0]}:{raw}"
    if len(hits) > 1:
        raise SystemExit(f"'{raw}' exists in multiple capsules ({hits}); qualify it as capsule:node")
    raise SystemExit(f"'{raw}' not found in any capsule's nodes.tsv")


def walk(start, graph, node_ids):
    """DFS backward from start, yielding (depth, node_id, is_cross_capsule_edge, is_root)."""
    visited = set()

    def recurse(node, depth, crossed):
        capsule_of_node = node.split(":", 1)[0]
        preds = graph.get(node, [])
        is_root = len(preds) == 0
        yield (depth, node, crossed, is_root)
        if node in visited:
            return
        visited.add(node)
        for p in preds:
            p_capsule = p.split(":", 1)[0]
            crossed_edge = p_capsule != capsule_of_node
            yield from recurse(p, depth + 1, crossed_edge)

    yield from recurse(start, 0, False)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("node", help="capsule:node_id, or bare node_id if unambiguous")
    ap.add_argument("--roots-only", action="store_true", help="print only the terminal roots reached")
    args = ap.parse_args()

    graph, node_ids = build_graph()
    start = qualify(args.node, node_ids)

    all_node_ids = set()
    for c in CAPSULES:
        all_node_ids |= {f"{c}:{n}" for n in node_ids[c]}
    if start not in all_node_ids:
        raise SystemExit(f"'{start}' not a registered node id")

    roots = []
    for depth, node, crossed, is_root in walk(start, graph, node_ids):
        if is_root:
            roots.append(node)
        if args.roots_only:
            continue
        marker = " <-- CROSSES CAPSULE BOUNDARY" if crossed else ""
        root_marker = "  [ROOT]" if is_root else ""
        print("  " * depth + node + root_marker + marker)

    if args.roots_only:
        for r in sorted(set(roots)):
            print(r)

    print(f"\n{len(set(roots))} distinct terminal roots reached, {sum(1 for r in roots)} root occurrences.", file=sys.stderr)


if __name__ == "__main__":
    main()
