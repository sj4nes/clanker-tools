# Fat outline — Parts I, II, IV, V

Part III is drafted (`../parts/03-findings/`). Governing structure pattern:
**problem → solution → evidence → worked examples → open**.

Concept introduction order is fixed by `deps.txt` via `tsort`; no chapter may
use a term an earlier chapter has not introduced. That rule is checked against
the DRAFTS, not just this outline: `tools/check-intro-order.py` (register in
`concepts.tsv`, which also lists named skills and tools; `// intro: <id>` markers
in the prose; gates self-tested by `tools/check-intro-order-mutations.py`). Chapters marked **GENERATED**
are produced from the repository and gated for freshness, not authored.

---

# Part I — The pile

## I.1 — You have a corpus and you do not know if it is an asset

- **Entering question.** I have written fifteen skills. Is that fifteen assets,
  or fifteen liabilities I now have to maintain?
- **Central claim.** A skill you cannot evaluate is not neutral. It spends the
  agent's context and your confidence, and a corpus compounds both.
- **Why now.** The category is months old. Every book on the shelf teaches
  production; none teaches evaluation, so the default is to keep writing.
- **Evidence.** The corpus: 50 skills, 161 commits, ten days. The comps survey.
- **Running example.** One real skill from this corpus, followed through the
  whole book — `test-writing` is the candidate: short, verified, and its own
  premise is one of the few backed by outside evidence.
- **Likely objection.** *"Quality here is a craft judgement; you cannot measure
  it."* Answered by Part III, and by the fact that four audits found defects no
  amount of careful reading had.
- **Reader can now** state why the pile is a problem, in terms of context spent
  and confidence borrowed.

## I.2 — A skill makes a claim

- **Entering question.** What, exactly, does a skill assert?
- **Central claim.** A skill claims to displace a **default behaviour** with a
  better one. That is falsifiable, and naming it is the whole difference
  between a document and a check.
- **Evidence.** danluu's eval, cited by `test-writing`: agents fell back to poor
  default testing across the techniques named (NOT "all 26 conditions" —
  see claim-ledger.md, C-I-02). And the counter-case from Part III —
  two defaults asserted here and measured false.
- **Objection.** *"My skill teaches something the model does not know; there is
  no default to displace."* Real, and it is the tool-fact case — a genuine
  second category, not an exemption.
- **Reader can now** write the one sentence their skill is trying to be true.

> **Through-line.** If a skill is a claim, it can be checked — and the next part
> is how.

---

# Part II — The standard

The prescriptive heart. Each chapter is one move, in dependency order.

## II.1 — Name the default you displace

- **Entering question.** How do I write down what this skill is for, so that
  someone could disagree?
- **Framework.** The displacement table: section → default displaced → where
  the default visibly fails. A row with an empty third cell is advice. A row
  that no fixture can falsify is marked `judgement` — and naming those is the
  point, not a loophole.
- **Objection.** *"Most of my skill is judgement."* Then most of it is advice,
  and the table tells you how much — `statistics` came out 7 covered, 5
  judgement, 5 gaps, and the gaps were the yield.
- **Reader can now** produce a displacement table for one skill and count its
  three blocks.
- **Backed by:** `docs/verifying-skills.md` §7 — **docs only. See GAPS.md.**

## II.2 — Build a harness that can fail

- **Entering question.** My verification passes. What would it take for it not
  to?
- **Framework.** Assert rather than annotate; one failure marker; and then the
  move that matters — **break each guard alone**.
- **Evidence.** Part III chapter 1: 4 of 24, and a marker grep dead in 8 of 9.
- **Objection.** *"My check is simple enough that it obviously works."* Every
  one of the twenty was.
- **Reader can now** plant a defect, watch a guard fail in isolation, and
  revert.
- **Lineage — name it, do not claim it (added 2026-09-16).** Deliberate
  breakage is not new. Its nearest relative is TDD's red step, and its exact
  ancestor is **mutation testing**: traced to a 1971 student paper by Lipton,
  with the field's birth in DeMillo, Lipton & Sayward (1978) and Hamlet (1977)
  (Jia & Harman's survey; ledger C-II-01, C-II-02). Part III currently reads as
  if the corpus invented the practice — fix there too.
- **Objection to answer: "Isn't this just TDD?"** Same instinct (never trust a
  test you have not seen fail), four differences:
  1. **Red proves the test can fail, not that it fails for the reason you care
     about.** Red comes from absence. Worked case, measured (C-II-03): a `bc`
     harness written test-first goes RED on a missing file (exit 4), GREEN once
     the file exists — a textbook cycle — and a FALSE claim still exits 0.
     Red-green exercised *nothing → something*; the defect lived on
     *right → wrong*, which only mutating a correct artifact reaches.
  2. **Each guard alone.** One red per test says nothing about guards masking
     each other (the graph table: 3 caught, 2 not).
  3. **Retroactive.** Most corpus checks were written after the artifact —
     capsules, proofs, graphs — so there was never a red step. Breakage
     manufactures one.
  4. **It recurses.** Red happens once, at authorship; the check on the check
     needs the same treatment (the mutation that reported itself surviving).
- **Evidence that "just do TDD" is not the answer for agents** (C-II-04): in
  Luu's eval the TDD prompt DID produce red steps — failing tests before
  substantial implementation in 67 of 160 runs vs 0 of 160 under Default — and
  still gave worse tests and worse implementations: more small trivial tests,
  hard cases avoided (four identical, trivial Huffman streams), and iterating to
  green "tended to get agents to write more incorrect tests that would enforce
  incorrect behavior". The red step happened; it was not aimed at the defect.
  Do NOT say the red steps "passed trivially" — an earlier chat summary said so
  and the source does not.
- **Backed by:** `docs/verifying-skills.md` §2, §8 — **docs only.**

## II.3 — Choose an oracle that is not the thing you are checking

- **Entering question.** Where does the expected value come from?
- **Framework.** Independence as the property, not count: re-derivation from the
  spec, a model-based reference, a metamorphic relation, a genuinely separate
  implementation. Two implementations sharing a helper are one oracle.
- **Related open problem.** An oracle can also be **stale** — see the
  source-authority gap. Flagged here, not solved.
- **Reader can now** name their oracle and say what it shares with the subject.
- **Backed by:** `skills/test-writing`.
- **⚠ Evidence flag (2026-09-16).** Do NOT present "agents copy the expected
  value from the code's output" as an observed default. It is Yossi Kreinin's
  hypothesis, misattributed to the danluu eval in `2c387db` and inherited by
  `test-writing` behaviour 3 (ledger C-I-17). The independence test ("same
  thing twice") and asymmetric fixtures (palindromic tests) are observed
  (C-I-18). Candidate move: use behaviour 3 openly as the corpus's own
  unmeasured default — Part I.2's argument, applied to the running example.

## II.4 — Measure the premise before you build on it

- **Entering question.** Is the default I named actually what people do?
- **Framework.** `claim-fixture`'s six conditions: split the claim, naive
  subjects, unforgeable measurement, pre-registration in its own commit, a
  fixture where the shortcut passes its own check, strike rather than reword.
- **Evidence.** Both refutations, and the honest limitation — the method has
  produced no confirmations, so it may be biased toward refutation.
- **Objection.** *"I cannot run experiments on people."* Sixteen fresh agents,
  four minutes.
- **Reader can now** run one fixture against their own load-bearing premise.
- **Backed by:** `skills/claim-fixture`.

## II.5 — Version what you got wrong

- **Entering question.** How does a reader know whether the text in front of
  them is current, and how much it matters if it is not?
- **Framework.** MAJOR means *the skill was wrong* — re-do work done under the
  old text. So `MAJOR − 1` counts the times it has been wrong, and is a number
  worth being reluctant to increment.
- **Evidence.** `role-deck` 1.0.0 → 2.0.0 within a day, for a `verify` that
  reported a spurious failure on a valid run.
- **Reader can now** bump honestly, and write a changelog entry that says what
  a reader must *do*.
- **Backed by:** `docs/skill-versioning.md` — **docs only.**

## II.6 — Work with the agent, not at it

- **Entering question.** Which half of this should I be doing?
- **Central claim.** The agent is a participant in quality, not a text
  generator. It builds the harness, plants the defect, runs the fixture, and
  reports what it found *against you* — which is the only part that matters.
- **Evidence.** This corpus: every skill produced this way; two premises
  refuted by the agent that had asserted them; a `1/0` backstop catching its own
  author's arithmetic error mid-build.
- **Objection.** *"It will just agree with me."* Then the measurement is
  unforgeable or it is worthless — which is II.4, applied to your collaborator.
- **Reader can now** direct a verification task and recognise a result that
  disagrees with them as the valuable case.
- **Backed by:** **nothing. See GAPS.md — this is the book's differentiator and
  the corpus has no skill for it.**

## II.7 — Author a skill to the standard

- **Entering question.** All of the above, on a blank page. Where do I start?
- **Framework.** The synthesis: fixture-first, then prose; displacement table
  before the checklist; harness before the claim; premise before the harness.
- **Reader can now** author a new skill end to end.
- **Backed by:** **nothing. The largest gap. See GAPS.md.**

> **Through-line.** The standard is worth what it finds — and what it found is
> Part III.

---

# Part III — What the standard found

Drafted. Five chapters, four audits and a synthesis, each closing on a practice.

> **Through-line.** Those practices were applied to fifty skills. Here is what
> that produced.

---

# Part IV — The corpus as worked examples  **GENERATED**

- **Function.** Not an inventory. Each entry is a **worked example of the
  standard**: what it displaces, its table counts (covered / judgement / gaps),
  its verification headline, and its version history as a record of being wrong.
- **Generated from** SKILL.md frontmatter, verification READMEs, and CHANGELOGs.
  Gated by a freshness check in the spirit of `tools/check-skills.sh`.
- **Framing chapter (authored).** How to read an entry, and why a high gap count
  is a better sign than a zero one.
- **Reader can now** find the nearest example to the skill they are writing.

# Part V — What is still wrong  **GENERATED**

- **Function.** The open backlog, honestly. Including that the method of II.4
  has never returned a positive, and that this book has no reader interviews.
- **Generated from** `BACKLOG.md`.
- **Reader can now** see what a corpus held to this standard still gets wrong,
  which is the last argument against treating any of it as finished.
