# Claim ledger — The Missing Manual

One row per assertion the book may make, per the `nonfiction-book` skill's
Phase 2. Fact, interpretation and recommendation are separate rows even when
they share a paragraph. A row enters drafting only when `drafting_status` is
`resolved` or explicitly `draft-anyway`.

Rows so far: **Part I only** (built 2026-09-16, before drafting Part I). Part
III was drafted before this ledger existed and has no rows yet — that is a
recorded gap, not an implied pass.

---

## Finding that came out of building this ledger

**The corpus's one external citation had drifted from its source.** danluu's
eval is cited in four places (`docs/verifying-skills.md` §7,
`skills/test-writing/SKILL.md` l.29, `BACKLOG.md` ×2), each time as:

> agents fell back to poor default testing across **all 26 conditions**; the
> skill that helped most was a five-bullet nudge; several tutorial-style
> skills, including ones from repositories with ~250k stars, performed
> **worse than no skill at all**.

Read against the article on 2026-09-16:

| corpus says | article says | status |
|---|---|---|
| fell back across all 26 conditions | 26 *prompt* conditions, including Default and "Make no mistakes", which name no technique; the 4 skills were tested **in addition** to the 26. "regardless of the library or technique suggested, agents failed to use the technique" | **correction**: across the techniques and libraries named, not "all 26 conditions" |
| five-bullet nudge helped most | five bullets, "This got the highest score, but **didn't work as intended**"; the fresh-context instruction was almost never followed; "would need more than the 2 minutes I spent on it to be actually useful" | supported, **with a caveat the corpus dropped** |
| several tutorial-style skills worse than no skill | Hegel skill: correctness worse than plain Hegel, "close enough that this could've been random". ECC (the 250k-star one — a *collection*, not a skill): raw score "almost as well as Default"; **only when restricted to runs the skill influenced** is it "worse than no instruction and no skill". ToB skill: underperformed, confounded by a dependency-approval instruction. | **correction**: one skill worse on an exposure analysis, one worse possibly by chance, one confounded. "Several … worse than no skill" overstates it |
| — | "I would caution anyone against drawing any kind of strong conclusions from the ordering"; one harness and model (codex, GPT-5.6 Sol, medium/xhigh), one task (Zstd in Rust), 80 runs per condition and effort, written up as "half-baked" | **caveats the corpus never carried** |

The *direction* of the corpus's use survives: a default behaviour distribution
exists, named techniques did not displace it, and the author's own reading is
that nudges should "modify that behavior" rather than teach. The *strength*
does not. This is a `source-authority`-shaped failure: every restatement was
made from an earlier restatement, not from the article.

### Origin, traced 2026-09-16

First appearance: commit `2c387db` (2026-09-09, "backlog: promote test-writing
skill", co-authored with Claude Sonnet 5; session link in the commit). **The
article's URL has never been in the repository** — `git log -S agentic-testing`
is empty — so nothing in the repo shows whether that session read the article.
The overstatement is present **in the first commit**, not added by drift;
`883c698` (2026-09-13) then strengthened it into `docs/verifying-skills.md` §7
("worse than no skill at all"), and every later citation copies §7.

### A second misattribution, in the same commit

`2c387db` also filed `test-oracle-design`, motivated by: *"agents
overwhelmingly encode the code's own output as the expected value and never
build a separate oracle."* **The eval did not measure this.** It is a hedged
comment by Yossi Kreinin, quoted in the article's TDD section: "i think the
fixed input/output style of testing encourages this in machines and humans
alike … with fixed outputs you are quite likely to just encode the output of
the code". `test-oracle-design` was later folded into `test-writing`, so
**behaviour 3's founding default is an opinion, not an observation.** What the
article does observe, from transcripts: palindromic test data that could not
detect a reversed bitstream (backs behaviour 4), and differential testing where
agents "would generally just write the same thing twice" (backs behaviour 3's
independence test — not its expected-value rule).

**Not fixed here.** Correcting `test-writing/SKILL.md` is a skill change (a
MINOR bump under `docs/skill-versioning.md`) and is logged in `BACKLOG.md`
rather than done silently inside book work.

---

## Part I rows

```yaml
- id: C-I-01
  claim_text: "danluu's 'How well do agents use test/verification techniques?'
    (September 2026) ran a Zstd implementation task in Rust under 26 prompt
    conditions plus 4 skills, on codex with GPT-5.6 Sol at medium and xhigh
    effort, averaging 80 runs per condition and effort."
  claim_type: fact
  evidence_needed: the article itself
  source: "Dan Luu, 'How well do agents use test/verification techniques?',
    https://danluu.com/agentic-testing/ — methods paragraphs"
  source_tier: primary
  date_checked: 2026-09-16
  confidence: high
  caveats: "Self-described 'half-baked' write-up. One task, one harness, one
    model family. Not peer reviewed."
  chapter: I.2
  citation_status: footnote
  citation_check: verified
  drafting_status: resolved

- id: C-I-02
  claim_text: "Regardless of the technique or library named, agents mostly
    wrote the tests they would have written anyway, inside the named framework."
  claim_type: interpretation   # the author's, from inspecting transcripts
  evidence_needed: the article's own summary
  source: "ibid. — 'agents just write the tests they would normally write, but
    inside a framework for a different type of test technique'; 'regardless of
    the library or technique suggested, agents failed to use the technique'"
  source_tier: primary
  date_checked: 2026-09-16
  confidence: medium
  caveats: "The author's qualitative reading of transcripts, not a scored
    measure. Default (no instructions) scored WELL ABOVE average — the default
    is poor testing, but naming a technique made it worse, not better. Must not
    be stated as 'across all 26 conditions'."
  chapter: I.2
  citation_status: footnote
  citation_check: verified-with-correction
  drafting_status: resolved

- id: C-I-03
  claim_text: "The highest-scoring condition was a five-bullet skill the author
    wrote in about two minutes, designed to nudge away from default behaviour
    rather than teach — and he reports it did not work as intended."
  claim_type: fact
  evidence_needed: the article
  source: "ibid. — 'Skill' section and results summary"
  source_tier: primary
  date_checked: 2026-09-16
  confidence: high
  caveats: "'Highest score' with an explicit warning against reading the
    ordering. The half that failed to work is part of the claim, not a footnote
    to it."
  chapter: I.2
  citation_status: footnote
  citation_check: verified-with-correction
  drafting_status: resolved

- id: C-I-04
  claim_text: "The ECC Rust test skill, from a collection with 250k GitHub
    stars, scored almost as well as no instructions — but only because the runs
    that never really read it did unusually well. Restricted to runs the skill
    actually influenced, it scored below average, 'worse than no instruction and
    no skill', and the earlier an agent read it the worse its result."
  claim_type: fact
  evidence_needed: the article
  source: "ibid. — ECC section"
  source_tier: primary
  date_checked: 2026-09-16
  confidence: high
  caveats: "Exposure analysis on 160 runs; the author notes possible bias in
    when the skill is invoked. The 250k stars belong to the collection, not to
    this skill."
  chapter: I.1
  citation_status: footnote
  citation_check: verified
  drafting_status: resolved

- id: C-I-05
  claim_text: "A top-line score can make an ineffective skill look fine; it
    took reading the runs to see it."
  claim_type: interpretation
  evidence_needed: C-I-04 plus the author's own statement
  source: "ibid. — 'superficially, if we just look at the score, ECC seems ok';
    'people are often misled into thinking a skill is useful by a few small
    runs'"
  source_tier: primary
  date_checked: 2026-09-16
  confidence: medium
  caveats: "One instance. Supports 'can', not 'usually does'."
  chapter: I.1
  citation_status: footnote
  citation_check: verified
  drafting_status: resolved

- id: C-I-06
  claim_text: "The official Hegel skill is over 20k tokens, was re-read on many
    actions, and raised cost 26% (medium) and 41% (xhigh) without improving
    correctness."
  claim_type: statistic
  evidence_needed: the article
  source: "ibid. — Hegel section"
  source_tier: primary
  date_checked: 2026-09-16
  confidence: high
  caveats: "Correctness 'worse (though it was close enough that this could've
    been random)'. The cost increase the author calls causal; the correctness
    change he does not."
  chapter: I.1
  citation_status: footnote
  citation_check: verified
  drafting_status: resolved

- id: C-I-07
  claim_text: "A skill is not neutral: it costs context and money on every run
    that loads it, whether or not it helps."
  claim_type: interpretation
  evidence_needed: C-I-06 as the measured instance
  source: "derived from C-I-06"
  source_tier: primary
  date_checked: 2026-09-16
  confidence: medium
  caveats: "Measured for one large skill in one harness. In harnesses that
    load a skill's body only on invocation, the always-on cost is the
    description, not the body."
  chapter: I.1
  citation_status: no-citation-needed
  citation_check: n/a
  drafting_status: resolved

- id: C-I-08
  claim_text: "The corpus this book reports on: 53 skills, 190 commits, built
    between 5 and 16 September 2026; the SKILL.md files alone run to about
    98,000 words."
  claim_type: statistic
  evidence_needed: repository measurement
  source: "clanker-tools @ 729d3aa — `ls skills/*/SKILL.md | wc -l`;
    `git rev-list --count HEAD`; first/last commit dates;
    `cat skills/*/SKILL.md | wc -w` (97,730)"
  source_tier: primary
  date_checked: 2026-09-16
  confidence: high
  caveats: "ROTS. The outline's '50 skills, 161 commits, ten days' was already
    stale a day later. Draft states it as-of a commit; the eventual fix is to
    generate it, as Parts IV and V are."
  chapter: I.1
  citation_status: no-citation-needed
  citation_check: n/a
  drafting_status: draft-anyway   # until generated

- id: C-I-09
  claim_text: "Every SKILL.md-focused book on the shelf in September 2026 is
    dated February–August 2026, and by title and subtitle all promise
    production — building and shipping skills — rather than evaluating them."
  claim_type: fact
  evidence_needed: shelf survey
  source: "docs/book/comps-table.md (author's Amazon survey, 2026-09-15)"
  source_tier: primary
  date_checked: 2026-09-15
  confidence: medium
  caveats: "NONE OF THE BOOKS HAVE BEEN READ (positioning brief). Supports a
    claim about the genre's framing only. The outline's 'none teaches
    evaluation' is an assertion about content and is NOT supported — do not
    draft it."
  chapter: I.1
  citation_status: no-citation-needed
  citation_check: n/a
  drafting_status: resolved   # in the genre-framing wording only

- id: C-I-10
  claim_text: "Four audits in this corpus found checks that could not fail —
    in bc, Lean, tsort and a methodology's own premise — and none was found by
    reading; each was found by breaking something on purpose."
  claim_type: fact
  evidence_needed: Part III, and the commits it cites
  source: "docs/book/parts/03-findings/; memory rows bc-verification-audit,
    lean-core-audit, graph-verification-audit; skills/claim-fixture"
  source_tier: primary
  date_checked: 2026-09-16
  confidence: high
  caveats: "Part III has no ledger rows yet; this row inherits whatever its
    evidence pass finds."
  chapter: I.1
  citation_status: no-citation-needed   # internal cross-reference
  citation_check: n/a
  drafting_status: draft-anyway

- id: C-I-11
  claim_text: "A skill claims to displace a default behaviour with a better
    one, and that claim is falsifiable."
  claim_type: interpretation   # the book's central thesis
  evidence_needed: argument, plus the danluu author's independent statement
  source: "docs/verifying-skills.md §7; danluu, 'Naive thoughts on skill
    writing': 'The model is already going to have some kind of default
    behavior distribution, so … give statements that will modify that
    behavior, not write instructions that would allow a human or
    non-knowledgeable agent to do the behavior at all.'"
  source_tier: primary
  date_checked: 2026-09-16
  confidence: medium
  caveats: "danluu frames this as a naive guess from someone who has 'written
    all of one skill'. Convergence, not proof."
  chapter: I.2
  citation_status: footnote
  citation_check: verified
  drafting_status: resolved

- id: C-I-12
  claim_text: "Two defaults this corpus asserted were measured and were false:
    'an agent will skip the expensive step' (8/8 ran it) and 'an agent will
    confirm rather than discriminate' (0/8 confirmatory)."
  claim_type: fact
  evidence_needed: the fixtures
  source: "skills/role-deck/verification/premise-fixture/,
    ordering-fixture/; docs/refuted-premises/"
  source_tier: primary
  date_checked: 2026-09-16
  confidence: medium
  caveats: "claim-fixture has never returned a positive, so its sensitivity is
    untested: read as 'no effect detected by an instrument of unknown
    sensitivity'. n=8 each. Must travel with the claim wherever it appears."
  chapter: I.2
  citation_status: no-citation-needed
  citation_check: n/a
  drafting_status: draft-anyway

- id: C-I-13
  claim_text: "Some skills have no default to displace: they carry facts the
    agent cannot derive — BSD tsort exits 0 on a cycle; bc truncates rather than
    rounds. These are a second kind of skill, judged by omission rather than
    displacement."
  claim_type: interpretation
  evidence_needed: the taxonomy, plus the tool facts
  source: "docs/verifying-skills.md §7 table; skills/tsort, skills/bc"
  source_tier: primary
  date_checked: 2026-09-16
  confidence: high
  caveats: "The classification is per section, not per skill (§7)."
  chapter: I.2
  citation_status: no-citation-needed
  citation_check: n/a
  drafting_status: resolved

- id: C-I-14
  claim_text: "test-writing's six behaviours were built fixture-first against
    planted bugs, and its first two behaviours track the first bullet of the
    skill that scored highest in danluu's eval."
  claim_type: fact
  evidence_needed: the skill and its verification directory
  source: "skills/test-writing/SKILL.md behaviours 1–2;
    skills/test-writing/verification/README.md; danluu 'Skill' section bullet 1"
  source_tier: primary
  date_checked: 2026-09-16
  confidence: high
  caveats: "Tracking a highest-scoring skill is not evidence test-writing
    works: that skill 'didn't work as intended'. test-writing's own behavioural
    claim has NEVER been fixtured; the neighbouring claim directed-verification
    b1 has been run three times, all invalid. (An earlier draft conflated the
    two — caught in the evidence check.)"
  chapter: I.1, I.2 (running example)
  citation_status: no-citation-needed
  citation_check: n/a
  drafting_status: resolved
```

```yaml
- id: C-I-15
  claim_text: "Before running, Luu pre-registered at 55–65% confidence that
    none of the three public skills would outperform, and all three
    predictions came true."
  claim_type: fact
  evidence_needed: the article's predictions appendix
  source: "danluu.com/agentic-testing/ — pre-registered guesses and their
    outcomes (ECC 65%, Hegel 65%, ToB 55%; each marked True)"
  source_tier: primary
  date_checked: 2026-09-16
  confidence: high
  caveats: "Cuts AGAINST the book's thesis — reading the skills did predict
    the direction. Used honestly in I.1's objection section: judgement got the
    direction at low confidence; only measurement settled it."
  chapter: I.1
  citation_status: footnote
  citation_check: verified
  drafting_status: resolved

- id: C-I-16
  claim_text: "The corpus records 34 open authoring-standard failures."
  claim_type: statistic
  evidence_needed: the ratchet
  source: "skills/skill-authoring/verification/baseline.txt @ 729d3aa"
  source_tier: primary
  date_checked: 2026-09-16
  confidence: high
  caveats: "ROTS; a ratchet cannot tell 'fixed two, broke two'."
  chapter: I.1
  citation_status: no-citation-needed
  citation_check: n/a
  drafting_status: draft-anyway
```

```yaml
- id: C-I-17
  claim_text: "Agents writing tests tend to take the expected value from the
    code's own output."
  claim_type: interpretation   # a commenter's hypothesis, NOT a finding
  evidence_needed: a measurement of what agents do by default
  source: "Yossi Kreinin, quoted in danluu.com/agentic-testing/ (TDD section):
    'i think the fixed input/output style of testing encourages this in
    machines and humans alike'"
  source_tier: primary   # for the quote; carries no evidential weight as a finding
  date_checked: 2026-09-16
  confidence: low
  caveats: "Hedged ('i think'), generalised across humans and machines, not
    measured in the eval. The corpus (2c387db, then test-writing behaviour 3)
    attributes it to the eval as a finding. Must not appear in the book as an
    observed default; it is the ASSUMED default under test-writing's most
    prominent rule — which is itself an instance of Part I.2's argument."
  chapter: I.2 (only as a counter-example), II.3
  citation_status: footnote
  citation_check: contradicted   # as attributed; verified as a quote of Kreinin
  drafting_status: blocking   # for any sentence stating it as observed

- id: C-I-18
  claim_text: "In the eval, agents wrote palindromic test data that could not
    detect a reversed bitstream, and when asked for differential testing would
    'generally just write the same thing twice'."
  claim_type: fact   # the author's observation from transcripts
  evidence_needed: the article
  source: "danluu.com/agentic-testing/ — formal-methods section (palindromic
    tests); Differential testing section ('same thing twice'; 135 of 160 runs
    did something like differential testing, generally trivial)"
  source_tier: primary
  date_checked: 2026-09-16
  confidence: medium
  caveats: "Qualitative, from transcript reading; no frequency stated for the
    palindromic case."
  chapter: I.2, II.3
  citation_status: footnote
  citation_check: verified
  drafting_status: resolved
```

```yaml
- id: C-I-19
  claim_text: "ECC stands for Everything Claude Code: the repository
    affaan-m/ECC was formerly affaan-m/everything-claude-code."
  claim_type: fact
  evidence_needed: repository record
  source: "GitHub REST API, 2026-09-16: repos/affaan-m/everything-claude-code
    and repos/affaan-m/ECC both resolve to repository id 1136590548 (created
    2026-01-18). Luu links affaan-m/ECC without expanding the name; the current
    README does not expand it either."
  source_tier: primary
  date_checked: 2026-09-16
  confidence: high
  caveats: "Inferred from the rename redirect, not from a statement by the
    maintainer. Stars were 260,046 / forks 38,924 on 2026-09-16; the book uses
    Luu's '250k' as the figure at experiment time."
  chapter: I.1
  citation_status: footnote
  citation_check: verified
  drafting_status: resolved
```

## Part III rows (started 2026-09-16; Part III's evidence pass is still owed)

```yaml
- id: C-III-01
  claim_text: "Fourteen of the corpus's skills are knowledge capsules, holding
    about 1,500 nodes between them; in math-probability, bayes_theorem's entry
    lists conditional_probability, law_of_total_probability and
    multiplication_rule as dependencies, and the edge file carries the same
    three edges, and its lean_ref points at a Lean core."
  claim_type: fact
  evidence_needed: repository measurement
  source: "clanker-tools @ 729d3aa — skills/*/nodes/nodes.tsv row counts minus
    header (14 capsules, 1,521 nodes; physics-formula-atlas is a bridge with no
    node registry); skills/math-probability/results/bayes_theorem.yaml;
    edges/dependencies.plan lines 134–136"
  source_tier: primary
  date_checked: 2026-09-16
  confidence: high
  caveats: "ROTS (counts). 'Fourteen' matches Part III's audit count. The
    Bayes Lean core proves the denominator identity plus a decide instance, not
    the full theorem — the chapter says 'the step that needs one', not 'a
    proof of the theorem'."
  chapter: III.3 (book chapter 5)
  citation_status: no-citation-needed
  citation_check: n/a
  drafting_status: resolved
```

```yaml
- id: C-III-02
  claim_text: "The diagnose deck has eight cards (open, hunch, gather,
    hypothesize, support, falsify, run, close) with the hats, needs and outputs
    shown in the chapter table; budget 11, run costs 2; gather and run carry
    instruments; 36 reachable states, 8 distinct complete runs, 17 gates."
  claim_type: fact
  evidence_needed: the deck file and the checker's output
  source: "skills/role-deck/decks/diagnose.json v0.8.0;
    `python3 check_deck.py decks/diagnose.json` @ 729d3aa (17 'ok' gate lines)"
  source_tier: primary
  date_checked: 2026-09-16
  confidence: high
  caveats: "ROTS with the deck version. SKILL.md's workflow comment still says
    '16 gates' — stale by one (min-items was added as gate 17)."
  chapter: III.4 (book chapter 6)
  citation_status: no-citation-needed
  citation_check: n/a
  drafting_status: resolved

- id: C-III-03
  claim_text: "The roles are de Bono's Six Thinking Hats plus an EXECUTE role
    added by the corpus; white = facts, red = feelings, green = alternatives,
    yellow = benefits, black = caution, blue = process control."
  claim_type: fact
  evidence_needed: the book, and the deck files
  source: "Edward de Bono, Six Thinking Hats (Little, Brown, 1985) — as cited
    in docs/refuted-premises/references.bib; decks/*.json role lists"
  source_tier: secondary-high-quality   # the hat meanings are widely documented; the book itself not re-read
  date_checked: 2026-09-16
  confidence: medium
  caveats: "The de Bono book was not re-read for this row; the colour meanings
    are the standard ones. Run citation-check on the edition before production."
  chapter: III.4 (book chapter 6)
  citation_status: footnote
  citation_check: likely
  drafting_status: draft-anyway

- id: C-III-04
  claim_text: "The first real diagnose run: 10 plays, spend 11/11, hunch
    played second, two gathers, four hypotheses, a discriminator that probed
    the wrong file, one reroll to record a corrected test; conclusion wrong
    though every fact gathered was true."
  claim_type: anecdote
  evidence_needed: the archived ledger
  source: "skills/role-deck/examples/structorder-drift.ledger.json
    (`run_deck.py log`, from the skill directory); examples/README.md"
  source_tier: primary
  date_checked: 2026-09-16
  confidence: high
  caveats: "The subject is the author's own private project (StructOrder);
    the chapter describes it generically. Naming it is the author's call.
    `run_deck.py log` fails from the repo root: the ledger stores a relative
    deck_path."
  chapter: III.4 (book chapter 6)
  citation_status: no-citation-needed
  citation_check: n/a
  drafting_status: resolved
```

## Part II rows (started 2026-09-16)

### citation-check report — DeMillo, Lipton & Sayward (1978)

Raw: *DeMillo, Lipton, Sayward, "Hints on Test Data Selection: Help for the
Practicing Programmer", IEEE Computer, 1978.* No identifier supplied; type
inferred **journal/magazine article**.

| | |
|---|---|
| status | **`verified`** (existence), FRBR **manifestation** |
| canonical | R. A. DeMillo, R. J. Lipton, F. G. Sayward, "Hints on Test Data Selection: Help for the Practicing Programmer," *Computer* 11(4):34–41, April 1978. doi:10.1109/C-M.1978.218136 |
| sources | Crossref `query.bibliographic` → DOI 10.1109/c-m.1978.218136, all fields match (score 105, runner-up 49 = a different 1979 report); doi.org 302 → IEEE Xplore document 1646911; OpenAlex W2049695835 (independent pipeline) — same title, authors, vol 11, iss 4, pp 34–41, 1978 |
| corrections | none to the cited fields; add volume/issue/pages/DOI. Venue is IEEE's *Computer* magazine |
| flags | none (no retraction or erratum found) |
| claim support | **the ledger's "origin of mutation testing" is NOT supported as worded.** Jia & Harman: "The history of Mutation Testing can be traced back to 1971 in a student paper by Richard Lipton. The birth of the field can also be identified in papers published in the late 1970s by DeMillo et al. and Hamlet." Say *one of the two founding papers*, not *the origin* |
| retrieved | 2026-09-16 |

```yaml
- id: C-II-01
  claim_text: "Mutation testing's founding papers are DeMillo, Lipton and
    Sayward (1978) and Hamlet (1977); the idea traces to a 1971 student paper by
    Lipton."
  claim_type: fact
  evidence_needed: the papers' bibliographic records + a survey of the field
  source: "DeMillo, Lipton & Sayward, Computer 11(4):34–41, 1978,
    doi:10.1109/C-M.1978.218136; Hamlet, 'Testing Programs with the Aid of a
    Compiler', IEEE TSE 3(4):279–290, 1977 (as cited by Jia & Harman, not
    independently checked); history per C-II-02"
  source_tier: primary + secondary-high-quality
  date_checked: 2026-09-16
  confidence: high
  caveats: "Hamlet 1977 and Lipton 1971 are verified only as Jia & Harman cite
    them. Lipton 1971 is an unpublished CMU student report."
  chapter: II.2
  citation_status: footnote
  citation_check: verified   # DeMillo 1978; Hamlet 1977 Crossref-verified 2026-09-16:
                             # IEEE TSE SE-3(4):279–290, July 1977, doi:10.1109/TSE.1977.231145
  drafting_status: resolved

- id: C-II-02
  claim_text: "Jia and Harman's survey dates mutation testing to a 1971 student
    paper by Lipton, with the field's birth in the late-1970s papers of DeMillo
    et al. and Hamlet."
  claim_type: fact
  evidence_needed: the survey text
  source: "Y. Jia, M. Harman, 'An Analysis and Survey of the Development of
    Mutation Testing', IEEE TSE 37(5):649–678, Sept 2011,
    doi:10.1109/TSE.2010.62 (Crossref-verified); quote read from the
    accepted-manuscript PDF, crest.cs.ucl.ac.uk/fileadmin/crest/sebasepaper/JiaH10.pdf,
    Introduction"
  source_tier: secondary-high-quality
  date_checked: 2026-09-16
  confidence: high
  caveats: "Quote is from the accepted manuscript ('not been fully edited'),
    not the version of record; check wording against the published version
    before quoting in print."
  chapter: II.2
  citation_status: footnote
  citation_check: verified
  drafting_status: resolved

- id: C-II-03
  claim_text: "GNU/BSD-style bc 7.0.3 exits 4 on a missing file and 2 on a
    syntax error, but 0 on a file whose assertion is false."
  claim_type: fact
  evidence_needed: direct measurement
  source: "measured 2026-09-16, bc 7.0.3 (macOS): `bc -lq nonexist.bc` → 4;
    a file containing `x = (` → 2; a file printing '*** FAIL' for a false
    claim → 0"
  source_tier: primary
  date_checked: 2026-09-16
  confidence: high
  caveats: "Exit codes are implementation-specific; state the version. Agrees
    with Part III chapter 1 (bc audit)."
  chapter: II.2
  citation_status: no-citation-needed
  citation_check: n/a
  drafting_status: resolved

- id: C-II-04
  claim_text: "In Luu's eval the TDD prompt produced failing tests before
    substantial implementation in 67 of 160 runs (0 of 160 under Default),
    doubled the test count, and still gave worse tests: hard cases avoided, and
    iterating to green tended to produce tests that enforced incorrect
    behaviour."
  claim_type: fact
  evidence_needed: the article
  source: "danluu.com/agentic-testing/ — TDD section; the 'more incorrect
    tests that would enforce incorrect behavior' sentence is stated across
    conditions and two iterative skills, not TDD alone"
  source_tier: primary
  date_checked: 2026-09-16
  confidence: high
  caveats: "Luu: 'a TDD advocate would probably say that agents didn't
    actually use TDD'. The finding is about PROMPTING agents with TDD, not
    about TDD as practised by people. Luu does not know why ('not obvious from
    the outside'). An earlier chat summary said the red steps 'passed
    trivially' — unsupported, do not use."
  chapter: II.2
  citation_status: footnote
  citation_check: verified
  drafting_status: resolved
```

### II.1 rows (built 2026-09-16, before drafting II.1)

Two findings from building these rows, neither fixed here:

- **The third column certifies a procedure, not a behaviour.** `role-deck`'s
  row b1 is `covered` — a naive procedure is shown failing — while the
  stronger premise behind it (agents *would* skip the work) was fixtured and
  refuted 8/8. A covered row proves the default is bad if an agent does it; it
  does not prove agents do it. That is II.4's question, and the chapter says so.
- **`directed-verification`'s README says "Compare `test-writing` at 6
  covered".** `test-writing`'s table has 5 covered rows (3, 4, 5, 6,
  "properties must discriminate"), 2 `judgement`, and 1 row with an empty
  second cell. Do not repeat "6".
- **FIXED 2026-09-16:** **`concepts.tsv` chapter numbers were stale** against the fat outline
  (`displacement-table` listed at II.3; the outline puts it at II.1). The
  `tsort` order is unaffected. Note: `harness` is introduced in II.2, so II.1
  may only gesture at it.

```yaml
- id: C-II-05
  claim_text: "The corpus's rule: every section of a behaviour skill must name
    the default it displaces, and the verification must show that default
    failing. The table is section → default displaced → where it visibly fails;
    rows sort into covered, judgement, and gaps, and the counts are the
    deliverable."
  claim_type: fact
  evidence_needed: the rule text
  source: "docs/verifying-skills.md §7; skills/skill-authoring/SKILL.md
    behaviour 2 (v1.0.0)"
  source_tier: primary
  date_checked: 2026-09-16
  confidence: high
  caveats: "§7's own paragraph on danluu carries the overstated citation
    (C-I-17 family). Do NOT quote §7's evidence paragraph; I.2 already carries
    the corrected wording."
  chapter: II.1
  citation_status: no-citation-needed
  citation_check: n/a
  drafting_status: resolved

- id: C-II-06
  claim_text: "statistics, the second skill put through the rule and the first
    not designed around it, came out 7 covered, 5 judgement, 5 gaps. No
    SKILL.md claim was found wrong; five were asserted on the skill's authority
    where a harness could carry them. The five gaps are still open."
  claim_type: fact
  evidence_needed: the table; the backlog item
  source: "skills/statistics/verification/README.md 'Displacement table' (row
    counts checked 2026-09-16: 7/5/5); commit f44cf86 (2026-09-13); BACKLOG.md
    item unchecked as of 2026-09-16"
  source_tier: primary
  date_checked: 2026-09-16
  confidence: high
  caveats: "'still open' rots — re-check at the evidence pass. statistics
    README says 437-line SKILL.md at the time (commit body)."
  chapter: II.1
  citation_status: no-citation-needed
  citation_check: n/a
  drafting_status: resolved

- id: C-II-07
  claim_text: "Covered-row numbers in statistics: the naive z-interval covers
    0.880 at n = 5 where the exact t-interval covers 0.950; 20 unadjusted tests
    give a realised family-wise error of 0.638 against 0.047 with Bonferroni;
    a bootstrap for the maximum of a uniform covers 0.000."
  claim_type: statistic
  evidence_needed: a fresh harness run
  source: "sh skills/statistics/verification/run.sh, run 2026-09-16, exit 0"
  source_tier: primary
  date_checked: 2026-09-16
  confidence: high
  caveats: "Monte Carlo with fixed seeds; numbers are this harness's, not
    general coverage figures."
  chapter: II.1
  citation_status: no-citation-needed
  citation_check: n/a
  drafting_status: resolved

- id: C-II-08
  claim_text: "Building the statistics table meant reading the harness output
    closely enough to notice a stray stderr line, which exposed the dead
    `grep -q '*** FAIL'` clause (Part III chapter 1)."
  claim_type: anecdote
  evidence_needed: commit record
  source: "commit f44cf86 body; skills/statistics/verification/README.md
    'Findings folded back'"
  source_tier: primary
  date_checked: 2026-09-16
  confidence: high
  caveats: none
  chapter: II.1
  citation_status: no-citation-needed
  citation_check: n/a
  drafting_status: resolved

- id: C-II-09
  claim_text: "test-writing's table: 8 rows, 5 covered, 2 judgement — both
    about choosing what to test — and one pre-ship gate row that displaces
    nothing. Behaviour 5's default fails visibly: 0.0000% of 20,000 uniform
    random inputs reach the branch under test, against 72.3% for a steered
    generator."
  claim_type: fact
  evidence_needed: the table; a fresh run
  source: "skills/test-writing/verification/README.md 'Displacement table';
    sh skills/test-writing/verification/run.sh, 2026-09-16, exit 0 (72.3150%)"
  source_tier: primary
  date_checked: 2026-09-16
  confidence: high
  caveats: "Row 3's DEFAULT is assumed, not observed (C-I-17). The third cell
    shows the pasted-output suite failing, which is true; that agents paste
    output is Kreinin's hypothesis."
  chapter: II.1
  citation_status: no-citation-needed
  citation_check: n/a
  drafting_status: resolved

- id: C-II-10
  claim_text: "directed-verification reported its own table as weak: 1
    covered, 4 judgement, 2 gaps."
  claim_type: fact
  evidence_needed: the table
  source: "skills/directed-verification/verification/README.md (rows checked
    2026-09-16)"
  source_tier: primary
  date_checked: 2026-09-16
  confidence: high
  caveats: "Its comparison figure for test-writing (6 covered) is wrong; see
    finding above."
  chapter: II.1
  citation_status: no-citation-needed
  citation_check: n/a
  drafting_status: resolved

- id: C-II-11
  claim_text: "role-deck row b1 is covered, yet the stronger premise behind it —
    that an agent would skip the work — was measured and refuted 8/8. A covered
    row shows the default procedure failing, not that agents default to it."
  claim_type: interpretation
  evidence_needed: the table + the premise fixture result
  source: "skills/role-deck/verification/README.md displacement table, row b1
    and its note; skills/role-deck/verification/premise-fixture/RESULT.md"
  source_tier: primary
  date_checked: 2026-09-16
  confidence: high
  caveats: "The interpretation (what a covered row does not prove) is the
    book's; the facts are the README's."
  chapter: II.1
  citation_status: no-citation-needed
  citation_check: n/a
  drafting_status: resolved

- id: C-II-12
  claim_text: "Of 21 skills declared `behaviour`, 8 carry a displacement table."
  claim_type: statistic
  evidence_needed: the corpus checker
  source: "python3 skills/skill-authoring/verification/check_authoring.py
    skills, 2026-09-16: behaviour=21; 10 [displacement] failures + 3 [harness]
    failures (no verification README) = 13 without a table"
  source_tier: primary
  date_checked: 2026-09-16
  confidence: high
  caveats: "Rots on every table added. The checker tests for the phrase
    'displacement table' in the README, not for a well-formed table."
  chapter: II.1
  citation_status: no-citation-needed
  citation_check: n/a
  drafting_status: draft-anyway   # until generated (same as C-I-08)

- id: C-II-13
  claim_text: "Recommendation: write the table before the prose; mark
    unfalsifiable rows judgement; log gaps as concrete harness work rather than
    fixing the prose."
  claim_type: recommendation
  evidence_needed: the practice as recorded
  source: "skills/skill-authoring/SKILL.md behaviours 2–3; docs/verifying-skills.md §7"
  source_tier: primary
  date_checked: 2026-09-16
  confidence: medium
  caveats: "Evidence is this corpus's practice (8 tables), not a comparison
    against authors who did not use the table."
  chapter: II.1
  citation_status: no-citation-needed
  citation_check: n/a
  drafting_status: resolved
```

### II.2 rows (built 2026-09-16, before drafting II.2)

Developmental note: Part III chapter 1 (bc) already closes on the practice
"Break each guard on its own", which is II.2's central move. II.2 states the
rule and points at III.1 for the story; its own practice is planting a defect
in a correct artifact. Outline correction: the "graph table: 3 caught, 2 not"
is evidence about hygiene vs truth (III.3), not about guards masking each
other; the masking evidence is the bc marker grep (C-II-15).

```yaml
- id: C-II-14
  claim_text: "A bc check run written test-first goes red on a missing file
    (exit 4), green once a true claim exists (exit 0), and a false claim prints
    its failure marker and still exits 0."
  claim_type: fact
  evidence_needed: direct measurement
  source: "re-measured 2026-09-16, bc 7.0.3 (macOS), `set -e; bc -lq checks.bc`
    over: no file → 4; `x = 2 + 2` asserted != 4 → 0; asserted != 5 → prints
    '*** FAIL: two plus two is five', exit 0"
  source_tier: primary
  date_checked: 2026-09-16
  confidence: high
  caveats: "Same measurement as C-II-03, re-run as the worked TDD case. Exit
    codes are implementation-specific; state the version."
  chapter: II.2
  citation_status: no-citation-needed
  citation_check: n/a
  drafting_status: resolved

- id: C-II-15
  claim_text: "Of 24 bc harnesses, 15 printed numbers beside prose instead of
    asserting, and only 4 would catch a wrong number. The failure-marker grep
    added in remediation never fired in 8 of 9 harnesses plus the template
    they were copied from, masked by the other two signals (pass banner, 1/0
    backstop)."
  claim_type: fact
  evidence_needed: the audit record
  source: "docs/bc-verification-audit.md (table l.68, 'Only 4 of 24' l.71,
    l.255–257); docs/verifying-skills.md §3 grep -F row"
  source_tier: primary
  date_checked: 2026-09-16
  confidence: high
  caveats: "Told in full in Part III chapter 1; II.2 uses the numbers only.
    PRECISION (audit addendum): a corrupted VALUE still failed the run (banner
    + backstop); a marker planted ALONE, other signals passing, exited 0 on
    skills/statistics. III.1 said 'a planted marker still failed the run' —
    corrected 2026-09-16."
  chapter: II.2 (also III.1)
  citation_status: no-citation-needed
  citation_check: n/a
  drafting_status: resolved

- id: C-II-16
  claim_text: "The mutation script for capsule graphs matched its target line
    literally, so a trailing evidence comment made the planted edge deletion
    silently do nothing — a mutation that reported itself as surviving."
  claim_type: anecdote
  evidence_needed: the record
  source: "docs/verifying-skills.md l.321–322; commit 904ea6a (2026-09-14)"
  source_tier: primary
  date_checked: 2026-09-16
  confidence: high
  caveats: "Told in III.3. In II.2 describe without the word 'capsule'
    (introduced III.1)."
  chapter: II.2 (also III.3)
  citation_status: no-citation-needed
  citation_check: n/a
  drafting_status: resolved

- id: C-II-17
  claim_text: "This book's own chapter-order check has a mutation script that
    breaks each gate alone; with the dependency gate disabled in the checker,
    the mutation script failed on exactly that mutation."
  claim_type: anecdote
  evidence_needed: the scripts and the run
  source: "docs/book/tools/check-intro-order-mutations.py; run 2026-09-16
    (gate disabled → '*** FAIL prerequisite introduced after its dependant',
    exit 1; restored → all caught); commit 17d5c91"
  source_tier: primary
  date_checked: 2026-09-16
  confidence: high
  caveats: "Agent-built in the same session that drafted II.2."
  chapter: II.2
  citation_status: no-citation-needed
  citation_check: n/a
  drafting_status: resolved

- id: C-II-18
  claim_text: "TDD's red step: write a failing test before the code that makes
    it pass (Beck, Test-Driven Development: By Example)."
  claim_type: fact
  evidence_needed: bibliographic record
  source: "Kent Beck, Test-Driven Development: By Example, Addison-Wesley,
    ISBN 978-0-321-14653-3 (Open Library ISBN record: title + publisher)"
  source_tier: primary
  date_checked: 2026-09-16
  confidence: medium
  caveats: "Year NOT verified: the Open Library record shows 2006, likely a
    printing; the first edition is commonly given as 2002/2003. Cite without a
    year until checked. The red step itself is common knowledge."
  chapter: II.2
  citation_status: footnote
  citation_check: likely
  drafting_status: resolved
```

### II.4 rows (built 2026-09-16, before drafting II.4; II.3 not yet drafted)

Developmental note: Part III chapter "Two premises, measured" tells both
refutations in full and closes on "Measure the sentence your skill rests on",
which is II.4's move. II.4 therefore carries the METHOD and the three INVALID
runs (not in III), retells the refutations in one paragraph, and gets its own
practice: prove the experiment can come out either way before spending a
subject.

Corpus finding (not fixed here): `claim-fixture` SKILL.md (v2.3.0) and
`references/case-studies.md` still say "four runs … two invalid … 50%
design-failure rate". b1 run 3 (RESULT3.md, af42b12, 2026-09-16) makes it five
runs, three invalid — and 2.3.0's own G9 came from run 3.

```yaml
- id: C-II-19
  claim_text: "This corpus has run five behavioural fixtures: two refuted the
    claim under test, three were invalid, and none has ever returned a
    positive."
  claim_type: fact
  evidence_needed: the run records
  source: "skills/claim-fixture/references/case-studies.md (cases 1–4);
    skills/directed-verification/verification/b1-fixture/RESULT3.md (run 3,
    commit af42b12)"
  source_tier: primary
  date_checked: 2026-09-16
  confidence: high
  caveats: "claim-fixture's own docs say four runs (stale). Rots when a sixth
    run lands."
  chapter: II.4
  citation_status: no-citation-needed
  citation_check: n/a
  drafting_status: draft-anyway   # count rots

- id: C-II-20
  claim_text: "Invalid run 1: the subject function used int(), wrong on negative
    ties, so a harness good enough to test them failed on clean code — the
    measurement inverted quality; four of five arm-B agents also hit a session
    limit, leaving n=1."
  claim_type: fact
  evidence_needed: the record
  source: "claim-fixture/references/case-studies.md §3; b1-fixture/RESULT.md"
  source_tier: primary
  date_checked: 2026-09-16
  confidence: high
  caveats: none
  chapter: II.4
  citation_status: no-citation-needed
  citation_check: n/a
  drafting_status: resolved

- id: C-II-21
  claim_text: "Invalid run 2: every control-arm subject had test-writing in
    context, a skill prescribing the discipline under test; both arms scored
    5/5. It was first reported as 'no headroom' under a pre-registered ceiling
    rule, which supplied a respectable reading of the null. The tell — five
    reports sharing a near-identical section heading — would have been caught
    by one grep."
  claim_type: fact
  evidence_needed: the record
  source: "claim-fixture/references/case-studies.md §4; b1-fixture/RESULT2.md;
    commit 3cf2da3"
  source_tier: primary
  date_checked: 2026-09-16
  confidence: high
  caveats: "Skills load from the session, not the working directory."
  chapter: II.4
  citation_status: no-citation-needed
  citation_check: n/a
  drafting_status: resolved

- id: C-II-22
  claim_text: "Invalid run 3: all fifteen subjects scored NO-HARNESS. Six ran
    with no tool permissions, so the treatment ('confirm it fails against a
    wrong implementation') could not be carried out; nine hit a session limit.
    The isolation probe had proved the environment clean; nothing proved it
    capable."
  claim_type: fact
  evidence_needed: the record
  source: "b1-fixture/RESULT3.md; commit af42b12 (claim-fixture 2.3.0 adds G9)"
  source_tier: primary
  date_checked: 2026-09-16
  confidence: high
  caveats: "D1 was a harness defect (author's), D2 a resource limit."
  chapter: II.4
  citation_status: no-citation-needed
  citation_check: n/a
  drafting_status: resolved

- id: C-II-23
  claim_text: "claim-fixture's pre-flight gate blocks run 2, as actually run, at
    G2a, G2b, G4, G8 and G9, and clears the repaired fixture."
  claim_type: fact
  evidence_needed: a fresh run
  source: "sh skills/claim-fixture/verification/run.sh, 2026-09-16, exit 0"
  source_tier: primary
  date_checked: 2026-09-16
  confidence: high
  caveats: "The gates were derived FROM these failures, so blocking them is
    expected, not a test of generality."
  chapter: II.4
  citation_status: no-citation-needed
  citation_check: n/a
  drafting_status: resolved

- id: C-II-24
  claim_text: "check_preregistration.sh passes the ordering fixture (scorer
    2b75803 twelve minutes before results da8cfa7) and permanently fails the
    premise fixture, whose scorer and results landed in one commit (1cb9ee5)."
  claim_type: fact
  evidence_needed: a fresh run
  source: "sh skills/claim-fixture/verification/run.sh, 2026-09-16"
  source_tier: primary
  date_checked: 2026-09-16
  confidence: high
  caveats: "The scorer was written first, in-session; the record cannot show it."
  chapter: II.4
  citation_status: no-citation-needed
  citation_check: n/a
  drafting_status: resolved
```

### II.3 rows (built 2026-09-16, before drafting II.3)

Developmental note: Part III chapter "A graph that could not be wrong" closes
on "Find the oracle you already have" (node text as a free independent
oracle). II.3 points there for that case; its own practice is naming the oracle
and what it shares with the subject. Evidence flag honoured: C-I-17 (expected
values copied from output) appears ONLY as the corpus's unmeasured default.

```yaml
- id: C-II-25
  claim_text: "test-writing behaviour 3 names four sources of an expected value
    — re-derivation from the spec sentence, a model-based reference, a
    metamorphic relation, differential testing against a genuinely independent
    implementation — and an independence test: does the oracle share code with
    what it judges?"
  claim_type: fact
  evidence_needed: the skill text
  source: "skills/test-writing/SKILL.md behaviour 3"
  source_tier: primary
  date_checked: 2026-09-16
  confidence: high
  caveats: "Behaviour 3's DEFAULT is unmeasured (C-I-17)."
  chapter: II.3
  citation_status: no-citation-needed
  citation_check: n/a
  drafting_status: resolved

- id: C-II-26
  claim_text: "Subject A: a discount rounded half-up; the planted bug truncates.
    At 19.90 with 15% off the exact net is 1691.5 cents, half-up 1692,
    truncated 1691. A suite built from captured output passes the bug and fails
    the fix."
  claim_type: fact
  evidence_needed: a fresh run
  source: "sh skills/test-writing/verification/run.sh, 2026-09-16, exit 0;
    verification/README.md step 1 and 'A's fourth cell'"
  source_tier: primary
  date_checked: 2026-09-16
  confidence: high
  caveats: "Demonstrates the consequence of the default, not its frequency."
  chapter: II.3
  citation_status: no-citation-needed
  citation_check: n/a
  drafting_status: resolved

- id: C-II-27
  claim_text: "Subject F: two base-conversion renderers with different
    algorithms share one defective digit helper; their diff is green over 2,000
    random pairs, and a round trip through the standard library's parser, which
    shares no code with either, catches it."
  claim_type: fact
  evidence_needed: a fresh run
  source: "sh skills/test-writing/verification/run.sh, 2026-09-16 (F row
    detects/green/misses); verification/README.md 'F's premise'"
  source_tier: primary
  date_checked: 2026-09-16
  confidence: high
  caveats: none
  chapter: II.3
  citation_status: no-citation-needed
  citation_check: n/a
  drafting_status: resolved

- id: C-II-28
  claim_text: "Two statistics checks compared a quantity with itself — one
    literally (lam/n)/(lam/n) — and printed the expected 1 by construction."
  claim_type: fact
  evidence_needed: the audit
  source: "docs/bc-verification-audit.md finding 1 (l.25–27)"
  source_tier: primary
  date_checked: 2026-09-16
  confidence: high
  caveats: "Told in Part III chapter 1."
  chapter: II.3 (also III.1)
  citation_status: no-citation-needed
  citation_check: n/a
  drafting_status: resolved

- id: C-II-29
  claim_text: "In the first real role-deck run, the evidence gathered was a
    status file last touched in July, from a process the project had abandoned;
    the code it described was a month newer. Every fact was true and the
    conclusion wrong. The proposed fix — declare authoritative sources, warn
    when a source predates what it describes — is unbuilt."
  claim_type: fact
  evidence_needed: the backlog record
  source: "BACKLOG.md l.1255–1279 (2026-09-15); Part III premises chapter"
  source_tier: primary
  date_checked: 2026-09-16
  confidence: high
  caveats: "The project is the author's private one; describe generically."
  chapter: II.3 (also III.4)
  citation_status: no-citation-needed
  citation_check: n/a
  drafting_status: resolved

- id: C-II-30
  claim_text: "The corpus's citation of Luu's eval was restated from earlier
    restatements; the article's URL had never been in the repository, and the
    first version was already overstated."
  claim_type: fact
  evidence_needed: the ledger finding
  source: "claim-ledger.md 'Finding that came out of building this ledger';
    commits 2c387db, 883c698"
  source_tier: primary
  date_checked: 2026-09-16
  confidence: high
  caveats: "Framed as an oracle problem is the book's interpretation."
  chapter: II.3
  citation_status: no-citation-needed
  citation_check: n/a
  drafting_status: resolved

- id: C-II-31
  claim_text: "test-writing was built fixture-first: its planted-bug fixture was
    committed (352703c, 11:15) before its SKILL.md (65d9656, 11:17) on
    2026-09-13. skill-authoring's rule: prose written first becomes the thing
    the fixture is bent to confirm."
  claim_type: fact
  evidence_needed: commit order; skill text
  source: "git log --diff-filter=A on the two files; skills/test-writing/
    verification/README.md 'Fixture-first'; skills/skill-authoring/SKILL.md b3"
  source_tier: primary
  date_checked: 2026-09-16
  confidence: high
  caveats: "Two minutes apart in one session: commit order shows the fixture
    was finished first, not that the prose was not being thought about."
  chapter: II.3
  citation_status: no-citation-needed
  citation_check: n/a
  drafting_status: resolved
```

### II.5 rows (built 2026-09-16, before drafting II.5)

Developmental note: II.4 closes by promising that "a refuted premise changes
what a skill is, and someone who relied on the old version needs to know. How to
record that is the next chapter." The corpus's own answer is that a refuted
premise is MINOR (role-deck 2.2.0, 2.4.0): the version counts wrong
PRESCRIPTIONS, not wrong reasons. II.5 must say that plainly rather than let the
hook imply the premise refutations were MAJOR.

Corpus findings (not fixed here; skill changes, logged in the unresolved list):
`tools/check-skills.sh` gates one clause of the changelog contract (newest
heading = `version:`). `tools/audit-changelog-levels.py`, written for this
chapter, reports the rest: three entries that do not open with their level
(directed-verification 1.1.0, 1.2.0; math-linear-algebra 2.0.1) and three
changelogs with no `## 1.0.0` heading (knap-markdown-rendering,
math-linear-algebra, math-statistics — the last two keep it as "Release 0.1",
knap has none). Zero declared/moved mismatches in 51 transitions.

```yaml
- id: C-II-32
  claim_text: "In this corpus the three version numbers mean what a reader must
    do: MAJOR, the skill was wrong, re-do work done under the old text; MINOR, a
    statement changed or grew, re-read before relying on it; PATCH, nothing."
  claim_type: fact
  evidence_needed: the policy text
  source: "docs/skill-versioning.md §1"
  source_tier: primary
  date_checked: 2026-09-16
  confidence: high
  caveats: "A policy, not an observation that it is followed; see C-II-40."
  chapter: II.5
  citation_status: no-citation-needed
  citation_check: n/a
  drafting_status: resolved

- id: C-II-33
  claim_text: "The policy exists because on 2026-09-13 two copies of the bc skill,
    the repo's and a copy in ~/.claude/skills that had drifted 29 lines
    including a correctness fix, both read version 1.0.0 with byte-identical
    descriptions."
  claim_type: fact
  evidence_needed: the recorded audit
  source: "docs/skill-versioning.md (preamble); docs/bc-verification-audit.md"
  source_tier: secondary   # the corpus's own record; the drifted copy is gone
  date_checked: 2026-09-16
  confidence: medium
  caveats: "The ~/.claude/skills copy was replaced by a symlink, so the 29-line
    diff cannot be re-run. Attribute as 'recorded', not re-measured."
  chapter: II.5
  citation_status: no-citation-needed
  citation_check: n/a
  drafting_status: resolved

- id: C-II-34
  claim_text: "A correction is MAJOR only if a published state carried the
    error. bc was committed at 13:38 on 5 September, copied for use at 13:44,
    and its portability fixes committed at 14:10; the copy served the broken
    rounding idiom for a week, so the fix is MAJOR."
  claim_type: fact
  evidence_needed: commit timestamps
  source: "docs/skill-versioning.md §2; git show 9dd8165 (13:38:11 -0500),
    ffc32ff (14:10:37 -0500)"
  source_tier: primary
  date_checked: 2026-09-16
  confidence: high
  caveats: "13:44 (the copy) and 'a week' are recorded in the doc only; git
    cannot show a copy outside the repo."
  chapter: II.5
  citation_status: no-citation-needed
  citation_check: n/a
  drafting_status: resolved

- id: C-II-35
  claim_text: "role-deck was released as 1.0.0 at 02:43 on 15 September and went
    to 2.0.0 at 08:56 the same morning, because verify reported 'run completed
    without wearing required roles' on a valid completed run of any deck whose
    required_roles is a map: set() of a dict yields its keys, card ids, which
    were compared against role names."
  claim_type: fact
  evidence_needed: changelog and commits
  source: "skills/role-deck/CHANGELOG.md 2.0.0; git fa25e11, 7304aaa"
  source_tier: primary
  date_checked: 2026-09-16
  confidence: high
  caveats: "Latent because no map-form deck had been played to a terminal.
    1.0.0 shipped with 73 assertions (CHANGELOG 1.0.0)."
  chapter: II.5
  citation_status: no-citation-needed
  citation_check: n/a
  drafting_status: resolved

- id: C-II-36
  claim_text: "When role-deck's founding premise was refuted, the bump was
    MINOR, recorded as a judgement call: 'the skill's stated REASON was wrong;
    none of its prescriptions were'. The second refutation (2.4.0) was MINOR
    too."
  claim_type: fact
  evidence_needed: changelog
  source: "skills/role-deck/CHANGELOG.md 2.2.0 (1cb9ee5), 2.4.0 (da8cfa7)"
  source_tier: primary
  date_checked: 2026-09-16
  confidence: high
  caveats: none
  chapter: II.5
  citation_status: no-citation-needed
  citation_check: n/a
  drafting_status: resolved

- id: C-II-37
  claim_text: "claim-fixture 2.0.0 was MAJOR for an omission: the method had no
    step proving the control arm did not receive the treatment, and 'any fixture
    designed under 1.0.0 needs re-checking against the new gate before its
    result is believed'."
  claim_type: fact
  evidence_needed: changelog
  source: "skills/claim-fixture/CHANGELOG.md 2.0.0 (e9f5753)"
  source_tier: primary
  date_checked: 2026-09-16
  confidence: high
  caveats: "An omission is MAJOR when results produced under the old text may
    be wrong — the 'produces an incorrect result' limb."
  chapter: II.5
  citation_status: no-citation-needed
  citation_check: n/a
  drafting_status: resolved

- id: C-II-38
  claim_text: "directed-verification 1.1.0 published run 2 as 'no headroom';
    1.2.0 corrected it to invalid (the control arm had the treatment) as a
    MINOR bump."
  claim_type: fact
  evidence_needed: changelog
  source: "skills/directed-verification/CHANGELOG.md 1.1.0, 1.2.0"
  source_tier: primary
  date_checked: 2026-09-16
  confidence: high
  caveats: "Neither entry declares its level in words (C-II-40); MINOR is read
    from the digits."
  chapter: II.5
  citation_status: no-citation-needed
  citation_check: n/a
  drafting_status: resolved

- id: C-II-39
  claim_text: "Across 53 skills the MAJOR digits sum to 27 corrections
    (MAJOR − 1), spread over 18 skills; 35 skills are still at major version 1.
    Of the 27, 9 were recorded on 13 September (the re-base, adjudicated from
    git history) and 15 on 14 September (the graph-evidence and Lean-core
    audits); 3 came afterwards."
  claim_type: fact
  evidence_needed: a count over SKILL.md and changelogs
  source: "version: fields of skills/*/SKILL.md, 2026-09-16;
    python3 docs/book/tools/audit-changelog-levels.py (24 dated MAJOR
    transitions: 13th 9, 14th 13, 15th 2) plus the three with no 1.0.0 heading,
    dated from git: math-linear-algebra and math-statistics 2.0.0 in 904ea6a
    (14th), knap-markdown-rendering 2.0.0 in ef6578b (16th)"
  source_tier: primary
  date_checked: 2026-09-16
  confidence: high
  caveats: "Rots with every bump; generate it for Part IV. The two skills at
    4.0.0 (math-number-systems, math-probability) each took 2.0.0 on the 13th
    (re-base) and 3.0.0 + 4.0.0 on the 14th (graph audit, Lean audit)."
  chapter: II.5
  citation_status: no-citation-needed
  citation_check: n/a
  drafting_status: draft-anyway   # count rots

- id: C-II-40
  claim_text: "tools/check-skills.sh gates one clause of the changelog contract,
    newest heading = version. Of the ungated clauses, an audit of 51 version
    transitions found no level that disagreed with its digits, three entries
    that do not open with their level, and three changelogs with no 1.0.0
    heading."
  claim_type: fact
  evidence_needed: the gate source and a fresh run
  source: "tools/check-skills.sh (checks 2, 6); python3
    docs/book/tools/audit-changelog-levels.py, 2026-09-16; each of its three
    rules broken alone on a synthetic changelog, each fired only its own counter"
  source_tier: primary
  date_checked: 2026-09-16
  confidence: high
  caveats: "Small, cosmetic decay; its interest is WHERE it is (ungated clauses
    only), not its size."
  chapter: II.5
  citation_status: no-citation-needed
  citation_check: n/a
  drafting_status: resolved

- id: C-II-41
  claim_text: "The count of MAJOR bumps measures how often a skill was found
    wrong, not how often it was wrong: 24 of 27 were recorded on the two days
    the corpus was systematically looked at, so a skill at 1.0.0 is either right
    or not yet examined, and the number cannot say which."
  claim_type: interpretation
  evidence_needed: C-II-39
  source: C-II-39
  source_tier: primary
  date_checked: 2026-09-16
  confidence: medium
  caveats: "The two audits targeted capsules; the 35 skills at 1.x are mostly
    methodology skills no audit of that kind has touched. Do not claim they are
    wrong — only that the number is silent."
  chapter: II.5
  citation_status: no-citation-needed
  citation_check: n/a
  drafting_status: resolved

- id: C-II-42
  claim_text: "Recommendation: bump by what the reader must do, decide whether
    the old text was ever published, keep wrong reasons separate from wrong
    prescriptions, and gate every changelog clause you want to stay true."
  claim_type: recommendation
  evidence_needed: C-II-32..41
  source: C-II-32..41
  source_tier: primary
  date_checked: 2026-09-16
  confidence: medium
  caveats: none
  chapter: II.5
  citation_status: no-citation-needed
  citation_check: n/a
  drafting_status: resolved
```

### II.6 rows (built 2026-09-17, before drafting II.6)

Developmental note: the outline's II.6 was "backed by nothing". Since then
`directed-verification` exists (6fbfac2, 2026-09-15), reported weak by its own
table (1 covered, 4 judgement, 2 gaps). II.6 must not borrow confidence the
skill does not claim. The chapter's defensible claim is the skill's own
boundary: directing changes what the director can CHECK, not how good the
agent's work is. The clean evidence about undirected agents (role-deck, 8/8
twice) cuts AGAINST a "the agent will cut corners" framing; use it that way.

Corpus finding (not fixed here; a skill change, logged in the unresolved list):
**the one covered row's detector overcounts.** `detect_selfcorrection.py`
reports 5 self-corrections on 2026-09-17. Reading each matched sentence: 3 are
real admissions (197b313, 95a8cb1, d084b25). 2 are false positives: 0fbb03c
matches a hypothetical ("whether the instruction content or the harness was
wrong"), and 6fbfac2 is the skill's OWN release commit describing what the
detector counts. Replayed at the release parent (6fbfac2^), the scan reports 3,
of which 0fbb03c is one: the "at least three" published at release rested on 2
real matches. It also misses real incidents in other words (dde3f82, the dead
marker grep; d084b25's own body calls itself "the fourth occasion"). A count
with both false positives and misses is not a lower bound. The claim ">= 3" is
true today, by hand. The self-test's negatives were four sentences the author
wrote, never the repository's own prose.

```yaml
- id: C-II-43
  claim_text: "181 of the repository's 194 commits carry a Co-Authored-By:
    Claude trailer."
  claim_type: fact
  evidence_needed: a count over git log
  source: "git log --format=%B, 2026-09-17 (HEAD 4bf0d7b)"
  source_tier: primary
  date_checked: 2026-09-17
  confidence: high
  caveats: "A missing trailer does not show a human-only commit (12 of the 13
    are one day's capsule work, 2026-09-11). Rots with every commit; say
    'at the time of writing'."
  chapter: II.6
  citation_status: no-citation-needed
  citation_check: n/a
  drafting_status: draft-anyway   # count rots

- id: C-II-44
  claim_text: "While building experience-library, the first draft of checks.bc
    hard-coded the optimum at n = 54; the true integer argmax is 55 (crossover
    at 54.05). bc printed a FAIL line and exited 1 through the 1/0 backstop, and
    the section was rewritten to find the optimum by scan rather than assert a
    remembered constant."
  claim_type: fact
  evidence_needed: the recorded incident
  source: "skills/experience-library/verification/README.md 'Findings folded
    back'; checks.bc l.88-89 comment; commit d88d272 (agent co-authored)"
  source_tier: secondary   # recorded in-build; the failing draft was never committed
  date_checked: 2026-09-17
  confidence: medium
  caveats: "The failing run is not in git history; only the record of it is.
    Say 'recorded', not 'shown'."
  chapter: II.6
  citation_status: no-citation-needed
  citation_check: n/a
  drafting_status: resolved

- id: C-II-45
  claim_text: "directed-verification's premise is that an agent asked to verify
    reports that it verified, fluently, whether the work was done well, badly,
    or not at all; so the question is what it produced that could have come
    out the other way. Six behaviours: ask for the failing case, demand an
    artifact that can fail, suspect the test first, keep proposing separate
    from deciding, re-run what you were told, check what the command was aimed
    at."
  claim_type: fact
  evidence_needed: the skill text
  source: "skills/directed-verification/SKILL.md v1.2.2"
  source_tier: primary
  date_checked: 2026-09-17
  confidence: high
  caveats: "A statement of the skill, not evidence for it; see C-II-46."
  chapter: II.6
  citation_status: no-citation-needed
  citation_check: n/a
  drafting_status: resolved

- id: C-II-46
  claim_text: "Its table is 1 covered, 4 judgement, 2 gaps. Behaviour 1, the
    most testable, has been fixtured three times and all three runs were
    invalid; it is still unmeasured."
  claim_type: fact
  evidence_needed: README table and run records
  source: "directed-verification/verification/README.md; b1-fixture/RESULT.md,
    RESULT2.md, RESULT3.md; CHANGELOG 1.2.2"
  source_tier: primary
  date_checked: 2026-09-17
  confidence: high
  caveats: "Runs already told in II.4 (C-II-20..22); cite, do not retell."
  chapter: II.6
  citation_status: no-citation-needed
  citation_check: n/a
  drafting_status: resolved

- id: C-II-47
  claim_text: "The covered row's detector reports 5 self-corrections; 2 are
    false positives, one of them the skill's own release commit. At release
    its 'at least three' rested on 2 real matches. It also misses incidents
    phrased otherwise, so the count is neither a lower bound nor an upper one."
  claim_type: fact
  evidence_needed: a fresh run, each match read in context, and a replay at
    the release parent
  source: "sh skills/directed-verification/verification/run.sh, 2026-09-17
    (5 hits); matched sentences printed per commit; scan of git log 6fbfac2^
    (3 hits: 197b313, 95a8cb1, 0fbb03c); dde3f82 as a missed incident"
  source_tier: primary
  date_checked: 2026-09-17
  confidence: high
  caveats: "The claim '>= 3 occasions' is TRUE today (197b313, 95a8cb1,
    d084b25, and dde3f82 unmatched). What fails is the instrument, not the
    conclusion. Corpus fix, not made in the book commit."
  chapter: II.6
  citation_status: no-citation-needed
  citation_check: n/a
  drafting_status: resolved

- id: C-II-48
  claim_text: "In b1 run 1, the subject function was itself wrong, and the
    defect was exposed by the subjects: arm-A agents' harnesses failed on the
    'clean' code and were scored BROKEN. The commit reporting it opens its first
    reason with 'it is mine' and calls the episode the fourth occasion where the
    test was wrong and the subject fine."
  claim_type: fact
  evidence_needed: the commit and result record
  source: "commit d084b25 (2026-09-15, agent co-authored); b1-fixture/RESULT.md"
  source_tier: primary
  date_checked: 2026-09-17
  confidence: high
  caveats: "'Mine' is the author-plus-agent session that designed the fixture;
    do not attribute it to a person or a model alone. Run 1's observation that
    undirected agents also built oracles is CONFOUNDED (subjects had the
    corpus's skills loaded; the same commit says so). Do not use it as
    evidence about undirected agents."
  chapter: II.6
  citation_status: no-citation-needed
  citation_check: n/a
  drafting_status: resolved

- id: C-II-49
  claim_text: "The agent's first reading of b1 run 2 was the agreeable one:
    1.1.0 (22:38, 15 Sept) called both arms' 5/5 'no headroom' and read five
    near-identical report headings as independent convergence on good
    practice. 35 minutes later (3cf2da3, 23:13) 1.2.0 withdrew it: the control
    arm had test-writing loaded, so the arms were one condition."
  claim_type: fact
  evidence_needed: commits and changelog
  source: "commits 23f184c, 3cf2da3 (both agent co-authored);
    directed-verification/CHANGELOG.md 1.1.0, 1.2.0"
  source_tier: primary
  date_checked: 2026-09-17
  confidence: high
  caveats: "The record does not say who spotted the tell; do not say."
  chapter: II.6
  citation_status: no-citation-needed
  citation_check: n/a
  drafting_status: resolved

- id: C-II-50
  claim_text: "role-deck's premise that an agent will skip the expensive step
    was written in agent co-authored commits (914af76, 2026-09-15) and
    fixtured and struck in agent co-authored commits (1cb9ee5, da8cfa7): 8 of 8
    fresh agents did the work unprompted, twice."
  claim_type: fact
  evidence_needed: commits
  source: "git show 914af76, 1cb9ee5, da8cfa7; Part III ch. 4 (C-III-*)"
  source_tier: primary
  date_checked: 2026-09-17
  confidence: high
  caveats: "Sessions differ; say 'the same collaboration', never 'the same
    agent'. Unaffected by the run-1/2 confound: both measured unforgeable
    artifacts."
  chapter: II.6
  citation_status: no-citation-needed
  citation_check: n/a
  drafting_status: resolved

- id: C-II-51
  claim_text: "Interpretation: the evidence this corpus has does not support
    directing verification because agents cut corners — the clean measurements
    say they did not. It supports it because agreeable prose is present in
    every case, so only an artifact that could have come out the other way lets
    the director tell good work from bad. That is the skill's own stated
    boundary."
  claim_type: interpretation
  evidence_needed: C-II-44..50
  source: "C-II-44..50; directed-verification SKILL.md 'What this cannot do'"
  source_tier: primary
  date_checked: 2026-09-17
  confidence: medium
  caveats: "Two premise fixtures are not a general finding about agents; say
    'in this corpus's two clean measurements'."
  chapter: II.6
  citation_status: no-citation-needed
  citation_check: n/a
  drafting_status: resolved

- id: C-II-52
  claim_text: "Recommendation: ask for the case that would prove you wrong and
    an artifact that could have failed; treat a result that disagrees with you
    as the valuable case; and audit the evidence FOR your collaboration
    practice with the same suspicion, including detectors that count your own
    good behaviour."
  claim_type: recommendation
  evidence_needed: C-II-43..51
  source: C-II-43..51
  source_tier: primary
  date_checked: 2026-09-17
  confidence: medium
  caveats: none
  chapter: II.6
  citation_status: no-citation-needed
  citation_check: n/a
  drafting_status: resolved
```

## Unresolved-research list

- **C-I-08** — the corpus figures rot; generate them (same mechanism as Parts IV/V).
- **C-I-09** — read the two or three closest comps before any sentence about
  what they contain.
- **C-I-10, C-I-12** — Part III needs its own ledger rows and evidence pass.
- **C-I-17** — test-writing behaviour 3's default ("expected values copied from
  the code's output") is unmeasured. Either fixture it or restate the behaviour
  as resting on Kreinin's hypothesis.
- **C-II-18** — verify the first-edition year of Beck's TDD book (Hamlet 1977
  now Crossref-verified; C-II-01 closed).
- **C-II-12** — behaviour-skill table count rots; generate it.
- **claim-fixture docs** — "four runs, two invalid, 50%" is stale; five runs,
  three invalid (run 3, af42b12). Corpus fix.
- **directed-verification README** — "test-writing at 6 covered" is 5; a
  corpus fix, not book work.
- **Part III** — reword wherever deliberate breakage reads as the corpus's
  invention; it is mutation testing.
- **Reader** — every statement of what the reader believes is the author's
  assumption (brief: accepted exception, no interviews).
- **Changelog contract (II.5, C-II-40)** — three entries do not open with their
  level; three changelogs lack a `## 1.0.0` heading. Corpus fix, and a candidate
  for `tools/check-skills.sh` (promote `tools/audit-changelog-levels.py`).
- **C-II-39** — MAJOR totals rot; generate them with Part IV.
- **C-II-47** — `directed-verification`'s self-correction detector counts 2
  false positives in 5 (one is the skill's own release commit) and misses
  incidents phrased otherwise; its README and SKILL.md call the count a lower
  bound. Corpus fix: add the repository's real matched sentences as negatives,
  exclude commits that describe the detector, and stop calling it a bound.
- **C-II-43** — the co-authored commit count rots; generate it.
