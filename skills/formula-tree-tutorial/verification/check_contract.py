#!/usr/bin/env python3
"""Check that both tutorial skills still defer to the shared contract.

`docs/capsule-tutorial-contract.md` exists because the skeleton was maintained
in two copies and drifted -- the lead beat was in one and not the other, and
the Lean beat in the other and not the one. Single-sourcing it only helps while
both skills actually point at it, so that is checked rather than assumed.

    check_contract.py [--json]
"""

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
CONTRACT = ROOT / "docs/capsule-tutorial-contract.md"
SKILLS = ("formula-tree-tutorial", "theorem-tree-tutorial")

# Headings that belong to the contract alone. A skill re-declaring one has
# started a second copy, which is the failure this file exists to catch.
OWNED = ("## The lead", "## The document skeleton", "## Block vocabulary",
         "## Block-naming convention")


def check():
    problems = []
    if not CONTRACT.exists():
        return [f"the contract is missing: {CONTRACT}"]

    contract = CONTRACT.read_text()
    for heading in ("## The lead", "## The document skeleton",
                    "## Block vocabulary", "## The workflow"):
        if heading not in contract:
            problems.append(f"the contract has no `{heading}` section")

    for skill in SKILLS:
        sdir = ROOT / "skills" / skill
        if not sdir.is_dir():
            problems.append(f"{skill}: missing")
            continue
        docs = list(sdir.rglob("*.md"))
        if not any("capsule-tutorial-contract.md" in d.read_text() for d in docs):
            problems.append(f"{skill}: does not reference the shared contract")
        # the skill's own SKILL.md must point at it, not only a reference file
        if "capsule-tutorial-contract.md" not in (sdir / "SKILL.md").read_text():
            problems.append(f"{skill}/SKILL.md: does not reference the contract")
        for d in docs:
            if "verification" in d.parts or d.name == "CHANGELOG.md":
                continue
            for heading in OWNED:
                if re.search(rf"^{re.escape(heading)}\s*$", d.read_text(), re.M):
                    problems.append(
                        f"{d.relative_to(ROOT)}: re-declares `{heading}`, which "
                        f"the contract owns — this is how the skeleton drifted")
    return problems


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    problems = check()
    if args.json:
        print(json.dumps({"problems": problems}, indent=2))
    elif problems:
        for p in problems:
            print(f"*** FAIL {p}")
    else:
        print(f"PASS both skills defer to docs/capsule-tutorial-contract.md, "
              f"and neither re-declares a section it owns.")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
