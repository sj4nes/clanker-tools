#!/usr/bin/env python3
"""Audit every skills/*/CHANGELOG.md against the clauses of
docs/skill-versioning.md §3b that tools/check-skills.sh does NOT gate.

check-skills.sh gates one clause: the newest heading equals `version:`.
This reports the other three, for chapter II.5 (ledger C-II-32..):

  - one heading per version held   -> the oldest heading should be 1.0.0
  - each entry opens with its level -> **MAJOR / **MINOR / **PATCH
  - the declared level matches the digit that moved

It also tallies MAJOR entries by date. Report-only: always exits 0, because
these are findings to cite, not a gate (yet).

    python3 docs/book/tools/audit-changelog-levels.py     # from the repo root
"""
import collections
import glob
import re

HEAD = re.compile(r"^## (\d+)\.(\d+)\.(\d+) — (\d{4}-\d{2}-\d{2})", re.M)
LEVEL = re.compile(r"\*\*(MAJOR|MINOR|PATCH)\b")

files = sorted(glob.glob("skills/*/CHANGELOG.md"))
transitions = mismatched = undeclared = 0
no_first = []
majors_by_date = collections.Counter()

for f in files:
    txt = open(f).read()
    heads = list(HEAD.finditer(txt))
    ents = []
    for i, m in enumerate(heads):
        end = heads[i + 1].start() if i + 1 < len(heads) else len(txt)
        body = txt[m.end():end].lstrip()
        ver = tuple(int(g) for g in m.groups()[:3])
        # the level must OPEN the entry, per §3b
        lvl = LEVEL.match(body)
        ents.append((ver, m.group(4), lvl.group(1) if lvl else None))
    ents.reverse()  # oldest first
    if not ents or ents[0][0] != (1, 0, 0):
        no_first.append(f"{f} (oldest: {'.'.join(map(str, ents[0][0])) if ents else 'none'})")
    for (a, _, _), (b, date, decl) in zip(ents, ents[1:]):
        transitions += 1
        moved = ("MAJOR" if b[0] != a[0] else "MINOR" if b[1] != a[1]
                 else "PATCH" if b[2] != a[2] else "NONE")
        if moved == "MAJOR":
            majors_by_date[date] += 1
        if decl is None:
            undeclared += 1
            print(f"undeclared  {f}: {'.'.join(map(str, b))} (moved {moved})")
        elif decl != moved:
            mismatched += 1
            print(f"mismatch    {f}: {'.'.join(map(str, b))} declared {decl}, moved {moved}")

for x in no_first:
    print(f"no 1.0.0    {x}")
print(f"changelogs={len(files)} transitions={transitions} "
      f"undeclared={undeclared} mismatched={mismatched} no-1.0.0-entry={len(no_first)}")
print("MAJOR transitions recorded, by date:",
      ", ".join(f"{d} {n}" for d, n in sorted(majors_by_date.items())),
      f"(total {sum(majors_by_date.values())})")
