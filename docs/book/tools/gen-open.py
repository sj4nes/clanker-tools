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

#import "../../preamble.typ": note

"""

ITEM = re.compile(r"^- \[( |x)\] (.*)$")
LEAD = re.compile(r"^\*\*(.+?):?\*\*:? *")


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
            cur["text"] += " " + line.strip()      # a wrapped continuation
        elif not line.strip():
            cur = None
    for it in items:
        it["text"] = " ".join(it["text"].split())
        lead = LEAD.match(it["text"])
        it["subject"] = lead.group(1) if lead else None
        it["body"] = it["text"][lead.end():] if lead else it["text"]
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
            subj = (f"#strong[{inline(it['subject'])}] — " if it["subject"]
                    else "")
            out.append(f"- {subj}{inline(it['body'])}\n")
        out.append("\n")
    return "".join(out)


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
