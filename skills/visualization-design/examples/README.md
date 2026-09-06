# `visualization-design` — worked examples

End-to-end runs of the [`SKILL.md`](../SKILL.md) workflow on real-shaped inputs.

| Example | Scenario | Demonstrates |
|---|---|---|
| [`support-contact-rate/`](support-contact-rate/) | A support lead asks for "a bar chart of tickets per quarter, going up and to the right" for a board headcount request. Messy monthly CSV: inconsistent date strings, one missing month, one partial month, a customer base that grew faster than ticket volume. | Reframing a *desired shape* into a *question*; job classification (change-over-time + confound); rate vs count; marking missing/partial data; truncated-baseline lie factor (4.2); the full accessibility package; a Vega-Lite source; a rubric critique + an alternative. |

Each example directory has: `data.csv` (raw), `brief.md` (step 1),
`walkthrough.md` (steps 2–9), `chart.vl.json` (the semantic source), and
`check.py` — a stdlib script that recomputes every quantitative claim in the
walkthrough and writes the tidy `chart_data.json`. Run `python3 check.py`
(exit 0 = all claims hold). The example checks also run as part of
[`../verification/run.sh`](../verification/run.sh).
