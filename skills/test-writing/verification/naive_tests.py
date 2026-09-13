"""The NAIVE test suites -- the negative contrast.

Each `naive_<x>` is the test an agent writes by default, per the eval: it looks
like a test, it runs green, and it does not constrain the planted bug.  Each
returns True when the suite passes.

These are DELIBERATELY BAD.  Do not copy them.
"""

import random

import subjects as S

TRIALS = 20000


def naive_a(buggy):
    """Fixed input/output test whose expected values were CAPTURED FROM A RUN
    of the implementation.  No independent oracle, so the bug is the spec."""
    captured = [
        (1999, 15, 1699),
        (1990, 15, 1691),   # true answer is 1692; this is the bug, recorded
        (500,  10, 450),
        (1234, 33,  826),   # true answer is 827
    ]
    for gross, pct, expect in captured:
        if S.net_cents(gross, pct, buggy=buggy) != expect:
            return False
    return True


def naive_b(buggy):
    """Round-trip on PALINDROMIC data only.  reversed(buf) == buf, so the
    reader's direction is unobservable."""
    for symbols in ([7], [3, 3], [1, 2, 1], [4, 9, 9, 4], [5, 5, 5, 5]):
        buf = S.pack(symbols)
        if S.unpack(buf, buggy=buggy) != list(symbols):
            return False
    return True


def naive_c(buggy):
    """Jump-table test on a SYMMETRIC table, driven by four IDENTICAL streams.
    table[s][c] == table[c][s] everywhere, so a transposed index is invisible."""
    table = [
        [0, 1, 2, 3],
        [1, 5, 6, 7],
        [2, 6, 10, 11],
        [3, 7, 11, 15],
    ]
    stream = [0, 1, 2, 3]
    for state in range(4):
        for symbol in stream:
            got = S.step(table, state, symbol, buggy=buggy)
            if got != table[state][symbol]:
                return False
    return True


def naive_d(buggy, seed=20260913):
    """Uniform random bytes, asserting only 'parses or raises ValueError'.
    Every input is rejected at the first guard; the buggy branch is never
    reached, and the assertion is satisfied by the rejection itself."""
    rng = random.Random(seed)
    alphabet = [chr(c) for c in range(32, 127)]
    for _ in range(TRIALS):
        line = "".join(rng.choice(alphabet) for _ in range(rng.randint(1, 24)))
        try:
            S.parse_kv(line, buggy=buggy)
        except ValueError:
            pass
        except Exception:
            return False
    return True


def naive_d_coverage(seed=20260913):
    """Fraction of naive inputs that actually reach the buggy branch."""
    rng = random.Random(seed)
    alphabet = [chr(c) for c in range(32, 127)]
    hits = 0
    for _ in range(TRIALS):
        line = "".join(rng.choice(alphabet) for _ in range(rng.randint(1, 24)))
        hits += S.reaches_repeated_key(line)
    return hits / TRIALS


def naive_e(buggy, seed=20260913):
    """One trivial always-true property: min <= median <= max.  Holds for the
    bug, for the fix, and for every other value in range."""
    rng = random.Random(seed)
    for _ in range(2000):
        xs = [rng.randint(-50, 50) for _ in range(rng.randint(1, 8))]
        m = S.median(xs, buggy=buggy)
        if not (min(xs) <= m <= max(xs)):
            return False
    return True


def naive_f(buggy, seed=20260913):
    """DIFFERENTIAL test against a "second implementation" -- a different
    algorithm that calls the same helper.  Both are wrong identically, so the
    comparison is green.  Two implementations are not two oracles."""
    rng = random.Random(seed)
    for _ in range(2000):
        n = rng.randint(0, 10 ** 6)
        b = rng.randint(2, 36)
        if S.to_base_iterative(n, b, buggy=buggy) != \
           S.to_base_recursive(n, b, buggy=buggy):
            return False
    return True
