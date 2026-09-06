# Visual selection

Identify the **visual job** first — the relationship that matters in the message
— then take a chart or diagram type as a *starting hypothesis*, and keep it only
if it preserves the comparisons the audience's task needs. The FT Visual
Vocabulary and the EU data-visualisation guide both work this way: story-first,
not chart-first.

## The visual jobs

| Job | You are showing… |
|---|---|
| Comparison | which categories are larger / smaller |
| Change over time | how a value moves across an ordered time axis |
| Distribution | the shape, spread, centre, and tails of one variable |
| Relationship | how two (or more) variables co-vary |
| Composition | parts of a whole, possibly changing |
| Ranking | order by value, where the order is the point |
| Uncertainty | the range or probability around an estimate |
| Process / sequence | ordered steps, control flow, handoffs |
| Hierarchy | nested containment or classification |
| Network / dependency | who connects to / depends on whom |
| Spatial | variation across geography |
| Causal mechanism | claimed cause-and-effect structure |
| Architecture | structural components of a system |
| Sequence of messages | ordered interactions between actors over time |
| Decision tradeoff | competing objectives, frontiers, thresholds |
| Dynamic behaviour | a simulation state or system evolving over time |

A single artifact serves **one** primary job. If two jobs are essential, use two
linked views or small multiples, not one overloaded chart.

## Chart chooser

| Primary question | Preferred forms | Usually avoid |
|---|---|---|
| Which category is larger / smaller? | Sorted horizontal bar, dot plot, lollipop (only if labels stay legible) | Pie with many slices, 3D bars, alphabetical order when ranking is the message |
| How does a value change over time? | Line, interval/ribbon line, indexed line, seasonal small multiples | Bar chart with hundreds of periods, over-smoothed line hiding volatility |
| What is the distribution? | Histogram, dot/strip plot, box plot, violin **with raw points**, ECDF | Mean-only bar, undisclosed bin widths, density plot with hidden bandwidth |
| How do two variables relate? | Scatter, hexbin / density scatter, scatter with LOESS + uncertainty band, faceted scatter | Dual-axis line charts implying correspondence |
| Part-to-whole composition? | Stacked bar (few categories), 100% stacked bar for shares, treemap for hierarchy/exploration, waffle for a single proportion | Pie / donut with many or similar-sized slices, stacked areas where non-baseline segments must be compared |
| How do categories rank? | Sorted bar, dot plot, slopegraph / bump chart for rank change | Alphabetical bar when ranking is the message |
| What uncertainty surrounds an estimate? | Point + labelled interval, gradient interval, fan chart, quantile band, half-eye / distribution | Bare point estimate, opaque band with no definition |
| What changed between two conditions? | Slopegraph, paired dot plot, dumbbell / connected dot | Two separate bar charts that hide the pairing |
| Geographic variation? | Choropleth for **rates**, proportional symbols for **counts**, dot density, flow map, hex/tile cartogram | Choropleth of raw counts, a map used only because place names exist |
| Decision tradeoffs? | Scatter with Pareto frontier, frontier chart, decision matrix, parallel coordinates (sparingly) | Radar / spider charts for precise comparison |
| Nested components? | Tree, icicle, sunburst (exploration), treemap, nested boxes | Deep trees with no progressive disclosure |
| Flow of quantity between stages? | Sankey / alluvial | A generic flowchart when the amounts are the point |
| Many series, broad pattern? | Heatmap, horizon chart, small multiples | Spaghetti line chart with a 12-colour legend |

Precise value needed? Use a **labelled table** or add direct value labels. A
heatmap is for scanning patterns, not reading numbers.

## Diagram chooser

| Question | Diagram | Connector means |
|---|---|---|
| What are the steps / decision logic? | Flowchart | sequence / control flow |
| Who does each step, across teams? | Swimlane | flow + responsibility |
| What causes what? | Causal DAG | claimed causal influence |
| What is inside vs outside the system? | System context diagram | interface / external relationship |
| What are the components and how are they wired? | Architecture diagram | structural / data-flow relationship |
| What messages pass, in what order? | Sequence diagram | ordered message over time |
| What are the valid states and transitions? | State machine | allowed transition |
| What are the data entities and relations? | ERD | relationship / cardinality |
| What depends on / connects to what? | Dependency or network graph | dependency / association / topology |
| How are ideas related for teaching? | Concept map | associative / explanatory link |
| How much flows between stages? | Sankey / alluvial | quantitative flow |
| Software system at multiple zoom levels? | C4 views (context → container → component → code) | relationship at that abstraction |

Every diagram states its arrow grammar explicitly and uses one meaning per arrow
style. See [`diagrams.md`](diagrams.md).

## When it should be a table, not a chart

- The audience needs exact values more than a shape.
- There are very few numbers.
- Rows are looked up individually rather than compared as a set.
- Multiple incommensurable units sit side by side.

A well-set table (aligned decimals, right-aligned numbers, restrained rules,
a highlighted row or column) is a legitimate visualization.
