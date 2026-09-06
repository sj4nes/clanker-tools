# Execution: randomization, controls, replication, blinding, and data integrity

## Randomization

Random assignment makes treatment groups comparable in expectation and licenses
causal inference. Specify:

- assignment unit;
- allocation ratio;
- randomization method;
- blocking / stratification variables;
- sequence generation (how the random sequence is produced);
- allocation concealment (the sequence is hidden from whoever enrolls units);
- treatment-assignment logging (an immutable record of who got what, when);
- a reproducibility seed or an auditable randomization record;
- handling of re-randomization, exclusions, and failed assignments.

Methods:

- simple randomization;
- blocked randomization (balanced within blocks; vary block size to prevent
  prediction);
- stratified blocked randomization;
- cluster randomization;
- matched-pair randomization;
- rerandomization with a pre-specified balance criterion;
- response-adaptive randomization — only with strong justification and
  pre-specified inference control.

## Controls

The control condition should be the counterfactual that most directly answers
the decision question:

- no treatment;
- status quo / current policy or configuration (the usual choice for
  operational experiments);
- placebo / sham;
- standard of care;
- active comparator;
- matched alternative;
- historical baseline — only when a contemporaneous control is infeasible, and
  with the limitations stated explicitly.

Ask whether a placebo, sham, or "do nothing" comparison is ethical and
meaningful in this context.

## Replication

Replication estimates variability and stops one unusual run / batch / day /
cluster from being read as an effect. Distinguish:

- **Technical replication** — repeated measurements of the same unit or
  material. Improves *measurement* precision; does **not** add independent
  experimental units.
- **Biological / operational replication** — independent units drawn from the
  target population. This is what the sample-size calculation counts.
- **Computational replication** — independent stochastic simulation runs.
- **Temporal replication** — repetitions across relevant time periods.
- **Site replication** — repetitions across locations, machines, teams,
  environments.

## Blinding

Blinding removes measurement and behavior bias. Assess at each level:

- Can participants be blinded?
- Can operators be blinded?
- Can outcome adjudicators be blinded?
- Can analysts work with masked treatment labels until the pipeline is locked?
- If blinding is impossible, which objective, automated, or independently
  audited outcomes mitigate the bias?

## Data-quality and instrumentation audit

Many experiments fail before analysis because instrumentation is unreliable.
Audit:

- event-logging completeness;
- stable identifiers and assignment records;
- correct assignment-to-exposure linkage;
- timestamp timezones and clock synchronization;
- duplicates and bot / automation filtering;
- data-latency rules (when is a day's data "final"?);
- schema / version changes during the run;
- metric-definition drift;
- **sample-ratio mismatch** — observed allocation vs intended (a χ² test; a
  failure means the assignment or logging is broken, and the experiment is
  invalid until explained);
- missingness and delayed outcomes;
- experiment overlap and treatment contamination;
- guardrail-data capture;
- audit trail for manual interventions;
- differential measurement error by treatment arm.

## A/A test

Where feasible, run a pre-analysis **A/A test** (or equivalent instrumentation
check): both arms get the control experience. It does not establish causal
validity, but it reveals assignment bugs, sample-ratio mismatch, unstable
metrics, data loss, and inflated false-positive rates before the real
comparison.

## Monitoring during the run

- Assignment-balance and SRM checks on a schedule.
- Guardrail-metric monitoring against pre-set thresholds.
- Harm monitoring with a pre-specified stop rule.
- A rollback plan that can be executed quickly and that is tested before launch.
