"""The PRESCRIBED checks -- what the `test-writing` skill tells an agent to do
instead.  Each `prescribed_<x>` returns True when the suite passes, so the
harness can assert it FAILS on the buggy subject and PASSES on the fixed one.

The behaviours exercised, one per subject:

  A  independent re-derivation of the expected value from the SPEC (exact
     arithmetic), never a value captured from the implementation
  B  asymmetric fixtures, plus an assertion that the fixture is asymmetric
  C  an oracle stated as a FORMULA over the indices, so index order is
     observable; plus an asymmetry assertion on the table
  D  a STRUCTURED generator that steers toward the interesting branch, with a
     coverage assertion, and an oracle carried by the generator's bookkeeping
  E  a property with real discriminating power (metamorphic negation symmetry
     and a symmetric-multiset oracle), not a trivial range bound
"""

import random
from fractions import Fraction

import subjects as S

TRIALS = 20000


def _half_up(x):
    """Round a Fraction half-up.  Derived from the spec sentence, not from the
    implementation's integer trick."""
    return (x + Fraction(1, 2)).__floor__()


def prescribed_a(buggy):
    # Sweep, including every input whose exact answer lands on .5 -- the only
    # place truncation and half-up disagree, and the place a captured-output
    # test is least likely to sit.
    for gross in range(1, 3000, 7):
        for pct in (0, 3, 15, 33, 50, 67, 85, 100):
            want = _half_up(Fraction(gross * (100 - pct), 100))
            if S.net_cents(gross, pct, buggy=buggy) != want:
                return False
    # boundary on both sides of the rounding threshold, explicitly
    for gross, pct in ((1990, 15), (1994, 15), (1996, 15)):
        want = _half_up(Fraction(gross * (100 - pct), 100))
        if S.net_cents(gross, pct, buggy=buggy) != want:
            return False
    return True


def prescribed_b(buggy, seed=20260913):
    rng = random.Random(seed)
    checked = 0
    for _ in range(500):
        n = rng.randint(2, 9)
        symbols = [rng.randint(0, 255) for _ in range(n)]
        if symbols == list(reversed(symbols)):
            continue                      # a palindrome cannot discriminate
        # fixture-quality assertion: the data must break the symmetry the bug
        # hides behind, or this check is the naive one wearing a costume.
        assert symbols != list(reversed(symbols))
        checked += 1
        if S.unpack(S.pack(symbols), buggy=buggy) != symbols:
            return False
    assert checked >= 400, "fixture generated too few asymmetric cases"
    return True


def prescribed_c(buggy):
    # Table defined by a FORMULA that is not symmetric in its indices, so the
    # oracle constrains index ORDER rather than restating the lookup.
    table = [[4 * s + c for c in range(4)] for s in range(4)]
    for i in range(4):
        for j in range(4):
            if i != j:
                assert table[i][j] != table[j][i], "fixture is symmetric"
    for state in range(4):
        for symbol in range(4):
            if S.step(table, state, symbol, buggy=buggy) != 4 * state + symbol:
                return False
    return True


def _structured_line(rng):
    """Grammar-driven generator, steered toward repeated keys.  Returns the
    line and the SEMANTIC expectation built as the line is built -- the oracle
    is the generator's bookkeeping, not a second copy of the parser."""
    keys = ["a", "b", "k7", "mode"]
    nfields = rng.randint(1, 5)
    chosen = [rng.choice(keys[: rng.randint(1, 2)]) for _ in range(nfields)]
    fields = []
    expect = {}
    for key in chosen:
        value = rng.randint(0, 999)
        fields.append("%s=%d" % (key, value))
        expect[key] = value                 # last write wins, by construction
    return ";".join(fields), expect


def prescribed_d(buggy, seed=20260913):
    rng = random.Random(seed)
    hits = 0
    ok = True
    for _ in range(4000):
        line, expect = _structured_line(rng)
        hits += S.reaches_repeated_key(line)
        if S.parse_kv(line, buggy=buggy) != expect:
            ok = False
            break
    # coverage assertion: a generator that never reaches the branch under test
    # has not tested it, however green it runs.
    assert hits > 0, "structured generator never reached the repeated-key branch"
    return ok


def prescribed_d_coverage(seed=20260913):
    rng = random.Random(seed)
    hits = 0
    for _ in range(TRIALS):
        line, _ = _structured_line(rng)
        hits += S.reaches_repeated_key(line)
    return hits / TRIALS


def prescribed_e(buggy, seed=20260913):
    rng = random.Random(seed)
    for _ in range(2000):
        xs = [rng.randint(-50, 50) for _ in range(rng.randint(1, 8))]
        # metamorphic: negating the sample must negate the median
        if S.median([-x for x in xs], buggy=buggy) != -S.median(xs, buggy=buggy):
            return False
        # independent oracle on a multiset symmetric about a known centre
        centre = rng.randint(-20, 20)
        offsets = [rng.randint(1, 9) for _ in range(rng.randint(1, 4))]
        sym = [centre + d for d in offsets] + [centre - d for d in offsets]
        if S.median(sym, buggy=buggy) != centre:
            return False
    return True
