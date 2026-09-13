"""The detection matrix: for each planted bug, run the prescribed check and the
naive check against BOTH the buggy and the fixed subject, and assert the three
cells that make the fixture meaningful.

  1. prescribed(buggy)  must FAIL   -- the check detects the bug
  2. prescribed(fixed)  must PASS   -- the check is not simply always-failing
  3. naive(buggy)       must PASS   -- the naive test misses the bug

Cell 2 is the one that is easy to omit, and without it a check that returns
False unconditionally would score as a perfect detector.

A fourth cell is reported where it is informative: naive(fixed).  For bug A it
must FAIL -- the captured-output test does not merely miss the bug, it
CERTIFIES it, and would reject the correct implementation.  (Kreinin.)
"""

import naive_tests as N
import prescribed_tests as P

SUBJECTS = [
    ("A", "expected values encode the implementation's own output",
     P.prescribed_a, N.naive_a, False),
    ("B", "palindromic data masks a reversal bug",
     P.prescribed_b, N.naive_b, None),
    ("C", "symmetric jump table masks an index transposition",
     P.prescribed_c, N.naive_c, None),
    ("D", "naive randomization: every input hits the same rejection path",
     P.prescribed_d, N.naive_d, None),
    ("E", "a property test that checks one trivial always-true property",
     P.prescribed_e, N.naive_e, None),
]


def run():
    fail = 0
    print("%-3s %-11s %-11s %-11s %s" % (
        "id", "prescribed", "prescribed", "naive", "verdict"))
    print("%-3s %-11s %-11s %-11s %s" % (
        "", "on buggy", "on fixed", "on buggy", ""))
    print("-" * 78)
    for tag, shape, prescribed, naive, naive_on_fixed_want in SUBJECTS:
        pb = prescribed(True)
        pf = prescribed(False)
        nb = naive(True)
        cells = [("prescribed detects the bug", pb is False),
                 ("prescribed passes the fixed code", pf is True),
                 ("naive misses the bug", nb is True)]
        if naive_on_fixed_want is not None:
            nf = naive(False)
            cells.append(("naive(fixed) is %s" % naive_on_fixed_want,
                          nf is naive_on_fixed_want))
        bad = [name for name, ok in cells if not ok]
        print("%-3s %-11s %-11s %-11s %s" % (
            tag,
            "detects" if not pb else "MISSES",
            "green" if pf else "FALSE ALARM",
            "misses" if nb else "detects",
            "PASS" if not bad else "*** FAIL: " + "; ".join(bad)))
        print("      shape: %s" % shape)
        fail += len(bad) > 0
    return fail


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
