"""Independent second implementation of SPEC.md, for score3.sh's precondition.

Written from the spec by a different route than subject3/duration.py: a regular
expression and an explicit table, rather than a scanning loop. Agreement between
two implementations that share no code is the evidence that the reference is
correct. Subjects never see this file.
"""

import re

_COMPONENT = re.compile(r"\A(0|[1-9][0-9]*)([hms])\Z", re.ASCII)
_ORDER = "hms"
_SIZE = {"h": 3600, "m": 60, "s": 1}
_LIMIT = 360000


def parse_duration(text):
    if type(text) is not str:
        raise ValueError("not a duration string")
    parts = text.split(" ")
    if not 1 <= len(parts) <= 3:
        raise ValueError("not a duration string")
    units, values = [], []
    for part in parts:
        m = _COMPONENT.match(part)
        if m is None:
            raise ValueError("not a duration string")
        values.append(int(m.group(1)))
        units.append(m.group(2))
    ranks = [_ORDER.index(u) for u in units]
    if ranks != sorted(set(ranks)):
        raise ValueError("not a duration string")
    for i, (u, v) in enumerate(zip(units, values)):
        if i and u in ("m", "s") and v > 59:
            raise ValueError("not a duration string")
    total = sum(_SIZE[u] * v for u, v in zip(units, values))
    if not total < _LIMIT:
        raise ValueError("not a duration string")
    return total


def format_duration(seconds):
    if type(seconds) is not int:
        raise TypeError("not an integer")
    if not 0 <= seconds < _LIMIT:
        raise ValueError("outside the duration range")
    if seconds == 0:
        return "0s"
    h, r = seconds // 3600, seconds % 3600
    m, s = r // 60, r % 60
    return " ".join(f"{v}{u}" for v, u in ((h, "h"), (m, "m"), (s, "s")) if v)
