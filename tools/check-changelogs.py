#!/usr/bin/env python3
"""Gate the clauses of docs/skill-versioning.md §3b that check-skills.sh's
check 6 does not (check 6: newest heading = `version:`).

  1.0.0     every changelog has a `## 1.0.0 — date` heading (one per version
            held, so the oldest is 1.0.0)
  level     every entry after 1.0.0 opens with **MAJOR / **MINOR / **PATCH
  mismatch  the declared level is the digit that moved

Promoted from docs/book/tools/audit-changelog-levels.py (2026-09-17), which
found these clauses decaying precisely because nothing checked them: three
entries with no level, three changelogs with no 1.0.0 heading.

    python3 tools/check-changelogs.py            gate: exit 1 on any failure
    python3 tools/check-changelogs.py --report   also tally MAJOR bumps by date
    python3 tools/check-changelogs.py --root D   check D/skills/*/CHANGELOG.md
"""
import collections
import pathlib
import re
import sys

HEAD = re.compile(r"^## (\d+)\.(\d+)\.(\d+) — (\d{4}-\d{2}-\d{2})[^\n]*$", re.M)
LEVEL = re.compile(r"\*\*(MAJOR|MINOR|PATCH)\b")

root = pathlib.Path(sys.argv[sys.argv.index("--root") + 1]) if "--root" in sys.argv \
    else pathlib.Path(__file__).resolve().parent.parent
files = sorted((root / "skills").glob("*/CHANGELOG.md"))
fails = collections.Counter()
transitions = 0
majors_by_date = collections.Counter()


def fail(gate, msg):
    fails[gate] += 1
    print(f"*** FAIL [{gate}] {msg}")


for f in files:
    rel = f.relative_to(root)
    txt = f.read_text()
    heads = list(HEAD.finditer(txt))
    ents = []
    for i, m in enumerate(heads):
        end = heads[i + 1].start() if i + 1 < len(heads) else len(txt)
        body = txt[m.end():end].lstrip()  # the heading's own line is excluded
        lvl = LEVEL.match(body)  # the level must OPEN the entry
        ents.append((tuple(int(g) for g in m.groups()[:3]), m.group(4),
                     lvl.group(1) if lvl else None))
    ents.reverse()  # oldest first
    if (1, 0, 0) not in [v for v, _, _ in ents]:
        fail("1.0.0", f"{rel}: no '## 1.0.0 — date' heading")
    for (a, _, _), (b, date, decl) in zip(ents, ents[1:]):
        transitions += 1
        moved = ("MAJOR" if b[0] != a[0] else "MINOR" if b[1] != a[1]
                 else "PATCH" if b[2] != a[2] else "NONE")
        if moved == "MAJOR":
            majors_by_date[date] += 1
        v = ".".join(map(str, b))
        if decl is None:
            fail("level", f"{rel}: {v} does not open with its level (moved {moved})")
        elif decl != moved:
            fail("mismatch", f"{rel}: {v} declares {decl}, but {moved} moved")

print(f"changelogs={len(files)} transitions={transitions}")
if "--report" in sys.argv:
    print("MAJOR transitions recorded, by date:",
          ", ".join(f"{d} {n}" for d, n in sorted(majors_by_date.items())),
          f"(total {sum(majors_by_date.values())})")
if fails:
    print(f"*** {sum(fails.values())} CHANGELOG FAILURE(S); gates: {', '.join(sorted(fails))}")
    sys.exit(1)
print("CHANGELOG CONTRACT OK")
