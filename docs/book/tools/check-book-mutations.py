#!/usr/bin/env python3
"""Break check-book.sh's gates one at a time and confirm each fires ALONE.

Same standard as check-intro-order-mutations.py: a gate seen failing only
alongside another has not been tested (docs/verifying-skills.md §8). Every
mutation runs on a scratch copy of BACKLOG.md, skills/ and docs/book/, never on
the real files.

The point is narrow and worth stating: Parts IV and V are generated, and the
only thing making "generated" mean anything is a gate that fails when they go
stale. A freshness gate nobody has broken on purpose is the same artifact Part
III is four audits of.

Usage: check-book-mutations.py        Exit 0 if every mutation behaves.
"""
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile

BOOK = pathlib.Path(__file__).resolve().parent.parent
ROOT = BOOK.parents[1]
CHECK = "docs/book/tools/check-book.sh"


def scratch():
    """A copy of everything the gate reads, with nothing it writes."""
    d = pathlib.Path(tempfile.mkdtemp(prefix="book-mut-"))
    # The whole of docs/, not just docs/book: Part VI's capsule ordering reads
    # docs/tutorial-map.md, and a fixture missing it made every mutation look
    # caught for the wrong reason (2026-09-17). Copy what the gate READS.
    shutil.copytree(ROOT / "docs", d / "docs",
                    ignore=shutil.ignore_patterns("build", "__pycache__"))
    shutil.copytree(ROOT / "skills", d / "skills",
                    ignore=shutil.ignore_patterns("__pycache__", ".lake"))
    shutil.copy2(ROOT / "BACKLOG.md", d / "BACKLOG.md")
    return d


def run(root):
    p = subprocess.run(["sh", CHECK], cwd=root, capture_output=True, text=True)
    m = re.search(r"^gates:(.*)$", p.stdout, re.M)
    return p.returncode, set(m.group(1).split()) if m else set(), p.stdout


def edit(root, rel, old, new, count=1):
    f = root / rel
    s = f.read_text()
    assert s.count(old) == count, \
        f"mutation anchor appears {s.count(old)}x in {rel} (want {count}): {old!r}"
    f.write_text(s.replace(old, new))


def append(root, rel, text):
    f = root / rel
    f.write_text(f.read_text() + text)


MUTATIONS = [
    # --- the freshness gates: the repository moves, the book does not --------
    ("a skill's version moves", {"part4"},
     lambda d: edit(d, "skills/citation-check/SKILL.md",
                    "version: 1.0.0", "version: 1.1.0")),
    ("a skill gains a displacement table", {"part4"},
     lambda d: append(d, "skills/simulation/verification/README.md",
                      "\n## Displacement table\n\n**3 covered · 1 judgement · 2 gaps.**\n")),
    ("a skill is added", {"part4"},
     lambda d: _add_skill(d)),
    ("an open backlog item is added", {"part5"},
     lambda d: edit(d, "BACKLOG.md", "\n## Done\n",
                    "\n- [ ] **invented:** an item nobody wrote\n\n## Done\n")),
    ("an open backlog item is closed", {"part5"},
     lambda d: edit(d, "BACKLOG.md",
                    "- [ ] **simulation:** Extend", "- [x] **simulation:** Extend")),
    # --- hand-editing the generated file, which is the whole failure mode ----
    ("Part IV is hand-edited", {"part4"},
     lambda d: append(d, "docs/book/parts/04-catalogue/01-entries.typ",
                      '\n#skillentry("hand-written", "9.9.9", "behaviour", [Added by hand.], ())\n')),
    ("Part V is hand-edited", {"part5"},
     # Anchored on wording, not on the item COUNT: the count changes every time
     # the backlog does, and a mutation test that breaks whenever the corpus
     # moves gets disabled rather than fixed.
     lambda d: edit(d, "docs/book/parts/05-open/01-backlog.typ",
                    "open items, read from", "open items, silently miscounted,")),
    ("a tutorial gains a runnable block", {"part6"},
     lambda d: append(d, "skills/physics-newtonian/tutorial/pendulum.md",
                      "\n```bash [name:chk_invented, deps:setup]\nbc -l <<< '1+1'\n```\n")),
    ("a tutorial is added", {"part6"},
     lambda d: (d / "skills/physics-acoustics/tutorial/invented.md").write_text(
         "# An Invented Tutorial\n\n> Generated from the `physics-acoustics`"
         " capsule (Release 0.1) with the `formula-tree-tutorial` skill.\n\n"
         "It teaches nothing.\n\n```bash [name:setup]\ntrue\n```\n")),
    ("Part VI is hand-edited", {"part6"},
     lambda d: append(d, "docs/book/parts/06-tutorials/01-entries.typ",
                      '\n#tutorialentry([Hand-written], [by hand], ())\n')),
    # --- the generators' own refusals ---------------------------------------
    ("an open item is filed under Done", {"gen-open"},
     lambda d: edit(d, "BACKLOG.md", "\n## Skill standard & verification debt\n",
                    "\n- [ ] **misfiled:** open, under Done\n"
                    "\n## Skill standard & verification debt\n")),
    # The ordering is load-bearing: Part VI is in dependency order, so a cycle
    # in the evidence must stop the build rather than emit an arbitrary order.
    ("tutorial prerequisites form a cycle", {"gen-tutorials"},
     lambda d: edit(d, "skills/physics-acoustics/tutorial/how-fast-does-sound-travel.md",
                    "## What you need first\n",
                    "## What you need first\n\nNeeds [horns-and-reciprocity.md]"
                    "(horns-and-reciprocity.md) first.\n")),
    ("a skill declares an unknown archetype", {"gen-catalogue"},
     lambda d: edit(d, "skills/simulation/SKILL.md",
                    "archetype: behaviour", "archetype: invented")),
    # --- the escaper, and the two defects it exists to prevent --------------
    # Isolating only because no generated text currently contains an unmatched
    # `*`.  When first run this fired {part4} and NOT typstlib: the suite's
    # stars were all inside matched pairs, so dropping `*` from SPECIAL changed
    # the book without failing the self-test.  Both were fixed — the suite
    # gained a bare-star case, and a `**MAJOR.** **headline.**` changelog entry
    # that had been leaking literal stars into Part IV was parsed properly.
    ("typstlib stops escaping", {"typstlib"},
     lambda d: edit(d, "docs/book/tools/typstlib.py",
                    'SPECIAL = "\\\\#$@*_<>`[]~"', 'SPECIAL = "\\\\#$@_<>`[]~"')),
    ("Markdown bold reaches Typst", {"warnings"},
     lambda d: append(d, "docs/book/parts/04-catalogue/00-howtoread.typ",
                      "\nA **bold** word straight from Markdown.\n")),
    ("the book stops compiling", {"compile"},
     lambda d: append(d, "docs/book/parts/05-open/00-intro.typ",
                      "\n#no-such-function()\n")),
]


def _add_skill(d):
    """A new skill appears on disk and the catalogue does not know about it."""
    s = d / "skills/invented-skill"
    s.mkdir()
    (s / "SKILL.md").write_text(
        "---\nname: invented-skill\ndescription: >-\n  A skill that was added"
        " after the book was generated.\nversion: 1.0.0\narchetype: behaviour\n"
        "---\n\n# Invented\n")
    (s / "CHANGELOG.md").write_text("# Changelog\n\n## 1.0.0 — 2026-09-17\n\n"
                                    "First release, verified at release.\n")


if __name__ == "__main__":
    bad = 0
    for name, want, mutate in MUTATIONS:
        d = scratch()
        try:
            mutate(d)
            rc, gates, out = run(d)
        finally:
            shutil.rmtree(d)
        ok = rc == 1 and gates == want
        bad += not ok
        print(f"{'caught ' if ok else '*** FAIL'}  {name}: exit {rc}, "
              f"gates {sorted(gates)} (want {sorted(want)})")
        if not ok:
            print("\n".join("      " + x for x in out.splitlines()[:12]))

    # The control: an unmutated copy must PASS. Without it, a scratch copy that
    # is broken for some unrelated reason would score every mutation above as
    # "caught" and the whole file would be vacuous.
    d = scratch()
    try:
        rc, gates, out = run(d)
    finally:
        shutil.rmtree(d)
    ok = rc == 0 and not gates
    bad += not ok
    print(f"{'caught ' if ok else '*** FAIL'}  CONTROL (no mutation): exit {rc},"
          f" gates {sorted(gates)} (want exit 0, none)")
    if not ok:
        print("\n".join("      " + x for x in out.splitlines()[:12]))

    if bad:
        print(f"*** {bad} MUTATION(S) NOT CAUGHT AS EXPECTED")
        sys.exit(1)
    print("ALL MUTATIONS CAUGHT, EACH BY ITS OWN GATE")
