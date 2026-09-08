# Reporting template

The final deliverable. State the result as a distribution or interval within a
named validity domain — never "the simulation proves X". For the result figures
(output histogram / ECDF, fan chart, tornado sensitivity plot,
exceedance-probability curve, warm-up diagnostic, observed-vs-predicted
validation scatter) and their labelling rules, see
[`visualization-design`](../../visualization-design/SKILL.md) §"Simulation and
DOE visualization" in
[`references/evidence-and-domains.md`](../../visualization-design/references/evidence-and-domains.md).

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
[…] assumptions, option B has a 0.82 probability of the lower 90th-percentile
cycle time; the ranking reverses if arrival variance exceeds […]."
