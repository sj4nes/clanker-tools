# Evidence-aware and domain visualization

## The "means without variance" anti-pattern

For any stochastic or distributional quantity where spread could change the
decision, showing only the mean is a defect. Show the distribution, an interval,
quantiles, an exceedance probability, or a scenario range. A bar chart of group
means with no error representation is the canonical bad case — replace with a dot
plot + interval, a box/violin with raw points, or a gradient interval.

## Simulation and DOE visualization

Pairs with the `simulation` and `design-of-experiments` skills.

| Task | Forms |
|---|---|
| Factor screening | Pareto chart of standardized effects, main-effect plots, interaction plots, normal / half-normal effect plots |
| Factorial designs | interaction plots, cube plots, contour plots |
| Response-surface optimization | contour maps, response surfaces, desirability plots, Pareto fronts, uncertainty-aware optimum region |
| Monte Carlo | histogram / ECDF of the output, fan chart over time, tornado sensitivity plot, exceedance-probability curve |
| Discrete-event simulation | queue-length and time-in-system distributions, utilization intervals, warm-up diagnostic (running mean), replication CIs |
| System dynamics | stock-and-flow diagram, causal-loop diagram, behaviour-over-time graph with scenario bands |
| Agent-based models | spatial snapshots, state-transition summary, ensemble trajectory spaghetti + median band, parameter-sweep small multiples |
| Model validation | observed-vs-predicted scatter with the 45° line, residual plots, calibration curve, error distribution, out-of-sample overlay |
| DOE results | effect sizes with intervals, interaction matrix, predicted-vs-observed, residual diagnostics, run-order plot (to catch drift) |

Always label: which factors are held fixed, the scenario or parameter set, the
number of replications, the Monte Carlo error, and whether a band is a prediction
interval or a scenario envelope. Distinguish observed data from simulation output
visually, not just in the caption.

## Causal and policy visualization

- Solid arrows for well-supported causal pathways; dashed for hypothesized.
- Separate observed from latent / unobserved variables.
- Label confounders, mediators, colliders, treatments, outcomes; mark
  intervention points.
- A causal DAG is not a temporal flowchart unless time order is part of the
  claim.
- Attach an assumptions note and the evidence-status label.
- For a policy decision brief: show the effect with its interval against the
  practical threshold, the guardrail movements, and the conditions that reverse
  the recommendation — not a single number.

## Architecture and systems visualization

Support layered abstraction — context, containers/services, components,
runtime/deployment, sequence, data lineage (see
[`diagrams.md`](diagrams.md)). For every architecture diagram require: a stated
viewpoint and audience; a named system boundary; a legend / controlled icon
vocabulary; arrows labelled with interaction, protocol, or data type; trust /
security boundaries where relevant; deliberate omission of low-level detail;
and a version / date plus the source-of-truth reference.

## Static vs interactive vs animated

**Static** when the message is stable and specific, the medium is a report /
deck / PDF / print, reproducibility and citation matter, and interaction would
not change the conclusion. A static chart must answer the key question with no
clicking, hovering, or filtering.

**Interactive** when users must explore many categories or variables, inspect
exact values, compare scenarios, filter to their own context, drill from summary
to evidence, manipulate parameters, or interrogate uncertainty. Provide a strong
initial view, sensible defaults, discoverable controls, a reset, and an
accessible alternative. A dashboard should not require every viewer to become an
analyst before the headline is legible; each tile needs a trend, benchmark,
target, or decision implication — not an isolated KPI.

**Animated** only when change, sequence, causality, or state transition *is* the
subject. Animation is weak for comparing values (the viewer cannot see multiple
states at once). Prefer a static before/after, small multiples, a controllable
scrubber, or an annotated timeline when accurate comparison is needed. Respect
reduced-motion; never flash or strobe.
