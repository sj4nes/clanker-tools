#!/usr/bin/env python3
"""Count occasions where the TEST was found wrong, not the thing under test.

This is the mechanically checkable part of `directed-verification`. Most of the
skill is judgement and says so; this one behaviour leaves a trace, because a
repository that records its own corrections records them in commit bodies.

The number is NOT A BOUND in either direction. It misses incidents described in
other words (dde3f82, the dead marker grep, says "was dead"), and it once
matched sentences that are not admissions. Until 2026-09-17 it reported 5, of
which 2 were false: a hypothetical ("whether the instruction content or the
harness was wrong", 0fbb03c) and this skill's own release commit describing
what the detector counts (6fbfac2). The "at least three" published at release
rested on 2 real matches. So:

  - the self-test negatives include those two REAL sentences, not only
    sentences written for the test;
  - a commit that touches this file is skipped, because it describes the
    detector and every such description contains the phrases it looks for;
  - --history checks the scan against named commits in the real history, in
    both directions.

The claim the skill makes (>= 3 occasions) is checked by --history against
three commits read by hand, not by the size of the count.

Usage:
    detect_selfcorrection.py            scan git history in this repo
    detect_selfcorrection.py --self-test   prove the detector can fail
    detect_selfcorrection.py --history     check it against hand-read commits
"""
import re
import subprocess
import sys

PATTERNS = [
    r"(?<!or the )harness was wrong",
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
    # real sentences from this repository that an earlier version matched
    "where the record does not say clearly whether the instruction content or "
    "the harness was wrong, the skill stays at 1.0.0",
]

# Read by hand, 2026-09-17. The scan must find every REAL commit and none of the
# FALSE ones. A detector judged only by its count can drift either way silently.
REAL = {"197b313", "95a8cb1", "d084b25"}
FALSE = {"0fbb03c", "6fbfac2"}
SELF = "skills/directed-verification/verification/detect_selfcorrection.py"


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


def describes_detector(sha):
    files = subprocess.run(["git", "show", "--name-only", "--format=", sha],
                           capture_output=True, text=True, check=True).stdout
    return SELF in files.split()


def scan(quiet=False):
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
        if hits(body) and not describes_detector(h):
            found.append((h[:7], subj[:58]))
    if not quiet:
        print(f"    self-corrections matched in commit bodies: {len(found)} "
              f"(not a bound -- see module docstring)")
        for h, s in found:
            print(f"      {h}  {s}")
    return found


def history():
    got = {h for h, _ in scan(quiet=True)}
    bad = 0
    for h in sorted(REAL - got):
        print(f"*** FAIL missed a real admission in history: {h}")
        bad += 1
    for h in sorted(FALSE & got):
        print(f"*** FAIL matched a non-admission in history: {h}")
        bad += 1
    if bad:
        print(f"\n*** {bad} HISTORY FAILURE(S)")
        return 1
    print(f"    history: {len(REAL)} real admissions found, "
          f"{len(FALSE)} known non-admissions rejected")
    return 0


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        raise SystemExit(self_test())
    if "--history" in sys.argv:
        raise SystemExit(history())
    scan()
