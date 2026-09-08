# Model charter

The first deliverable — written before any code. Every "out of scope" line and
every fixed parameter is a scientific claim about what does not matter for this
decision.

```
DECISION
  question          : <the choice / forecast / explanation at stake>
  owner             : <who acts on the result>
  action            : <what they may do differently>
  outputs           : <metric, units, aggregation level, reporting cadence>
  horizon / scope   : <time span, spatial extent, operating regimes>
  acceptable uncert.: <e.g. ±3 pp on a probability; rank-order only>
  counterfactuals   : <the alternatives being compared>
  asymmetry         : <cost of false confidence vs cost of conservatism>

BOUNDARY
  in scope          : <entities, processes, interfaces modeled>
  out of scope      : <deliberately excluded — each is a scientific claim>

MODEL
  entities / states : <what exists; what can change; minimal state>
  inputs            : controllable = <...>   exogenous = <...>
  parameters        : <name, value, source, fixed-from-theory | estimated>
  initial conditions: <state at t0>
  boundary conditions: <spatial / interface constraints>
  random variables  : <name, fitted distribution, rationale>
  dependencies      : <correlations / copulas that matter>
  causal structure  : <diagram | stock-and-flow | process map | equations>
  invariants        : <conservation / positivity / bounds checked every run>
  time / space scale: <seconds vs years; meters vs regions>

DATA PROVENANCE
  source            : <system of record, sensor, survey, vendor>
  collection method : <how sampled; period covered>
  coverage / gaps   : <what is missing; known bias>
  cleaning          : <steps applied; assumptions made>
  rights            : <licence / privacy / retention constraints>

VALIDITY DOMAIN
  applies for       : <regimes where conclusions hold>
  does NOT apply for : <extrapolation the result must not be used for>
  failure modes     : <high-consequence ways the model could mislead>
```
