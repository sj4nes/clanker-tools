#!/usr/bin/env python3
"""Break each beat on its own and confirm `check_beats.py` says so.

A structural check that has only ever been run against conforming documents has
not been shown to detect anything. Every guard gets its own mutant, and a guard
whose mutant still passes is reported as DEAD -- it is decoration, not a check.

One mutant per guard, in isolation: a mutant that removes two beats cannot tell
you which guard fired.
"""

import re
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
# A tutorial that carries every beat, so each mutant removes exactly one.
SUBJECT = HERE.parents[1] / "chemistry-foundations/tutorial/solving-an-equilibrium.md"


def drop_lead(t):
    body = t[t.index("\n## How to run this"):]
    head = t[:t.index("\n## How to run this")]
    # keep title + blockquote, drop the ordinary paragraph between them
    keep = [p for p in re.split(r"\n\s*\n", head)
            if not p.strip() or p.strip().startswith(("#", ">"))]
    return "\n\n".join(keep) + body


MUTANTS = {
    "lead": (drop_lead, "no lead paragraph"),
    "provenance": (lambda t: re.sub(r"^> .*$", "", t, flags=re.M),
                   "no provenance blockquote"),
    "title": (lambda t: re.sub(r"^# .*$", "", t, count=1, flags=re.M),
              "no `# ` title"),
    "how-to-run": (lambda t: t.replace("## How to run this", "## Running it"),
                   "no `## How to run this` section"),
    "prereqs": (lambda t: t.replace("## What you need first", "## Assumed"),
                "no `## What you need first` section"),
    "capstone-section": (lambda t: re.sub(r"^## Capstone.*$", "## Finale", t,
                                          flags=re.M),
                         "no `## Capstone` section"),
    "where-next": (lambda t: t.replace("## Where to go next", "## Onward"),
                   "no `## Where to go next` section"),
    "setup-block": (lambda t: t.replace("[name:setup]", "[name:init]"),
                    "no `[name:setup]` block"),
    "chk-block": (lambda t: t.replace("[name:chk_", "[name:x_"),
                  "no `chk_<node>` block"),
    "capstone-block": (lambda t: t.replace("[name:capstone", "[name:final"),
                       "no `[name:capstone]` block"),
    "short-lead": (lambda t: drop_lead(t).replace(
        "\n## How to run this", "\n\nToo short.\n\n## How to run this", 1),
        "too short"),
    "lead-restates-title": (lambda t: drop_lead(t).replace(
        "\n## How to run this",
        "\n\nSolving an Equilibrium with an ICE Table\n\n## How to run this", 1),
        "restates the title"),
}


def run(path):
    proc = subprocess.run([sys.executable, str(HERE / "check_beats.py"), str(path)],
                          capture_output=True, text=True)
    return proc.returncode, proc.stdout + proc.stderr


# --- the contract guard: mutate the repository copy, not a temp file, because
# --- check_contract.py reads fixed paths. Each mutation is reverted immediately.
CONTRACT_MUTANTS = {
    "skill-drops-contract-ref": (
        "skills/theorem-tree-tutorial/SKILL.md",
        lambda t: t.replace("capsule-tutorial-contract.md", "nothing.md"),
        "does not reference the contract"),
    "skill-redeclares-owned-section": (
        "skills/theorem-tree-tutorial/references/document-structure.md",
        lambda t: t + "\n## The lead\n\nA second copy.\n",
        "re-declares `## The lead`"),
    "contract-loses-a-section": (
        "docs/capsule-tutorial-contract.md",
        lambda t: t.replace("## The lead", "## Opening"),
        "has no `## The lead` section"),
}


def contract_mutations(root):
    """Break the drift guard's own assumptions, one at a time."""
    import shutil
    dead = []
    script = HERE / "check_contract.py"
    proc = subprocess.run([sys.executable, str(script)], capture_output=True, text=True)
    if proc.returncode != 0:
        print("*** FAIL contract negative control: unmutated repo does not pass")
        print(proc.stdout + proc.stderr)
        return ["negative-control"]
    print("PASS contract control      unmutated repo passes")

    for name, (rel, mutate, expect) in CONTRACT_MUTANTS.items():
        target = root / rel
        backup = target.read_text()
        try:
            target.write_text(mutate(backup))
            proc = subprocess.run([sys.executable, str(script)],
                                  capture_output=True, text=True)
            out = proc.stdout + proc.stderr
            if proc.returncode != 0 and expect in out:
                print(f"PASS {name:24} caught: {expect!r}")
            elif proc.returncode != 0:
                print(f"*** FAIL {name:20} failed, but not for the stated reason")
                dead.append(name)
            else:
                print(f"*** FAIL {name:20} DEAD GUARD: mutant passed")
                dead.append(name)
        finally:
            target.write_text(backup)
    return dead


def main():
    if not SUBJECT.exists():
        print(f"subject missing: {SUBJECT}", file=sys.stderr)
        return 2
    original = SUBJECT.read_text()

    code, out = run(SUBJECT)
    if code != 0:
        print("*** FAIL negative control: the unmutated subject does not pass")
        print(out)
        return 1
    print("PASS negative control      unmutated subject passes")

    dead = []
    with tempfile.TemporaryDirectory() as tmp:
        for name, (mutate, expect) in MUTANTS.items():
            target = Path(tmp) / SUBJECT.name
            target.write_text(mutate(original))
            code, out = run(target)
            if code != 0 and expect in out:
                print(f"PASS {name:24} caught: {expect!r}")
            elif code != 0:
                print(f"*** FAIL {name:20} failed, but not for the stated reason")
                print(f"       expected {expect!r} in:\n{out}")
                dead.append(name)
            else:
                print(f"*** FAIL {name:20} DEAD GUARD: mutant passed the check")
                dead.append(name)

    print()
    dead += contract_mutations(HERE.parents[2])

    total = len(MUTANTS) + len(CONTRACT_MUTANTS)
    print(f"\n{total - len(dead)}/{total} guards demonstrated to fail on their "
          f"own mutant.")
    if dead:
        print(f"dead guards: {', '.join(dead)}")
        return 1
    print("ALL MUTATION CHECKS PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
