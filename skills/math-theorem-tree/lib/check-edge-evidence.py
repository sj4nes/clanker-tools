#!/usr/bin/env python3
"""Edge TRUTH check: does the graph carry the dependencies the node text uses?

`graph-check.sh` and `build-tree.sh` are hygiene -- they check the emitted order
against the edge list they were handed.  Mutation testing (see
`validation/mutation-check.sh`) shows both a SPURIOUS edge and a MISSING edge
pass them silently.  This script is the missing oracle: it reads the node text,
which was written independently of the edge list, and asks whether every
dependency the text actually leans on is in the graph.

Two evidence classes, treated differently:

  HARD  a declared prerequisite list -- `related.requires` / `related.uses` in a
        results YAML, or the `Prereqs:` line of a formula entry.  Machine-
        readable and unambiguous, so a violation FAILS the build.

  SOFT  another registered node id appearing verbatim in proof / derivation /
        well-definedness prose.  A strong signal and the source of most real
        findings, but it also fires on node ids that are ordinary English words
        ("function", "model", "moment") and on legitimate forward references to
        a downstream node.  Every soft hit must therefore be ADJUDICATED once
        and recorded in `validation/edge-evidence-ignore.txt`; an unadjudicated
        hit fails, and so does a stale entry for a hit that no longer occurs.
        The ignore file is the audit trail, not a mute button.

A reference is only a candidate missing edge if adding it would keep the graph
acyclic -- a mention of a DESCENDANT is a forward reference, which is normal
prose and is reported separately (never a failure).

  Usage: python3 check-edge-evidence.py <capsule-root> [--report]

`--report` prints the full triage list with the matching sentence and exits 0;
use it to build the ignore file.  Without it the script is a build gate.

CANONICAL SOURCE: skills/math-theorem-tree/lib/check-edge-evidence.py
See docs/verifying-skills.md §5.
"""
import glob
import os
import re
import sys

IGNORE_PATH = "validation/edge-evidence-ignore.txt"
# Adjudication vocabulary. `homonym` is the one that surprised us: a capsule can
# hold BOTH a propositional `satisfaction` node and first-order satisfaction
# prose, so a verbatim match is not always a reference to the node.
VERDICTS = {"english-word", "homonym", "forward-ref", "cited-not-used",
            "stated-elsewhere", "judged-independent"}

# YAML fields whose prose is evidence of USE. `proof` is a block; the rest are
# scalars. Deliberately NOT included: `common_misuse`, `counterexamples_when_dropped`,
# `type_check_note`, `related.complement_of` -- those name nodes a result is
# contrasted WITH or warned about, which is exactly the case where an edge would
# be WRONG. Widening this tuple widens the noise, not the yield.
PROSE_FIELDS = ("proof", "well_definedness", "derivation")
DECLARED_KEYS = ("requires", "uses")


def load_graph(root):
    ids, typ = [], {}
    with open(os.path.join(root, "nodes/nodes.tsv")) as fh:
        for line in fh.read().splitlines()[1:]:
            if line.strip():
                f = line.split("\t")
                ids.append(f[0])
                typ[f[0]] = f[1] if len(f) > 1 else ""
    parents, children = {}, {}
    with open(os.path.join(root, "build/dependencies.sorted.edges")) as fh:
        for line in fh:
            p = line.split()
            if len(p) == 2:
                parents.setdefault(p[1], set()).add(p[0])
                children.setdefault(p[0], set()).add(p[1])
    return set(ids), typ, parents, children


def closure(start, adj):
    out, stack = set(), list(adj.get(start, ()))
    while stack:
        x = stack.pop()
        if x in out:
            continue
        out.add(x)
        stack.extend(adj.get(x, ()))
    return out


def sentence_around(text, needle):
    m = re.search(r"[^.;\n]*\b" + re.escape(needle) + r"\b[^.;\n]*", text)
    return " ".join(m.group(0).split())[:160] if m else ""


def yaml_nodes(root, ids):
    """(node_id, declared_set, prose) for a math/bridge capsule.

    `declared` is the union of the node's own `dependencies:` list (which must
    match the graph EXACTLY -- it is the same claim written twice, and a
    deleted edge shows up here and nowhere else) and the weaker
    `related.requires` / `related.uses` naming (which must merely lie in the
    prerequisite closure).  The two are gated differently in main().
    """
    try:
        import yaml
    except ImportError:
        print("PyYAML required: pip install pyyaml", file=sys.stderr)
        sys.exit(2)
    for path in sorted(glob.glob(os.path.join(root, "results/*.yaml"))):
        nid = os.path.basename(path)[:-5]
        if nid not in ids:
            continue
        d = yaml.safe_load(open(path)) or {}
        own = {x for x in (d.get("dependencies") or []) if isinstance(x, str)}
        declared = set()
        rel = d.get("related")
        if isinstance(rel, dict):
            for k in DECLARED_KEYS:
                v = rel.get(k) or []
                if isinstance(v, list):
                    declared |= {x for x in v if x in ids}
        prose = []
        for f in PROSE_FIELDS:
            v = d.get(f)
            if isinstance(v, dict):
                # `lean_status` / `lean_ref` live in the same block but are Lean
                # bookkeeping, not mathematical prose -- a declaration name like
                # `cov_bilinear_raw` is not a claim that this node USES `moment`.
                prose += [str(x) for k, x in v.items() if not str(k).startswith("lean")]
            elif v:
                prose.append(str(v))
        yield nid, declared, "\n".join(prose), own


ENTRY_RE = re.compile(r"^## ", re.M)
PREREQ_RE = re.compile(r"Prereqs?:\s*(.*?)\.\s", re.S)
# Assumption/regime nodes are registered graph nodes in the formula capsules, and
# an entry lists them under `Assumptions:` rather than `Prereqs:`. Both are
# declarations, so both count.
ASSUME_RE = re.compile(r"Assumptions?:\s*(.*?)\.\s", re.S)


def entry_nodes(root, ids):
    """(node_id, declared_set, prose) for a physics/chemistry capsule."""
    text = "\n".join(open(f).read() for f in sorted(glob.glob(os.path.join(root, "formulas/*.md"))))
    for sec in ENTRY_RE.split(text)[1:]:
        nid = re.split(r"[ —]", sec.strip())[0].strip("`")
        if nid not in ids:
            continue
        m = PREREQ_RE.search(sec)
        declared = set()
        for rx in (PREREQ_RE, ASSUME_RE):
            mm = rx.search(sec)
            if mm:
                declared |= {t.strip().strip("`") for t in re.split(r"[,;\n]", mm.group(1))}
        declared = {t for t in declared if t in ids}
        if not m:
            print(f"FAIL: {nid}: formula entry has no `Prereqs:` line")
            globals()["_noprereq"] = globals().get("_noprereq", 0) + 1
        # Evidence prose = the `- Label:` bullet, which carries the derivation
        # ("derived_exact -- from X and Y"), and nothing else.  Symbol lines
        # ("g: free-fall acceleration") are definitional, and the `Special case:`
        # / `Failure:` clauses name nodes the formula is CONTRASTED with --
        # precisely the case where an edge would be WRONG.  Neither is evidence
        # of use, and including them buries the real findings.
        mm = re.search(r"^[-\s]*Label\s*:(.*?)(?=\n[-\s]*[A-Z][a-z]+(?: [a-z]+)*\s*:|\Z)", sec, re.S | re.M)
        prose = mm.group(1) if mm else ""
        yield nid, declared, prose, declared


def load_ignore(root):
    path = os.path.join(root, IGNORE_PATH)
    entries = {}
    if not os.path.exists(path):
        return entries
    for i, line in enumerate(open(path), 1):
        line = line.split("#")[0].strip()
        if not line:
            continue
        f = line.split("\t")
        if len(f) < 3:
            print(f"FAIL: {IGNORE_PATH}:{i}: expected <node> <ref> <verdict> [note], tab-separated")
            continue
        if f[2] not in VERDICTS:
            print(f"FAIL: {IGNORE_PATH}:{i}: unknown verdict {f[2]!r} (use one of {sorted(VERDICTS)})")
            continue
        entries[(f[0], f[1])] = f[2]
    return entries


def main(argv):
    report = "--report" in argv
    root = os.path.abspath([a for a in argv[1:] if not a.startswith("-")][0])
    ids, typ, parents, children = load_graph(root)
    is_entry_capsule = bool(glob.glob(os.path.join(root, "formulas/*.md")))
    source = entry_nodes if is_entry_capsule else yaml_nodes

    ignore = load_ignore(root)
    hard, soft, forward, seen_soft = [], [], [], set()
    nodes_read = 0
    # Per-edge evidence grade, COMPUTED (a hand-maintained grade on ~3800 edges
    # would rot): `derived` = the target's proof/derivation prose names this
    # prereq; `declared` = the target's dependency list names it, which the hard
    # gate holds equal to the graph; `unbacked` = the target carries no text, so
    # nothing in the capsule could contradict the edge.
    grade = {"derived": 0, "declared": 0}
    covered_nodes = set()

    for nid, declared, prose, own in source(root, ids):
        nodes_read += 1
        covered_nodes.add(nid)
        anc = closure(nid, parents)
        desc = closure(nid, children)
        direct = parents.get(nid, set())

        # the node's OWN dependency list must equal the graph's edges into it
        for r in sorted(own - direct - {nid}):
            hard.append((nid, r, "node's own dependency list names it; no such edge in the graph"))
        for r in sorted(direct - own):
            hard.append((nid, r, "graph edge absent from the node's own dependency list"))

        for r in sorted(declared - own - {nid}):
            if is_entry_capsule:
                if r not in direct:
                    hard.append((nid, r, "entry lists it as a prereq; no such edge in the graph"))
            elif r not in anc:
                hard.append((nid, r, "related.requires/uses names it; not in the prerequisite closure"))
        for r in sorted(direct):
            if re.search(r"\b" + re.escape(r) + r"\b", prose):
                grade["derived"] += 1
            else:
                grade["declared"] += 1

        for r in sorted(ids):
            if r == nid or r in anc or r in declared:
                continue
            if not re.search(r"\b" + re.escape(r) + r"\b", prose):
                continue
            if r in desc:
                forward.append((nid, r))
            else:
                seen_soft.add((nid, r))
                if (nid, r) not in ignore:
                    soft.append((nid, r, sentence_around(prose, r)))

    stale = sorted(set(ignore) - seen_soft)

    if report:
        print(f"# edge-evidence triage for {os.path.basename(root)}")
        print(f"# {nodes_read} nodes read, {len(hard)} hard, {len(soft)} unadjudicated soft, "
              f"{len(forward)} forward refs, {len(stale)} stale ignore entries\n")
        for nid, r, why in hard:
            print(f"HARD\t{nid}\t{r}\t{why}")
        for nid, r, sent in soft:
            print(f"SOFT\t{nid}\t{r}\t{typ.get(r,'')}\t{sent}")
        return 0

    if not nodes_read:
        # A check that inspects nothing must never report "ok" -- that is the
        # vacuous pass this whole layer exists to prevent.
        print("check-edge-evidence: SKIP -- no node text found "
              "(results/*.yaml or formulas/*.md); nothing to check against the graph")
        return 0

    err = 0
    for nid, r, why in hard:
        print(f"FAIL: {nid}: {why}: {r}")
        err += 1
    for nid, r, sent in soft:
        print(f"FAIL: {nid}: text uses '{r}' but it is not a prerequisite -- add the edge, "
              f"or adjudicate it in {IGNORE_PATH}\n      {sent}")
        err += 1
    for nid, r in stale:
        print(f"FAIL: {IGNORE_PATH} has a stale entry {nid} -> {r} (no longer detected); remove it")
        err += 1
    err += globals().get("_noprereq", 0)

    if err:
        print(f"\n{err} problem(s) across {nodes_read} nodes")
        return 1
    # Coverage is part of the result: a capsule whose nodes mostly have no text
    # yet is only checked where text exists, and saying "ok" without saying over
    # how much is the same vacuous pass as reporting ok on zero nodes.
    unbacked = sum(len(v) for k, v in parents.items() if k not in covered_nodes)
    total = grade["derived"] + grade["declared"] + unbacked
    print(f"check-edge-evidence: ok ({nodes_read} of {len(ids)} registered nodes carry "
          f"text; {len(ignore)} adjudicated, {len(forward)} forward references)")
    print(f"  edge evidence: {grade['derived']} derived, {grade['declared']} declared, "
          f"{unbacked} unbacked (of {total})")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
