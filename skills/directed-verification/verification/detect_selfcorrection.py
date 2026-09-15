#!/usr/bin/env python3
"""Count occasions where the TEST was found wrong, not the thing under test.

This is the mechanically checkable part of `directed-verification`. Most of the
skill is judgement and says so; this one behaviour leaves a trace, because a
repository that records its own corrections records them in commit bodies.

The number is a LOWER BOUND. The detector matches explicit admissions, and an
incident described in other words is missed -- which was demonstrated while
building it: a survey of "which harnesses plant a defect" produced both false
positives and false negatives on two different patterns, so no precise count is
claimed anywhere in this skill.

Usage:
    detect_selfcorrection.py            scan git history in this repo
    detect_selfcorrection.py --self-test   prove the detector can fail
"""
import re
import subprocess
import sys

PATTERNS = [
    r"harness was wrong",
    r"test was broken",
    r"mutation was wrong",
    r"my (own )?(test|mutation|discriminator|scorer|probe)\b.{0,40}\b(wrong|broken|flawed)",
    r"corrections? (went )?to the harness",
    r"wrong, not the (checker|thing|subject)",
    r"the (checker|harness) (is|was) correct",
]

# Known-good / known-bad fixtures. The detector is useless unless it can be
# shown to say NO, so both directions are asserted.
POSITIVE = [
    "the harness was wrong, not the checker",
    "two corrections went to the harness rather than to a capsule",
    "my mutation was wrong: it planted a cycle, not an unplayable card",
    "wrong, not the thing under test",
]
NEGATIVE = [
    "fix a bug in the parser",
    "the checker found 35 failures across 29 skills",
    "add a mutation harness with eight planted defects",
    "the test suite passes",
]


def hits(text):
    low = text.lower()
    return [p for p in PATTERNS if re.search(p, low)]


def self_test():
    bad = 0
    for t in POSITIVE:
        if not hits(t):
            print(f"*** FAIL missed a real admission: {t!r}")
            bad += 1
    for t in NEGATIVE:
        h = hits(t)
        if h:
            print(f"*** FAIL false positive on {t!r} via {h}")
            bad += 1
    if bad:
        print(f"\n*** {bad} DETECTOR FAILURE(S)")
        return 1
    print(f"    detector: {len(POSITIVE)} positives matched, "
          f"{len(NEGATIVE)} negatives rejected")
    return 0


def scan():
    log = subprocess.run(["git", "log", "--format=%H%x1e%s%x1e%b%x1f"],
                         capture_output=True, text=True, check=True).stdout
    found = []
    for rec in log.split("\x1f"):
        if not rec.strip():
            continue
        parts = rec.strip().split("\x1e")
        if len(parts) < 3:
            continue
        h, subj, body = parts[0], parts[1], parts[2]
        if hits(body):
            found.append((h[:7], subj[:58]))
    print(f"    self-corrections recorded in commit bodies: {len(found)} "
          f"(LOWER BOUND -- see module docstring)")
    for h, s in found:
        print(f"      {h}  {s}")
    return 0


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        raise SystemExit(self_test())
    raise SystemExit(scan())
