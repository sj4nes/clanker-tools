"""The enumerated probe domain for the run-3 fixture. Subjects never see this.

Both of score3.sh's preconditions read from here:
  * the reference agrees with the independent oracle on every probe;
  * every mutant DISAGREES with the reference on at least one probe.

The second is the one that is easy to skip and expensive to skip: a mutant that
happens to be equivalent to the reference is unkillable, and would silently drag
down every subject's kill rate in both arms.
"""

VALID_NONCANONICAL = [
    "0h 0m 0s", "0m 0s", "0h", "0m", "1h 0m 0s", "1h 0m", "0h 30m",
    "90m", "5400s", "119m 59s", "359999s", "5999m 59s",
]

INVALID = [
    "", " ", "  ", "1h 1h", "1s 1m", "1m 1h", "1s 1s", "01s", "001s", "0001h",
    "1h 60m", "1h 1m 60s", "1h 99m", "1h 1m 99s", "1x", "x", "h", "s", "1",
    "12", "1.5s", "-1s", "+1s", "1h30m", "1h  30m", " 1s", "1s ", "1h\t30m",
    "1H", "1M", "1S", "1h 30M", "100h", "100h 0m 0s", "360000s", "99h 60m",
    "１s", "١s", "1h 1s 1m", "1s 1h", "\n1s", "1s\n", "1 s", "1h 1", "1e1s",
    "0x1s", "1_0s", "٣h", "1h 0m 0s 0s", "1h 2m 3s 4s", "0s 0s",
    "99h 3599s",   # a later `s` component may not reach 60, whatever the total
]


def strings():
    """Every parse probe, in a fixed order."""
    out = []
    from_ref = _reference()
    for n in range(0, 7201):
        out.append(from_ref.format_duration(n))
    for n in range(0, 360000, 997):
        out.append(from_ref.format_duration(n))
    out.extend(VALID_NONCANONICAL)
    out.extend(INVALID)
    out.extend([5, None, 1.0, True, b"1s", ["1s"]])   # non-str probes
    return out


def ints():
    """Every format probe, in a fixed order."""
    out = list(range(0, 360000, 7))
    out.extend([0, 1, 59, 60, 61, 3599, 3600, 3601, 359998, 359999])
    out.extend([-1, -60, 360000, 360001, 999999])      # out of range
    out.extend([1.0, "5", None, True, False])          # wrong type
    return out


def outcomes(mod):
    """A comparable token per probe: the value, or the exception class name."""
    res = []
    for s in strings():
        try:
            res.append(("p", repr(s), mod.parse_duration(s)))
        except Exception as e:                          # noqa: BLE001
            res.append(("p", repr(s), type(e).__name__))
    for n in ints():
        try:
            res.append(("f", repr(n), mod.format_duration(n)))
        except Exception as e:                          # noqa: BLE001
            res.append(("f", repr(n), type(e).__name__))
    return res


def _reference():
    import importlib.util
    import os
    here = os.path.dirname(os.path.abspath(__file__))
    spec = importlib.util.spec_from_file_location(
        "_ref", os.path.join(here, "subject3", "duration.py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def load(path):
    import importlib.util
    spec = importlib.util.spec_from_file_location("_m", path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m
