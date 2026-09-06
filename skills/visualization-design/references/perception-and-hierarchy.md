# Perception, Tufte, colour, hierarchy

## Cleveland–McGill: encode important quantities with accurate channels

Graphs are decoded as perceptual tasks. For comparisons the reader must make
*accurately*, use channels near the top of this ordering; reserve the lower ones
for secondary or categorical information.

1. Position on a common, aligned scale
2. Position on identical but non-aligned scales
3. Length
4. Angle / slope
5. Area
6. Volume / curvature
7. Colour luminance / saturation
8. Colour hue / shape / texture (categorical only — not magnitude)

Consequences:

- Exact quantitative comparison → dot plot, bar, line, interval plot.
- Relationship → scatter (position–position).
- Subgroup comparison → small multiples with **aligned** axes.
- Broad pattern scan, not exact reading → heatmap (luminance).
- Precise values matter → labelled table or direct value labels.
- Part-to-whole with few, well-separated parts → a single stacked bar reads
  better than a pie; a pie is acceptable only for 2–4 clearly different slices.
- Never 3D bars / 3D pies / perspective for quantitative comparison — they move
  the encoding down to area/volume *and* add distortion.

## Tufte principles → agent rules (with caveats)

| Principle | Rule | Caveat |
|---|---|---|
| Maximize data-ink ratio | Remove marks that don't help the reader read, compare, navigate, or interpret | Titles, labels, uncertainty notes, annotations, and reference lines are often essential — not waste |
| Minimize chartjunk | Reject decorative 3D, gradients, drop shadows, ornamental icons, fake texture, busy backgrounds, moiré | Instructional cues and visual grouping can aid comprehension in explanatory diagrams |
| Graphical integrity | Preserve proportional encoding, scales, baselines, denominators, context | Zero baseline is mandatory for bars, often not for lines — explain the choice |
| Small multiples | Repeated consistent panels for comparison across group / place / scenario / time | Share the scale whenever magnitude comparison across panels matters |
| Data density | Prefer compact, information-rich displays over slideware | Density must not become illegibility at the actual viewing size |
| Direct labelling | Label series next to the marks | Fall back to a legend only when labels would collide |
| Show causality cautiously | Don't imply mechanism through arrows, ordering, or emphasis without evidence | Distinguish causal claims, correlations, processes, hypotheses explicitly |

Minimalism is a default, not a law. An onboarding diagram or a teaching figure
may use redundancy, enclosure, and annotation that a data-ink purist would cut.

## Cognitive and narrative rules

- One primary question per view; one focal point.
- Visual hierarchy order: **position and spatial grouping first**, then contrast,
  then size, then colour, then annotation, then motion.
- Establish context before highlighting the exception.
- Group with the Gestalt cues: proximity, alignment, enclosure, similarity,
  connectedness.
- Don't make the reader hold a distant legend in working memory.
- Minimize eye travel and mental arithmetic (show the difference if the
  difference is the point).
- Annotate the **specific insight**, not just a generic subject label.
- A title should be the conclusion when the evidence supports one:
  - weak: "Monthly Revenue by Region"
  - better: "Midwest growth offset a 12% decline in West revenue after April"
  - not: "Midwest growth caused overall revenue to recover" (causal claim, needs
    a causal design)
- Keep the underlying values, definitions, and source inspectable.

## Colour

| Data type | Palette | Rule |
|---|---|---|
| Ordered low→high | Sequential | Vary luminance monotonically; strongest intensity for the highest / most important value |
| Deviation around a meaningful zero / target | Diverging | Only when the midpoint is meaningful; label the midpoint |
| Unordered categories | Categorical / qualitative | Keep the count small (≤ ~7); pair with direct labels and a non-colour cue |
| One focal series in context | Neutral greys + one accent | A single high-contrast accent for the focus; everything else grey |
| Status / risk | Semantically consistent | Never red/green alone; pair with icon, text, or shape |

- Default to neutral greys for context and one accent for the message.
- One consistent colour meaning across a whole report / dashboard / diagram set.
- No rainbow / jet ramps for continuous data — they invent boundaries and uneven
  emphasis.
- Contrast is a limited resource: if everything is vivid, nothing stands out.

## Typography

- One legible family, or a tightly controlled pair.
- Hierarchy through size, weight, position, spacing — not ALL-CAPS everywhere.
- Sentence case for titles and labels.
- Concise axis labels and annotations; avoid rotated labels — use a horizontal
  bar chart, abbreviations, small multiples, or a table instead.
- Aligned numerals, consistent decimal places, locale-aware separators, tabular
  figures for columns of numbers.
- Enough white space to carry the grouping.
- Annotation labels sit next to their referents.

## Hierarchy heuristic

```
attention priority = f(position, contrast, size, colour, annotation, motion)
```

Position and grouping carry the structural signal. Use colour and size as
selective reinforcement of the one thing that matters — never as the sole
organizing system.
