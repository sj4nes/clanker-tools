# Simulation workflow — templates and a worked example

## Fidelity ladder

Climb only when the current rung cannot answer the decision question or cannot
bound its uncertainty tightly enough to justify the cost of the next rung.

1. Back-of-the-envelope analytic model (closed form, spreadsheet, `bc`).
2. Simple deterministic simulation.
3. Stochastic extension (add the uncertain inputs and their distributions).
4. Calibrated domain model (parameters estimated from data, identifiability checked).
5. High-fidelity / multi-physics model.
6. Hardware-in-the-loop or a physical experiment — only if the stakes justify it.

At each rung ask: does the added detail change the decision, or shrink the
decision-relevant uncertainty enough to be worth its cost and maintenance burden?

## Model charter template

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

## Formal specification checklist (before writing code)

- Every variable: name, meaning, unit, type, valid range, update rule.
- Equations / event logic / transition tables / pseudo-code, unambiguous.
- Random variables: fitted distribution + why that family; parameters + fit method.
- Dependencies and correlations between uncertain inputs.
- Initial and boundary conditions.
- Parameter values, priors, sources, calibration method.
- Numerical method, tolerances, solver constraints, event handling, sample rate.
- Conservation / invariant checks and where they run.
- Scenario definitions (baseline + each alternative, differing only in named factors).

## Reproducible implementation manifest

Record for every run:

- Model source version (commit) and the exact config file used.
- Dependency environment (lockfile / container digest).
- Random seeds and RNG-stream assignment (per entity stream, per alternative).
- Raw input snapshot hash (content-addressed) — inputs immutable.
- Wall-clock start/end, host, solver settings actually used.
- Output file hashes.

For stochastic comparisons a single seed is necessary but not sufficient: use
independent streams, or **common random numbers** paired across alternatives, and
state which. Paired CRN sharpens the comparison of alternatives; it does not make
a single realization representative.

## Experiment-design template

```
BASELINE      : <scenario, and why it is the reference>
ALTERNATIVES  : <each differs from baseline only in: factor = value>
FACTORS       : <full-factorial | fractional | one-at-a-time | Latin hypercube>
RANDOMIZATION : <independent streams | common random numbers>  seed log: <path>
REPLICATIONS  : n = <...>   convergence criterion : <half-width < X on metric M>
WARM-UP       : <duration discarded; how chosen>
TERMINATION   : <horizon | completion count | steady-state test>
METRICS       : <primary + secondary, each with units and decision threshold>
COMPARISON    : <paired t / Welch / bootstrap CI / ranking + probability best>
STOPPING RULE : <fixed n | sequential with error control>
RETENTION     : <what is kept for audit; for how long>
```

## Reporting template

```
DECISION QUESTION   : <restated>
MAIN RESULT         : <plain language, one or two sentences>
RESULT WITH UNITS   : <distribution or interval, not a bare point>
MODEL SCOPE         : <boundary; validity domain>
SCENARIO + ASSUMPTIONS : <baseline and alternatives; key assumptions>
VERIFICATION        : <checks run; which passed; which failed and impact>
VALIDATION          : <evidence; data compared against; gaps>
UNCERTAINTY         : <aleatory / epistemic / numerical / scenario / model-form;
                       intervals; what dominates>
SENSITIVITY DRIVERS : <ranked; the 1–3 inputs that move the metric most>
REVERSAL CONDITIONS : <what assumption change flips the recommendation>
REPRODUCIBILITY     : <commit, config, seeds, environment>
NON-CLAIMS          : <what this analysis does NOT establish>
NEXT MEASUREMENT    : <the data collection / test that most reduces decision risk>
```

Avoid: "The simulation proves option B is best."

Prefer: "Within the observed demand range and the modeled labor, outage, and
service-time distributions, option B reduced the estimated deadline-miss
probability from 14–19% to 5–9%. This conclusion is most sensitive to the
assumed packing-time distribution and the absenteeism rate; it should not be
extrapolated to peak-season demand beyond the tested range."

## Worked example — pack-station capacity (discrete-event)

**Frame.** Decision: add a second pack station? Owner: fulfillment ops lead.
Action: approve capex + hire. Output: P(daily outbound orders miss the 17:00
carrier cutoff), by month. Acceptable uncertainty: ±3 percentage points, 95% CI.
Counterfactuals: 1 station (baseline) vs 2 stations, labor schedule unchanged.
Asymmetry: a missed cutoff costs a full day of delivery SLA; an idle station
costs one shift of labor.

**Charter (extract).** Boundary: order release → pick → pack → carrier handoff;
excludes inbound receiving and returns (separate flow, no shared resource in the
cutoff window). Entities: orders. Resources: pickers (schedule fixed), pack
stations (1 or 2). Random variables: order arrivals — non-homogeneous Poisson
with hourly rate profile fitted from 12 months; pick time — lognormal per SKU
class; pack time — lognormal, station-independent; station breakdown — exponential
time-to-failure, lognormal repair; picker absenteeism — daily Bernoulli per
picker. Dependence: arrival-rate profile and absenteeism both correlate with day
of week — model day-of-week as a shared factor, do not sample independently.
Invariant: orders out ≤ orders in; queue ≥ 0.

**Paradigm.** Discrete-event: the decision is driven by queueing under variable
arrivals, finite servers, breakdowns, and shift patterns — averages alone would
understate the tail (the most common modeling mistake here).

**Formalize.** Event set: arrival, pick-start, pick-complete, pack-start,
pack-complete, station-fail, station-repair, shift-change, cutoff. Metric:
indicator that the pack queue is non-empty at 17:00; aggregate to a monthly
probability over replications.

**Implement.** One run = one simulated day. Independent arrival / service /
breakdown / absenteeism streams; **common random numbers** across the 1- vs
2-station comparison (same arrival and pick realizations, only station count
differs) so the paired difference has low variance. Seeds logged per stream.

**Verify.** Zero arrivals → queue stays 0 (pass). Infinite pack capacity →
deadline-miss probability → 0 (pass). Single deterministic order, no variability
→ hand-computed completion time matches to the second (pass). Halving the
event-time resolution does not change the monthly probability by more than
Monte-Carlo noise (pass). Event trace for day 1 inspected by the ops lead
(face-valid).

**Validate.** Replay the last 12 months' actual arrival files through the
1-station model; compare simulated vs recorded daily cutoff misses — 41 simulated
vs 38 recorded over 250 working days, within the model's CI. Hold out the most
recent month from distribution fitting; predicted miss rate 12% vs actual 11%.
Gap: no data on carrier-side variability in the handoff window — treated as a
scenario, not calibrated.

**Uncertainty & sensitivity.** 2,000 replications per month per alternative;
monthly probability half-width < 2 pp. Global sensitivity (Latin hypercube over
the parameter posteriors): pack-time distribution scale and absenteeism rate
together explain ~70% of output variance; breakdown parameters ~10%.

**Report.** "Over the 12 modeled months, a second pack station reduces the
estimated probability of missing the 17:00 cutoff from 9–14% to 1–3% in peak
months (Nov–Dec) and from 2–4% to <1% otherwise, holding the current picker
schedule. The result is most sensitive to pack-time variability and absenteeism;
if mean pack time improves by 15% (a process change under evaluation), the
1-station peak-month miss probability falls to 4–7% and the case for a second
station weakens. Not established: behavior under demand above the highest modeled
peak day, or under a changed picker schedule. Next measurement: instrument
actual pack-station cycle times for one peak week to tighten the dominant input."
