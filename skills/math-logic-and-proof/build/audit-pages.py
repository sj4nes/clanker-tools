#!/usr/bin/env python3
"""Audit every node detail page for the math-theorem-tree step-7 elements
required to promote its registry row from draft -> reviewed.

Required (prefix match on '## '):
  Type, Statement, Symbols, Prerequisites, 'Type / well-formedness check',
  a specialization section, a hypothesis-dropped / limits section,
  'Lean status', Sources.
Boundary-area nodes are exempt from the Lean-status requirement (stated_not_proved).
"""
import os, re, sys, csv

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
rows = list(csv.DictReader(open(os.path.join(ROOT,"nodes/nodes.tsv")), delimiter="\t"))
area = {r["id"]: r["area"] for r in rows}
status = {r["id"]: r["status"] for r in rows}

def headings(path):
    return [l[3:].strip() for l in open(path) if l.startswith("## ")]

def has(hs, *prefixes):
    return any(any(h.startswith(p) for p in prefixes) for h in hs)

problems = {}
for r in rows:
    nid = r["id"]
    p = os.path.join(ROOT, "nodes", nid + ".md")
    if not os.path.exists(p):
        problems[nid] = ["NO PAGE"]; continue
    hs = headings(p)
    body = open(p).read()
    miss = []
    if not has(hs, "Type"): miss.append("Type")
    if not has(hs, "Statement"): miss.append("Statement")
    if not has(hs, "Symbols"): miss.append("Symbols")
    if not has(hs, "Prerequisites"): miss.append("Prerequisites")
    if not has(hs, "Type / well-formedness", "Well-defined", "Type check"):
        miss.append("type-check")
    if not has(hs, "Specialization", "Specialisation"):
        miss.append("specialization")
    if not has(hs, "Hypothesis-dropped", "Where it fails", "Where the", "Hypothesis-dropped /",
               "Where it misleads", "Where it does not", "Where the metatheory"):
        miss.append("counterexample/limits")
    if area.get(nid) != "boundary" and not has(hs, "Lean status"):
        miss.append("Lean status")
    if not has(hs, "Sources"): miss.append("Sources")
    # stub check: very short section bodies
    if len(body) < 600: miss.append("STUB(<600 chars)")
    if miss:
        problems[nid] = miss

for nid in sorted(problems):
    print(f"  {status.get(nid,'?'):8} {area.get(nid,'?'):16} {nid}: {', '.join(problems[nid])}")
print(f"audit-pages: {len(rows)} nodes, {len(problems)} with gaps")
sys.exit(1 if problems else 0)
