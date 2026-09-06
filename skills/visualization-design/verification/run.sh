#!/bin/sh
# Verification run for the `visualization-design` skill.
#
# The skill is methodology-only (no bespoke CLI), so verification means:
# exercise the quantitative checks the skill prescribes and confirm each
# behaves as claimed.
#
#   1. WCAG contrast-ratio formula + red/green-alone failure   (bc)
#   2. Tufte lie-factor / proportional-distortion ratio        (bc)
#   3. categorical-palette grayscale + colour-vision separation (python)
#   4. rainbow-ramp non-monotonic-luminance failure vs a good sequential ramp
set -e
cd "$(dirname "$0")"

echo "=== 1-2. contrast ratios + lie factors (bc) ==="
bc -l -q checks.bc
echo

echo "=== 3-4. palette accessibility checks (python) ==="
python3 palette_check.py
echo

echo "=== 5. worked example: support-contact-rate end-to-end ==="
python3 ../examples/support-contact-rate/check.py
