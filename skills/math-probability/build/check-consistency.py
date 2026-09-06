#!/usr/bin/env python3
"""Cross-checks that must pass for a publishable release.

  1. every registry node has a results/<id>.yaml and a nodes/<id>.md
  2. every YAML `dependencies:` list == the graph's edges into that node
  3. every YAML `sources:` key appears in sources/bibliography.md
  4. every relations.tsv endpoint is a registered node; 4 fields per line
  5. every YAML parses; required fields present
"""
import glob, os, sys

try:
    import yaml
except ImportError:
    print("PyYAML required: pip install pyyaml", file=sys.stderr); sys.exit(2)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
err = 0


def fail(msg):
    global err
    err += 1
    print("FAIL:", msg)


reg = [l.split("\t")[0] for l in open("nodes/nodes.tsv").read().splitlines()[1:] if l.strip()]
regset = set(reg)

deps = {}
for line in open("build/node-deps.txt"):
    k, rest = line.split(":", 1)
    deps[k.strip()] = set(x.strip() for x in rest.strip().strip("[]").split(",") if x.strip())

bib = open("sources/bibliography.md").read()
REQUIRED = ["id", "node", "status_label", "display", "parseable", "type_check_status",
            "hypotheses", "dependencies", "specialization_cases", "sources", "status"]

for nid in reg:
    yp, mp = f"results/{nid}.yaml", f"nodes/{nid}.md"
    if not os.path.exists(yp):
        fail(f"{nid}: no results/{nid}.yaml"); continue
    if not os.path.exists(mp):
        fail(f"{nid}: no nodes/{nid}.md")
    try:
        d = yaml.safe_load(open(yp))
    except Exception as e:
        fail(f"{nid}: YAML parse: {str(e).splitlines()[-1]}"); continue
    for k in REQUIRED:
        if k not in d:
            fail(f"{nid}: missing field '{k}'")
    ydeps = set(d.get("dependencies") or [])
    gdeps = deps.get(nid, set())
    if ydeps != gdeps:
        fail(f"{nid}: dependencies mismatch  yaml-only={ydeps - gdeps}  graph-only={gdeps - ydeps}")
    for s in (d.get("sources") or []):
        if s not in bib:
            fail(f"{nid}: source '{s}' not in bibliography.md")
    if not (d.get("specialization_cases")):
        fail(f"{nid}: no specialization_cases")
    if d.get("status_label", "").startswith("proved") and "proof" not in d:
        fail(f"{nid}: proved_* but no proof block")

for i, line in enumerate(open("edges/relations.tsv").read().splitlines()[1:], 2):
    if not line.strip():
        continue
    parts = line.split("\t")
    if len(parts) != 4:
        fail(f"relations.tsv line {i}: {len(parts)} fields, expected 4"); continue
    _, s, t, _ = parts
    for e in (s, t):
        if e not in regset:
            fail(f"relations.tsv line {i}: unregistered node '{e}'")

n = len(reg)
if err:
    print(f"\n{err} problem(s) across {n} nodes")
    sys.exit(1)
print(f"check-consistency: ok ({n} nodes, all YAML+MD present, deps match graph, sources known, relations valid)")
