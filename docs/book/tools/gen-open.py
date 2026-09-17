#!/usr/bin/env python3
"""Generate Part V — what is still wrong — from BACKLOG.md.

Generated for the same reason as Part IV, and one more: a closing chapter about
open problems is the chapter an author is most tempted to quietly let close.
Here it cannot be, because it is the backlog, and the backlog is where the work
is tracked either way.

Only `- [ ]` items are carried.  `- [x]` items are the repository's record of
work done and are Part III's subject, not this one.

    python3 docs/book/tools/gen-open.py            write the .typ
    python3 docs/book/tools/gen-open.py --stdout   print it instead
    python3 docs/book/tools/gen-open.py --list     one line per open item
"""
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from corpus import ROOT                       # noqa: E402
from typstlib import esc, inline              # noqa: E402

SRC = ROOT / "BACKLOG.md"
OUT = ROOT / "docs/book/parts/05-open/01-backlog.typ"

BANNER = """// GENERATED FILE — DO NOT EDIT.
//   source:    BACKLOG.md  (the open `- [ ]` items only)
//   generator: docs/book/tools/gen-open.py
//   gate:      docs/book/tools/check-book.sh  (regenerates and diffs)
// Edit BACKLOG.md, or the generator; an edit here is reverted by the gate.

#import "../../preamble.typ": note, backlogitem, points

"""

ITEM = re.compile(r"^- \[( |x)\] (.*)$")
LEAD = re.compile(r"^\*\*(.+?):?\*\*:? *")
# A trailing `(2026-09-15)` — the date the item was opened or last touched.
DATE = re.compile(r"\s*\((\d{4}-\d{2}-\d{2})\)\s*$")
# `(1)`, `(2)`, ... — several items carry their own enumerated sub-lists.
MARK = re.compile(r"\((\d+)\)\s*")
# A bold run opening a new sentence, e.g. `**PARTIALLY ADDRESSED 2026-09-16.**`
# Items accrete status updates in place, and they are the part a reader most
# needs separated from the original text.
UPDATE = re.compile(r"(?<=[.!?)])\s+(?=\*\*)")
# Sentinels marking where a Markdown sub-bullet of an item began and where the
# list returned to the item's own indentation. Control characters, so they
# cannot collide with anything BACKLOG.md contains.
BULLET, ENDBULLET = "\x00", "\x01"


def _run(text):
    """The first ascending `(1) (2) (3) ...` run in `text`, as match objects.

    Ascending-from-one only: a stray `(3)` mid-sentence, or a second run later
    in the same item, must not be read as the start of a list.
    """
    run, expect = [], 1
    for m in MARK.finditer(text):
        if int(m.group(1)) == expect:
            run.append(m)
            expect += 1
    return run if len(run) >= 2 else []


def blocks(text):
    """Break one item's body into Typst blocks: paragraphs and point lists.

    Returns a list of ("para", str) and ("points", [blocks, ...]) — each point
    is itself a block list, because a point commonly absorbs everything that
    follows it, including later status updates and a second `(1)(2)(3)` run of
    its own. Without the recursion the last point of a run came out as a
    2,500-character paragraph (found by reading page 80, 2026-09-17).
    """
    text = text.strip()
    if not text:
        return []
    if BULLET in text:
        head, rest = text.split(BULLET, 1)
        bullets = rest.split(BULLET)
        tail = ""
        if ENDBULLET in bullets[-1]:
            bullets[-1], tail = bullets[-1].split(ENDBULLET, 1)
        return (blocks(head)
                + [("points", [blocks(b) for b in bullets])]
                + blocks(tail))
    run = _run(text)
    if not run:
        return [("para", p) for p in UPDATE.split(text) if p.strip()]
    # The lede usually ends "... — " or "...:" introducing the list; the
    # punctuation is doing a job the layout now does.
    lede = text[:run[0].start()].strip().rstrip("—-:; ").strip()
    out = [("para", p) for p in UPDATE.split(lede) if p.strip()]
    pts = []
    for i, m in enumerate(run):
        end = run[i + 1].start() if i + 1 < len(run) else len(text)
        pts.append(blocks(text[m.end():end].strip().rstrip(";").strip()))
    return out + [("points", pts)]


def parse(text):
    """Open items, each with the `##` domain and `###` section it sits under.

    Fenced code blocks are skipped: BACKLOG.md documents its own item format
    inside a fence, and a parser that reads the example as an item would put a
    skill called `skill-name` in the book.  That is not hypothetical — it is
    the first `- [ ]` in the file.
    """
    domain = section = None
    items, cur, fenced = [], None, False
    for line in text.splitlines():
        if line.startswith("```"):
            fenced = not fenced
            continue
        if fenced:
            continue
        if line.startswith("## "):
            domain, section, cur = line[3:].strip(), None, None
            continue
        if line.startswith("### "):
            section, cur = line[4:].strip(), None
            continue
        m = ITEM.match(line)
        if m:
            cur = None
            if m.group(1) == " ":
                if domain == "Done":
                    # An OPEN item filed under Done is a contradiction, and a
                    # silent one: the generator would just not print it.  That
                    # is exactly the Part III failure mode -- a check with no
                    # way to fail -- so this raises instead.  It has fired
                    # once, on 14 items appended to the file's tail
                    # (2026-09-17); the fix was a heading in BACKLOG.md, not a
                    # tolerance here.
                    raise SystemExit(
                        "*** FAIL: open item filed under '## Done' in "
                        f"BACKLOG.md:\n      - [ ] {m.group(2)[:70]}\n"
                        "    Give it a heading of its own; do not relax this.")
                cur = {"domain": domain, "section": section,
                       "text": m.group(2).strip()}
                items.append(cur)
            continue
        if cur is not None and line.startswith("  ") and line.strip():
            indent = len(line) - len(line.lstrip())
            sub = re.match(r"-\s+(.*)$", line.strip())
            if sub:
                # A real Markdown sub-bullet of this item. Flattening these
                # into the paragraph printed a literal "- " mid-sentence
                # (page 73, 2026-09-17), so they are kept as structure.
                cur["bullet"] = indent
                cur["text"] += BULLET + sub.group(1)
                continue
            if cur.get("bullet") is not None and indent <= cur["bullet"]:
                cur["bullet"] = None          # back out to the item's own level
                cur["text"] += ENDBULLET + line.strip()
                continue
            # A wrapped continuation.  A line ending in a single hyphen after a
            # letter is a word broken across the wrap ("authoritative-\nLOOKING
            # dead file"), so it rejoins with NO space; an em-dash or a double
            # hyphen is punctuation and keeps its space.
            joiner = "" if re.search(r"(?<![-\s])-$", cur["text"]) else " "
            cur["text"] += joiner + line.strip()
        elif not line.strip():
            cur = None
    for it in items:
        it["text"] = " ".join(it["text"].split())
        lead = LEAD.match(it["text"])
        it["subject"] = lead.group(1) if lead else None
        body = it["text"][lead.end():] if lead else it["text"]
        d = DATE.search(body)
        it["date"] = d.group(1) if d else None
        it["body"] = body[:d.start()] if d else body
    return items


def generate(items):
    out = [BANNER]
    domains = []
    for it in items:
        if not domains or domains[-1][0] != it["domain"]:
            domains.append((it["domain"], []))
        domains[-1][1].append(it)
    out.append(
        f"#note[{len(items)} open items, read from #raw(\"BACKLOG.md\") at "
        f"generation time and grouped by the domain they sit under. The count "
        f"is not a burndown: an item closes when the work is done, and new "
        f"ones are opened by the audits of Part III.]\n\n")
    for domain, group in domains:
        out.append(f"= {esc(domain or 'Unfiled')}\n\n")
        out.append(f"#note[{len(group)} open.]\n\n")
        last = object()
        for it in group:
            if it["section"] != last:
                last = it["section"]
                if last:
                    out.append(f"== {inline(last)}\n\n")
            out.append(render(it, it["section"]))
        out.append("\n")
    return "".join(out)


def emit(bs, depth=1):
    """A block list as Typst content. Paragraphs are separated by a blank line,
    which is what makes Typst start a new paragraph rather than run them on."""
    pad = "  " * depth
    out = []
    for kind, payload in bs:
        if kind == "para":
            out.append(f"{pad}{inline(payload)}\n")
        else:
            items = ",\n".join(
                f"{pad}  [\n{emit(p, depth + 2)}{pad}  ]" for p in payload)
            out.append(f"{pad}#points(\n{items},\n{pad})\n")
    return "\n".join(out)


def render(it, section=None):
    """One item as a #backlogitem call.

    A subject that only repeats the section heading it sits under is dropped:
    three consecutive items titled `math-linear-algebra`, under a heading that
    already says `math-linear-algebra`, is noise (page 73, 2026-09-17). The
    block's own rule and spacing still separate the items.
    """
    subject = it["subject"]
    if subject and section and subject.strip("`").lower() == \
            section.split("  ")[0].split(" (")[0].strip("`").lower():
        subject = None
    subj = f"[{inline(subject)}]" if subject else "none"
    date = f'[{it["date"]}]' if it["date"] else "none"
    return (f"#backlogitem({subj}, {date})[\n"
            + emit(blocks(it["body"])) + "]\n")


if __name__ == "__main__":
    items = parse(SRC.read_text())
    if not items:
        raise SystemExit("*** FAIL: no open items parsed from BACKLOG.md")
    if "--list" in sys.argv:
        for it in items:
            print(f"{it['domain']} / {it['section']} :: "
                  f"{it['subject']} :: {it['body'][:70]}")
        sys.exit(0)
    text = generate(items)
    if "--stdout" in sys.argv:
        print(text, end="")
    else:
        OUT.parent.mkdir(parents=True, exist_ok=True)
        OUT.write_text(text)
        print(f"wrote {OUT.relative_to(ROOT)} ({len(items)} open items)")
