# Accessibility and inclusive design

Accessibility is a mandatory quality dimension, checked during design — not a
final polish. The core test:

> Would the meaningful distinctions still be understandable **in grayscale, when
> printed, and read by a screen reader**? If not, add another encoding channel.

## WCAG "Use of Color" (SC 1.4.1)

Colour must not be the **only** visual means of conveying information,
distinguishing elements, or indicating an action or state. Text, shape, pattern,
position, or line style must also carry the distinction.

## Accessibility checklist

- No meaning by colour alone — add direct labels, markers, patterns, line
  styles, shapes, or position.
- Sufficient contrast for text, lines, marks, and interactive states (see
  targets below).
- Categorical palette tested against common colour-vision differences
  (deuteranopia, protanopia, tritanopia). Never red/green as the only contrast.
- Palette type matches the data: sequential for ordered magnitude, diverging only
  around a meaningful labelled midpoint, categorical for unordered groups.
- Labels legible at the intended viewing size / distance; adequate font size,
  line thickness, whitespace.
- No critical conclusion behind hover-only or tooltip-only content.
- Alt text / textual equivalent that carries the **key insight**, not "a chart".
- Accessible data table or downloadable structured data when exact values matter.
- Interactive artifacts: keyboard navigable, screen-reader interpretable, with a
  visible focus state and a reset control.
- Respect `prefers-reduced-motion`; no auto-advancing, flashing, or strobing
  content (seizure and cognitive risk).
- Usable in print, grayscale, projection, on mobile, and at low bandwidth.

Reusing one colour for different meanings within a single visualization, or a
colour system so elaborate it needs a paragraph to explain, is a sign the visual
is trying to say too much — split it.

## Contrast targets

| Element | Minimum contrast ratio vs its background |
|---|---|
| Body / label text (< ~18 pt) | 4.5 : 1 |
| Large text (≥ ~18 pt or 14 pt bold) | 3 : 1 |
| Data marks, lines, borders, icons that carry meaning | 3 : 1 |
| Adjacent categorical fills (bar vs bar, slice vs slice) | perceptibly distinct in grayscale — aim ≥ 3 : 1 luminance-contrast between neighbours, or separate them with white gaps + labels |
| Focus indicator | 3 : 1 against both focused and unfocused states |

Contrast ratio is `(L1 + 0.05) / (L2 + 0.05)` where `L` is WCAG relative
luminance and `L1 ≥ L2`. The `bc` verification check computes this.

## Alt-text protocol

**Simple chart** — one sentence: chart type, what's on each axis, the headline
finding, and the largest exception.

> Line chart of monthly defect rate, January–June 2026. The rate fell from 4.8%
> in January to 2.1% in June, with the steepest drop between March and April.

**Complex chart** — four parts:

1. Short alt text: chart type + headline finding.
2. Extended description: axes, series, key patterns, uncertainty treatment,
   notable exceptions.
3. Accessible data table, or a link to source data.
4. Method note: calculations, definitions, caveats.

**Diagram** — describe the entities and the flow, using the arrow grammar:

> System context diagram showing customers, the web application, the payment
> processor, the inventory service, and the shipping provider. Orders flow from
> customers to the web application, then to payment authorization and inventory
> reservation; shipping status returns through the application to customers.

Write alt text so that someone who cannot see the image still gets the point the
image was made to convey.
