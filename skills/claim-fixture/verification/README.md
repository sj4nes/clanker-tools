# `claim-fixture` skill — verification run

`claim-fixture` is a **behaviour-modification** skill: it displaces the default
of building a methodology on an unmeasured assertion about what people or
agents do. Per `docs/verifying-skills.md` §7 every section must name the
default it displaces and the verification must show that default failing.

Here the default failing is not simulated. **It is the author's own work**: two
claims asserted confidently enough to build 2,300 lines of machinery on, both
measured, both false.

## Run

```
sh skills/claim-fixture/verification/run.sh
```

`git` + `/bin/sh`. < 1 s. Must be run inside the repo (it reads commit order).

## What is checked, and what cannot be

Most of this method is judgement — whether subjects were truly naive, whether a
fixture came from a real failure, whether a confound was weighed or leaned on.
None of that is mechanizable and the skill says so.

**One part is.** "Pre-registered" is either provable from the record or it is a
claim the reader must take on faith, which is what pre-registration exists to
avoid. `check_preregistration.sh` asserts a fixture's scorer was committed
strictly before its first result, treating *the same commit* as a failure.

| Case study | Scorer | First result | Verdict |
|---|---|---|---|
| ordering fixture | `2b75803` | `da8cfa7`, 12 min later | **ok** |
| premise fixture | `1cb9ee5` | `1cb9ee5`, same commit | ***FAIL*** |

The failure is permanent and deliberate. The premise fixture's scorer *was*
written before any result — in-session, while the agents ran — and committed
alongside them. The record cannot distinguish that from writing it afterwards,
which is exactly the point behaviour 4 makes when it says *separate commit*.
Repairing it by rewriting history would destroy the only honest demonstration
this skill has.

## Displacement table

| `SKILL.md` section | Default behaviour it displaces | Where the default visibly fails |
|---|---|---|
| b1 split the claim | fixture the whole claim, including the half a gate already settles | premise fixture: the structural half was gate-proven, halving the design to one arm |
| b2 you cannot be the subject | test your own claim on yourself | `judgement` — no fixture can catch an author who believes they are neutral |
| b3 unforgeable measurement | ask the subject what they did | both case studies: an unreachable stderr string; executing the subject's own patch |
| b4 pre-register in a separate commit | claim you decided the bands beforehand | **`check_preregistration.sh` — the premise fixture fails it** |
| b5 real failure, shortcut passes its own check | build a trick puzzle where the shortcut obviously fails | ordering fixture: fixing the anchor alone *catches the presented bug* |
| b6 strike, do not reword | substitute a similar untested claim | case study 2 exists because the reflex after case study 1 was exactly that substitution |
| what this cannot tell you (4 items) | read a refutation as proving the method worthless | `judgement` |

**4 covered · 2 judgement · 2 gaps.**

### Gaps

1. **n=2 case studies, one author, one day, one model.** The method produced
   two refutations; it has never produced a *confirmation*, so nothing
   demonstrates it can return positive when the claim is true. A fixture
   against a claim already known true would be the control this lacks.
2. **Subject naivety is asserted, not verified.** Both case studies used fresh
   agents with filesystem access to a repo documenting the hypotheses. Scoring
   was unforgeable, so priming could not fake a result — but nothing measured
   whether subjects read that material.
