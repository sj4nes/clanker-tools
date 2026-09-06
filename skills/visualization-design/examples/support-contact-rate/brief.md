# Visual brief — support contact rate

> Filled instance of [`templates/visual-brief.md`](../../templates/visual-brief.md).

## Objective

- **Question to answer:** Is the support team's workload growing faster than the
  business, i.e. is per-customer demand rising?
- **Decision or learning goal:** The support lead wants to take a headcount
  request to the Q1 board meeting. The board will decide whether to approve 3
  new hires.
- **Intended takeaway (if known and supported by the data):** *Unknown at
  briefing time* — the lead asked for "a bar chart of tickets per quarter,
  going up and to the right". That is a desired shape, not a finding. The
  takeaway must come from the data.
- **Primary visual job:** change over time — with a **confound to remove**
  (the customer base grew over the same period).
- **Product class:** decision visualization.

## Audience

- **Primary audience:** company board (finance-literate, not support-domain
  experts), plus the support lead.
- **Expertise level:** high numeracy, low context on support operations.
- **Accessibility needs:** deck is printed in grayscale handouts and projected;
  assume at least one reader with a colour-vision difference.
- **Viewing context:** one slide, ~20 seconds of attention, then discussion.

## Content

- **Data sources:** `data.csv` — monthly export from the ticketing system, joined
  to the monthly active-customer count from billing.
- **Data dictionary:**
  - `period` — calendar month (raw strings are inconsistent: `2024-01`,
    `Feb 2024`, `2024/03`).
  - `tickets_received` — inbound support tickets created that month (count).
  - `tickets_resolved` — tickets closed that month (count).
  - `active_customers` — paying customer accounts at month end (count).
  - `note` — data-quality annotations.
- **Evidence status:** observed, except December (partial month) and May
  (`tickets_received` missing).
- **Required terms and labels:** "tickets received", "active customers",
  "contact rate = tickets received per 100 active customers".

## Constraints

- **Medium:** slide (16:9) + grayscale print handout.
- **Static or interactive:** static.
- **Brand / style constraints:** one accent colour; sentence-case titles.
- **Deadline:** board pack due in 3 days.

## Integrity

- **Units and denominators:** raw counts confound business growth. The
  decision-relevant quantity is a **rate** with `active_customers` as the
  denominator.
- **Uncertainty definition:** no sampling uncertainty (full population of
  tickets); the real uncertainty is the **incomplete December** and the
  **missing May** value.
- **Transformations and filters:** rate = `tickets_received / active_customers *
  100`. December is shown but marked incomplete. May's rate is not computed.
- **Privacy / sensitivity constraints:** none — aggregate counts only.

## Accessibility requirements

- Colour-vision robustness required: **yes**
- Screen-reader support required: **yes** (board pack PDF)
- Keyboard navigation required: no (static)
- Grayscale / print fidelity required: **yes**

## Assumptions made

- The board's real question is efficiency (demand per customer), not absolute
  volume — confirmed with the lead before designing.
- Active-customer counts are month-end and reasonably accurate.

## Blocking questions (asked the lead)

- "Do you want to show absolute ticket volume, or workload relative to the
  business size?" → **relative** (that is the argument for or against more
  hires).
