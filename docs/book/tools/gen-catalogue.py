#!/usr/bin/env python3
"""Generate Part IV — the corpus as worked examples — from the repository.

Part IV is GENERATED, not authored, for one reason: an authored catalogue of
fifty skills is stale the day after it is written, and a book whose Part III is
four audits of things nothing checked cannot ship a chapter nothing checks.
Freshness is gated by tools/check-book.sh, which regenerates and diffs.

Every number here is read, never asserted.  Where the repository says nothing —
a skill with no displacement table, a skill with no harness — the entry says so
in as many words.  That absence is the book's own subject matter.

    python3 docs/book/tools/gen-catalogue.py            write the .typ
    python3 docs/book/tools/gen-catalogue.py --stdout   print it instead
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from corpus import ROOT, read_corpus          # noqa: E402
from typstlib import esc, inline              # noqa: E402

OUT = ROOT / "docs/book/parts/04-catalogue/01-entries.typ"

BANNER = """// GENERATED FILE — DO NOT EDIT.
//   source:    skills/*/SKILL.md, skills/*/CHANGELOG.md,
//              skills/*/verification/README.md
//   generator: docs/book/tools/gen-catalogue.py
//   gate:      docs/book/tools/check-book.sh  (regenerates and diffs)
// Edit the repository, or the generator; an edit here is reverted by the gate.

#import "../../preamble.typ": note, skillentry

"""

# Ordered by how much of the book's standard applies to the archetype, which is
# also the order the reader meets them in Part II.
GROUPS = [
    ("behaviour", "Behaviour skills",
     "Each claims to displace a default the agent already has. The standard "
     "of Part II applies to these in full: the displacement table is the "
     "deliverable, and a skill with no table has not yet been held to it."),
    ("meta", "Meta skills",
     "These orchestrate other skills. Their default is displaced at the level "
     "of the workflow, so their harnesses verify a produced artefact rather "
     "than a single prescribed check."),
    ("tool-fact", "Tool-fact skills",
     "These carry facts an agent cannot derive — which "
     "#raw(\"bc\") identifiers are legal, which exit code a cycle produces. "
     "The displacement rule does not apply: there is no wrong default to "
     "displace, only an absent fact, and the harness runs the real binary."),
    ("capsule", "Knowledge capsules",
     "Dependency-ordered graphs of a domain's results, verified by their own "
     "graph, Lean and #raw(\"bc\") harnesses rather than by a displacement "
     "table. Part III's audits are audits of these."),
]


def fact_displaces(r):
    if r["counts"]:
        c = r["counts"]
        order = ["covered", "judgement", "tool-fact", "gaps"]
        parts = [f"{c[k]} {k}" for k in order if k in c]
        body = " #sym.dot.c ".join(parts)
        if c.get("gaps"):
            body += (f", the {c['gaps']} logged in #raw(\"BACKLOG.md\")")
        return body
    if r["has_table"]:
        # docs/verifying-skills.md §7: "report the counts -- they are the
        # deliverable, not the prose".  A table whose counts are only in prose
        # is a half-applied rule, and saying so is the point of the entry.
        return ("a displacement table, but its counts are stated in prose "
                "rather than reported")
    if r["archetype"] in ("behaviour", "meta"):
        return "#emph[no displacement table]"
    return "#emph[not applicable to this archetype]"


def fact_harness(r):
    if not r["has_verification"]:
        return "#emph[no verification directory]"
    bits = []
    bits.append("#raw(\"run.sh\")" if r["has_runner"]
                else "#emph[no runner]")
    bits.append("README" if r["has_verification_readme"]
                else "#emph[no README]")
    return f"#raw(\"skills/{r['name']}/verification/\") — " + ", ".join(bits)


def fact_wrong(r):
    """Version history read as a record of being wrong.

    MAJOR is the level that means the skill WAS wrong (docs/skill-versioning.md),
    so it is the one printed in full.  A skill at 1.0.0 is not thereby correct;
    it is unrevised, and the entry says that instead.
    """
    vs, majors = r["versions"], r["majors"]
    if not vs:
        return "#emph[no parsable changelog]"
    held = len(vs)
    if not majors:
        tail = ("never revised" if held == 1 else
                f"{held} versions held, none MAJOR")
        return f"{tail} (at {esc(r['version'])}, {esc(vs[-1]['date'])})"
    lines = [f"{len(majors)} MAJOR of {held} versions held:"]
    for m in majors:
        lines.append(f"#h(0.6em) {esc(m['version'])} ({esc(m['date'])}) — "
                     f"{inline(m['headline'])}")
    return " \\\n".join(lines)


def entry(r):
    facts = [("displaces", fact_displaces(r)),
             ("harness", fact_harness(r)),
             ("wrong", fact_wrong(r))]
    rows = ",\n    ".join(f'([{label}], [{body}])' for label, body in facts)
    return (f'#skillentry("{r["name"]}", "{esc(r["version"])}", '
            f'"{esc(r["archetype"])}",\n'
            f'  [{inline(r["claim"])}],\n'
            f'  (\n    {rows},\n  ))\n')


def generate(recs):
    out = [BANNER]
    seen = set()
    for key, title, blurb in GROUPS:
        group = [r for r in recs if r.get("archetype") == key]
        seen.update(r["name"] for r in group)
        if not group:
            continue
        out.append(f"= {title}\n\n{blurb}\n\n")
        tabled = sum(1 for r in group if r["counts"])
        harnessed = sum(1 for r in group if r["has_verification"])
        out.append(
            f"#note[{len(group)} skills. {harnessed} carry a verification "
            f"directory; {tabled} report displacement counts.]\n\n")
        for r in sorted(group, key=lambda r: r["name"]):
            out.append(entry(r))
    stray = [r for r in recs if r["name"] not in seen]
    if stray:  # an archetype nobody taught the generator about
        raise SystemExit("*** FAIL: unknown archetype(s): " + ", ".join(
            f"{r['name']}={r.get('archetype')!r}" for r in stray))
    return "".join(out)


if __name__ == "__main__":
    text = generate(read_corpus())
    if "--stdout" in sys.argv:
        print(text, end="")
    else:
        OUT.parent.mkdir(parents=True, exist_ok=True)
        OUT.write_text(text)
        print(f"wrote {OUT.relative_to(ROOT)} ({len(text.splitlines())} lines)")
