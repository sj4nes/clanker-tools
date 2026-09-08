#!/usr/bin/env python3
"""Generate the three validation worksheets from results/*.yaml (the source of
truth).  Each headline node gets one `## <node>` section, so the `checks:`
anchors in every result YAML resolve:

    checks:
      type:           validation/type-checks.md#<node>
      specialization: validation/specialization-cases.md#<node>
      instances:      validation/instance-checks.bc
      proof:          validation/proof-checks.md#<node>

Only the 21 headline nodes carry a result YAML; the other 109 nodes carry the
same material in prose on their `nodes/<id>.md` detail page (audited by
`build/audit-pages.py`).  Run from anywhere; wired into `build/all.sh`.
"""
import glob, os, sys
try:
    import yaml
except ImportError:
    print("gen-validation-md: PyYAML required (pip install pyyaml)", file=sys.stderr)
    sys.exit(2)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

# headline nodes whose specialization / counterexample is also checked numerically
# in validation/instance-checks.bc
BC_NODES = {"de_morgan_prop", "functional_completeness", "quantifier_order",
            "free_for", "quantifier_negation", "induction_equivalence",
            "undecidability_fol_validity"}

order = [l.split("\t")[0] for l in open("nodes/nodes.tsv").read().splitlines()[1:] if l.strip()]
D = {}
for f in glob.glob("results/*.yaml"):
    d = yaml.safe_load(open(f))
    D[d["node"]] = d

TC = ["# Type / well-formedness checks (generated from results/*.yaml)\n",
      "One `## <node>` section per headline result: the statement's type-check",
      "status, the well-formedness note (what must hold for the statement to even",
      "make sense), and each symbol's type. A passing type check is **necessary,**",
      "**not sufficient** — a well-typed statement can still be false on a missing",
      "hypothesis, a strictness, a constructive-grade slip, or a quantifier order.",
      "The remaining 109 nodes carry this on their `nodes/<id>.md` detail page.\n"]
SC = ["# Specializations & hypothesis-dropped counterexamples (generated from results/*.yaml)\n",
      "One `## <node>` section per headline result: at least one specialization /",
      "boundary case, and at least one counterexample showing a named hypothesis",
      "cannot be dropped (or a note that every hypothesis is essential / the",
      "statement is unconditional). The remaining 109 nodes carry this on their",
      "`nodes/<id>.md` detail page.\n"]
IC = ["# Instance checks — index (generated from results/*.yaml)\n",
      "Which concrete check backs each headline node. Kernel-checked cores and",
      "`decide` instances live in `validation/proof-checks.lean` (see",
      "`proof-checks.md` for the genuine-vs-instance split); numerical worksheets",
      "in `validation/instance-checks.bc`. `cited` / `partial` = established in the",
      "literature or downstream of a cited result, not fully re-checked here.\n"]


def lean_status(d):
    pr = d.get("proof")
    if isinstance(pr, dict):
        return pr.get("lean_status"), pr.get("lean_ref")
    return None, None


for nid in order:
    d = D.get(nid)
    if not d:
        continue

    TC.append(f"\n## {nid}\n")
    TC.append(f"- **status:** `{d.get('type_check_status', '?')}`")
    if d.get("type_check_note"):
        TC.append(f"- **note:** {d['type_check_note']}")
    syms = d.get("symbols") or {}
    if syms:
        TC.append("- **symbols:**")
        for k, v in syms.items():
            if isinstance(v, dict):
                meaning = v.get("meaning", "")
                typ = v.get("type", "")
                TC.append(f"  - `{k}` — {meaning}" + (f" (`{typ}`)" if typ else ""))
            else:
                TC.append(f"  - `{k}` — {v}")
    hy = d.get("hypotheses") or []
    TC.append(f"- **hypotheses:** {', '.join(hy) if hy else '(none / unconditional within scope)'}")
    if d.get("constructive_grade"):
        TC.append(f"- **constructive grade:** `{d['constructive_grade']}`"
                  + (f" — {d['constructive_note']}" if d.get("constructive_note") else ""))

    SC.append(f"\n## {nid}\n")
    for s in (d.get("specialization_cases") or []):
        SC.append(f"- **spec:** {s}")
    cx = d.get("counterexamples_when_dropped") or {}
    for k, v in cx.items():
        SC.append(f"- **drop `{k}`:** {v}")
    if not cx and d.get("essential_hypotheses_note"):
        SC.append(f"- **essential:** {d['essential_hypotheses_note']}")

    IC.append(f"\n## {nid}\n")
    ls, lr = lean_status(d)
    if d.get("status_label") in ("definition", "axiom", "notation_convention") and d.get("well_definedness"):
        IC.append(f"- **well-definedness:** {d['well_definedness']}")
    if ls:
        IC.append(f"- **lean_status:** `{ls}`" + (f" — {lr}" if lr else ""))
    elif d.get("status_label") not in ("definition", "axiom", "notation_convention"):
        IC.append("- **lean_status:** see `validation/proof-checks.md`")
    IC.append("- **bc:** `validation/instance-checks.bc` (numeric worksheet)" if nid in BC_NODES
              else "- **bc:** (no numeric worksheet; the type check and specialization cases apply)")

n = len([x for x in order if x in D])
open("validation/type-checks.md", "w").write("\n".join(TC) + "\n")
open("validation/specialization-cases.md", "w").write("\n".join(SC) + "\n")
open("validation/instance-checks.md", "w").write("\n".join(IC) + "\n")
print(f"gen-validation-md: type-checks / specialization-cases / instance-checks "
      f"({n} node sections each)")
