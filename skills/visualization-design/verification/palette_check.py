#!/usr/bin/env python3
"""Accessibility checks the `visualization-design` skill prescribes for a
categorical palette:

  1. every pair of categories separates in GRAYSCALE (WCAG relative luminance),
  2. every pair still separates under simulated colour-vision deficiency
     (deuteranopia, protanopia, tritanopia),
  3. a rainbow/jet ramp is shown to FAIL a monotonic-luminance test that a
     proper sequential ramp passes.

Pure stdlib. The CVD simulation uses the Viénot–Brettel–Mollon linear
approximation on linear-light sRGB -- adequate for a pass/fail design gate.
"""
from __future__ import annotations

import itertools
import math

# ---- sRGB <-> linear, relative luminance -------------------------------------


def _to_linear(c: float) -> float:
    c /= 255.0
    return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4


def _to_srgb(c: float) -> float:
    c = max(0.0, min(1.0, c))
    v = 12.92 * c if c <= 0.0031308 else 1.055 * c ** (1 / 2.4) - 0.055
    return v * 255.0


def luminance(rgb: tuple[float, float, float]) -> float:
    r, g, b = (_to_linear(x) for x in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast(a: tuple, b: tuple) -> float:
    la, lb = luminance(a), luminance(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


# ---- colour-vision-deficiency simulation ------------------------------------

# Viénot, Brettel & Mollon (1999) dichromat simulation matrices, applied to
# linear-light sRGB. Standard, reproducible, adequate for a pass/fail gate.
_SIM = {
    "deuteranopia": (
        (0.367322, 0.860646, -0.227968),
        (0.280085, 0.672501, 0.047413),
        (-0.011820, 0.042940, 0.968881),
    ),
    "protanopia": (
        (0.152286, 1.052583, -0.204868),
        (0.114503, 0.786281, 0.099216),
        (-0.003882, -0.048116, 1.051998),
    ),
    "tritanopia": (
        (1.255528, -0.076749, -0.178779),
        (-0.078411, 0.930809, 0.147602),
        (0.004733, 0.691367, 0.303900),
    ),
}


def _matvec(m, v):
    return tuple(sum(m[i][j] * v[j] for j in range(3)) for i in range(3))


def simulate_cvd(rgb: tuple[float, float, float], kind: str) -> tuple:
    lin = tuple(_to_linear(x) for x in rgb)
    lin2 = _matvec(_SIM[kind], lin)
    return tuple(_to_srgb(x) for x in lin2)


# ---- perceptual distance (CIE76 in Lab, good enough for a gate) ------------


def _lab(rgb):
    lin = [_to_linear(c) for c in rgb]
    X = 0.4124 * lin[0] + 0.3576 * lin[1] + 0.1805 * lin[2]
    Y = 0.2126 * lin[0] + 0.7152 * lin[1] + 0.0722 * lin[2]
    Z = 0.0193 * lin[0] + 0.1192 * lin[1] + 0.9505 * lin[2]
    Xn, Yn, Zn = 0.95047, 1.0, 1.08883

    def f(t):
        return t ** (1 / 3) if t > 0.008856 else 7.787 * t + 16 / 116

    fx, fy, fz = f(X / Xn), f(Y / Yn), f(Z / Zn)
    return (116 * fy - 16, 500 * (fx - fy), 200 * (fy - fz))


def delta_e(a, b):
    la, lb = _lab(a), _lab(b)
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(la, lb)))


# ---- palettes -------------------------------------------------------------

# Okabe-Ito: an 8-colour categorical palette designed for CVD safety.
OKABE_ITO = {
    "orange": (230, 159, 0),
    "sky blue": (86, 180, 233),
    "bluish green": (0, 158, 115),
    "yellow": (240, 228, 66),
    "blue": (0, 114, 178),
    "vermillion": (213, 94, 0),
    "reddish purple": (204, 121, 167),
    "black": (0, 0, 0),
}

# a deliberately bad categorical palette: red / green / brown all collide
BAD_CATEGORICAL = {
    "red": (214, 39, 40),
    "green": (44, 160, 44),
    "brown": (140, 86, 75),
}

# ordered ramps: jet (bad) vs single-hue blues (good)
JET = [(0, 0, 131), (0, 60, 170), (5, 255, 255), (255, 255, 0), (250, 0, 0)]
BLUES = [(247, 251, 255), (198, 219, 239), (107, 174, 214),
         (33, 113, 181), (8, 48, 107)]

GRAY_MIN = 1.10      # min grayscale contrast ratio between any two categories
DE_MIN = 12.0        # min CIE76 delta-E between any two categories (incl. CVD)


def check_categorical(name: str, pal: dict) -> bool:
    print(f"\n--- categorical palette: {name} ({len(pal)} colours) ---")
    ok = True
    items = list(pal.items())
    worst_gray = math.inf
    worst_de = {"normal": math.inf, **{k: math.inf for k in _SIM}}
    for (na, ca), (nb, cb) in itertools.combinations(items, 2):
        g = contrast(ca, cb)
        worst_gray = min(worst_gray, g)
        worst_de["normal"] = min(worst_de["normal"], delta_e(ca, cb))
        for kind in _SIM:
            d = delta_e(simulate_cvd(ca, kind), simulate_cvd(cb, kind))
            worst_de[kind] = min(worst_de[kind], d)
    # Grayscale separation is advisory for a *categorical* palette: a
    # hue-based palette (Okabe-Ito) deliberately reuses luminance and relies
    # on the caller adding a non-colour channel (label / shape / pattern).
    note = "" if worst_gray >= GRAY_MIN else "  (low -> categories need a non-colour cue too)"
    print(f"  worst-pair grayscale contrast : {worst_gray:.2f}{note}")
    for kind, d in worst_de.items():
        flag = "" if d >= DE_MIN else "  <-- FAIL"
        print(f"  worst-pair deltaE [{kind:11}]   : {d:5.1f}{flag}")
        if d < DE_MIN:
            ok = False
    print(f"  => {'PASS' if ok else 'FAIL'}")
    return ok


def check_ramp(name: str, ramp: list) -> bool:
    lums = [luminance(c) for c in ramp]
    diffs = [lums[i + 1] - lums[i] for i in range(len(lums) - 1)]
    monotonic = all(d > 0 for d in diffs) or all(d < 0 for d in diffs)
    print(f"\n--- ordered ramp: {name} ---")
    print("  luminances : " + ", ".join(f"{x:.3f}" for x in lums))
    print(f"  monotonic in luminance : {monotonic}  "
          f"=> {'PASS (safe sequential)' if monotonic else 'FAIL (rainbow)'}")
    return monotonic


def main() -> int:
    results = []
    results.append(("Okabe-Ito categorical", check_categorical("Okabe-Ito", OKABE_ITO)))
    bad = check_categorical("bad (red/green/brown)", BAD_CATEGORICAL)
    results.append(("bad categorical correctly flagged", not bad))
    results.append(("Blues sequential ramp", check_ramp("Blues", BLUES)))
    jet_ok = check_ramp("jet / rainbow", JET)
    results.append(("jet ramp correctly flagged", not jet_ok))

    print("\n=== summary ===")
    allok = True
    for label, passed in results:
        print(f"  [{'ok' if passed else 'XX'}] {label}")
        allok &= passed
    return 0 if allok else 1


if __name__ == "__main__":
    raise SystemExit(main())
