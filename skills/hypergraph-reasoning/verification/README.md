# Verifying `hypergraph-reasoning`

## What verification means for this skill

Methodology-only — there is no bespoke CLI. Verification re-solves cases with a
known answer using the operators `SKILL.md` prescribes, and for each one shows
the **negative contrast**: the naive method the guardrail exists to prevent,
failing visibly on the same case.

## Cases and why they were chosen

Each is small enough to check by hand and isolates one operator:

- **Retrieval score** — a linear blend with closed-form values; the
  structural-fit term is the only thing that changes the ranking.
- **Precondition conjunction** — a 5-term boolean AND; a truth table.
- **Context collapse** — one n-ary edge vs its 4-edge binary decomposition; the
  out-of-scope query has an unambiguous right answer (no).
- **Temporal scope** — an approval interval and a superseding policy interval
  with a query date outside the first; `valid_time` arithmetic only.
- **Contradiction with role typing** — three owner claims; exactly one pair
  shares the `operational` ownership role.
- **Epistemic / provenance gating** — three claims, one `proposed`, one with no
  source span; the partition is determined.

## Run

```
sh verification/run.sh
```

`bc` 7.0.3 (`-l`), Python 3.14 stdlib only. Wall time < 1 s. Exits non-zero on
any failed check.

## What each step demonstrates

| SKILL element | Prescribed check | Result |
|---|---|---|
| Retrieval ranking with structural fit (`references/retrieval-and-reasoning.md`) | Role-complete `Decision` edge must outrank a lexically-closer role-poor `Event` edge | `score` 0.7375 vs 0.6550 → role-complete wins; text-only similarity (0.90 vs 0.55) would pick the wrong edge |
| Precondition conjunction (principle "an action is allowed only when its preconditions jointly hold") | `Allowed = ∧ ci` over the context; naive single-conjunct check must not admit | window-closed case: `Allowed = 0`, naive `= 1`; all-true case: `Allowed = 1` |
| "Preserve joint context — never shatter a qualified fact" | n-ary edge denies `use(Alice, gpu, project-y)`; binary shatter grants it | n-ary → `False`, shattered → `True`; in-scope query still `True` on the n-ary edge |
| "Attach time to everything" / temporal-scope resolution | `valid_time` denies an expired + superseded approval; time-blind check grants it | time-aware → `False`, time-blind → `True` |
| Contradiction detection with role typing | Role-typed check flags only the same-role clash; role-blind check also raises a false operational-vs-budget alarm | role-typed → `{(o1,o3)}`; role-blind → also `(o1,o2)` |
| Provenance-aware synthesis / `epistemic_status` ladder | `proposed` and unsourced claims stay out of the facts list; flat synthesis promotes them | facts = `[Maya chose PostgreSQL]`; `proposed` → uncertain; unsourced → dropped; flat method puts both in facts |

## Findings folded back into the skill

No correctness fix was needed in the skill body — the operators as described in
`SKILL.md` and the references produced the right call on every case on the first
pass. One verification-code fix: the time-blind contrast must model the *actual*
naive method (an approval exists → authorized, with no policy awareness), not a
partially time-aware one, or the contrast does not exercise `valid_time`.

## The checks are necessary, not sufficient

They confirm the operators behave as specified on clean, unambiguous cases. They
do **not** verify the hard, human part: whether an extraction captured the right
roles and modality from messy prose, whether an identity merge is safe, whether
a source is authoritative, or whether "the roles differ" is the right reading of
two conflicting claims rather than a genuine dispute. Those stay with the
reviewer, as `SKILL.md` states.
