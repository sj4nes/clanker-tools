# Diagram intelligence

## Match the diagram type to the connector meaning

| Diagram | Connector means | Best use |
|---|---|---|
| Flowchart | sequence / control flow | procedure, decision logic, exception paths |
| Swimlane | flow + responsibility | cross-functional process, handoffs |
| Causal DAG | claimed causal influence | confounding analysis, intervention reasoning, stated assumptions |
| System context diagram | interface / external relationship | what is inside vs outside the system boundary |
| Architecture diagram | structural / component relationship | software, hardware, infrastructure, services |
| Sequence diagram | ordered message over time | API, protocol, user/service interaction |
| State machine | allowed state transition | device, software, workflow lifecycle |
| ERD | data entities and relationships | schemas, databases |
| Network / dependency graph | relationship / topology | dependencies, social ties, infrastructure |
| Concept map | associative / explanatory link | teaching, knowledge structure, ideation |
| Sankey / alluvial | quantitative flow | money, material, users, traffic between stages |
| C4 views | relationship at a fixed abstraction level | software at context / container / component / code |

## Explicit arrow grammar — mandatory

Every diagram declares, in a legend or a note, what its arrows mean. Pick one:

- "happens next" / "then"
- "sends data to" (label the payload or protocol)
- "causes" / "influences" (causal DAG only)
- "contains" / "is composed of"
- "depends on" / "is called by"
- "transforms into"
- "is measured by"

Do not mix meanings in one diagram without distinct arrow styles and a key.
A dashed arrow, a solid arrow, and an open-headed arrow must each have a stated
meaning.

## Layout heuristics

- One dominant flow direction: left-to-right or top-to-bottom. Don't make the
  reader's eye backtrack.
- Minimize edge crossings; route long edges around clusters, not through them.
- Align nodes on a grid; equalize spacing within a rank.
- Group related nodes by enclosure or proximity; label the group.
- Progressive disclosure for anything large: a context view first, then drill
  into one subsystem per view. Don't ship a 60-node hairball.
- Keep node labels short; put detail in a side note or a linked view.
- Consistent shape vocabulary: one shape per node kind, defined in the legend.

## Causal-DAG conventions

- Solid arrow: well-supported causal pathway.
- Dashed arrow: hypothesized or uncertain pathway.
- Distinguish observed variables from latent / unobserved (e.g. circle vs
  dashed circle).
- Label treatments, outcomes, confounders, mediators, colliders.
- Mark intervention points distinctly.
- Do **not** draw a causal DAG as a left-to-right temporal flowchart unless
  temporal order is part of the causal claim.
- Attach an assumptions block and an evidence-status line.

## Layered architecture views

Offer the layer the audience needs, not all at once:

1. **Context** — users, external systems, trust boundaries.
2. **Containers / services** — deployable units and major data flows.
3. **Components** — internal modules and responsibilities.
4. **Runtime / deployment** — nodes, zones, networks, scaling, resilience.
5. **Sequence** — critical request flows and failure paths.
6. **Data lineage** — sources, transformations, storage, consumers.

Every architecture diagram carries: a stated viewpoint and audience; a named
system boundary; a legend / controlled icon vocabulary; arrows labelled with
interaction, protocol, or data type; trust / security boundaries where relevant;
deliberate omission of low-level detail; and a version / date plus the
source-of-truth reference.

## Diagram-as-code and chart-as-code

Prefer a declarative or code specification when accuracy, review,
maintainability, and version control matter. Emit **both** a rendered artifact
and the source.

| Need | Tool |
|---|---|
| Markdown-adjacent flow / architecture, renders on many platforms | Mermaid |
| Dependency / network layout, fine layout control | Graphviz / DOT |
| UML, sequence, component diagrams | PlantUML |
| Declarative architecture / process with good auto-layout | D2 |
| Formal business-process semantics | BPMN tooling |
| Precise, inspectable, accessible vector output | hand-authored SVG (with `<title>`/`<desc>`) |
| Declarative quantitative charts | Vega-Lite / Altair |
| Concise JS charts | Observable Plot, D3 |
| Notebook / scripted charts | matplotlib, plotly, ggplot2, Plotnine |

Include in the source: the data (or a path to it), labels, colour definitions,
layout rules, and provenance (source, date, definitions, and who owns the truth).
This is what lets the artifact be audited, translated, made accessible, and
regenerated when the data change.
