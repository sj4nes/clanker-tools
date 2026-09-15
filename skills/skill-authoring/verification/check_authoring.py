#!/usr/bin/env python3
"""Hold every skill in the corpus to the standard for its ARCHETYPE.

`tools/check-skills.sh` checks what is true of every skill regardless of kind:
a version of the right shape, a name matching its directory, a changelog whose
newest entry agrees, a symlink that resolves. This checks what is true of a
skill BECAUSE OF WHAT KIND OF SKILL IT IS, which is a different question and
was previously unchecked because the kind was never declared.

    behaviour   displaces a default the agent already has. Needs a harness AND
                a displacement table, because "it reads well" is exactly the
                failure mode. (docs/verifying-skills.md §7)
    tool-fact   the agent's prior is empty; the payload is facts it cannot
                derive. A displacement table is meaningless -- there is no
                default to displace -- but reference material is the point.
    capsule     a dependency graph of knowledge. Verified by its build and
                validation scripts, not by a verification/ directory.
    meta        orchestrates other skills. Must name the ones it orchestrates.

Usage:  python3 check_authoring.py [skills-dir]
Exits 0 if every skill meets its archetype's requirements.
"""
import pathlib
import re
import sys

FAILS = []
REQUIRED_FRONTMATTER = ("name", "description", "version", "archetype", "author", "tags")
ARCHETYPES = ("behaviour", "tool-fact", "capsule", "meta")


def fail(skill, gate, msg):
    print(f"*** FAIL [{gate}] {skill}: {msg}")
    FAILS.append((skill, gate))


def frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None
    out, key = {}, None
    for line in m.group(1).split("\n"):
        k = re.match(r"^([a-z_]+):\s*(.*)$", line)
        if k:
            key = k.group(1)
            out[key] = k.group(2)
        elif key and line.startswith(" "):
            out[key] += " " + line.strip()
    return out


def check(skill_dir):
    s = skill_dir.name
    f = skill_dir / "SKILL.md"
    if not f.is_file():
        fail(s, "frontmatter", "directory under skills/ with no SKILL.md")
        return
    text = f.read_text()
    fm = frontmatter(text)
    if fm is None:
        fail(s, "frontmatter", "no frontmatter block")
        return

    for k in REQUIRED_FRONTMATTER:
        if k not in fm or not fm[k].strip():
            fail(s, "frontmatter", f"missing or empty `{k}:`")

    arch = fm.get("archetype", "").strip()
    if arch and arch not in ARCHETYPES:
        fail(s, "archetype", f"unknown archetype '{arch}' "
                             f"(known: {', '.join(ARCHETYPES)})")
        return
    if not arch:
        return

    # Every description must say what the skill is NOT for. An unbounded
    # description gets loaded for tasks it cannot help with, which costs the
    # agent context and the reader trust.
    desc = fm.get("description", "")
    # A boundary can be stated several honest ways, and the first version of
    # this gate accepted only one of them -- it flagged `chemistry-foundations`
    # ("Excludes kinetics, electrochemistry...") and `ptx` ("no conclusion may
    # rest on ptx output alone"), both of which draw a real boundary. Two of
    # the corrections on a first run are usually to the harness.
    BOUNDARY = (r"\bNOT\b|\bnot a\b|\bnot an\b|\bnot for\b|\bnot the\b"
                r"|\bexclude|\bexcluding\b|\bomits\b"
                r"|does not (cover|include|handle|replace|address|extend)"
                r"|\bout of scope\b|\brather than a\b|\bmay not\b"
                r"|\bnever\b|\bno .{0,60} may rest\b|\bstops? short\b")
    if not re.search(BOUNDARY, desc, re.I):
        fail(s, "scope", "description states no boundary — nothing says where "
                         "the skill stops applying")

    ver = skill_dir / "verification"
    if arch == "behaviour":
        if not ver.is_dir():
            fail(s, "harness", "behaviour skill with no verification/")
        else:
            if not (ver / "run.sh").is_file():
                fail(s, "harness", "verification/ with no run.sh")
            rd = ver / "README.md"
            if not rd.is_file():
                fail(s, "harness", "verification/ with no README.md "
                                   "(docs/verifying-skills.md §6)")
            elif "displacement table" not in rd.read_text().lower():
                fail(s, "displacement", "no displacement table — a behaviour "
                                        "skill must name the default each "
                                        "section displaces (§7)")
    elif arch == "tool-fact":
        if not (skill_dir / "references").is_dir():
            fail(s, "payload", "tool-fact skill with no references/ — the "
                               "lookup material IS the payload")
    elif arch == "capsule":
        for d in ("build", "validation"):
            if not (skill_dir / d).is_dir():
                fail(s, "capsule", f"no {d}/ directory")
    elif arch == "meta":
        if not re.search(r"orchestrat|consumes|invoke", text, re.I):
            fail(s, "meta", "meta skill that never names what it orchestrates")


def main(root="skills"):
    skills = sorted(p for p in pathlib.Path(root).iterdir() if p.is_dir())
    by_arch = {}
    for p in skills:
        sk = p / "SKILL.md"
        fm = (frontmatter(sk.read_text()) or {}) if sk.is_file() else {}
        by_arch.setdefault(fm.get("archetype", "?").strip(), []).append(p.name)
        check(p)
    print()
    print("  " + "  ".join(f"{k}={len(v)}" for k, v in sorted(by_arch.items())))
    if FAILS:
        gates = sorted({g for _, g in FAILS})
        print(f"\n*** {len(FAILS)} AUTHORING FAILURE(S) across {len({s for s,_ in FAILS})} "
              f"skill(s); gates: {', '.join(gates)}")
        return 1
    print(f"\nALL {len(skills)} SKILLS MEET THEIR ARCHETYPE'S STANDARD")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1] if len(sys.argv) > 1 else "skills"))
