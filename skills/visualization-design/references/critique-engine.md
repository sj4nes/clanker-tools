# Design critique engine

Use this to critique an existing chart or diagram, or to self-review before
delivery. Score every dimension, run the red-flag list, then for each issue state
*why it matters for the reader's task* and propose a concrete revision.

## Scoring rubric

| Dimension | Questions |
|---|---|
| Purpose | Is the audience's key question explicit, and does the visual answer it? One focal point? |
| Semantic correctness | Does the chart / diagram type accurately encode the intended relationship? |
| Data integrity | Are scales, transformations, denominators, units, baselines, and uncertainty truthful and disclosed? |
| Perceptual effectiveness | Are the primary comparisons encoded with accurate channels (aligned position, length)? |
| Hierarchy | Is the main takeaway visually obvious without suppressing needed context? |
| Cognitive load | Can the reader interpret it without legend hunting, scrolling, or mental arithmetic? |
| Accessibility | Does the meaning survive grayscale, colour-vision differences, small size, no hover, a screen reader? |
| Annotation | Are title, labels, method, source, and caveats sufficient and correctly placed? |
| Context | Are baseline, benchmark, time frame, population, and denominator supplied? |
| Decision utility | Does it expose tradeoffs, uncertainty, and action-relevant thresholds? |
| Aesthetic coherence | Consistent, calm, intentional, free of distracting ornament? |
| Maintainability | Is it reproducible from source data / a specification? |

Score each 0–3 (absent / weak / adequate / strong). Anything below "adequate" on
Data integrity, Semantic correctness, or Accessibility blocks delivery.

## Automated red flags

- 3D pie, 3D bars, perspective effects on a quantitative comparison
- Dual y-axes without explicit justification and annotation of both scales
- Pie / donut with more than ~5–6 slices, or similar-sized slices
- Rainbow / jet scale for ordered continuous data
- Red/green-only status encoding
- Missing units or unlabelled axes
- Truncated bar / column / area baseline without a prominent break marker
- Inconsistent y-axis scales across comparable panels
- Area or volume encoding for values meant to be read as length
- Legend far from the marks where direct labelling would fit
- Overplotting with no aggregation, jitter, transparency, or density encoding
- Smoothed line masking individual observations or volatility
- Choropleth of raw counts (should be a rate, or proportional symbols)
- More than one primary message in one view
- Diagram arrows with undefined or mixed semantics
- Dense network "hairball" with no grouping, filtering, or stated task
- Dashboard tiles with isolated KPIs and no trend / benchmark / target / action
- "Statistically significant" with no effect size or interval
- Forecast rendered identically to observed data
- Simulation output with no scenario definition or uncertainty
- Mean shown for a stochastic quantity whose spread matters
- Causal diagram that conflates correlation, mediation, and temporal sequence
- Title asserts causation without a causal design

## Evaluation cases

The skill must diagnose each of these, explain the harm, propose a concrete fix,
and produce a *more interpretable* alternative (not merely a prettier one):

1. **Truncated-axis bar chart** — a 2% gap on a 90–100 axis reads as ~5×. Fix:
   zero baseline; if the small difference is the point, plot the difference
   directly with an interval.
2. **Dual-axis correlation chart** — two series scaled to overlap suggest a
   relationship that vanishes on independent axes. Fix: indexed lines on one
   axis, or a scatter of the two series, or two stacked panels.
3. **Rainbow heatmap** — hue ramp invents boundaries and uneven emphasis. Fix:
   single-hue sequential (or diverging around a meaningful midpoint), decade or
   quantile breaks labelled.
4. **3D pie chart** — perspective distorts the front slices. Fix: sorted
   horizontal bar, or a single 100% stacked bar.
5. **Hairball dependency network** — no structure visible. Fix: cluster and
   colour by module, filter to the subgraph the task needs, or switch to a
   dependency matrix / layered architecture view.
6. **Process diagram with ambiguous arrows** — same arrow means "next" and
   "sends data". Fix: declare the grammar; use distinct styles; split into a
   flowchart and a data-flow view if both are needed.
7. **Dashboard with no decision context** — KPI tiles, no trend or target. Fix:
   add sparkline + benchmark + target + "so what" line to each tile; lead with
   the one metric that drives a decision.
8. **Simulation chart showing a mean without variance** — Fix: overlay the
   distribution / interval / quantile band; state replications and MC error.
9. **Forecast indistinguishable from observed data** — Fix: solid vs dashed,
   shade the projected region, label the interval and its definition.
10. **Colour-only status chart** — red/green with no other cue. Fix: add
    icon/shape/text; choose a CVD-safe palette; ensure grayscale separation.
11. **Causal diagram confusing correlation, mediation, and sequence** — Fix:
    solid vs dashed edges, label mediators/confounders/colliders, add an
    assumptions block, don't render it as a timeline unless time is the claim.

Success = the flaw is named, its cost to the reader's task is explained, a
specific revision is given, and the rebuilt version is genuinely easier to read
correctly.
