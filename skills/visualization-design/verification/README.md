# `visualization-design` skill — verification run

Methodology-only skill (no bespoke CLI), so verification means: run the
quantitative checks the skill prescribes and confirm each behaves as claimed.

## Run

```
sh skills/visualization-design/verification/run.sh
```

Tooling: `bc` 7.x (`-l`), Python 3.x (stdlib only), macOS. < 1 s.

## What each step demonstrates (SKILL.md workflow step → result)

| Step | Prescribed check | Result |
|---|---|---|
| 6 accessibility — contrast | WCAG relative-luminance + contrast-ratio formula (`checks.bc`) | black/white = `21.00`; `#767676` on white = `4.54` (the documented 4.5:1 boundary) — **pass** |
| 6 accessibility — red/green alone | contrast between two status colours used as the *only* cue | tab10 red vs green = `1.48` (< 3) — correctly flagged as failing to stand alone — **pass** |
| 5 integrity — proportional distortion | Tufte lie factor for a truncated bar and an area-for-length icon (`checks.bc`) | truncated bar (96→100 on a 90–100 axis) = `16.0`; doubled value drawn as a 2D icon = `3.0`; honest zero-baseline bar = `1.0` — **pass** |
| 6 accessibility — categorical palette | worst-pair CIE76 ΔE under normal vision and simulated deuteranopia / protanopia / tritanopia (Viénot 1999), plus grayscale separation (`palette_check.py`) | Okabe–Ito: min ΔE `16.1` across all CVD types → **PASS**; red/green/brown: deuteranopia ΔE `7.3` → correctly **FAIL** |
| 6 accessibility — sequential vs rainbow ramp | monotonic-luminance test | Blues ramp monotonic → **PASS**; jet/rainbow non-monotonic (`0.02, 0.06, 0.79, 0.93, 0.20`) → correctly **FAIL** |
| 1–9 full workflow | the [`support-contact-rate`](../examples/support-contact-rate/) worked example — messy CSV → brief → job → spec → integrity audit → a11y package → Vega-Lite source → critique (`examples/support-contact-rate/check.py`) | date normalisation; missing/partial data carried not filled; the count-vs-rate sign flip (+53% volume, −18% rate); naive quarterly bars doubly wrong; truncated-baseline lie factor `4.2`; pro-rated December on trend; `chart.vl.json` valid, zero-baseline, alt text present — **all pass** |

`run.sh` exits `0` — every check produced the call and the conclusion the skill
prescribes, including correctly failing the two deliberately bad inputs.

## Notes folded into the skill

- `bc` needs `-l` for `e()` / `l()` (used in the sRGB→linear `x^2.4` term);
  identifiers stay lowercase, letters/digits only (per the [`bc`](../../bc/SKILL.md)
  skill) — no `_`, no single uppercase letters.
- Grayscale contrast is an **advisory** signal for a *categorical* palette:
  Okabe–Ito deliberately reuses luminance across hues and expects the caller to
  add a non-colour channel (direct label, shape, pattern). This is exactly the
  `references/accessibility.md` rule ("no meaning by colour alone"), so the
  check warns rather than failing.
