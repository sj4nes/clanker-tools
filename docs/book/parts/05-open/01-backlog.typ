// GENERATED FILE — DO NOT EDIT.
//   source:    BACKLOG.md  (the open `- [ ]` items only)
//   generator: docs/book/tools/gen-open.py
//   gate:      docs/book/tools/check-book.sh  (regenerates and diffs)
// Edit BACKLOG.md, or the generator; an edit here is reverted by the gate.

#import "../../preamble.typ": note, backlogitem, points

#note[46 open items, read from #raw("BACKLOG.md") at generation time and grouped by the domain they sit under. The count is not a burndown: an item closes when the work is done, and new ones are opened by the audits of Part III.]

= Physics

#note[5 open.]

== physics-formula-atlas  (new bridge capsule — Release 0.1 COMPLETE, 2026-09-11)

#backlogitem(none, none)[
  Release 0.2 — extend to #raw("chemistry-foundations") and #raw("chemistry-electrochemistry") (both already claim #raw("physics-thermodynamics") as background in prose; roughly doubles the capsule count and the discharge-audit work).
]
#backlogitem(none, none)[
  discharge each physics capsule's bare #raw("derivative")/#raw("integral") math primitives against #raw("math-real-analysis") (flagged in #raw("validation/duplicate-primitives.md")'s "Known limitation" — mirrors what the #raw("math-*") capsule stack already does internally).
]
== physics-thermodynamics

#backlogitem(none, none)[
  Release 0.2 scope expansion — open systems and chemical potential (#raw("dG = −S dT + V dP + μ dN")), phase equilibria + Clausius–Clapeyron, a real-gas node (van der Waals) as the correction the ideal-gas model omits. (#raw("scope.md") "Excluded" list)
]
#backlogitem(none, none)[
  per-node detail pages (#raw("nodes/<id>.md")) — the capsule currently collapses to the formula view; promote the 15 #raw("draft") derived-formula nodes to #raw("reviewed") with per-node #raw("bc")/#raw("lean") cross-checks.
]
#backlogitem(none, none)[
  cross-capsule — #raw("physics-thermoacoustics") re-declares ideal-gas + first/second-law + entropy primitives; replace with #raw("requires") edges into this capsule's developed nodes (0.2, mirrors the #raw("math-*") stack pattern).
]

= Mathematics

#note[5 open.]

== math-statistics  (Release 0.1 COMPLETE, 2026-09-08)  +  statistics

#backlogitem([statistics → verification: the 5 gaps from the §7 displacement table], none)[
  (2026-09-13). The table came out #strong[7 covered / 5 judgement / 5 gaps]; no #raw("SKILL.md") claim was found #emph[wrong], but five rest on the skill's authority where the harness could carry them. Each is a concrete section, cheap:

  #points(
    [
      #strong[CI/test duality] — the #raw("n = 5") t-interval must exclude #raw("mu_0") exactly when the level-α test rejects, over many samples. Exact; reuses step 2's sampler. (Principle: #emph[report the interval, not a bare p].)
    ],
    [
      #strong[p-value uniformity under the null] + power ≈ 0.2 at a plausible effect at small #raw("n"). One MC loop. (Principle: #emph[a non-significant result is not evidence of no effect] — currently the skill's strongest claim with no local evidence at all.)
    ],
    [
      #strong[pseudoreplication] — clustered data analysed at the observation level inflates the FPR.

      #strong[Already demonstrated in #raw("design-of-experiments")] (#raw("0.29") vs #raw("0.06")) and never ported; cite it or port it.
    ],
    [
      #strong[prior sensitivity] — the same data under two defensible priors at small #raw("n"), posterior interval moving materially. Conjugate Beta–Binomial, closed form.
    ],
    [
      #strong[regression as projection] — there is no regression case anywhere in the harness. The one row at risk of being tutorial prose rather than a gap: if no case is added, shrink the principle to a pointer into the capsule.
    ],
  )

  Table lives in the new #raw("skills/statistics/verification/README.md") (which did not exist — a §6 violation, now fixed).
]
== math-linear-algebra  (new capsule — Release 0.1 COMPLETE, 2026-09-13)

#backlogitem(none, none)[
  Release 0.2 — prove the Jordan normal form via cyclic subspaces (currently a #raw("draft") boundary node, prerequisites developed); tensor/exterior algebra (which would demote the determinant's alternating-form definition from definition to consequence); modules over a PID.
]
#backlogitem(none, none)[
  discharge the three stack-internal cited roots — #raw("real_number") against #raw("math-number-systems"), #raw("compactness_cited") and #raw("extreme_value_cited") against #raw("math-real-analysis"). (#raw("complex_number"), #raw("polynomial_ring"), and #raw("fundamental_theorem_of_algebra") are genuine gaps with no capsule in the stack; FTA is the capsule's largest cited dependency.)
]
#backlogitem(none, none)[
  #raw("upmd") tutorial via #raw("theorem-tree-tutorial") — the #raw("field_scope") tag is a natural beat (run the same statement over R and over F\_2 and watch it break), as is the paired orthogonal-vs-oblique projection Lean check.
]
== math-logic-and-proof

#backlogitem(none, none)[
  Mathlib-backed completeness formalisation — connect #raw("godel_completeness_theorem") to #raw("Mathlib.ModelTheory") (#raw("FirstOrder.Language") + its completeness development) and upgrade #raw("lean_status") from #raw("cited") to #raw("mathlib_cited") where the kernel actually verifies the link. Also #raw("post_completeness_theorem") for a countable atom set is feasible in plain Lean (Lindenbaum by #raw("Nat")\-recursion + LEM, truth lemma by structural induction — no Mathlib). (#raw("validation/proof-checks.lean"), #raw("validation/proof-checks.md"))
]

= Chemistry

#note[10 open.]

== chemistry-foundations  (Release 0.1 COMPLETE, 2026-09-09; 113 nodes, all draft)

#backlogitem(none, none)[
  the review pass — all 113 nodes are still #raw("status: draft") in #raw("nodes/nodes.tsv"). Release 0.1 was declared complete with no node ever reviewed, which is the capsule-scale version of a check that cannot fail: the status column has only ever held one value, so nothing distinguishes a reviewed node from an unreviewed one. (#raw("validation/consistency-audit.md"))
]
#backlogitem(none, none)[
  promote #raw("ideal_gas") to a first-class assumption node — it is currently prose inside the #raw("bridge_imported") #raw("ideal_gas_law") entry, so every gas-law dependent lacks the explicit edge that #raw("dilute_ideal_solution") gets. An assumption that is prose rather than a node is invisible to the graph audit that found the 2 missing edges in #raw("3.0.0"). (#raw("validation/consistency-audit.md"))
]
#backlogitem(none, none)[
  per-node detail pages under #raw("nodes/"), plus #raw("formulas/*.yaml") structured entries and #raw("sources/source-map.tsv") — primitives and conventions currently live in #raw("conventions.md") and formula nodes in #raw("formulas/chemistry-foundations.md"). The #raw("math-*") capsules have all three.
]
#backlogitem(none, none)[
  upgrade the Lean instance checks to universal #raw("by ring") / #raw("by nlinarith") proofs once Mathlib is on the toolchain. The lean-core audit (#raw("docs/lean-core-audit.md")) counts a numeral-instance check as unbacked, and this capsule has 1 Lean core.
]
== chemistry-electrochemistry  (Release 0.1 COMPLETE, 2026-09-09; 112 nodes, all draft)

#backlogitem(none, none)[
  the review pass — all 112 nodes are still #raw("status: draft"). (#raw("validation/consistency-audit.md"))
]
#backlogitem(none, none)[
  import the electrical primitives properly — #raw("electric_charge") / #raw("electric_current") / #raw("electric_potential") / #raw("electrical_work") / #raw("electrical_power") / #raw("resistance") / #raw("ohms_law") are a root set here and should be owned by a #raw("physics-circuits") capsule. This is the same undischarged-root shape #raw("physics-formula-atlas") was built to audit, and no atlas edge reaches chemistry yet (see the atlas Release 0.2 item under Physics).
]
#backlogitem(none, none)[
  promote the embedded assumptions to nodes — #raw("298.15 K"), #raw("ideal_gas") for electrolysis products, #raw("α ≈ 0.5") (transfer coefficient), ideal membrane selectivity.
]
#backlogitem(none, none)[
  per-node detail pages, #raw("formulas/*.yaml"), #raw("sources/source-map.tsv"); and upgrade the Lean instance checks to universal #raw("by ring") proofs with Mathlib.
]
== chemistry — cross-capsule

#backlogitem([chemistry], none)[
  neither capsule is reachable from #raw("physics-formula-atlas"), though both claim #raw("physics-thermodynamics") as background in prose. Tracked as the atlas's Release 0.2 under Physics; noted here because the undischarged roots are on this side.
]
#backlogitem([chemistry], none)[
  capsules have no displacement-table analogue. §7 of #raw("docs/verifying-skills.md") gives behaviour skills a table whose gap count is the deliverable; a capsule's equivalent question — which claims rest on the capsule's authority rather than on a check that could fail — has no artifact. The chemistry capsules are the cheapest place to try one, because their Lean cores are instance checks and their #raw("status") column has never moved off #raw("draft").
]

= Analysis & inference methodology

#note[3 open.]

== simulation

#backlogitem(none, none)[
  Extend #raw("verification/") beyond the M/M/1 DES case — one continuous-time (analytic ODE benchmark) and one Monte Carlo (dependence / tail-risk) worked check would cover more of the paradigm table.
]
== visualization-design

#backlogitem(none, none)[
  extend #raw("verification/") with a diagram-grammar check (parse a Mermaid/DOT source, confirm every edge style has a declared meaning in a legend node).
]
== unknown-discovery

#backlogitem(none, none)[
  worked end-to-end example — take one messy decision (capacity commitment or a post-release metric drop) through steps 1–9: charter → epistemic map → ranked assumptions → premortem + ACH → signal cards → VoI-ranked backlog → forecast ledger → monitoring plan; #raw("check.py") recomputes the EVPI / Brier / diagnosticity claims, wired into #raw("run.sh").
]

= Engineering practice

#note[1 open.]

== test-writing  (new skill — promoted 2026-09-08 from BACKLOG-BACKLOG)

#backlogitem([methodology-skill-builder (BACKLOG-BACKLOG)], none)[
  when built, it must #emph[emit] the §7 displacement table as a required artifact, and refuse a section that neither displaces a nameable default nor declares itself judgement. Row annotated.
]

= Tutorials

#note[3 open.]

== formula-tree-tutorial

#backlogitem(none, none)[
  the 5 physics tutorials have no hook paragraph. #raw("pendulum"), #raw("why-heat-engines-have-a-ceiling"), #raw("how-fast-does-sound-travel"), #raw("designing-an-organ-pipe") and #raw("horns-and-reciprocity") go straight from the provenance blockquote to #raw("## How to run this"), so a reader browsing has nothing telling them what the tutorial is for. All 19 chemistry and math tutorials open with one. Found 2026-09-17 by #raw("docs/book/tools/gen-tutorials.py"), which generates Part VI of the book and has to print "no lead paragraph" for exactly these five. Either add the hook to each, or make it a required beat in the skill so the next one cannot ship without it — the second is the reason this sits under the skill rather than under the capsules.
]
== theorem-tree-tutorial  (new meta skill — started 2026-09-06)

#backlogitem(none, none)[
  decide the "one skill or two" question (#raw("docs/tutorial-map.md") §7) — whether to merge with #raw("formula-tree-tutorial") into #raw("capsule-tutorial") once both are exercised.
]
#backlogitem(none, none)[
  settle the cross-capsule #raw("deps:") convention before any Tier-4 (discharge-chain) tutorial — #raw("docs/tutorial-map.md") §7.
]

= Cross-cutting

#note[3 open.]

#backlogitem([user-level symlinks are absolute], none)[
  (#raw("/Users/sjanes/work26/clanker-tools/...")) because #raw("~/.claude/skills") cannot use a relative path into the repo. They break if the repo moves or is renamed. Note it in the README's setup section, or provide an install script that rewrites them.
]
#backlogitem([displacement tables, retro-fit], none)[
  #raw("docs/verifying-skills.md") §7 now requires one per behaviour-modification skill, and exactly one skill has one (#raw("test-writing"), where the rule was derived). A repo-wide rule that only the newest skill follows is not a rule. #raw("statistics") done 2026-09-13 (#strong[7 covered / 5 judgement / 5 gaps]; gap list in the math-statistics section). n=2 changed the rule twice: §7 now classifies #strong[sections, not skills] (#raw("statistics") is a nudge skill holding two legitimate reference tables), and requires the covered/judgement/gaps counts as the reportable output. Building it also found the dead #raw("grep -q '*** FAIL'") clause, so the table doubles as a review of the harness. Retro-fit the rest, in descending order of expected yield — the long ones are where tutorial prose hides: #raw("nonfiction-book"), #raw("agent-automation"), #raw("unattended-automation"), #raw("local-first-backup"), #raw("simulation"), #raw("design-of-experiments"), #raw("control-systems"), #raw("unknown-discovery"), #raw("temporal-data-modeling"), #raw("hypergraph-reasoning"), #raw("causal-sandbox"), #raw("skill-evolution"), #raw("citation-check"), #raw("simple-technical-english"). Expect the table to surface (a) sections displacing nothing nameable → move to #raw("references/"), and (b) #raw("judgement") rows currently written as though the harness covered them. Do #strong[not] apply it to the tool-fact skills (#raw("bc"), #raw("ed"), #raw("csplit"), #raw("tsort"), #raw("ptx"), #raw("octave"), #raw("uv"), #raw("typst")) — §7's two-column distinction exists precisely to protect their reference tables, which are the payload, not padding.
]
== octave  (new skill — built 2026-09-13)

#backlogitem(none, none)[
  consider a second consumer — #raw("math-statistics")' Gaussian linear model block (hat matrix, Cochran, ANOVA decomposition) is matrix content currently checked only at the 3-point design in #raw("bc").
]

= Skill standard & verification debt

#note[16 open.]

#backlogitem([evaluator-integrity], [2026-09-14])[
  five harness gaps from the displacement table (#raw("skills/evaluator-integrity/verification/README.md"))

  #points(
    [
      an evaluator-CALL budget section, showing a loop that wins on query count alone at equal compute (b2 claims call-matching; only attempt-matching is demonstrated)
    ],
    [
      early stopping on the reporting set, a different leak channel from the argmax selection already covered (b3)
    ],
    [
      coupled solver+evaluator co-evolution, where BOTH move and attribution fails — the paper's central L5 problem, and b5's "hold one fixed" has no fixture
    ],
    [
      anchor noise, a small/noisy anchor producing a wrong ACCEPT, where the harness supplies a perfect anchor by construction
    ],
    [
      protocol-link families (#raw("references/headroom-index.md") §1) — the rule gating whether two scores may be pooled at all is unchecked and sits upstream of every verified formula.
    ],
  )
]
#backlogitem([experience-library], [2026-09-14])[
  four harness gaps from the displacement table (#raw("skills/experience-library/verification/README.md"))

  #points(
    [
      cross-executor transfer (b6): no fixture plants an artifact that helps executor A and HURTS executor B, which is exactly the claim
    ],
    [
      the promotion gate (b1): "a tool is admitted only after it compiles and runs" has no fixture, and the recurrence criterion is unmodelled
    ],
    [
      activation and execution as interventions (b5): #raw("bc") §5 supplies the three factors rather than generating them from a realistic retrieval or instruction-following failure
    ],
    [
      staged admission (b2): HDSO runs the comparison in stages of increasing size, the harness runs one fixed-n comparison, and the sequential multiplicity is unmodelled — #raw("evaluator-integrity")'s look-count sweep suggests it is not small.
    ],
  )
]
#backlogitem([role-deck: the #raw("improve") deck (TBD).], [2026-09-15])[
  The RSI loop — diagnose the bottleneck, propose, verify, retain, revise the improver — is the one goal shape this machinery structurally CANNOT express. L5 means the process revises itself, and every gate assumes the deck is fixed for the duration of a run: exhaustive enumeration, exact path probability, the budget look-ahead and #raw("preserve_exit") all depend on a static rulebook. Supporting it is not a feature but a different architecture (a deck that emits a successor deck, with the gates re-run on the successor and some inheritance rule between them). Note the irony for the record: this whole line of work started from an RSI survey, and the RSI loop is the shape it cannot model.
]
#backlogitem([role-deck: four remaining verification gaps], [2026-09-15])[
  (was five; the founding premise closed above)

  #points(
    [
      the reroll log is claimed as a behavioural signal and never exercised
    ],
    [
      #raw("terminal-live") and #raw("options-sweep") have no isolating mutation, so neither has been seen to fail alone
    ],
    [
      the #raw("die") gate has never fired on a real bias
    ],
    [
      #raw("decide")'s #raw("expected_order") has no regression mutation, where #raw("diagnose")'s does.
    ],
  )
]
#backlogitem([role-deck: nothing sizes the question to the budget.], [2026-09-15])[
  Found by the first real run of the #raw("diagnose") deck (StructOrder drift, 2026-09-15). The #raw("open") card asks for a #raw("stop_condition") and nothing anywhere checks it is REACHABLE within the budget. The run scoped "a per-capability inventory across all the brief's must-ship claims" and 11 budget bought depth on one capability; the mismatch only became visible at the exit, where it had to be confessed in #raw("residual_uncertainty") rather than fixed. Mostly a judgement gap — a stop condition is prose and no gate can read it — but two parts are mechanical and worth doing: (a) #raw("next") already prints #raw("spent")/#raw("budget") and should also print the FLOOR and the remaining play headroom, so the author sizes the question against what is actually left; (b) the #raw("open") card's brief should say so explicitly. Note the shape: this is the same class as the founding-premise gap — the deck constrains execution well and says nothing about whether the question was the right size to ask.
]
#backlogitem([role-deck: an instrument can be aimed at a corpse, and nothing catches it.], none)[
  Found by the first real #raw("diagnose") run (StructOrder, 2026-09-15), where it cost the entire recommendation. Grounding worked perfectly: three commands ran, output captured, hashed, replay-verified, nothing fabricable. And it was worthless, because the WHITE hat gathered #raw("_bmad-output/sprint-status.yaml") (last touched 2026-07-29, commit message "wip lots of weird lol") and the brief's Current Build State block — both artifacts of a process the project had ABANDONED in favour of #raw("kata"). The code they described was a month newer. The facts gathered were true and the conclusion drawn from them ("the tracker is stale, update it") was wrong, because the tracker had already been replaced. An authoritative-LOOKING dead file is indistinguishable from a live one at the instrument layer.
]
#backlogitem([claim-fixture: the method has never returned a POSITIVE.], [2026-09-15])[
  Both case studies refuted their claims (8/8 each) \[one is 3/8 proven, F10\]. Nothing demonstrates the method can confirm a true claim rather than being biased toward refutation — possibly because the fixtures are built by someone motivated to be thorough, possibly because both claims were simply false. The control is a fixture against a default that is already known real: danluu's eval (cited by #raw("test-writing")) found agents fall back to poor default testing across all 26 conditions \[overstated: across the techniques named\], so a fixture reproducing that shape SHOULD come back positive. If it does not, the method is broken rather than the claims being false, and every result from it is suspect.
]
#backlogitem([claim-fixture: subject naivety is asserted, not verified.], [2026-09-15])[
  Both case studies used fresh agents with filesystem access to a repo documenting the hypotheses under test. Unforgeable scoring means priming could not fake a result, but nothing measured whether subjects read that material, and a primed subject inflates a positive. Options: run subjects in a directory with no repo access, or instrument what they read.
]
#backlogitem([NEW SKILL: #raw("skill-authoring") — the standard this corpus enforces is not itself invocable.], [2026-09-15])[
  Found by building the book's fat outline as a concept dependency graph (#raw("docs/book/outline/")): of the 23 concepts the book needs, #strong[10 are backed only by #raw("docs/")] — displacement table, judgement row, harness shape, negative contrast, guard isolation, skill taxonomy, version-as-wrongness, changelog. 889 lines of standard governing 50 skills, cited by 3 of them and loadable by none. There is a meta-skill for building a physics capsule, a math capsule and a tutorial from a capsule, and none for authoring a skill to the standard every skill here is held to. #raw("tsort") puts #raw("authoring-to-the-standard") at position 21 of 23 — it depends on nearly everything, which is why it keeps being re-explained by hand. Absorbing the ten docs-only concepts is the largest single payoff available in the corpus.
]
#backlogitem([NEW SKILL (or a section of the above): the collaboration itself.], [2026-09-15])[
  Three concepts have no source at all and they cluster on the book's own stated differentiator: #raw("agent-as-collaborator") (the agent as participant in quality, not producer of text), #raw("directing-verification") (getting an agent to build the harness, plant the defect, run the fixture, and report what it found AGAINST you), and #raw("authoring-to-the-standard"). Fifty skills, every one of them produced by a human and an agent working together, and not one skill about doing that. Same shape as the refuted premises: the thing most relied on was the thing never written down. Decide whether it is a distinct workflow or a chapter of #raw("skill-authoring").
]
#backlogitem([Corpus remediation: 35 archetype-standard failures across 29 skills.], [2026-09-15])[
  Found by #raw("skills/skill-authoring/verification/check_authoring.py") on its first run, and gated by a RATCHET (#raw("baseline.txt")) so the count cannot grow while remediation proceeds. By gate: #strong[13 #raw("scope")] — descriptions stating no boundary at all, so nothing says where the skill stops applying (ed, tsort, uv, math-linear-algebra, math-real-analysis, math-sets-functions-cardinality, math-theorem-tree, physics-acoustics, physics-formula-tree, physics-newtonian, physics-thermoacoustics, formula-tree-tutorial, theorem-tree-tutorial); #strong[10 #raw("displacement")] — behaviour skills with no displacement table, because §7 was applied going forward and never backfilled; #strong[9 #raw("frontmatter")] — missing #raw("author:") or #raw("tags:"); #strong[3 #raw("harness")] — verification/ with a run.sh and no README.md, which is a §6 violation of the same kind #raw("statistics") had. Remediation lowers baseline.txt. Note the ratchet's known weakness: it cannot distinguish "fixed two, broke two".
]
#backlogitem([#raw("directed-verification") b1: TWO INVALID RUNS — run 3 blocked on ARM ISOLATION 2026-09-15.], [2026-09-16])[
  The claim (an agent asked to "verify this" produces a weaker artifact than one asked to "make this able to fail") is unmeasured, and neither attempt tested it.

  #strong[Run 1 INVALID] — the subject function was buggy, so a good harness failed on the clean implementation and scored BROKEN (#raw("skills/directed-verification/verification/b1-fixture/RESULT.md")).

  #strong[Run 2 INVALID] — the CONTROL ARM RECEIVED THE TREATMENT. Every arm-A subject had #raw("test-writing") in context, whose behaviour 1 prescribes the same thing; their transcripts quote #raw("test-writing/SKILL.md") lines 37 and 48 verbatim. Δ = 0 was structural, not a ceiling (#raw(".../RESULT2.md"), which records the superseded "no headroom" reading and the correction). The run-1 fixes all held — clean=0 asserted by a 28,824-case #raw("Fraction") oracle, n=5 per arm, interleaved spawn. What failed is the assumption that running subjects in a different WORKING DIRECTORY isolates them from the corpus. It does not; skills load from the session.

  #strong[Run 3 preconditions, in order — do not spawn subjects until 1 and 2 are solved:]

  #points(
    [
      a genuinely clean control environment with none of this corpus's skills in context
    ],
    [
      a MANIPULATION CHECK run before scoring, grepping each subject's context and transcript for the treatment's fingerprints, which invalidates the run if arm A shows them
    ],
    [
      only then the plant question — whether a defect a competent undirected suite genuinely misses can be built, which probably means leaving self-contained pure functions behind. Still #raw("claim-fixture")'s best candidate for a first POSITIVE — and note that method has now produced two refutations, two invalid runs, and zero confirmations.

      #strong[#raw("claim-fixture") needs its own review]: it caught the run-1 defect (buggy subject) via a precondition, but had nothing to say about a contaminated control, and a pre-registered ceiling rule actively CONCEALED the contamination by supplying a respectable reading of the symptom. A manipulation check belongs in #raw("claim-fixture") itself, not just in this fixture.

      #strong[DONE 2026-09-15] — #raw("claim-fixture") 2.0.0 adds behaviour 3, #raw("references/pre-flight.md") (7 gates, each derived from a named failure), and #raw("verification/preflight.sh"), which blocks the b1 fixture at G2a, the gate that caused its failure. Run 3 must clear the gate before subjects are spawned. (2026-09-15)

      #strong[PRE-REGISTERED 2026-09-16, NOT YET RUN (#raw("c60a32d")).] All three preconditions are now met and #raw("design3.md") clears all seven gates.

      #points(
        [
          Isolation: subjects are Bash-invoked separate #raw("claude -p --disable-slash-commands") processes outside the repo, verified by #raw("check_isolation.sh") to see ZERO skills.
        ],
        [
          Manipulation check: arm A transcripts grepped against #raw("fingerprints.txt"), ordered before the bands, contamination VOIDS.
        ],
        [
          The plant question is answered by dropping the single plant: the measure is now a KILL RATE over a frozen 20-mutant set, so the run no longer depends on guessing the one defect an undirected agent misses. The subject (#raw("subject3/"), a duration parser/formatter) keeps its intent in a separate #raw("SPEC.md") and carries no worked examples — run 2's docstring spelled out the discriminating case for the subject to read. A third arm C (handed the risky areas) is the positive control; if C does not beat A by +0.20 the run is UNINTERPRETABLE and no Δ is reported.

          #strong[RUN 3 SPENT AND INVALID 2026-09-16 (#raw("5d73988"), #raw("b1-fixture/RESULT3.md")).] All 15 subjects scored #raw("NO-HARNESS"). Two unrelated defects, neither about the subjects: 6 ran with every #raw("Write") and every #raw("python3") refused by the permission layer (#raw("claude -p") is non-interactive, no approval flow), and 9 hit an account session limit. #raw("run3.sh") had launched subjects with NO TOOL PERMISSIONS. The isolation probe passed — it proved the environment CLEAN, and nothing asked whether it was CAPABLE. Because arm B's treatment #emph[is] an instruction to execute, an incapable environment makes the treatment undeliverable and Δ is structurally zero regardless: run 2 turned the control into the treatment, run 3 turned the treatment into the control. Fixed: explicit identical toolset per arm, #raw("claim-fixture") G9 + #raw("check_capability.sh") before spawning, and attrition no longer written as #raw(".done") (a session-limit stub used to be, so a resumed run would have skipped the 9 that never ran).

          #strong[Confirmed working, and worth keeping:] run 2's contamination is gone (probe saw #raw("NONE"), all 5 arm-A transcripts clean), interleaving held (the limit truncated all three arms equally, vs run 1 losing 4 of 5 arm-B), and #raw("NO-HARNESS") staying distinct from #raw("0 killed") is the only reason the failure was legible at all.

          #strong[HELD 2026-09-16 at the user's direction] — the account hit its API limit, and a run 4 waits on a more cost-effective approach. Before spending 15 again: run an n=1-per-arm pilot end to end first. Three runs have now died to harness defects a 3-subject pilot would have exposed.
        ],
      )
    ],
  )
]
#backlogitem([#raw("claim-fixture") owes a POSITIVE CONTROL of itself.], [2026-09-16])[
  Four runs: two refutations, two invalid, ZERO positives. \[Now five runs, three invalid, still zero positives — 2026-09-17.\] The method has never detected an effect it knew was there, so its sensitivity is untested and its two refutations are weaker than they look — G4 demands a positive control of every fixture it gates, and the method does not have one. Cheapest form: a fixture whose treatment has a known large effect (subjects handed the answer vs not), run through the full apparatus. Until it exists, every #raw("claim-fixture") refutation should be read as "no effect detected by an instrument of unknown sensitivity". (2026-09-15)

  #strong[PARTIALLY ADDRESSED 2026-09-16 (#raw("c60a32d")), at the instrument level only.] b1 run 3 carries two positive controls. The INSTRUMENT one is already measured, before any subject exists: #raw("score3-check.sh") scores a two-assertion suite at 4/20 and an oracle-based suite at 20/20, so the scorer has a demonstrated dynamic range of 16 mutants. The SUBJECT-level one is arm C — an agent handed the risky areas — and it is #strong[not yet measured], because run 3 has not been spawned. This item does not close until arm C beats arm A in a real run. Note the distinction is the whole point: an instrument that separates a known-weak artifact from a known-strong one still says nothing about whether a POPULATION of agents moves under a prompt.

  #strong[Still unmeasured after run 3] — arm C was spawned but produced nothing, for the same harness reason as arms A and B.
]
#backlogitem([Drafting prose for an outside reader is an unnamed verification technique.], none)[
  Three corpus defects were found not by running a harness but by writing the book chapter about the skill: #raw("directed-verification")'s self-correction count held two false positives, one of them the skill's own release commit (#raw("8097530")); #raw("skill-authoring") carried two stale statements and a proposed check silent for 17 of 21 skills (#raw("b3ad6e6")); and the corpus's one external citation had drifted from its source in four places (#raw("a92cc8f")). In each case the defect survived the skill's own verification and did not survive having to state the claim precisely enough for a reader who cannot see the repository. #raw("docs/verifying-skills.md") does not name this, and the standard has no step for it. Decide whether it is a behaviour of #raw("skill-authoring") ("write the paragraph you would publish about this skill, then check it"), or a note that the audience is the instrument. Record 2026-09-17; instances tracked in #raw("docs/book/sidebars.md").
]
#backlogitem([#raw("test-writing") states a displacement table but not its counts.], none)[
  #raw("docs/verifying-skills.md") §7 calls the counts "the deliverable, not the prose", and names #raw("test-writing") as the worked example of the rule — but its #raw("verification/README.md") gives the eight rows and then says "Two of the eight rows are #raw("judgement")" in prose, with no #raw("**N covered · N judgement · N gaps**") line. Every other skill that has a table reports one. Found 2026-09-17 by #raw("docs/book/tools/corpus.py"), which parses the counts for Part IV of the book and had to print "a displacement table, but its counts are stated in prose rather than reported" for the one skill the rule points at. Add the line (6 covered, 2 judgement, 0 gaps, if the prose is right).
]
#backlogitem([Re-run the #raw("role-deck") premise fixture with subjects that cannot read the repository], [2026-09-17])[
  (planned week of 2026-09-21). The first run scored 8/8 EXECUTED but proved 3/8: #raw("score.py") accepted strings that #raw("docs/verifying-skills.md") and #raw("dde3f82") already held (claim-fixture F10, role-deck 2.5.0, book ledger C-III-18). Before spending subjects: run the isolation and capability probes (G2, G9), and apply G5 as rewritten — search the subjects' whole readable environment for every pattern the scorer accepts. Pilot n=1 first, per the run-3 note. If it comes back REFUTED, restore 8/8 in role-deck, claim-fixture case study 1, the research note and the book; if weakly supported, the premise was struck on too little and SKILL.md's rationale needs revisiting.
]

