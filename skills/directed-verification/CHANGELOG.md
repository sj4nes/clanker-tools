# Changelog — directed-verification

Versions follow [`docs/skill-versioning.md`](../../docs/skill-versioning.md):
`1.0.0` means "as verified at release"; **MAJOR** = the skill was wrong (re-do
work done under the old text), **MINOR** = a statement changed or grew (re-read
it), **PATCH** = nothing semantic.

    git log -- skills/directed-verification/

## 1.1.0 — 2026-09-15

Behaviour 1's fixture ran twice. It is still unmeasured, and the page now says
so precisely rather than calling it "logged as work".

- **Run 1 invalid.** The subject function was itself buggy (`int()` truncates
  toward zero), so arm-A agents scored `BROKEN` for correct work.
  `verification/b1-fixture/RESULT.md`.
- **Run 2: NO HEADROOM.** Clean subject, pre-registered design (`e3e8498`,
  committed before any subject ran). Both arms scored 5/5 `CATCHES`; Δ = 0. The
  pre-registered **ceiling rule** requires reporting this as *no headroom*, not
  as a refutation — a design in which the treatment cannot score higher has not
  tested the treatment. `verification/b1-fixture/RESULT2.md`.
- The plant had headroom (differed from correct code only at negative ties,
  931/28,824 cases); the **population** did not. All five undirected agents named
  the tie-and-sign discrimination unprompted, and one caught a stale-`.pyc`
  flake in its own mutation harness without being asked. A third run needs a
  defect a competent undirected suite genuinely misses.

No behaviour changed. `SKILL.md` and `verification/README.md` restate
behaviour 1's evidential status; the six behaviours are as released.

## 1.0.0 — 2026-09-15

First release. Closes the second gap the book's fat outline found: three
concepts with no source at all, clustered on the book's own stated
differentiator — the agent as a participant in quality rather than a producer of
text. Fifty-one skills, every one produced by a human and an agent working
together, and none about doing that.

Displacement table: **1 covered, 4 judgement, 2 gaps** — a weak table, reported
as weak. Behaviour 1 is measurable with `claim-fixture` and has not been
measured; that is logged rather than glossed.
