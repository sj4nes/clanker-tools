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


def read_tutorial(path):
    text = path.read_text()
    quote = " ".join(l.lstrip("> ").strip()
                     for l in text.splitlines() if l.startswith(">"))
    prov = PROV.search(quote)
    blocks = BLOCK.findall(text)
    bodies = "\n".join(b for _, _, b in blocks)
    # The lead: the first ordinary paragraph, after the title and the
    # provenance blockquote.
    body = text[text.index("\n", TITLE.search(text).start()):]
    paras = [p.strip() for p in re.split(r"\n\s*\n", body)
             if p.strip() and not p.strip().startswith((">", "#", "`"))]
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
    return sorted(
        (read_tutorial(p) for p in (root / "skills").glob("*/tutorial/*.md")
         if p.name != "README.md"),
        key=lambda t: (t["capsule"], t["slug"]))


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
