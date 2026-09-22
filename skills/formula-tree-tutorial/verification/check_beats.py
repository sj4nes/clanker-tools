#!/usr/bin/env python3
"""Check every shipped tutorial against the beats this skill prescribes.

The skill generates documents, so its verification is structural: the claim
under test is "a tutorial produced by this skill has these parts", and the
harness fails when one is missing. It is deliberately NOT a style checker --
each beat below is something `references/document-structure.md` states, and
nothing is enforced that the skeleton does not ask for.

    check_beats.py [--json] [path ...]

With no paths, checks every `skills/*/tutorial/*.md` in the repository.
"""

import argparse
import json
import re
import sys
from pathlib import Path

TITLE = re.compile(r"^#\s+(.+)$", re.M)
SECTION = re.compile(r"^## (.+)$", re.M)
BLOCK = re.compile(r"^```[a-z]*\s*\[name:([A-Za-z0-9_]+)", re.M)

# Bound the lead at the first `## ` heading: the first section is always
# "How to run this", whose install text is identical in every tutorial. An
# earlier audit that took "the first paragraph not starting with > # or `"
# mistook `predicting-ph`'s opening backtick for a heading and reported the
# install instructions as the lead (docs/book/tools/gen-tutorials.py, 2026-09-17).
def strip_fences(text):
    """Blank the INSIDE of every fenced block, keeping the opener lines.

    Without this, ``^#\\s+`` matches a shell comment inside a bash block and
    `^## ` matches any commented heading, so a tutorial with its title deleted
    still reports a title -- found 2026-09-22 by this check's own mutation test,
    which is the only reason the defect is not still here. Opener lines survive
    because the `[name:...]` guards parse them.
    """
    out, inside = [], False
    for line in text.split("\n"):
        if line.lstrip().startswith("```"):
            out.append(line)
            inside = not inside
            continue
        out.append("" if inside else line)
    return "\n".join(out)


def lead_of(text):
    title = TITLE.search(text)
    if not title:
        return None
    body = text[text.index("\n", title.start()):]
    intro = re.split(r"^## ", body, maxsplit=1, flags=re.M)[0]
    paras = [p.strip() for p in re.split(r"\n\s*\n", intro)
             if p.strip() and not p.strip().startswith((">", "#"))]
    return " ".join(paras[0].split()) if paras else None


def check(path):
    raw = path.read_text()
    text = strip_fences(raw)        # structure: headings and prose only
    sections = SECTION.findall(text)
    blocks = BLOCK.findall(raw)     # block names live on the fence openers
    lead = lead_of(text)
    problems = []

    if not TITLE.search(text):
        problems.append("no `# ` title")
    if not re.search(r"^> Generated from the `[\w-]+` capsule", text, re.M):
        problems.append("no provenance blockquote naming the capsule")
    if lead is None:
        problems.append("no lead paragraph between the blockquote and the "
                        "first section (references/document-structure.md, "
                        "'The lead')")
    else:
        words = len(lead.split())
        if words < 15:
            problems.append(f"lead is {words} words: too short to orient a reader")
        title = TITLE.search(text).group(1).strip().lower()
        if lead.strip().lower().rstrip(".") == title:
            problems.append("lead restates the title")
    for required in ("How to run this", "What you need first"):
        if required not in sections:
            problems.append(f"no `## {required}` section")
    # "Capstone" need not start the heading: `hole-in-the-rationals` numbers it
    # `## 12. Capstone -- the verdict`, and a startswith() match called that
    # tutorial capstone-less on this check's first run.
    if not any("capstone" in s.lower() for s in sections):
        problems.append("no `## Capstone` section")
    if "Where to go next" not in sections:
        problems.append("no `## Where to go next` section")
    if "setup" not in blocks:
        problems.append("no `[name:setup]` block")
    if not any(b.startswith("chk_") for b in blocks):
        problems.append("no `chk_<node>` block")
    if "capstone" not in blocks:
        problems.append("no `[name:capstone]` block")

    return {"path": path.as_posix(), "lead_words": len(lead.split()) if lead else 0,
            "sections": len(sections), "blocks": len(blocks), "problems": problems}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="*", type=Path)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    if args.paths:
        targets = sorted(args.paths)
    else:
        root = Path(__file__).resolve().parents[3]
        targets = sorted(p for p in root.glob("skills/*/tutorial/*.md")
                         if p.name != "README.md")
    if not targets:
        print("no tutorials found: the check would pass vacuously", file=sys.stderr)
        return 2

    results = [check(p) for p in targets]
    bad = [r for r in results if r["problems"]]

    if args.json:
        print(json.dumps(results, indent=2))
    else:
        for r in results:
            name = Path(r["path"]).stem
            if r["problems"]:
                print(f"FAIL {name}")
                for p in r["problems"]:
                    print(f"       - {p}")
            else:
                print(f"PASS {name:34} lead {r['lead_words']:>3}w  "
                      f"{r['sections']:>2} sections  {r['blocks']:>2} blocks")
        print(f"\n{len(results) - len(bad)}/{len(results)} tutorials carry every "
              f"prescribed beat.")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
