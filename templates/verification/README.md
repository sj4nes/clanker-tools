# `<SKILL>` skill — verification run

The `<SKILL>` skill is methodology-only (no bespoke CLI), so verification means:
re-solve a case with a known answer using the workflow the skill prescribes, and
confirm each prescribed check — including each negative-contrast guardrail —
behaves as claimed.

**Case.** `<model / dataset / formula>` — chosen because `<it has a closed form:
... / it is small enough to also check by hand / a second independent method
exists>`.

## Run

```
sh skills/<SKILL>/verification/run.sh
```

Tooling: `bc` 7.x (`-l`), Python 3 (stdlib only), macOS. ~`<N>` s wall.

## What each step demonstrates (SKILL.md workflow step → result)

| Step | Prescribed check | Result |
|---|---|---|
| `<n>` `<name>` | `<what run.sh computes>` | `<actual numbers>` — **pass** |
| `<n>` `<name>` — negative contrast | `<the wrong method>` | `<undercovers / diverges / inflates FPR>` — **pass** (guardrail visibly trips) |

## Findings folded back into the skill

- `<fix>` — folded into `<file>`.
- `<or:>` Nothing in `SKILL.md` or the reference files needed a correctness fix;
  the prescribed workflow produced the right calls and the right conclusions.

## The gates are necessary, not sufficient

`run.sh` catches mechanical defects, not judgement. `<name what stays human:
model choice, the estimand, evidence adjudication, developmental editing>` — as
`SKILL.md` states.

---

See [`docs/verifying-skills.md`](../../../docs/verifying-skills.md) for the
shared run-script shape and the `bc` / Python / `tsort` / `lean` / `upmd`
portability rules.
