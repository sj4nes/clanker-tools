#!/usr/bin/env python3
"""Every result YAML: node registered, filename matches node, and every entry in
`dependencies:` is a real prerequisite edge in the graph."""
import glob, re, sys, os
os.chdir(os.path.join(os.path.dirname(__file__), ".."))

nodes = set()
for i, l in enumerate(open("nodes/nodes.tsv")):
    if i:
        nodes.add(l.split("\t")[0])

edges = set()
for l in open("edges/dependencies.edges"):
    a, b = l.split()
    edges.add((a, b))

bad = 0
files = sorted(glob.glob("results/*.yaml"))
for f in files:
    txt = open(f).read()
    base = os.path.basename(f)[:-5]
    m = re.search(r"^node:\s*(\S+)", txt, re.M)
    node = m.group(1) if m else None
    if node not in nodes:
        print(f"  {f}: unknown node {node}"); bad += 1
    if node != base:
        print(f"  {f}: filename/node mismatch ({node})"); bad += 1
    m = re.search(r"^dependencies:\s*\[([^\]]*)\]", txt, re.M)
    if m:
        for dp in (x.strip() for x in m.group(1).split(",") if x.strip()):
            if dp not in nodes:
                print(f"  {f}: unknown dep {dp}"); bad += 1
            elif (dp, node) not in edges:
                print(f"  {f}: dep {dp} is not a graph edge into {node}"); bad += 1

print(f"check-yaml: {len(files)} YAMLs, {len(glob.glob('nodes/*.md'))} detail pages -- "
      + ("FAIL" if bad else "ok (all deps match graph edges)"))
sys.exit(1 if bad else 0)
