# Graphical integrity

A visualization has integrity when the visual magnitude the reader perceives is
proportional to the quantity in the data, and when every choice that shapes the
picture (scale, denominator, transformation, filter, aggregation, time frame) is
disclosed. Run this audit on every quantitative artifact — yours or one under
review.

## Integrity audit checklist

- Does the visual encoding correspond **proportionally** to the data?
- Are all axes labelled with units and any transformation (log, per-capita,
  indexed, inflation-adjusted, standardized)?
- Does a bar / column / area chart start at **zero**? If not, is the truncation
  made prominent and justified? (A zero baseline is essential for bars; for line
  charts a non-zero baseline is often fine but must be stated.)
- Are bin widths, smoothing / bandwidth parameters, aggregation rules, and
  filters disclosed?
- Are denominator changes over time visible? Are **rates distinguished from
  counts**?
- Are time intervals equally spaced and accurately positioned? No gaps collapsed,
  no unequal periods drawn equal.
- Are missing data, revised data, estimates, forecasts, and suppressed values
  visibly marked (gap, dashed segment, hatching, annotation)?
- Are outliers omitted, capped, winsorized, or transformed? If so, is it
  disclosed?
- Are uncertainty intervals shown wherever uncertainty would change the reading?
- Does colour imply polarity / danger / good-bad appropriately and consistently?
- Does the visual language imply **causation** where only association exists
  (arrows, ordering, emphasis, a causal title)?
- Do sorting, cropping, zoom, or selective annotation manufacture a story the
  full data would not support?
- Does a map use geographic **area** to exaggerate sparsely populated regions?
- Does a stacked chart force comparison of non-baseline segments?
- Is a **dual axis** creating a coincidental-looking correlation? (Default: don't.
  If unavoidable, annotate both scales and their zero points, and say why.)

## Proportional-distortion test

For any encoding of value by length, area, or position, check that a data change
from `a` to `b` produces a proportional change in the displayed magnitude:

```
visual effect ratio = (displayed magnitude change) / (data value change)
```

For an honest linear encoding this ratio is constant across the chart. Flag
severe mismatch, especially from:

- 3D or perspective effects (near objects read larger);
- **area** encoding when the value is meant to be read as a **length** (doubling
  a value but scaling both width and height quadruples the ink — "Lie Factor");
- truncated bar baselines (a 3% difference on a 90–100 axis looks like 10×);
- non-linear axes presented without disclosure;
- inconsistent scales across panels that invite cross-panel comparison;
- map area standing in for a population-dependent count.

Compute the ratio two ways where feasible (from the axis geometry and from the
rendered pixel extent) and report both. The `bc` verification check does this for
a truncated bar and an area-for-length icon.

## Scale-choice rules

| Situation | Rule |
|---|---|
| Bar / column / area magnitude | Zero baseline, always. No exceptions without a prominent break marker and a stated reason. |
| Line chart of a level | Non-zero baseline allowed; state it; keep it stable across related charts. |
| Wide dynamic range, multiplicative change | Log axis is legitimate — label it clearly, use decade gridlines, note that equal vertical distances are equal *ratios*. |
| Rates of change / growth comparison | Index to a common base period (=100) and label the base. |
| Deviations around a reference | Diverging encoding centred on the reference; label the midpoint. |
| Comparable small multiples | One shared scale whenever cross-panel magnitude comparison matters; free scales only for shape-only comparison, and say so. |

## Evidence status and uncertainty

Every visualization built on modelled, estimated, forecast, simulated, or
incomplete data must make evidence status visible — with a visual treatment, not
only a caption.

Distinguish, with distinct visual treatments:

- observed vs forecast / projected;
- historical vs projected periods (e.g. solid vs dashed, shaded future region);
- measured vs modelled values;
- central estimate vs interval;
- probability interval vs scenario envelope;
- preliminary vs final / revised data;
- causal estimate vs descriptive association;
- real-world measurement vs simulation output;
- present vs missing / imputed / censored / suppressed values.

**Reject an unlabelled uncertainty band.** State exactly what it is:

> Solid line: observed monthly rate. Dashed line: model projection. Shaded
> region: 80% prediction interval under the baseline scenario.

The reader cannot otherwise tell a 95% confidence interval from a credible
interval, ±1 SD, a prediction interval, a min–max range, or a scenario range —
and each licenses a different conclusion.

## Causal-language check

Before shipping, read the title, subtitle, annotations, and arrow semantics and
ask: does any element assert that X *caused* Y? If so, is there a randomized or
otherwise identified causal design behind it? If not, rewrite to temporal or
associational language ("coincided with", "followed", "is associated with") or
add the explicit assumption note. Arrows in a process diagram mean "next"; only a
causal DAG's arrows mean "causes", and it carries an assumptions block.
