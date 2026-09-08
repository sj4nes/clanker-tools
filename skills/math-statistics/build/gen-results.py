#!/usr/bin/env python3
"""Driver: generate results/<id>.yaml and nodes/<id>.md for every spec.

    python3 build/gen-results.py

The N class, helpers, and ROOT() stub live in build/nodespec.py.  Node specs
live in build/specs/spec_*.py, each importing `from nodespec import N, ROOT`.
Dependency lists come from build/node-deps.txt (derived from the graph).
"""
import os, sys
BUILD = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BUILD)
sys.path.insert(0, os.path.join(BUILD, "specs"))

import nodespec
from nodespec import N

for mod in ("spec_roots", "spec_model", "spec_expfam", "spec_sufficiency",
            "spec_estimation", "spec_methods", "spec_decision", "spec_gaussian",
            "spec_intervals", "spec_testing", "spec_nonparam", "spec_regression",
            "spec_principles"):
    try:
        __import__(mod)
    except ModuleNotFoundError:
        print(f"  (spec module {mod} not present yet — skipping)")

ROOT_DIR = nodespec.ROOT_DIR

def emit():
    nr = 0
    for n in N.ALL:
        open(os.path.join(ROOT_DIR, "results", n.nid + ".yaml"), "w").write(n.yaml())
        open(os.path.join(ROOT_DIR, "nodes", n.nid + ".md"), "w").write(n.md())
        nr += 1
    print(f"gen-results: {nr} nodes written (yaml + md)")
    spec_ids = set(N.BY_ID)
    reg = [l.split("\t")[0] for i, l in enumerate(open(os.path.join(ROOT_DIR, "nodes/nodes.tsv"))) if i]
    missing = sorted(set(reg) - spec_ids)
    extra = sorted(spec_ids - set(reg))
    if missing:
        print(f"  NO SPEC YET ({len(missing)}): {' '.join(missing)}")
    if extra:
        print(f"  SPEC NOT IN REGISTRY ({len(extra)}): {' '.join(extra)}")

if __name__ == "__main__":
    emit()
