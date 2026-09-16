#!/usr/bin/env python3
"""Break check-intro-order.py's gates one at a time and confirm each fires ALONE.

Every mutation runs on a scratch copy of the book, never on the real files. A
mutation passes only if the checker exits 1 and the set of gates it reports is
exactly the expected one — a gate seen failing only alongside another has not
been tested (docs/verifying-skills.md §8). The waiver mutation can only raise a
WARN while II.2 is undrafted, so it asserts the warning count instead.

Usage: check-intro-order-mutations.py        Exit 0 if every mutation behaves.
"""
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile

BOOK = pathlib.Path(__file__).resolve().parent.parent
SKILLS = (BOOK / "../../skills").resolve()
CHECK = BOOK / "tools/check-intro-order.py"


def run(root):
    p = subprocess.run([sys.executable, str(CHECK), str(root), str(SKILLS)],
                       capture_output=True, text=True)
    m = re.search(r"gates: (.*)$", p.stdout, re.M)
    gates = set(m.group(1).split(", ")) if m else set()
    warns = len(re.findall(r"^WARN ", p.stdout, re.M))
    return p.returncode, gates, warns, p.stdout


def edit(root, rel, old, new):
    f = root / rel
    s = f.read_text()
    assert s.count(old) == 1, f"mutation anchor not unique in {rel}: {old!r}"
    f.write_text(s.replace(old, new))


def append(root, rel, text):
    f = root / rel
    f.write_text(f.read_text() + text)


MUTATIONS = [
    ("remove an intro marker", {"marker"},
     lambda r: edit(r, "parts/01-pile/02-claim.typ", "// intro: role-deck\n", "")),
    ("register says a later, undrafted chapter", {"marker"},
     lambda r: edit(r, "outline/concepts.tsv", "statistics\tskill\tII.1", "statistics\tskill\tII.2")),
    ("use a skill before its chapter", {"before-intro"},
     lambda r: append(r, "parts/01-pile/01-asset.typ", "\nSee `statistics`.\n")),
    ("name a skill with no register row", {"unregistered"},
     lambda r: append(r, "parts/02-standard/01-default.typ", "\nSee `simulation`.\n")),
    ("marker names an unknown id", {"register"},
     lambda r: append(r, "parts/02-standard/01-default.typ", "\n// intro: nonesuch\nText.\n")),
    ("prerequisite introduced after its dependant", {"deps"},
     lambda r: append(r, "outline/deps.txt", "role-deck test-writing\n")),
    ("cycle between two undrafted concepts", {"cycle"},
     lambda r: append(r, "outline/deps.txt", "pre-registration premise\n")),
    ("book.typ includes chapters out of order", {"order"},
     lambda r: edit(r, "book.typ",
                    '#include "parts/03-findings/04-premises.typ"\n#include "parts/03-findings/05-shape.typ"',
                    '#include "parts/03-findings/05-shape.typ"\n#include "parts/03-findings/04-premises.typ"')),
]


def scratch():
    d = pathlib.Path(tempfile.mkdtemp(prefix="intro-order-"))
    for name in ("book.typ", "outline", "parts"):
        src = BOOK / name
        (shutil.copytree if src.is_dir() else shutil.copy)(src, d / name)
    return d


bad = 0
base_rc, base_gates, base_warns, out = run(BOOK)
if base_rc != 0:
    print(out)
    print("*** FAIL: the unmutated book does not pass; mutations would prove nothing")
    sys.exit(1)
print(f"baseline: exit 0, {base_warns} warning(s)")

for name, want, mutate in MUTATIONS:
    d = scratch()
    try:
        mutate(d)
        rc, gates, _, out = run(d)
    finally:
        shutil.rmtree(d)
    ok = rc == 1 and gates == want
    print(f"{'caught ' if ok else '*** FAIL'}  {name}: exit {rc}, gates {sorted(gates)} (want {sorted(want)})")
    bad += not ok

d = scratch()
try:
    edit(d, "parts/01-pile/01-asset.typ", "// not-a-use: harness", "// (waiver removed)")
    rc, _, warns, _ = run(d)
finally:
    shutil.rmtree(d)
ok = rc == 0 and warns == base_warns + 1
print(f"{'caught ' if ok else '*** FAIL'}  remove a waiver: exit {rc}, warnings {base_warns} -> {warns}")
bad += not ok

if bad:
    print(f"*** {bad} MUTATION(S) NOT CAUGHT AS EXPECTED")
    sys.exit(1)
print("ALL MUTATIONS CAUGHT, EACH BY ITS OWN GATE")
