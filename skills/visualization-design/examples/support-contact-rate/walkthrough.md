# Worked example — "make the tickets-per-quarter chart go up and to the right"

A messy monthly dataset and a loaded request, taken through every step of the
[`visualization-design`](../../SKILL.md) workflow. Every number here is
recomputed by [`check.py`](check.py) (`python3 check.py`, exit 0).

Files: [`data.csv`](data.csv) (raw) · [`brief.md`](brief.md) (step 1) ·
[`chart.vl.json`](chart.vl.json) (step 7) · [`check.py`](check.py) /
[`chart_data.json`](chart_data.json).

---

## 1. Visual brief

Full brief in [`brief.md`](brief.md). The key move: the request —
*"a bar chart of tickets per quarter for 2024, going up and to the right"* — is a
**desired shape, not a finding**. One blocking question to the support lead
("absolute volume, or workload relative to business size?") establishes the real
decision: *should the board approve 3 support hires?* — which turns on
**per-customer demand**, not raw ticket count.

- Audience: company board — high numeracy, low support-domain context; grayscale
  handout + projector; assume a colour-vision difference in the room.
- Evidence status: observed, **except** May (`tickets_received` missing — system
  migration) and December (partial month, 20 of 31 days).

## 2. Classify the visual problem

- **Visual job:** change over time — with a **confound to remove** (the customer
  base grew over the same window).
- **Product class:** decision visualization (it backs a specific board vote).

Not "composition" (quarters aren't parts of a whole worth comparing), not
"ranking". The quarterly *bar* framing is already a mismatch: 12 monthly points
carry the trend; 4 quarterly bars throw away resolution and, here, hide two data
-quality problems (see step 5).

## 3. Select the form (as a hypothesis)

Starting hypothesis from the chooser for "change over time": **line chart**,
monthly. Confirmed — it preserves the month-to-month trajectory the decision
needs and has room to mark the missing and partial periods inline. A bar chart
is rejected: it invites "sum per quarter", which is exactly the error in step 5.

The **encoded quantity is a rate**, not a count: `contact_rate = tickets_received
/ active_customers × 100` ("tickets received per 100 active customers"). This is
the graphical-integrity fix for the changing denominator (step 5).

## 4. Encodings, scales, layout

| Channel | Variable | Scale / transform |
|---|---|---|
| x | `period` | temporal, month (`%b`) |
| y | `contact_rate` | linear, **zero baseline**, domain 0–100 |
| (no colour / size / facet) | one series | single accent `#1f5fa8` |

- Hierarchy: the trend line is the one focal element; May/December annotations
  are grey and secondary.
- Direct labels on the first and last observed months (92.0 → 75.5); no legend.
- December is drawn as a **detached hollow marker**, never joined to the trend
  line. The pro-rated estimate is a separate open square.
- Title is the supported conclusion, not a label:
  *"Support contact rate fell 18% in 2024 as the customer base outgrew ticket
  volume"* — temporal/associational, **no causal claim**.

## 5. Graphical-integrity audit

| Check | Finding | Fix |
|---|---|---|
| Proportional encoding | naive truncated bars (y from 2000) show the Q2→Q3 gap as **7.1×** vs a true **1.68×** — **lie factor 4.2** | zero baseline; plot the rate, not the bar |
| Denominator change | customers grew **+86%** (1,000→1,860) while tickets grew **+53%** (920→1,405/mo) | encode `tickets ÷ customers`, not tickets |
| Rate vs count | raw count rises; the **contact rate falls 18%** (92.0→75.5) — the two tell **opposite stories** | the rate is the decision-relevant quantity |
| Missing data | May `tickets_received` absent; a naive quarterly sum makes **Q2 (2,250) < Q1 (2,945)** on 2 months of data | break the line at May; annotate; do **not** impute silently |
| Unequal time interval | December is 20/31 days; as-reported rate **48.2** looks like a collapse; naive **Q4 (3,705) < Q3 (3,775)** | detached marker + "partial month" note; pro-rated estimate **74.7**, on trend, shown as an open square |
| Causal language | request wanted a growth story to "justify headcount" | title stays associational; the brief records that no causal design exists |

Full numbers: `python3 check.py`.

## 6. Accessibility package

- **No meaning by colour alone:** one series, distinguished from annotations by
  weight and marker, not hue. Missing/partial status shown by line break, marker
  fill, and text — survives grayscale and print.
- **Contrast:** accent `#1f5fa8` on white ≈ 6.4 : 1 (clears 4.5 : 1); grey note
  text `#666` ≈ 5.7 : 1; grey reference marks `#6f6f6f` ≈ 5.0 : 1 (clears the
  3 : 1 for meaningful non-text marks). Axis/label text ≥ 11 px.
- **Colour-vision:** single blue accent — no red/green pairing anywhere.
- **Alt text (short):** *"Line chart of monthly support contact rate for 2024.
  It falls from 92.0 tickets per 100 customers in January to 75.5 in November, an
  18% decline. May is not plotted (data lost in a system migration); December is
  a partial month shown separately."*
- **Extended description:** the `description` field of
  [`chart.vl.json`](chart.vl.json).
- **Accessible data table:**

  | Month | Tickets received | Active customers | Contact rate (per 100) |
  |---|---:|---:|---:|
  | Jan | 920 | 1,000 | 92.0 |
  | Feb | 990 | 1,080 | 91.7 |
  | Mar | 1,035 | 1,160 | 89.2 |
  | Apr | 1,080 | 1,250 | 86.4 |
  | May | *not recorded* | 1,330 | — |
  | Jun | 1,170 | 1,410 | 83.0 |
  | Jul | 1,210 | 1,500 | 80.7 |
  | Aug | 1,260 | 1,590 | 79.2 |
  | Sep | 1,305 | 1,680 | 77.7 |
  | Oct | 1,360 | 1,770 | 76.8 |
  | Nov | 1,405 | 1,860 | 75.5 |
  | Dec | 940 *(20/31 days)* | 1,950 | 48.2 as-reported · 74.7 pro-rated |

- **Method note:** contact rate = tickets received ÷ active customers × 100.
  December pro-rated as `received × 31 / 20`. May excluded from the trend line.

## 7. Semantic source

[`chart.vl.json`](chart.vl.json) — Vega-Lite v5, data embedded, y-scale pinned to
zero, `description` carrying the alt text, one accent colour, layered so the
missing/partial periods are explicit marks rather than silent gaps. Provenance
(ticketing export + billing, 2024, cutoff 2024-12-20) is stated in the subtitle
and method note.

## 8. Critique against the rubric

| Dimension | Score | Note |
|---|---|---|
| Purpose | 3 | answers "is per-customer demand rising?" directly |
| Semantic correctness | 3 | line for a trend; rate for the confound |
| Data integrity | 3 | zero baseline, denominator corrected, missing/partial marked |
| Perceptual effectiveness | 3 | position on a common aligned scale |
| Hierarchy | 3 | one focal line, secondary grey annotations |
| Cognitive load | 2 | December needs two sentences of annotation — unavoidable given the data |
| Accessibility | 3 | grayscale/CVD safe, alt text, data table |
| Annotation | 3 | conclusion title, direct labels, method note |
| Context | 3 | subtitle gives the raw-count and customer-count deltas |
| Decision utility | 3 | reframes the headcount case honestly |
| Aesthetic coherence | 3 | one colour, calm |
| Maintainability | 3 | Vega-Lite spec + `check.py` regenerate it from `data.csv` |

**Red flags checked and cleared:** no truncated baseline, no 3D, no dual axis,
no rainbow, no red/green, no forecast-drawn-as-observed (the pro-rated point is a
distinct open square), no isolated KPI, no causal title.

**Residual limitations:** single year, no prior-year baseline for seasonality;
active-customer counts assumed accurate; the pro-rated December assumes a flat
within-month arrival rate.

## 9. Alternative design offered

For the board *discussion* (not the headline slide): a **two-panel small
multiple** — raw tickets received (left) and contact rate (right), shared x-axis
— makes the "volume up, intensity down" tension explicit in one view. Rejected as
the headline because it splits attention across two magnitudes; kept as a backup
for the Q&A.

## What the example demonstrates (workflow step → artifact)

| Step | Where |
|---|---|
| 1 brief | [`brief.md`](brief.md) |
| 2 classify job | §2 — "change over time + confound" |
| 3 select form | §3 — line over bar, rate over count |
| 4 encodings | §4 + [`chart.vl.json`](chart.vl.json) |
| 5 integrity audit | §5, all numbers in [`check.py`](check.py) |
| 6 accessibility | §6 — alt text, contrast, data table |
| 7 semantic source | [`chart.vl.json`](chart.vl.json) |
| 8 critique + revise | §8 rubric + red-flag sweep |
| 9 alternative | §9 |
