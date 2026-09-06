# Searching for surprise

Unknowns usually announce themselves first as a weak signal, a residual the
model cannot explain, or a near-miss nobody logged. This is the detection layer.

## Horizon scanning

Horizon scanning is **early detection of possible change through weak,
distributed, incomplete, sometimes contradictory signals** — not a prediction
machine. Scan across:

scientific literature and preprints · patents, standards, regulatory
consultations · product releases and technical roadmaps · incident and safety
databases · job postings and skills shifts · procurement, supplier, trade data ·
public filings and earnings calls · customer support and field-service notes ·
operator logs and near-miss reports · security advisories and exploit trends ·
social and cultural behaviour · demographic, environmental, geopolitical change ·
adjacent industries and substitute technologies.

A weak signal is a **hypothesis trigger**, not evidence of a predicted outcome.
Treat it as: "if this is real and it continues, which of our assumptions
breaks?" — then set an indicator and a review date. Do not extrapolate a trend
line from one signal.

### Signal-card format

```yaml
signal:
  observation: ""
  source_and_date: ""
  source_reliability: "low | medium | high"
  novelty: ""
  possible_interpretations: []
  affected_systems_or_assumptions: []
  plausible_mechanisms: []
  evidence_against: []
  next_verification_step: ""
  monitoring_indicator: ""
  review_date: ""
```

The `evidence_against` and `next_verification_step` fields are mandatory — a
card without them is a rumour.

## Residual and anomaly analysis

Track `r_t = y_t − ŷ_t`, observed minus model-predicted. Persistent, clustered,
regime-specific, or growing residuals are evidence that something is missing: a
variable, an interaction, a structural break, a sensor fault, a selection bias,
or changed behaviour. An aggregate mean or a single global metric will often
hide this — always disaggregate.

Search for anomalies across: time · location · customer / user cohort · machine
/ asset · operator / team · supplier · software version · environmental regime ·
data source · intervention status · rare-event and tail behaviour.

Before suppressing an anomaly as "noise", answer:

- Is this a measurement artifact?
- Is it a known-but-unmodelled condition?
- Is it an early signal of regime change?
- Is it a safety or security incident?
- Is it an outlier revealing a missing subgroup?
- Has the metric's definition stopped being stable?

Only after these are checked and answered can an anomaly be set aside — and the
answer is recorded.

## Near-misses and negative evidence

The strongest learning often comes from: failures that almost happened; controls
that barely held; customer workarounds; manual interventions; unexpected
successes; experiments that did not replicate; confidently wrong forecasts;
outcomes revealed only by audit; incidents in adjacent systems; policies that
work on average but fail for a subgroup.

## Blameless surprise review

Run this on anything that already violated expectations:

1. What did we expect?
2. What happened?
3. What differed?
4. Which assumption made the difference surprising?
5. What evidence was available but ignored or inaccessible?
6. What should we now instrument, test, change, or monitor?
7. What action must change before the next occurrence?

The output feeds the assumption register (step 4), the learning backlog (step 6),
and the monitoring plan (step 6–7) — and is written to searchable memory so the
next team can find it (see
[`governance-and-failure-modes.md`](governance-and-failure-modes.md)).
