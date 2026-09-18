#!/usr/bin/env python3
"""Read the run out: manipulation check, capability floor, then the bands.

Nothing here decides anything the design did not already fix in writing. It
reports the gates in the order design.md commits to, and refuses to print a
band reading while a gate is unmet.
"""
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).parent
RUNS = HERE / "runs"


def score(run):
    out = subprocess.run(
        [sys.executable, str(HERE / "score.py"), str(run / "work"),
         "--events", str(run / "events.jsonl"), "--json"],
        capture_output=True, text=True,
    )
    if out.returncode != 0:
        return None
    return json.loads(out.stdout)


def main():
    arms = {"A": [], "B": []}
    contaminated = []
    for run in sorted(RUNS.glob("[AB]*")):
        check = subprocess.run(["sh", str(HERE / "check.sh"), str(run)],
                               capture_output=True, text=True)
        if check.returncode != 0:
            contaminated.append((run.name, check.stdout.strip()))
        result = score(run)
        if result:
            arms[run.name[0]].append((run.name, result))

    print("gate 1 — manipulation check")
    if contaminated:
        for name, detail in contaminated:
            print(f"  {name}: {detail}")
        print("\n*** RUN VOID. The bands are not read.")
        return 1
    print(f"  clean: {sum(len(v) for v in arms.values())} transcripts\n")

    print("gate 2 — capability floor (build.py still runs)")
    floor_ok = True
    for arm, rows in arms.items():
        runs_ok = sum(1 for _, r in rows if r["build_ok"])
        print(f"  arm {arm}: {runs_ok}/{len(rows)} still build")
        if rows and runs_ok < max(6, len(rows) // 2):
            floor_ok = False
    if not floor_ok:
        print("\n*** RUN VOID: an arm measured competence, not default.")
        return 1

    print("\nprimary — zero unresolved references in the built site")
    for arm, rows in arms.items():
        passed = [n for n, r in rows if r["primary"] == "PASS"]
        print(f"  arm {arm}: {len(passed)}/{len(rows)} PASS  {passed}")

    print("\nsecondary (descriptive, never decisive)")
    for arm, rows in arms.items():
        if not rows:
            continue
        breadth = sum(r["breadth"] for _, r in rows) / len(rows)
        ran = sum(1 for _, r in rows if r["executed_build"])
        feats = sorted({f for _, r in rows for f in r["features_added"]})
        print(f"  arm {arm}: mean breadth {breadth:.1f} files, "
              f"{ran}/{len(rows)} executed the build")
        print(f"           features added: {', '.join(feats) or 'none'}")
    print("\nRead these against design.md's bands. Do not invent a band here.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
