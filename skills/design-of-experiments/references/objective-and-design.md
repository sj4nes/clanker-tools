# Objective classes, evidence classes, and the design catalogue

## Objective classes

Distinguish before designing. The class fixes the estimand and the design family.

| Class | Typical question | Design family |
|---|---|---|
| Causal confirmation | Does intervention X cause a change in Y? | RCT, randomized block, cluster-randomized, crossover |
| Screening | Which of many inputs matter enough to study further? | Fractional factorial, Plackett–Burman, definitive screening, sequential elimination / racing |
| Optimization | What factor settings maximize / minimize a response? | Factorial → response-surface methods, Bayesian optimization |
| Robustness | Which settings hold up under noise / variation? | Robust parameter designs, crossed noise-factor experiments, simulation ensembles |
| Estimation | What is the magnitude of an effect? | Parallel-group RCT, blocked design, repeated measures, regression-discontinuity where justified |
| Equivalence / non-inferiority | Is a cheaper or safer alternative acceptably close? | Equivalence / NI design with a pre-specified margin |
| Mechanism | Through which pathway does the intervention act? | Factorial mediation-aware designs, process / sequential experiments |
| Dose-response | How does the response vary with dose / intensity? | Dose-finding, response surface, adaptive escalation, spline designs |
| Policy / rollout | Which operational or policy version performs best? | Cluster trial, stepped-wedge, staggered rollout, switchback |
| Prediction / model comparison | Which model or configuration predicts best? | Benchmark suites, nested cross-validation, controlled ablations |
| Simulation study | How does a simulated system respond to scenarios? | Scenario factorials, common-random-number designs, replication with sequential stopping |

## Evidence classes

Pick one explicitly and state its interpretation limits.

| Evidence class | Meaning |
|---|---|
| Randomized causal experiment | Assignment randomized at the relevant unit; design and analysis aligned |
| Randomized but compromised | Random assignment exists but noncompliance, attrition, interference, contamination, or implementation failure limits interpretation |
| Quasi-experiment | Assignment not randomized, but a credible identification strategy is stated and defended (difference-in-differences, RDD, instrumental variable, interrupted time series) |
| Observational comparison | Associations may inform, but causal claims rest on untestable assumptions that must be spelled out |
| Simulation experiment | Causal effects hold *within the model*; real-world validity depends on verification, validation, and applicability of the model |

Randomization is the most direct protection against confounding but is not always
possible, ethical, or practical. When it is unavailable, label the design
quasi-experimental or observational and drop unqualified causal language.

## Estimands

- **ATE** — average effect across the eligible population, `E[Y(1) − Y(0)]`.
- **ATT** — average effect among treated units.
- **CATE** — effect in a defined subgroup or context.
- **ITT** — effect of *assignment*, regardless of compliance. The default for
  pragmatic and policy questions.
- **Per-protocol** — effect among adherent units; needs stronger (often
  untestable) assumptions.
- **Average marginal effect** — expected effect of changing a factor while
  averaging over the others.
- **Interaction effect** — how the effect of one factor changes with another.
- **Quantile effect** — impact on the 50th / 90th / 99th percentile, not the mean.
- **Risk ratio / odds ratio / hazard ratio / rate ratio** — match to outcome
  type and to the assumptions each carries (odds ratios mislead when the outcome
  is common; report absolute effects alongside).
- **Non-inferiority / equivalence estimand** — whether the difference lies
  within a pre-specified margin.

## Outcome hierarchy

1. **Primary decision metric** — the one metric the decision rule reads.
2. **Guardrail metrics** — must not worsen beyond a stated threshold.
3. **Diagnostic metrics** — explain mechanism and implementation behavior.
4. **Exploratory metrics** — hypothesis-generating; not decision-authoritative
   unless promoted to primary in a later confirmatory study.

Each outcome needs: measurement method, scale and units, observation window,
aggregation rule, direction of improvement, data source, missing-data treatment,
measurement reliability, and its tier.

## Baseline randomized designs

| Design | Best when | Advantages | Primary cautions |
|---|---|---|---|
| Completely randomized | Units independent and broadly comparable | Simple, transparent, efficient | Chance imbalance with small n; ignores known heterogeneity |
| Randomized block | A known nuisance source (site, shift, batch, baseline risk) | Precision from comparing like with like | Blocks must be defined right; treatment must vary within block |
| Stratified randomization | Key baseline covariates must be balanced | Reduces chance imbalance at small / moderate n | Keep strata few; analyze consistent with stratification |
| Matched pairs | Natural pairs exist (before/after counterparts, matched devices) | High precision when within-pair similarity is strong | Pairing errors and missing pair members complicate analysis |
| Crossover | Each unit can take multiple treatments with washout | Controls stable unit-level differences | Carryover, period effects, irreversible effects, dropout |
| Cluster randomized | Treatment must be assigned to groups | Avoids contamination; fits schools, stores, regions, teams | Effective n depends on number of clusters and the ICC, not total observations |
| Split-plot | Some factors are hard to change frequently | Operationally feasible | Different randomization levels need different error terms |
| Stepped-wedge | All clusters will eventually get the intervention | Practical for phased rollout | Strong sensitivity to time trends and staggered-implementation assumptions |
| Switchback | Treatment alternates by time window in a shared system | Fits marketplaces, logistics, pricing, dispatch | Autocorrelation, carryover, daily cycles, interference |

## Special-purpose designs

| Situation | Design patterns to consider |
|---|---|
| Mixture components sum to a constant | Simplex-lattice, simplex-centroid, Scheffé mixture models |
| Many nuisance factors | Blocking, random effects, covariate adjustment, Latin square (if assumptions fit) |
| Rare failures / reliability outcomes | Accelerated life testing, reliability demonstration, sequential testing, importance sampling |
| Binary conversion / success | Binomial models, stratification, sequential monitoring, risk-based sample size |
| Counts / rates | Poisson / negative-binomial models, exposure offsets, cluster-aware designs |
| Repeated measurements | Mixed-effects, longitudinal, crossover, stepped-wedge, autocorrelation-aware models |
| Networks / marketplaces | Cluster, geo, switchback, saturation / interference-aware designs |
| Delayed outcomes | Interim-safe surrogate metric plus a pre-specified final analysis |
| Expensive simulations | Space-filling (Latin hypercube, Sobol), Gaussian-process surrogates, Bayesian optimization |
| Human safety / clinical efficacy | Randomized controlled design with protocol, monitoring, prespecification, regulatory review |
| High-stakes public policy | Pilot, phased rollout, cluster design, equity analysis, independent oversight, transparency |

## Threats to map before choosing

Confounders; mediators; moderators / effect modifiers; colliders (do **not**
adjust for these); the exposure-assignment mechanism; spillovers and interference
(SUTVA); time trends and seasonality; learning, novelty, carryover, fatigue,
attrition; concurrent experiments or policy changes; measurement changes;
selection and survivorship bias; the missingness mechanism; data leakage;
regression to the mean; Hawthorne / observer effects.
