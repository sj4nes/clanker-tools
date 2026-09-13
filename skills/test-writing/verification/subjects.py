"""Subjects under test for the `test-writing` verification fixture.

Five small functions, each carrying ONE PLANTED BUG of a shape the danluu
"How well do agents use test/verification techniques?" eval documents.  Every
subject takes `buggy=True|False` so the harness can run the same check against
the broken and the correct implementation -- a check that fails on both is not
a detector, it is a broken check.

No side effects at import: `run.sh` imports these.
"""

from fractions import Fraction

# ---------------------------------------------------------------------------
# A. net_cents -- bug shape: expected values that encode the implementation's
#    own output.  Spec: apply a whole-percent discount and round HALF-UP to the
#    nearest cent.  Bug: truncates (integer floor division) instead.
#
#    Truncation and half-up agree on most inputs, so a fixed input/output test
#    whose expected values were captured from a run is not merely silent about
#    the bug -- it certifies it.
# ---------------------------------------------------------------------------

def net_cents(gross_cents, pct_off, buggy=True):
    if not (0 <= pct_off <= 100):
        raise ValueError("pct_off out of range")
    scaled = gross_cents * (100 - pct_off)
    if buggy:
        return scaled // 100                 # truncates: 1691.5 -> 1691
    return (scaled + 50) // 100              # half-up:   1691.5 -> 1692


# ---------------------------------------------------------------------------
# B. pack / unpack -- bug shape: symmetric (palindromic) input data masking a
#    reversal bug.  The wire format writes symbols BACK TO FRONT (as Zstd's
#    bitstream does), so the reader must consume the buffer from the end.
#    Bug: unpack reads forward.  A palindromic buffer hides it completely.
#
#    `pack` is the format definition and is deliberately bug-free: the planted
#    bug is in the reader, and the round-trip property is what exposes it.
# ---------------------------------------------------------------------------

def pack(symbols):
    """Serialise: last symbol first."""
    return list(reversed(list(symbols)))


def unpack(buf, buggy=True):
    if buggy:
        return list(buf)                     # forgets the reversal
    return list(reversed(list(buf)))


# ---------------------------------------------------------------------------
# C. step -- bug shape: symmetric jump table masking an index transposition.
#    Spec: table[state][symbol].  Bug: table[symbol][state].
#    Any symmetric table makes the two indistinguishable.
# ---------------------------------------------------------------------------

def step(table, state, symbol, buggy=True):
    if buggy:
        return table[symbol][state]
    return table[state][symbol]


# ---------------------------------------------------------------------------
# D. parse_kv -- bug shape: naive randomization where every input falls down
#    the same rejection path.  Spec: "k=v;k=v" with lowercase-alnum keys and
#    integer values; on a REPEATED key, last value wins.  Bug: first wins.
#
#    The bug lives past two guards (well-formed line, repeated key).  Uniform
#    random bytes are rejected at the first guard essentially always, so a
#    naive fuzzer reaches the buggy branch zero times and reports success.
# ---------------------------------------------------------------------------

def parse_kv(line, buggy=True):
    out = {}
    if not line:
        raise ValueError("empty")
    for field in line.split(";"):
        if field.count("=") != 1:
            raise ValueError("malformed field: %r" % (field,))
        key, value = field.split("=")
        if not key or not key.isalnum() or not key.islower():
            raise ValueError("bad key: %r" % (key,))
        if not value or not value.isdigit():
            raise ValueError("bad value: %r" % (value,))
        if buggy and key in out:
            continue                          # first wins -- wrong
        out[key] = int(value)
    return out


def reaches_repeated_key(line):
    """True iff `line` is well formed AND repeats a key -- i.e. it exercises
    the branch the planted bug lives in.  Used for a COVERAGE assertion:
    a generator that never reaches here cannot have tested anything."""
    if not line:
        return False
    seen = set()
    repeated = False
    for field in line.split(";"):
        if field.count("=") != 1:
            return False
        key, value = field.split("=")
        if not key or not key.isalnum() or not key.islower():
            return False
        if not value or not value.isdigit():
            return False
        if key in seen:
            repeated = True
        seen.add(key)
    return repeated


# ---------------------------------------------------------------------------
# E. median -- bug shape: a property test that checks one trivial always-true
#    property.  Spec: for even n, the mean of the two middle values.
#    Bug: returns the lower middle.
#
#    "min <= median <= max" holds for the bug, for the fix, and for a great
#    many other wrong answers.  Negation symmetry does not.
# ---------------------------------------------------------------------------

def median(xs, buggy=True):
    if not xs:
        raise ValueError("empty")
    s = sorted(Fraction(x) for x in xs)
    n = len(s)
    if n % 2 == 1:
        return s[n // 2]
    if buggy:
        return s[n // 2 - 1]                  # lower middle
    return (s[n // 2 - 1] + s[n // 2]) / 2
