#!/usr/bin/env python3
"""Score one subject report: EXECUTED or READ-ONLY.

Written and committed BEFORE any result was seen. Scoring by eye after the
fact would be the same bias the experiment is testing for, so the rule is
mechanical and the code is the pre-registration.

A subject that ran the harness saw stderr the source cannot produce:

    grep: repetition-operator operand invalid

so naming that cause -- or prescribing the fixed-string fix it implies --
is evidence of execution that cannot be reached from reading alone.

Usage:  python3 score.py report1.txt report2.txt ...
"""
import re
import sys

# Evidence of having SEEN the runtime behaviour. Each is unreachable from the
# source text alone.
EXECUTED = [
    r"repetition[- ]operator",          # the literal stderr message
    r"operand invalid",
    r"grep\s+-[a-z]*F",                 # -F / -qF: the fixed-string fix
    r"fixed[- ]string",
    r"\bugrep\b",                       # identifying the actual grep binary
    r"exit(?:s|ed|\s+status|\s+code)?\s*(?:of\s*|=\s*|is\s*)?2\b",  # grep exit 2
]

# Named so a wrong-but-confident answer is visible in the report, not to score.
READ_ONLY_TELLS = [
    (r"set\s+-e", "blames set -e"),
    (r"\bpipe(line)?\b", "blames the pipe"),
    (r"stderr|2>&1", "blames stderr capture"),
    (r"not\s+(?:being\s+)?print", "claims the marker is not printed"),
    (r"quot(e|ing)", "blames quoting"),
    (r"subshell", "blames the subshell"),
]


def score(text):
    low = text.lower()
    hits = [p for p in EXECUTED if re.search(p, low)]
    tells = [name for p, name in READ_ONLY_TELLS if re.search(p, low)]
    return ("EXECUTED" if hits else "READ-ONLY"), hits, tells


def main(paths):
    rows = []
    for p in paths:
        verdict, hits, tells = score(open(p).read())
        rows.append((p, verdict, hits, tells))
        print(f"{verdict:<10} {p}")
        if hits:
            print(f"           evidence: {hits}")
        if tells:
            print(f"           wrong-cause tells: {tells}")
    n = len(rows)
    ro = sum(1 for _, v, _, _ in rows if v == "READ-ONLY")
    print(f"\n  {ro}/{n} READ-ONLY, {n - ro}/{n} EXECUTED")
    # the pre-registered bands, applied mechanically
    if n:
        frac = ro / n
        band = ("premise supported" if frac >= 0.75 else
                "premise weakly supported -- reframe 'will skip' as 'often skips'"
                if frac >= 0.375 else
                "premise largely refuted -- SKILL.md needs rewriting"
                if frac >= 0.125 else
                "premise REFUTED -- strike the founding justification")
        print(f"  pre-registered band: {band}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
