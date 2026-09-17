#!/usr/bin/env python3
"""Read the skill corpus into records, for the Part IV and Part V generators.

Parts IV and V are GENERATED rather than authored, so they cannot go stale —
see docs/book/README.md.  This module is the single reader both generators use,
so "what the book says about a skill" and "what the repository says about a
skill" cannot drift apart in two different parsers.

The rule this file is written to: **report only what the repository actually
states.**  A skill with no displacement table gets `counts = None`, not a
guessed zero, and the generators print that absence.  The absence is content:
it is the same corpus the book's Part III audits, and the book's own claim is
that an unchecked field decays.

    python3 docs/book/tools/corpus.py          summary tally, for eyeballing
    python3 docs/book/tools/corpus.py --json   the records
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]

# --- frontmatter -------------------------------------------------------------
# Deliberately not a YAML parse: the gate in tools/check-skills.sh already
# enforces the shape of `name:` and `version:`, and a dependency-free reader is
# one fewer thing that can fail differently from that gate.
FM_SCALAR = re.compile(r"^(name|version|archetype|author): *(.+?) *$", re.M)

# `## 1.2.0 — 2026-09-17`, the changelog contract of docs/skill-versioning.md
# §3b, gated by tools/check-changelogs.py.
CL_HEAD = re.compile(r"^## (\d+)\.(\d+)\.(\d+) — (\d{4}-\d{2}-\d{2})[^\n]*$", re.M)
CL_LEVEL = re.compile(r"\*\*(MAJOR|MINOR|PATCH)\b[:.]? *(.*?)(?:\*\*|$)", re.S)

# `**4 covered · 2 judgement · 2 gaps.**` — the counts docs/verifying-skills.md
# §7 calls the deliverable.  `tool-fact` appears in one table (statistics) as a
# fourth block; it is read if present rather than silently folded into another.
COUNT = re.compile(
    r"\*\*(?P<body>[^*]*?\bcovered\b[^*]*?\bgaps?\b[^*]*?)\*\*", re.I)
# The counts line is hand-written prose, so the separators vary: `·` or `,`, a
# line wrap mid-list, and at least one block name in backticks (`statistics`
# writes ``5 `judgement`,``).  Tolerating that is not the same as guessing —
# a line with no counts at all still parses to nothing.
BLOCK = re.compile(
    r"(\d+)\s*[`'\"]?\s*(covered|judgement|judgment|tool-fact|gaps?)", re.I)
# Skills that HAVE a displacement table, whether or not they state its counts.
# The difference is a finding: docs/verifying-skills.md §7 calls the counts
# "the deliverable, not the prose".
TABLE = re.compile(r"^#+ .*displacement table", re.M | re.I)


def _first_sentence(text):
    """The claim line: a description's first sentence, whitespace collapsed."""
    t = " ".join(text.split())
    m = re.search(r"(?<=[.!?])\s", t)
    return (t[: m.start() + 1] if m else t).strip()


def read_description(body):
    """The `description:` block scalar, unfolded.

    Every SKILL.md in the corpus uses `description: >-`; a plain inline
    description is accepted too rather than assumed away.
    """
    m = re.search(r"^description: *(>-|>|\|-|\||)(.*)$", body, re.M)
    if not m:
        return ""
    if not m.group(1):
        return m.group(2).strip()
    lines = []
    for line in body[m.end():].splitlines()[1:]:
        if line.strip() and not line.startswith((" ", "\t")):
            break
        lines.append(line.strip())
    return " ".join(x for x in lines if x)


def read_changelog(path):
    """Every version the skill has held, oldest first, with its level.

    The level is read as DECLARED (the `**MAJOR` that opens the entry) rather
    than recomputed from the digits: tools/check-changelogs.py already gates
    that the two agree, and duplicating that judgement here would let the book
    disagree with the gate.
    """
    if not path.exists():
        return []
    txt = path.read_text()
    heads = list(CL_HEAD.finditer(txt))
    out = []
    for i, m in enumerate(heads):
        end = heads[i + 1].start() if i + 1 < len(heads) else len(txt)
        entry = txt[m.end():end].strip()
        lvl = CL_LEVEL.match(entry)
        # Two entry styles are in use: `**MAJOR: the skill was wrong.**` carries
        # the headline inside the bold, `**MINOR.** Behaviours 5-6 ...` after
        # it.  Taking only the first would silently print an empty headline.
        if lvl:
            inside = " ".join(lvl.group(2).split()).strip(" .:—-")
            after = entry[lvl.end():].lstrip(" .\n")
            if not inside and after.startswith("**"):
                # A third style: `**MAJOR.** **The headline.** body...` —
                # the headline is the SECOND bold.  Read as `after` it kept its
                # own `**` markers, which reached the book as literal stars
                # (found by the typstlib mutation, 2026-09-17).
                close = after.find("**", 2)
                if close != -1:
                    after = after[2:close]
            head = inside if inside else after.lstrip("* ")
        else:
            head = entry
        out.append({
            "version": ".".join(m.groups()[:3]),
            "date": m.group(4),
            "level": lvl.group(1) if lvl else None,
            "headline": _first_sentence(head.split("\n\n")[0]),
        })
    out.reverse()  # oldest first: the release, then each time it was wrong
    return out


def read_counts(path):
    """The displacement-table counts, or None if the skill has no table.

    None and `{"covered": 0}` are different facts and are kept different.
    """
    if not path.exists():
        return None
    m = COUNT.search(path.read_text())
    if not m:
        return None
    counts = {}
    for n, block in BLOCK.findall(m.group("body")):
        key = {"judgment": "judgement", "gap": "gaps"}.get(
            block.lower(), block.lower())
        counts[key] = int(n)
    return counts or None


def read_skill(d):
    skill = d.name
    body = (d / "SKILL.md").read_text()
    fm_end = body.index("\n---", 3) if body.startswith("---") else len(body)
    fm = body[:fm_end]
    vdir = d / "verification"
    rec = {
        "name": skill,
        "description": read_description(fm),
        "skill_lines": len(body.splitlines()),
        "versions": read_changelog(d / "CHANGELOG.md"),
        "counts": read_counts(vdir / "README.md"),
        "has_table": (vdir / "README.md").exists()
                     and bool(TABLE.search((vdir / "README.md").read_text())),
        "has_verification": vdir.is_dir(),
        "has_runner": (vdir / "run.sh").exists(),
        "has_verification_readme": (vdir / "README.md").exists(),
    }
    for k, v in FM_SCALAR.findall(fm):
        rec[k] = v
    rec["claim"] = _first_sentence(rec["description"])
    rec["majors"] = [v for v in rec["versions"] if v["level"] == "MAJOR"]
    return rec


def read_corpus(root=ROOT):
    return [read_skill(d) for d in sorted((root / "skills").iterdir())
            if d.is_dir()]


if __name__ == "__main__":
    recs = read_corpus()
    if "--json" in sys.argv:
        print(json.dumps(recs, indent=2))
        sys.exit(0)
    print(f"{len(recs)} skills")
    for key in ("archetype",):
        tally = {}
        for r in recs:
            tally[r.get(key)] = tally.get(r.get(key), 0) + 1
        print(f"  by {key}: " + ", ".join(
            f"{k} {v}" for k, v in sorted(tally.items(), key=lambda x: -x[1])))
    tabled = [r for r in recs if r["counts"]]
    print(f"  displacement tables: {sum(r['has_table'] for r in recs)}"
          f"/{len(recs)}, of which {len(tabled)} state their counts")
    print(f"    gaps logged: {sum(r['counts'].get('gaps', 0) for r in tabled)}")
    silent = [r["name"] for r in recs if r["has_table"] and not r["counts"]]
    if silent:
        print(f"    table but no counts line: {', '.join(silent)}")
    print(f"  with verification/: {sum(r['has_verification'] for r in recs)}"
          f"  with run.sh: {sum(r['has_runner'] for r in recs)}")
    print(f"  MAJOR bumps: {sum(len(r['majors']) for r in recs)}"
          f" across {sum(1 for r in recs if r['majors'])} skills")
    noc = [r["name"] for r in recs if not r["versions"]]
    if noc:
        print(f"  *** no parsable changelog: {', '.join(noc)}")
