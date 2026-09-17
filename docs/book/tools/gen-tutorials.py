#!/usr/bin/env python3
"""Generate Part VI — the tutorials cut from the capsules — from the repository.

The capsules exist to be checked by machines: a tsort graph, Lean cores, bc
checks. The tutorials are what happens when that same material is aimed at a
person, and they are generated from it rather than written beside it — each
section's runnable block IS the capsule's dimensional check, limiting case or
Lean core, with the reader running it.

So this part is a catalogue, not a reprint. The 24 tutorials come to some 60,000
words and their whole point is that they execute under `upmd` in a terminal,
which a PDF cannot do. What belongs in a book is which ones exist, what each
teaches, what its prerequisite chain is, and how much of it the reader runs
rather than reads — all of it read from the files, so it cannot go stale.

    python3 docs/book/tools/gen-tutorials.py            write the .typ
    python3 docs/book/tools/gen-tutorials.py --stdout   print it instead
    python3 docs/book/tools/gen-tutorials.py --list     one line per tutorial
"""
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from corpus import ROOT                       # noqa: E402
from typstlib import esc, inline              # noqa: E402

OUT = ROOT / "docs/book/parts/06-tutorials/01-entries.typ"

BANNER = """// GENERATED FILE — DO NOT EDIT.
//   source:    skills/*/tutorial/*.md
//   generator: docs/book/tools/gen-tutorials.py
//   gate:      docs/book/tools/check-book.sh  (regenerates and diffs)
// Edit the tutorials, or the generator; an edit here is reverted by the gate.

#import "../../preamble.typ": note, tutorialentry

"""

TITLE = re.compile(r"^# (.+)$", re.M)
# `> Generated from the `X` capsule (Release N) with the `Y` skill.` — the last
# clause varies: the oldest tutorial predates the skill and says "with the
# executable-tutorial method", which is a fact about the corpus, not a defect.
PROV = re.compile(r"`([\w-]+)` capsule \(Release ([\d.]+)\) with the "
                  r"(?:`([\w-]+)` skill|(.+?)\.)", re.S)
BLOCK = re.compile(r"^```bash \[name:([\w-]+)(?:, *deps:([^\]]*))?\]\n(.*?)^```",
                   re.M | re.S)
TOOLS = ("bc", "lean", "python3", "octave", "tsort", "awk")

DOMAINS = [
    ("chemistry", "Chemistry"),
    ("math", "Mathematics"),
    ("physics", "Physics"),
]

# --- ordering -----------------------------------------------------------------
# Everything below exists so that the book presents tutorials in DEPENDENCY
# order rather than alphabetically, which put electrochemistry before
# foundations. Nothing here hardcodes a sequence: every edge is read from a file
# in the repository, and where the evidence runs out the fallback is stated.

NEEDS = re.compile(r"^## What you need first\n(.*?)(?=^## )", re.M | re.S)
MDLINK = re.compile(r"\]\(([a-z0-9-]+)\.md\)")
# `1 · per-amp-hour` in a capsule's tutorial/README.md — the author's own
# declared teaching order, which outranks anything inferred.
NUMBERED = re.compile(r"(\d+) · ([a-z0-9-]+)")
# Block names are node ids with a role prefix: `chk_ideal_gas_law`.
ROLE = re.compile(r"^(chk|lean|try|cx|app|tight)_")


def toposort(items, edges, key):
    """Kahn's algorithm with a preference key: a total order that RESPECTS
    every declared edge and, among items that are free at the same moment,
    takes the smallest key. Raises on a cycle rather than emitting one.
    """
    items = list(items)
    incoming = {i: {a for a, b in edges if b == i and a in items} for i in items}
    out = []
    while incoming:
        free = sorted((i for i, deps in incoming.items() if not deps), key=key)
        if not free:
            raise SystemExit("*** FAIL: cycle among " + ", ".join(sorted(incoming)))
        pick = free[0]
        out.append(pick)
        del incoming[pick]
        for deps in incoming.values():
            deps.discard(pick)
    return out


def capsule_edges(root):
    """(before, after) pairs between capsules, from three sources of evidence.

    There is no single cross-capsule `deps:` convention in this repo — settling
    one is itself an open backlog item — so each source is read where it exists
    and named here, rather than a stack being written down in this file.
    """
    edges = set()
    caps = {p.name for p in (root / "skills").iterdir() if p.is_dir()}

    def resolve(name):
        """`math-sets-…` in a prose table means the capsule with that prefix."""
        name = name.rstrip("…. ")
        if name in caps:
            return name
        hits = sorted(c for c in caps if c.startswith(name))
        return hits[0] if len(hits) == 1 else None

    # 1. A capsule's SKILL.md saying "Builds on `X`" / "Builds directly on `X`".
    for cap in sorted(caps):
        f = root / "skills" / cap / "SKILL.md"
        if not f.exists():
            continue
        for m in re.finditer(r"Builds(?: directly)? on \[?`([\w-]+)`", f.read_text()):
            up = resolve(m.group(1))
            if up and up != cap:
                edges.add((up, cap))

    # 2. physics-formula-atlas: real cross-capsule `requires` edges, collapsed
    #    from `capsule:node` pairs to the capsules themselves.
    plan = root / "skills/physics-formula-atlas/edges/cross-capsule.plan"
    if plan.exists():
        for line in plan.read_text().splitlines():
            if line.startswith("#") or not line.strip():
                continue
            parts = line.split("\t")
            if len(parts) == 2 and all(":" in p for p in parts):
                a, b = (p.split(":", 1)[0] for p in parts)
                if a != b:
                    edges.add((a, b))

    # 3. docs/tutorial-map.md's "Discharges into" column, which is where the
    #    math stack's order is actually written down.
    tmap = root / "docs/tutorial-map.md"
    if tmap.exists():
        for line in tmap.read_text().splitlines():
            cells = [c.strip() for c in line.split("|")]
            if len(cells) < 6 or not cells[1].startswith("[`"):
                continue
            src = resolve(cells[1].split("`")[1])
            for m in re.finditer(r"`([\w-]+…?)`", cells[4]):
                dst = resolve(m.group(1))
                if src and dst and src != dst and dst in caps:
                    edges.add((src, dst))
    return edges


def tutorial_depth(t, root):
    """How deep into its capsule's own tsort order the tutorial reaches.

    The block names are node ids (`chk_henderson_hasselbalch`), and each capsule
    ships `indexes/tsort-order.txt`. A tutorial that ends on a later node is a
    later tutorial. Returns None when no block name resolves — the order then
    rests on the declared edges and the README numbering instead.
    """
    f = root / "skills" / t["capsule"] / "indexes/tsort-order.txt"
    if not f.exists():
        return None
    pos = {n.strip(): i for i, n in enumerate(f.read_text().splitlines())
           if n.strip()}
    hits = [pos[ROLE.sub("", b)] for b in t["blocks"] if ROLE.sub("", b) in pos]
    return max(hits) if hits else None


def declared_order(capsule, root):
    """`1 · per-amp-hour` from the capsule's tutorial/README.md, if it has one."""
    f = root / "skills" / capsule / "tutorial/README.md"
    if not f.exists():
        return {}
    return {slug: int(n) for n, slug in NUMBERED.findall(f.read_text())}


def order_tutorials(ts, root=ROOT):
    """Sort each capsule's tutorials into dependency order, in place."""
    out = []
    for capsule in {t["capsule"] for t in ts}:
        group = {t["slug"]: t for t in ts if t["capsule"] == capsule}
        numbered = declared_order(capsule, root)
        edges = set()
        for t in group.values():
            sec = NEEDS.search((root / t["path"]).read_text())
            for dep in MDLINK.findall(sec.group(1) if sec else ""):
                if dep in group and dep != t["slug"]:
                    edges.add((dep, t["slug"]))
        big = len(group) + 1

        def key(slug):
            d = tutorial_depth(group[slug], root)
            return (numbered.get(slug, big),
                    big if d is None else d,
                    slug)

        out += [group[s] for s in toposort(group, edges, key)]
    return out



def read_tutorial(path):
    text = path.read_text()
    quote = " ".join(l.lstrip("> ").strip()
                     for l in text.splitlines() if l.startswith(">"))
    prov = PROV.search(quote)
    blocks = BLOCK.findall(text)
    bodies = "\n".join(b for _, _, b in blocks)
    # The lead: the first ordinary paragraph of the introduction — after the
    # title and the provenance blockquote, and BEFORE the first `## ` section,
    # since the first section is always "How to run this".
    #
    # Bounding it at the first heading is what makes this right. An earlier
    # version took the first paragraph that did not begin with `>`, `#` or a
    # backtick, and `predicting-ph` opens "`pH` is just `−log(...)`" — so its
    # lead was skipped and the install instructions were printed as what the
    # tutorial teaches (found by reading page 88, 2026-09-17).
    body = text[text.index("\n", TITLE.search(text).start()):]
    intro = re.split(r"^## ", body, maxsplit=1, flags=re.M)[0]
    paras = [p.strip() for p in re.split(r"\n\s*\n", intro)
             if p.strip() and not p.strip().startswith((">", "#"))]
    return {
        "capsule": path.parent.parent.name,
        "slug": path.stem,
        "path": path.relative_to(ROOT).as_posix(),
        "title": TITLE.search(text).group(1).strip(),
        "release": prov.group(2) if prov else None,
        "method": (prov.group(3) or (prov.group(4) or "").strip())
                  if prov else None,
        "lead": " ".join(paras[0].split()) if paras else "",
        "blocks": [n for n, _, _ in blocks],
        # By what the block INVOKES, not by its name: `hole-in-the-rationals`
        # kernel-checks with Lean from blocks that are not named `lean_*`, and
        # counting on the convention under-reported it (2026-09-17).
        "lean_blocks": [n for n, _, b in blocks
                        if re.search(r"(?:^|[|(\s])lean\b", b, re.M)],
        "tools": [t for t in TOOLS
                  if re.search(rf"(?:^|[|(\s]){t}\b", bodies, re.M)],
        "lines": len(text.splitlines()),
        "words": len(text.split()),
    }


def read_tutorials(root=ROOT):
    ts = [read_tutorial(p) for p in (root / "skills").glob("*/tutorial/*.md")
          if p.name != "README.md"]
    ts = order_tutorials(ts, root)          # dependency order within a capsule
    caps = toposort({t["capsule"] for t in ts}, capsule_edges(root), lambda c: c)
    rank = {c: i for i, c in enumerate(caps)}
    ts.sort(key=lambda t: rank[t["capsule"]])   # stable: keeps the order above
    return ts


def entry(t):
    runs = len(t["blocks"])
    lean = len(t["lean_blocks"])
    ran = [f"{runs} runnable block{'s' if runs != 1 else ''}"]
    if lean:
        ran.append(f"{lean} of them a Lean core")
    if t["tools"]:
        ran.append("calls " + ", ".join(f'#raw("{x}")' for x in t["tools"]))
    facts = [
        ("teaches", inline(t["lead"]) or "#emph[no lead paragraph]"),
        ("runs", " #sym.dot.c ".join(ran)),
        ("command", f'#raw("upmd {t["path"]}")'),
    ]
    rows = ",\n    ".join(f"([{k}], [{v}])" for k, v in facts)
    method = (f'#raw("{t["method"]}")'
              if t["method"] and re.fullmatch(r"[\w-]+", t["method"] or "")
              else esc(t["method"] or "method not stated"))
    return (f'#tutorialentry([{inline(t["title"])}], '
            f'[#raw("{t["capsule"]}") #sym.dot.c {method}],\n'
            f"  (\n    {rows},\n  ))\n")


def generate(ts):
    out = [BANNER]
    seen = set()
    for prefix, title in DOMAINS:
        group = [t for t in ts if t["capsule"].startswith(prefix)]
        seen.update(t["path"] for t in group)
        if not group:
            continue
        out.append(f"= {title} tutorials\n\n")
        blocks = sum(len(t["blocks"]) for t in group)
        caps = len({t["capsule"] for t in group})
        out.append(
            f"#note[{len(group)} tutorials from {caps} "
            f"capsule{'s' if caps != 1 else ''}, "
            f"{blocks} runnable blocks between them.]\n\n")
        last = None
        for t in group:
            if t["capsule"] != last:
                last = t["capsule"]
                out.append(f'== #raw("{last}")\n\n')
            out.append(entry(t))
        out.append("\n")
    stray = [t for t in ts if t["path"] not in seen]
    if stray:  # a capsule whose name matches no domain prefix
        raise SystemExit("*** FAIL: tutorial in an unknown domain: " +
                         ", ".join(t["path"] for t in stray))
    return "".join(out)


if __name__ == "__main__":
    ts = read_tutorials()
    if not ts:
        raise SystemExit("*** FAIL: no tutorials found under skills/*/tutorial/")
    if "--list" in sys.argv:
        for t in ts:
            print(f"{t['capsule']:28} {t['slug']:34} "
                  f"{len(t['blocks']):3} blocks, {len(t['lean_blocks'])} lean, "
                  f"{t['words']:5} words, tools={t['tools']}")
        print(f"{len(ts)} tutorials, "
              f"{sum(len(t['blocks']) for t in ts)} blocks, "
              f"{sum(t['words'] for t in ts)} words")
        sys.exit(0)
    text = generate(ts)
    if "--stdout" in sys.argv:
        print(text, end="")
    else:
        OUT.parent.mkdir(parents=True, exist_ok=True)
        OUT.write_text(text)
        print(f"wrote {OUT.relative_to(ROOT)} ({len(ts)} tutorials)")
