#!/usr/bin/env python3
"""Check that the DRAFTED book introduces every term before it uses it.

The outline's `tsort` over deps.txt proves the PLAN is ordered. It says nothing
about the prose: a chapter can name `role-deck` three chapters before anything
explains it, and the plan stays green. This reads the chapters in the order
book.typ includes them and checks the text.

Inputs (paths relative to the book root):
  outline/concepts.tsv   the term register (format documented in its header)
  outline/deps.txt       "a b" = a must be introduced no later than b
  book.typ               chapter order = #include order
  parts/NN-x/MM-y.typ    chapter id derived from the path: part NN, chapter MM
                         (01-pile/02-claim.typ -> I.2; 03-findings/00-intro -> III.0)

Markers in chapter prose (Typst comments, invisible in the PDF):
  // intro: <id>        the next non-comment line introduces <id>
  // not-a-use: <id>    the next non-comment line uses the word in another
                        sense, or in a way that needs no introduction; say why
                        after the id

Gates (each reported by name, so a mutation can be checked to trip only one):
  register      malformed or duplicate rows; unknown ids in deps or markers
  order         book.typ includes chapters out of outline order
  cycle         deps.txt has a cycle (BSD tsort exits 0 on one; read stderr)
  marker        drafted introducing chapter with no marker, marker in the wrong
                chapter, or duplicate marker
  before-intro  a use precedes the introduction (earlier chapter, or earlier
                line in the introducing chapter)
  deps          an introduction precedes the introduction of its prerequisite
  unregistered  a backticked name of a directory under skills/ with no row

WARN (exit 0): a use of a term whose introducing chapter is not drafted yet.

Usage: check-intro-order.py [book-root] [skills-dir]
Exit 0 if no gate fails.
"""
import pathlib
import re
import subprocess
import sys

ROMAN = {1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI"}
PART = {v: k for k, v in ROMAN.items()}

root = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else pathlib.Path(__file__).parent.parent)
skills_dir = pathlib.Path(sys.argv[2] if len(sys.argv) > 2 else root / "../../skills")

FAILS, WARNS = [], []


def fail(gate, msg):
    FAILS.append(gate)
    print(f"*** FAIL [{gate}] {msg}")


def warn(msg):
    WARNS.append(msg)
    print(f"WARN {msg}")


def key(chapter):
    """'III.2' -> (3, 2), sortable."""
    part, num = chapter.split(".")
    return (PART[part], int(num))


# --- register --------------------------------------------------------------
terms = {}
for n, line in enumerate((root / "outline/concepts.tsv").read_text().splitlines(), 1):
    if not line.strip() or line.startswith("#"):
        continue
    cols = line.split("\t")
    if len(cols) != 5:
        fail("register", f"concepts.tsv:{n}: expected 5 tab-separated columns, got {len(cols)}")
        continue
    tid, kind, chapter, match, _ = cols
    if tid in terms:
        fail("register", f"concepts.tsv:{n}: duplicate id {tid}")
    if kind not in ("concept", "skill", "tool"):
        fail("register", f"concepts.tsv:{n}: unknown kind {kind!r}")
    if not re.fullmatch(r"(I|II|III|IV|V|VI)\.\d+", chapter):
        fail("register", f"concepts.tsv:{n}: bad chapter id {chapter!r}")
        continue
    if match == "auto":
        rx = re.compile(r"`" + re.escape(tid) + r"`")
    elif match == "-":
        rx = None
    else:
        rx = re.compile(match, re.I)
    terms[tid] = {"chapter": chapter, "rx": rx}

edges = []
for n, line in enumerate((root / "outline/deps.txt").read_text().splitlines(), 1):
    parts = line.split()
    if not parts:
        continue
    if len(parts) != 2:
        fail("register", f"deps.txt:{n}: expected 'a b'")
        continue
    for t in parts:
        if t not in terms:
            fail("register", f"deps.txt:{n}: {t} is not in concepts.tsv")
    edges.append(tuple(parts))

# --- cycle -----------------------------------------------------------------
ts = subprocess.run(["tsort", str(root / "outline/deps.txt")], capture_output=True, text=True)
if ts.returncode != 0 or "cycle" in ts.stderr.lower():
    fail("cycle", "deps.txt: " + (ts.stderr.strip().splitlines() or ["tsort failed"])[0])

# --- chapters, in include order --------------------------------------------
chapters = []  # (chapter id, path)
for inc in re.findall(r'^#include "(parts/[^"]+)"', (root / "book.typ").read_text(), re.M):
    m = re.match(r"parts/(\d+)-[^/]+/(\d+)-[^/]+\.typ$", inc)
    if not m:
        fail("order", f"book.typ: cannot derive a chapter id from {inc}")
        continue
    chapters.append((f"{ROMAN[int(m.group(1))]}.{int(m.group(2))}", root / inc))
for (a, pa), (b, pb) in zip(chapters, chapters[1:]):
    if key(a) >= key(b):
        fail("order", f"book.typ includes {pb.relative_to(root)} ({b}) after {pa.relative_to(root)} ({a})")
drafted = {c for c, _ in chapters}
pos_of_chapter = {c: i for i, (c, _) in enumerate(chapters)}

skill_names = {p.name for p in skills_dir.iterdir() if p.is_dir()} if skills_dir.is_dir() else set()

# --- scan prose ------------------------------------------------------------
intros = {}      # id -> (chapter, line)
first_use = {}   # id -> {chapter: (line, path)}, first use per chapter
unregistered = {}
for chapter, path in chapters:
    pending_intro, pending_waive = [], []
    for n, line in enumerate(path.read_text().splitlines(), 1):
        s = line.strip()
        m = re.match(r"//\s*(intro|not-a-use):\s*([a-z0-9-]+)", s)
        if m:
            tid = m.group(2)
            if tid not in terms:
                fail("register", f"{path.relative_to(root)}:{n}: marker names unknown id {tid}")
            (pending_intro if m.group(1) == "intro" else pending_waive).append(tid)
            continue
        if s.startswith("//") or not s:
            continue
        for tid in pending_intro:
            if tid in intros:
                fail("marker", f"{path.relative_to(root)}:{n}: second intro marker for {tid}")
            elif tid in terms and terms[tid]["chapter"] != chapter:
                fail("marker", f"{path.relative_to(root)}:{n}: {tid} introduced here ({chapter}) "
                               f"but concepts.tsv says {terms[tid]['chapter']}")
            intros.setdefault(tid, (chapter, n))
        waived = set(pending_waive)
        pending_intro, pending_waive = [], []
        if s.startswith("#import"):
            continue
        for tid, t in terms.items():
            if t["rx"] and tid not in waived and t["rx"].search(line):
                first_use.setdefault(tid, {}).setdefault(chapter, (n, path))
        for name in re.findall(r"`([a-z0-9]+(?:-[a-z0-9]+)*)`", line):
            if name in skill_names and name not in terms:
                unregistered.setdefault(name, f"{path.relative_to(root)}:{n}")

for name, where in sorted(unregistered.items()):
    fail("unregistered", f"{where}: `{name}` is a skill with no row in concepts.tsv")

# --- marker and before-intro ----------------------------------------------
for tid, t in terms.items():
    ch = t["chapter"]
    if ch in drafted and tid not in intros:
        fail("marker", f"{tid}: {ch} is drafted but has no `// intro: {tid}` marker")
    for uch, (uline, upath) in first_use.get(tid, {}).items():
        where = f"{upath.relative_to(root)}:{uline}"
        if ch not in drafted:
            if key(uch) < key(ch):
                warn(f"{where}: {tid} used in {uch}; introduced in {ch}, which is not drafted yet")
            continue
        if tid not in intros:
            continue  # already failed as a missing marker
        ich, iline = intros[tid]
        if (pos_of_chapter[uch], uline) < (pos_of_chapter[ich], iline):
            fail("before-intro", f"{where}: {tid} used before its introduction at {ich} line {iline}")

# --- deps -----------------------------------------------------------------
def intro_pos(tid):
    if tid in intros:
        ich, iline = intros[tid]
        return (key(ich), iline)
    return (key(terms[tid]["chapter"]), 0)

for a, b in edges:
    if a in terms and b in terms and intro_pos(a) > intro_pos(b):
        fail("deps", f"{b} is introduced ({terms[b]['chapter']}) before its prerequisite {a} "
                     f"({terms[a]['chapter']})")

print()
print(f"{len(terms)} terms, {len(edges)} edges, {len(chapters)} drafted chapters, "
      f"{len(intros)} intro markers, {len(WARNS)} warning(s)")
if FAILS:
    print(f"*** {len(FAILS)} INTRO-ORDER FAILURE(S); gates: {', '.join(sorted(set(FAILS)))}")
    sys.exit(1)
print("INTRO ORDER OK")
