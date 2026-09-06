#!/usr/bin/env python3
"""Generate the three validation worksheets from results/*.yaml (the source of
truth).  Each gets one `## <node>` section so the `checks:` anchors in every
YAML resolve.  Run after gen-results.py."""
import glob, os, sys
try:
    import yaml
except ImportError:
    print("PyYAML required", file=sys.stderr); sys.exit(2)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

BC_NODES = {"bernoulli_distribution", "binomial_distribution", "poisson_distribution",
            "poisson_limit_theorem", "exponential_distribution", "memorylessness",
            "normal_distribution", "standard_normal", "central_limit_theorem",
            "variance_computational", "geometric_distribution", "continuous_uniform_distribution"}

order = [l.split("\t")[0] for l in open("nodes/nodes.tsv").read().splitlines()[1:] if l.strip()]
D = {}
for f in glob.glob("results/*.yaml"):
    d = yaml.safe_load(open(f))
    D[d["node"]] = d

TC = ["# Type / well-formedness checks (generated from results/*.yaml)\n",
      "For every node: the statement's type-check status, the well-formedness note",
      "(what must hold for the statement to even make sense), and each symbol's type.",
      "A passing type check is **necessary, not sufficient** — a well-typed statement",
      "can still be false on a missing hypothesis, a strictness, or a quantifier order.\n"]
SC = ["# Specialization & hypothesis-dropped counterexamples (generated from results/*.yaml)\n",
      "For every node: at least one specialization / boundary case, and at least one",
      "counterexample showing a named hypothesis cannot be dropped (or a note that",
      "every hypothesis is essential / the statement is unconditional).\n"]
IC = ["# Instance checks — index (generated from results/*.yaml)\n",
      "Which concrete check backs each node. Kernel-checked cores and `decide`",
      "instances live in `validation/proof-checks.lean` (see `proof-checks.md` for",
      "the genuine-vs-instance split); numerical worksheets in",
      "`validation/instance-checks.bc`. `cited` = established in the literature,",
      "not re-checked here.\n"]

for nid in order:
    d = D.get(nid)
    if not d:
        continue
    TC.append(f"\n## {nid}\n")
    TC.append(f"- **status:** `{d.get('type_check_status','?')}`")
    if d.get("type_check_note"):
        TC.append(f"- **note:** {d['type_check_note']}")
    syms = d.get("symbols") or {}
    if syms:
        TC.append("- **symbols:**")
        for k, v in syms.items():
            TC.append(f"  - `{k}` — {v}")
    hy = d.get("hypotheses") or []
    TC.append(f"- **hypotheses:** {', '.join(hy) if hy else '(none / unconditional within scope)'}")

    SC.append(f"\n## {nid}\n")
    for s in (d.get("specialization_cases") or []):
        SC.append(f"- **spec:** {s}")
    cx = d.get("counterexamples_when_dropped") or {}
    for k, v in cx.items():
        SC.append(f"- **drop `{k}`:** {v}")

    IC.append(f"\n## {nid}\n")
    pr = d.get("proof") or {}
    ls = pr.get("lean_status")
    lr = pr.get("lean_ref")
    if d.get("status_label") in ("definition", "axiom", "notation_convention"):
        wd = d.get("well_definedness")
        IC.append(f"- **well-definedness:** {wd}" if wd else "- definition/axiom — see the type check")
    if ls:
        IC.append(f"- **lean_status:** `{ls}`" + (f" — {lr}" if lr else ""))
    IC.append("- **bc:** see `validation/instance-checks.bc`" if nid in BC_NODES
              else "- **bc:** (no numeric worksheet; the type check and specialization cases apply)")

open("validation/type-checks.md", "w").write("\n".join(TC) + "\n")
open("validation/specialization-cases.md", "w").write("\n".join(SC) + "\n")
open("validation/instance-checks.md", "w").write("\n".join(IC) + "\n")
print(f"gen-validation-md: type-checks / specialization-cases / instance-checks "
      f"({len([n for n in order if n in D])} node sections each)")
