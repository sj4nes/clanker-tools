#!/usr/bin/env python3
"""Generate results/<id>.yaml and nodes/<id>.md from a single node spec table.

Dependency lists are read from build/node-deps.txt (derived from
edges/dependencies.edges) so a YAML can never drift from the graph.  Run:

    python3 build/gen-results.py            # writes every node with a spec
    sh validation/graph-check.sh            # graph must be clean first

Root (cited bridge) nodes get a thin stub via ROOT(...); capsule nodes get a
full N(...) spec.  `regime` is this capsule's per-result tag
(exact | asymptotic | distribution_free | bayesian), the analogue of
math-probability's `convergence_mode`.
"""
import os, sys

ROOT_DIR = os.environ.get("CAPSULE_ROOT") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FORCE = "--force" in sys.argv

def load_deps():
    d = {}
    p = os.path.join(ROOT_DIR, "build", "node-deps.txt")
    for line in open(p):
        line = line.strip()
        if not line:
            continue
        k, rest = line.split(":", 1)
        rest = rest.strip().strip("[]")
        d[k.strip()] = [x.strip() for x in rest.split(",") if x.strip()]
    return d

DEPS = load_deps()
DEFAULT_SOURCES = ["casella_berger_2e", "van_der_vaart_asymptotic"]

def q(s):
    return "'" + str(s).replace("'", "''") + "'"

def block_list(key, items, indent=0):
    pad = " " * indent
    if not items:
        return f"{pad}{key}: []\n"
    out = f"{pad}{key}:\n"
    for it in items:
        out += f"{pad}  - {q(it)}\n"
    return out

def block_map(key, d):
    if not d:
        return f"{key}: {{}}\n"
    out = f"{key}:\n"
    for k, v in d.items():
        out += f"  {q(k)}: {q(v)}\n"
    return out

STATUS_BY_TYPE = {
    "definition": "definition", "axiom": "axiom", "structure": "definition",
    "notation_convention": "definition", "primitive": "definition",
    "construction": "constructive_result", "identity": "mathematical_identity",
    "counterexample": "counterexample", "example": "example",
    "bridge": "proved_theorem", "lemma": "proved_lemma",
    "proposition": "proposition", "theorem": "proved_theorem",
    "corollary": "corollary", "hypothesis": "definition", "regime": "definition",
    "algorithm": "constructive_result", "diagnostic": "definition",
}

class N:
    ALL = []
    BY_ID = {}
    def __init__(self, nid, ntype, area, display, parseable="", symbols=None,
                 tcn="", status_label=None, hyps=None, pre=None, welldef=None,
                 equiv=None, proof=None, choice=False, constructive=True,
                 regime=None, solving_for=None, spec=None, cxd=None, misuse=None,
                 related=None, sources=None, status="draft", tcs="well_formed",
                 apps=None):
        self.nid = nid; self.ntype = ntype; self.area = area
        self.display = display; self.parseable = parseable or display
        self.symbols = symbols or {}; self.tcn = tcn or "well-formed as stated"
        self.hyps = hyps or []; self.pre = pre or []
        self.welldef = welldef; self.equiv = equiv or []
        self.proof = proof; self.choice = choice; self.constructive = constructive
        self.regime = regime; self.solving_for = solving_for
        self.spec = spec or []; self.cxd = cxd or {}; self.misuse = misuse or []
        self.related = related or {}; self.sources = sources or DEFAULT_SOURCES
        self.status = status; self.tcs = tcs; self.apps = apps or []
        self.status_label = status_label or STATUS_BY_TYPE.get(ntype, "proved_theorem")
        N.ALL.append(self); N.BY_ID[nid] = self

    @property
    def deps(self):
        return DEPS.get(self.nid, [])

    def yaml(self):
        o = f"id: {self.area}.{self.nid}\n"
        o += f"node: {self.nid}\n"
        o += f"status_label: {self.status_label}\n"
        o += f"display: {q(self.display)}\n"
        o += f"parseable: {q(self.parseable)}\n"
        if self.regime:
            o += f"regime: {self.regime}\n"
        o += block_map("symbols", self.symbols)
        o += f"type_check_status: {self.tcs}\n"
        o += f"type_check_note: {q(self.tcn)}\n"
        o += block_list("hypotheses", self.hyps)
        o += block_list("preconditions", self.pre)
        o += block_list("dependencies", self.deps)
        if self.proof:
            tech, derives, lstat, lref = self.proof
            o += "proof:\n"
            o += f"  technique: {q(tech)}\n"
            o += f"  derives_from: {q(derives) if derives else 'null'}\n"
            o += f"  lean_status: {lstat}\n"
            o += f"  lean_ref: {q(lref) if lref else 'null'}\n"
        if self.welldef:
            o += f"well_definedness: {q(self.welldef)}\n"
        if self.equiv:
            o += block_list("equivalent_forms", self.equiv)
        o += f"uses_choice: {'true' if self.choice else 'false'}\n"
        o += f"constructive: {'true' if self.constructive else 'false'}\n"
        if self.solving_for:
            o += f"solving_for: {q(self.solving_for)}\n"
        o += block_list("specialization_cases", self.spec)
        if self.cxd:
            o += "counterexamples_when_dropped:\n"
            for k, v in self.cxd.items():
                o += f"  {k}: {q(v)}\n"
        else:
            o += ("counterexamples_when_dropped:\n"
                  "  none_all_hypotheses_essential: 'every listed hypothesis is used; see the block above'\n")
        o += block_list("common_misuse", self.misuse)
        if self.apps:
            o += block_list("applications", self.apps)
        if self.related:
            o += "related:\n"
            for k, v in self.related.items():
                if isinstance(v, list):
                    o += f"  {k}: [{', '.join(q(x) for x in v)}]\n"
                else:
                    o += f"  {k}: {q(v)}\n"
        o += block_list("sources", self.sources)
        o += f"status: {self.status}\n"
        o += "checks:\n"
        o += f"  type: validation/type-checks.md#{self.nid}\n"
        o += f"  specialization: validation/specialization-cases.md#{self.nid}\n"
        o += "  instances: validation/instance-checks.bc\n"
        o += f"  proof: validation/proof-checks.md#{self.nid}\n"
        return o

    def md(self):
        o = f"# {self.nid}\n\n## Type\n{self.ntype}\n\n## Statement\n{self.display}\n\n"
        o += "## Symbols\n"
        for k, v in self.symbols.items():
            o += f"- `{k}` — {v}\n"
        if not self.symbols:
            o += "(none beyond the statement)\n"
        o += f"\n## Epistemic status\n{self.status_label}"
        o += "" if self.constructive else " (non-constructive)"
        o += " (uses choice)" if self.choice else ""
        if self.regime:
            o += f"  ·  regime: {self.regime}"
        o += "\n\n## Prerequisites (tsort edges into this node)\n"
        o += ", ".join(self.deps) if self.deps else "(root — cited, see conventions.md)"
        o += "\n\n## Hypotheses\n"
        o += ", ".join(self.hyps) if self.hyps else "(none — unconditional within scope)"
        if self.proof:
            tech, derives, lstat, lref = self.proof
            o += f"\n\n## Proof provenance\ntechnique: {tech}\n"
            o += f"derives_from: {derives}\n" if derives else ""
            o += f"lean_status: {lstat}" + (f" — {lref}" if lref else "") + "\n"
        if self.welldef:
            o += f"\n## Well-definedness\n{self.welldef}\n"
        o += f"\n## Type / well-formedness check\n{self.tcn}\n"
        if self.spec:
            o += "\n## Specialization / boundary cases\n" + "".join(f"- {s}\n" for s in self.spec)
        if self.cxd:
            o += "\n## Hypothesis-dropped counterexamples\n" + "".join(f"- **{k}**: {v}\n" for k, v in self.cxd.items())
        if self.misuse:
            o += "\n## Common misuse\n" + "".join(f"- {m}\n" for m in self.misuse)
        if self.apps:
            o += "\n## In the wild\n" + "".join(f"- {a}\n" for a in self.apps)
        if self.related:
            o += "\n## Related nodes (non-prerequisite)\n"
            for k, v in self.related.items():
                o += f"- {k}: {', '.join(v) if isinstance(v, list) else v}\n"
        o += f"\n## Sources\n{', '.join(self.sources)}\n"
        return o

def ROOT(nid, cite, display):
    """Thin stub for a cited bridge root."""
    N(nid, "bridge", "foundations", display,
      parseable=display, symbols={}, tcn="cited; well-formedness established upstream",
      proof=("cited from " + cite, None, "cited", cite),
      sources=[cite.split(":")[0]], status="draft",
      misuse=[f"treating this as proved here — it is imported from {cite}"])

