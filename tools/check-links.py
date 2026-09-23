#!/usr/bin/env python3
"""Relative Markdown links across the corpus must resolve.

Nine were broken when this was written (2026-09-22), every one pointing at a
sibling skill or an index as though skills nested -- `../bc/SKILL.md` from
inside `design-of-experiments/references/`, which needs one more `..`. None of
them were noticed by any skill's own verification, because a link is exactly
the kind of claim a harness about the skill's SUBJECT never looks at.

Checks two things, reported separately:

  FILE    the target path exists                      (always fails the run)
  ANCHOR  `file.md#section` names a heading that      (fails the run)
          actually exists in that file

The anchor half exists because a section can move out of a file while every
path still resolves -- which happened the same day, when "The lead" moved to
the shared contract and a skill kept pointing at the file it left.

    check-links.py [--json] [--no-anchors]
"""

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+?)(#[^)\s]*)?\)")
HEADING = re.compile(r"^#{1,6}\s+(.+?)\s*$", re.M)
SKIP_SCHEME = re.compile(r"^(https?:|mailto:|ftp:|#|//)", re.I)

# Directories whose contents are not ours to police.
SKIP_DIRS = {".git", "node_modules", "__pycache__", ".claude"}

# Experiment FIXTURES are excluded, and only the fixtures. `experiments/
# finishing/subject/` is a static-site generator whose pages deliberately
# cannot reach each other -- those broken links ARE the defect the premise
# fixture measures, and a corpus check that "fixed" them would silently
# destroy the experiment. The experiments' own prose (design.md, RESULT.md,
# recovery.md) is still checked.
SKIP_PARTS = (("experiments", "subject"), ("experiments", "archive"))


def is_fixture(rel_parts):
    return any(all(p in rel_parts for p in combo) for combo in SKIP_PARTS)


def strip_code(text):
    """Blank code, fenced and inline: a link inside code is an EXAMPLE.

    Two separate false-positive sources, both found on this check's first run:
    the document skeletons in both tutorial skills carry illustrative `](...)`
    inside ```markdown fences, and `skills/typst` documents the Markdown it
    migrates FROM with inline spans like `[t](u)` and `![alt](img.png)`. The
    first version reported `u`, `f`, `url` and `img.png` as broken links.
    """
    out, inside = [], False
    for line in text.split("\n"):
        if line.lstrip().startswith("```"):
            inside = not inside
            out.append("")
            continue
        if inside:
            out.append("")
            continue
        # blank inline code spans, leaving the backticks so nothing shifts
        out.append(re.sub(r"`[^`]*`", lambda m: "`" + " " * (len(m.group(0)) - 2) + "`", line))
    return "\n".join(out)


def strip_fenced(text):
    """Fenced blocks only, keeping inline code.

    Headings must be read this way, NOT with strip_code: a heading's own
    backticked text is part of its anchor, and blanking it slugged
    "The `In the wild` beat" to a row of hyphens. Fences still go, because a
    shell comment inside one is not a heading -- the same lesson
    check_beats.py learned.
    """
    out, inside = [], False
    for line in text.split("\n"):
        if line.lstrip().startswith("```"):
            inside = not inside
            out.append("")
            continue
        out.append("" if inside else line)
    return "\n".join(out)


def slug(heading):
    """GitHub-style anchor slug: lowercase, drop punctuation, spaces to hyphens.

    Underscores are WORD characters and GitHub keeps them. The first version of
    this stripped them, so `app_<id>` slugged to `app` and the checker reported
    a live anchor as broken -- the checker's own defect presented as a corpus
    finding.

    Runs of hyphens are then collapsed on BOTH sides of the comparison (see
    `anchor_matches`). Exact hyphen counts depend on how a renderer treats
    removed punctuation between words, and that is brittle in a way this check
    should not be: the failure worth catching is a section that MOVED or
    VANISHED, not one whose anchor has one hyphen too few.
    """
    s = heading.strip().lower()
    # No HTML-tag strip: in a heading, `<id>` is almost always literal text
    # inside a code span (`app_<id>`), and removing it slugged that to `app_`
    # while the author -- correctly -- wrote `app_id`.
    s = re.sub(r"[^\w\s-]", "", s)         # punctuation, keeping _ and -
    return re.sub(r"\s", "-", s).strip("-")


def anchor_matches(want, have):
    """Compare with hyphen runs collapsed, so a renderer quirk is not a defect."""
    norm = lambda a: re.sub(r"-+", "-", a).strip("-")
    return norm(want) in {norm(h) for h in have}


def anchors_of(path, cache={}):
    if path not in cache:
        try:
            text = strip_fenced(path.read_text())
        except (OSError, UnicodeDecodeError):
            cache[path] = None
            return None
        found = {slug(h) for h in HEADING.findall(text)}
        # explicit <a name=> / id= anchors, rare but legitimate
        found |= set(re.findall(r'(?:name|id)="([^"]+)"', text))
        cache[path] = found
    return cache[path]


def markdown_files():
    """Tracked files only: the corpus is what is committed.

    `paper/` is gitignored working notes whose links are written relative to
    the repository root, and checking it reported 13 phantom failures about
    files that are exactly where they belong.
    """
    try:
        listing = subprocess.run(["git", "-C", str(ROOT), "ls-files", "*.md"],
                                 capture_output=True, text=True, check=True)
        paths = [ROOT / line for line in listing.stdout.splitlines() if line]
    except (OSError, subprocess.CalledProcessError):
        paths = sorted(ROOT.rglob("*.md"))
    for p in paths:
        parts = p.relative_to(ROOT).parts
        if any(part in SKIP_DIRS for part in parts) or is_fixture(parts):
            continue
        if p.is_symlink() or not p.is_file():
            continue
        yield p


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--no-anchors", action="store_true")
    args = ap.parse_args()

    file_bad, anchor_bad = [], []
    n_files = n_links = 0

    for src in markdown_files():
        n_files += 1
        try:
            text = strip_code(src.read_text())
        except (OSError, UnicodeDecodeError):
            continue
        for m in LINK.finditer(text):
            target, anchor = m.group(1), m.group(2)
            if SKIP_SCHEME.match(target):
                continue
            n_links += 1
            dest = (src.parent / target).resolve()
            rel = src.relative_to(ROOT).as_posix()
            if not dest.exists():
                file_bad.append({"from": rel, "link": target,
                                 "reason": "target does not exist"})
                continue
            if args.no_anchors or not anchor or dest.suffix != ".md":
                continue
            want = anchor[1:].lower()
            have = anchors_of(dest)
            if have is not None and want and not anchor_matches(want, have):
                anchor_bad.append({
                    "from": rel, "link": target + anchor,
                    "reason": f"no heading in {dest.name} slugs to '{want}'"})

    if args.json:
        print(json.dumps({"files": n_files, "links": n_links,
                          "file_bad": file_bad, "anchor_bad": anchor_bad},
                         indent=2))
    else:
        for b in file_bad:
            print(f"*** FAIL [file]   {b['from']} -> {b['link']}")
        for b in anchor_bad:
            print(f"*** FAIL [anchor] {b['from']} -> {b['link']}")
            print(f"                  {b['reason']}")
        print(f"checked {n_links} relative links in {n_files} markdown files")
        if not file_bad and not anchor_bad:
            print("ALL LINK CHECKS PASSED")
        else:
            print(f"*** {len(file_bad)} broken path(s), "
                  f"{len(anchor_bad)} broken anchor(s)", file=sys.stderr)
    return 1 if (file_bad or anchor_bad) else 0


if __name__ == "__main__":
    sys.exit(main())
