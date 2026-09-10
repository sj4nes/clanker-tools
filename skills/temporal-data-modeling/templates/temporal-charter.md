# Temporal charter — <model name>

## 1. Time base

```yaml
observation_kind: instants | intervals        # is each datum a point or a span?
time_shape: line | tree                        # tree = version history / scenario branches
finest_granularity: <e.g. 1 second | 1 day | 1 accounting period>
clock: event-time | processing-time | both     # when it happened vs when we recorded it
time_zone: <IANA zone or "UTC only" or "naive local">
calendar: <Gregorian | fiscal (define) | trading-day | ...>
horizon: {start: <ISO>, end: <ISO or "open">}
late_data: <how late an observation can arrive and still be accepted>
```

Blocking questions (ask only these; assume the rest and list assumptions):

- <question>

Assumptions made for missing inputs:

- <assumption> — revisit if <trigger>

## 2. Entities that vary over time

| entity type | key | what changes about it | expected lifespan |
|---|---|---|---|
| member | member_id | active status, plan, team | months–years |

## 3. Questions the model must answer

Mark each **P** (needs a persistent / as-of answer) or **C** (needs a
cumulative / to-date answer).

| # | question | P/C | resolution needed |
|---|---|---|---|
| Q1 | how many members were active *on* 2026-06-30? | P | day |
| Q2 | how many distinct members were active *during* June? | C | month |

## 4. Decisions these answers feed

| decision | driven by | reversibility if the model is wrong |
|---|---|---|
| quarterly headcount report | Q2 | partially-reversible (restatement) |

## 5. Reversibility of a wrong model

```yaml
overall_reversibility: reversible | partially-reversible | irreversible
worst_case_if_wrong: <one sentence>
what_would_make_us_rebuild: <trigger>
```
