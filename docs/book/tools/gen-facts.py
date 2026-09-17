#!/usr/bin/env python3
"""Generate corpus-facts.typ — the corpus counts, once, as named constants.

The same figures were being retyped into prose in four places and had already
drifted apart: one dated as-of, one "at the time of writing" with no date, one
rhetorical, one historical and undated (docs/book/drift-check.md §4, ledger row
C-I-08, which says "ROTS"). A chapter now writes `#n-skills`, and there is one
place for the number to be wrong.

    #import "../../corpus-facts.typ": n-skills, corpus-asof

TWO KINDS OF FACT, and the difference is why this file is not simply generated:

  GATED     structural counts — skills, archetypes, displacement tables,
            tutorials, MAJOR bumps. They change rarely and meaningfully, so
            check-book.sh regenerates and diffs them like any other generated
            part. A stale one is a real failure.

  STAMPED   the as-of date, the commit count, the corpus's age. These move with
            EVERY commit. Diff-gating them would fail check-book.sh immediately
            after each commit, and a gate that cries wolf is a gate somebody
            switches off -- which is this book's own subject. They are therefore
            carried forward from the existing file unchanged, and only move when
            a person runs `--stamp`.

    python3 docs/book/tools/gen-facts.py            write (stamps preserved)
    python3 docs/book/tools/gen-facts.py --stamp    also re-read git: new as-of
    python3 docs/book/tools/gen-facts.py --stdout   print instead of writing
"""
import datetime
import pathlib
import re
import subprocess
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from corpus import ROOT, read_corpus          # noqa: E402

OUT = ROOT / "docs/book/corpus-facts.typ"
STAMPED = ("corpus-asof", "n-commits", "corpus-days", "corpus-first-commit")


def git(*args):
    return subprocess.run(("git", *args), cwd=ROOT, capture_output=True,
                          text=True, check=True).stdout.strip()


def existing_stamps():
    """The stamped values already in the file, so a normal run does not move them."""
    if not OUT.exists():
        return {}
    txt = OUT.read_text()
    out = {}
    for k in STAMPED:
        m = re.search(rf'^#let {re.escape(k)} = (.+)$', txt, re.M)
        if m:
            out[k] = m.group(1).strip()
    return out


def fresh_stamps():
    first = git("log", "--reverse", "--format=%as").splitlines()[0]
    today = datetime.date.today()
    days = (today - datetime.date.fromisoformat(first)).days
    return {
        "corpus-asof": f'"{today.strftime("%-d %B %Y")}"',
        "corpus-first-commit": f'"{first}"',
        "n-commits": git("rev-list", "--count", "HEAD"),
        "corpus-days": str(days),
    }


def structural():
    recs = read_corpus()
    arche = {}
    for r in recs:
        arche[r["archetype"]] = arche.get(r["archetype"], 0) + 1
    words = sum(len((ROOT / "skills" / r["name"] / "SKILL.md").read_text().split())
                for r in recs)
    tut = [p for p in (ROOT / "skills").glob("*/tutorial/*.md")
           if p.name != "README.md"]
    blocks = sum(len(re.findall(r"^```bash \[name:", p.read_text(), re.M))
                 for p in tut)
    return {
        "n-skills": len(recs),
        "n-behaviour": arche.get("behaviour", 0),
        "n-capsule": arche.get("capsule", 0),
        "n-tool-fact": arche.get("tool-fact", 0),
        "n-meta": arche.get("meta", 0),
        # Rounded on purpose: the exact word count is noise in prose, and a
        # gated exact figure would move on any wording change in any skill.
        "skill-words": f'"{round(words, -3):,}"'.replace(",", ",") ,
        "n-with-table": sum(1 for r in recs if r["has_table"]),
        "n-reporting-counts": sum(1 for r in recs if r["counts"]),
        "n-major-bumps": sum(len(r["majors"]) for r in recs),
        "n-skills-ever-wrong": sum(1 for r in recs if r["majors"]),
        "n-tutorials": len(tut),
        "n-tutorial-blocks": blocks,
    }


def generate():
    # git is consulted ONLY when a stamp is being refreshed or is missing.
    # Without that condition the generator cannot run outside a git checkout —
    # which is exactly where the mutation harness runs it, and the no-mutation
    # control is what caught it (2026-09-17).
    stamps = {} if "--stamp" in sys.argv else existing_stamps()
    if "--stamp" in sys.argv or any(k not in stamps for k in STAMPED):
        stamps = {**fresh_stamps(), **stamps}
    s = structural()
    lines = [
        "// GENERATED FILE — DO NOT EDIT.",
        "//   generator: docs/book/tools/gen-facts.py",
        "//   gate:      docs/book/tools/check-book.sh  (regenerates and diffs)",
        "//",
        "// The corpus's own numbers, as named constants, so a figure is typed",
        "// once and cannot drift between chapters (drift-check.md §4).",
        "//",
        "// STAMPED values below move only when someone runs `gen-facts.py",
        "// --stamp`. They change with every commit, and diff-gating them would",
        "// fail the build after each one.",
        "",
        "// --- stamped: as-of the last deliberate stamp ------------------------",
    ]
    for k in STAMPED:
        lines.append(f"#let {k} = {stamps[k]}")
    lines += ["", "// --- gated: structural, regenerated and diffed ------------------------"]
    for k, v in s.items():
        lines.append(f"#let {k} = {v}")
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    text = generate()
    if "--stdout" in sys.argv:
        print(text, end="")
    else:
        OUT.write_text(text)
        print(f"wrote {OUT.relative_to(ROOT)}"
              f"{' (re-stamped)' if '--stamp' in sys.argv else ''}")
