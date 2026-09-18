# What opened each open backlog item

**Date:** 2026-09-17. **Items:** the 46 open `- [ ]` items in `BACKLOG.md`, as
`docs/book/tools/gen-open.py --list` enumerates them.

Written to settle claim-ledger row **C-V-03**, which recorded that V.0's
sentence *"roughly half the open backlog items were opened by the audits of
Part III"* had been **written without a count**. A keyword proxy matched 29 of
46 but also hit capsule items unrelated to those audits, so the row was filed at
`low` confidence with the real fix named: hand-classify by origin. This is that
classification.

It is a hand reading of each item's own text, not a matcher, so it cannot be
regenerated — which is why the prose it supports states no number.

## Result

| origin | items | n |
|---|---|---|
| **A Part III audit** | 14, 46 | **2** |
| The standard's own instruments (displacement tables, `check_authoring.py`, harness-gap lists) | 6, 20, 24, 29, 31, 32, 34, 37, 38, 41, 42, 43 | 12 |
| Planned capsule / skill roadmap | 1–5, 7–13, 15–19, 21–23, 25–27, 30, 33 | 25 |
| Writing this book | 39, 40, 44, 45 | 4 |
| A real run of a skill, in use | 35, 36 | 2 |
| Operational | 28 | 1 |

**Two of forty-six.** The claim was not merely imprecise; it was wrong by an
order of magnitude, and so is the softened "many" that replaced it.

## Why the true number is so small

The Part III audits mostly **closed** rather than opened. Four `- [x]` items
carry their machinery (the bc audit itself, its 15 unasserted harnesses, the
broken marker grep, and the role-deck founding premise), and the bc audit's
remediation landed the same day it ran (`26de48f..735a81a`, `dde3f82`). The
Lean and graph audits' counts — 41 unbacked claims, 36 missing edges — were
never written as backlog rows at all: they live in `docs/verifying-skills.md`
§5b and in each capsule's own `check-lean-cores.py` / `check-edge-evidence.py`
output, which is where the gate can see them.

So the mechanism V.0 describes is real — a standard that is working does
generate backlog — but **it is not what this backlog is mostly made of**. Most
of it is planned capsule work. The second-largest source is the standard's
displacement tables, which is the same mechanism by a different instrument and
is the honest thing for V.0 to point at.

## Two findings this pass produced

1. **V.0's other sentence was also wrong.** *"The audits of Part III mostly did
   not produce fixes. They produced entries."* The opposite: the bc audit
   produced fixes the same day, and the Lean and graph audits produced gates.
   Corrected 2026-09-17.
2. **A dangling reference.** Item 14 cited `docs/lean-core-audit.md`, which has
   never existed in this repository. The audit is `docs/verifying-skills.md`
   §5b. Fixed in `BACKLOG.md` 2026-09-17.

## Judgement calls, recorded

- **35, 36** (`role-deck`, found by the first real `diagnose` run) are narrated
  in Part III's premises chapter, but the run opened them, not the audit. Filed
  under use, not audit.
- **37, 38, 43** (`claim-fixture`'s missing positive control and unverified
  subject naivety) were opened 2026-09-15, before Part III existed; the book's
  evidence pass only annotated them (F10). Filed under the standard's
  instruments.
- **46** (re-run the premise fixture with isolated subjects) *was* opened by
  that evidence pass, which is Part III's work. Filed under audit.
- **42** (`directed-verification` b1) is a premise fixture, but not one Part III
  measures — the chapter's two claims are both `role-deck`'s.
