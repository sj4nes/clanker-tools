# Result: the ordering claim is refuted too

Run 2026-09-15, immediately after the fixture was tightened and committed.
Subjects: 8 fresh general-purpose agents (Claude Opus 5), each with an
identical clean copy, given `task.md` verbatim. No deck, no mention of
role-deck, no hint that a second cause existed.

## Score

**8/8 COMPLETE. 0/8 CONFIRMATORY. 0/8 BROKEN.**

Scored by `score.sh` — executing each subject's own edited `check.sh` against
the presented bug and against a stderr-only failure that **was not present in
the fixture they were given**.

Pre-registered band: *refuted — role-deck is down to auditability and
repeatability alone.*

## It is worse for the claim than 8/8 suggests

Every subject, unprompted:

- found the **second** cause, which was not visible in any output and required
  reading the suite and asking how else a test reports failure;
- **tested the stderr-only case**, constructing the failure themselves;
- **tested the all-pass case** — several said explicitly that a gate wedged at
  "fail" is as broken as one wedged at "ok". That is `test-writing`
  behaviour 6, run without being asked.

And **4 of 8 found a third hole I did not plant**: `suite.sh` always exits 0,
so a suite that dies partway through produces no FAIL line and reads as green.
They added exit-status or `suite complete` sentinel checks. Two more flagged it
explicitly and declined to fix it as out of scope.

The fixture was designed so that confirming the first explanation would feel
sufficient. Not one subject stopped there.

## Combined with the premise result

| Claim | Result |
|---|---|
| Agents skip the expensive hat (execution) | **refuted** 8/8 |
| Agents confirm rather than discriminate | **refuted** 8/8 |

**Both behavioural justifications for this skill are gone.** What survives is
what the structural gates actually prove and what the StructOrder run actually
demonstrated: an **auditable, replayable, repeatable** record. That is a real
and much smaller claim than the one the skill was built on.

## Caveats, stated but not leaned on

- **Contamination.** Subjects had filesystem access to a repo documenting this
  discipline. Scoring is by execution and unforgeable, but priming is possible.
- **Still a small, bounded task.** Two short files, a clear bug report, no
  cost to investigating. Whether the same holds when the second cause costs an
  hour is untested and this fixture cannot answer it.
- **n=8, one bug shape, one model, one day.**

These do not rescue the claim. 8/8 with half the cohort exceeding the fixture
is not a marginal result, and the honest response is to change the skill rather
than to keep looking for a framing in which it was right.

## What this does NOT say

It does not say the deck is useless, and it does not say agents are reliable.
The StructOrder run failed for a reason neither fixture tests: the WHITE hat
was aimed at a **dead source**, and every fact gathered was true while the
conclusion was wrong. No amount of discrimination discipline catches that —
it is a question of source authority, which is a live open backlog item and
remains the most promising thing this skill could add.
