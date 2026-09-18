#import "../../preamble.typ": keyterm, headline, practice, chref

// DRAFT 2026-09-16. Ledger rows: C-II-05..13 (and C-I-17 for the running example).

= Name the default you displace <ch-default>

#headline[5 of 17][
  Rows in a verified skill whose principles rested on the skill's say-so,
  though a check could have carried them. Nothing in the skill was wrong.
]

== A verified skill, asserted on authority

// intro: statistics
`statistics` is the corpus's skill for drawing conclusions from data already
collected: which estimate, which interval, which test, and what the result
does and does not license. By every sign this corpus had, it was finished. It had, at the time,
the longest SKILL.md in the repository. It had a checking script that ran green, a row
marked #emph[verified], and numbers to show: an exact interval that covered
0.950 of the time where the textbook shortcut covered 0.880; twenty
uncorrected tests that produced a false alarm 0.638 of the time, against 0.047
with a correction.

Then someone asked a narrower question of it, one section at a time: #emph[what
does an agent do here without this section, and where do we see that go
wrong?] The answers filled seventeen rows. Seven had evidence. Five
could never have evidence, for a reason this chapter will come to. And five
could have had evidence and did not. Those five included one of the skill's
strongest warnings, that a non-significant result is not evidence of no effect.
The skill stated it. Nothing had shown it.

No sentence in `statistics` turned out to be false. That is not the finding.
The finding is that a green check and a verified label were compatible with nearly a
third of the skill resting on the author's authority, and nobody could see
which third until the question was asked row by row.

== The table

The previous chapter ended with a sentence: #emph[without this, an agent does
\_\_\_; with it, the agent does \_\_\_ instead.] A skill has more than one
section, and each section is making its own version of that claim. The
// intro: displacement-table
#keyterm[displacement table] writes them down, one row per section, in three
columns:

#table(
  columns: (1fr, 1.2fr, 1.4fr),
  inset: 6pt,
  stroke: 0.4pt + luma(170),
  table.header[*Section*][*Default it displaces*][*Where the default visibly fails*],
  [randomize structurally, and report coverage],
  [feed uniform random input and call it fuzzed],
  [0.0000% of 20,000 random inputs reach the branch under test; a steered
   generator reaches it 72.3% of the time],
)

That row is from `test-writing`, and each cell does a separate job. The first
names the section, so every section must appear. The second names the
behaviour the section exists to replace. If you cannot fill it, the section is
either a fact the agent lacks—the tool-fact case from the previous chapter,
where a table means nothing—or it is tutorial prose restating what the agent
would do anyway. The third cell points at a run where the default is seen to
fail. Not argued to fail: seen, with a number.

A row with an empty third cell is advice. It may be good advice. It is not yet
a claim anyone has checked.

== Three blocks, and the one that matters

Sort the finished rows by their third cell, and they fall into three blocks.

#keyterm[Covered]: a run shows the default failing. Nothing to do.

#keyterm[Gaps]: a run #emph[could] show it and does not yet. Each gap is a
piece of checking work, small and specific. For `statistics`, one was a single
simulation loop; one had already been demonstrated in a neighbouring skill and
never carried across.

// intro: judgement-row
#keyterm[Judgement]: no run can show it, and the reason is structural. A test
case hands the checker its subject. The steps that consist of #emph[choosing]
the subject cannot be tested by a case that has already chosen it. In
`statistics` these were deciding what quantity the question is really about,
deciding a list of assumptions is complete, routing to a method, choosing
calibrated words, and refusing to answer. In `test-writing` they were the two
behaviours about deciding what is risky enough to test.

The counts are the output. The prose around them is not. And of the three
counts, #emph[gaps] is the one that pays: it is a work list that did not exist
before the table did. `statistics` logged its five as backlog items. It did not
rewrite the skill, because nothing in the skill was wrong. What was missing was
the evidence.

Building a table has a second yield that is easy to miss. To fill the third
column for `statistics`, someone had to read the checking script's output line
by line. That is how a stray error message was noticed, and behind it a failure
check that had never been able to fire, in that script and eight
others.#footnote[The whole story is #chref(<ch-bc>).] Writing the table is a
review of the checks, not only of the document.

== Judgement is a boundary, not a loophole

The obvious way to game the table is to mark every awkward row
#emph[judgement]. The honest reply is that you can, and the table will then say
so in public.

#emph["Most of my skill is judgement."]

Then most of it is advice, and the count tells you how much. This corpus holds
// intro: directed-verification
one skill that says exactly that about itself. `directed-verification`, about
how to get an agent to check work, came out at 1 covered, 4 judgement, 2 gaps,
and its own notes call it "a weak table … reported as one." That sentence is
worth more than a padded table. A reader of the skill now knows it rests mostly
on argument. They know which one claim has evidence, and which two could have
it next.

A judgement row is not an excuse. It names where the checking stops, and it
belongs in the skill's statement of what it cannot do. Every skill has that
limit somewhere. Without the table you only gesture at it. With the table you
can list it.

== What a covered row does not prove

There is a limit to #emph[covered] as well, and it is the most important thing
in this chapter.

The third cell shows the default #emph[procedure] failing. It does not show
that agents #emph[follow] the default. `role-deck`, the card-deck skill from
#chref(<ch-claim>), has a covered row saying an agent left to itself picks its
own next step, leaving no record anyone can audit. That row has a run behind
it. The stronger claim beside it is the one #chref(<ch-claim>) already
reported: that an agent left to itself would skip the expensive step. All
eight fresh agents ran the step.

The running example has the same shape. `test-writing` row 3 says the default
is to paste in whatever the code printed as the expected value. The third cell
is solid: a suite built that way passes the bug and fails the fix. But that
agents #emph[do] this was never observed. It was a hedged remark by someone
Luu quoted and later misremembered as one of its findings.

So a full table establishes one thing: #emph[if] an agent does what the second
column says, it goes wrong. Whether agents do it is a separate claim, with its
own method. That is the subject of a later chapter in this part. The table is where you find
out which defaults you are assuming.

== How far the rule has got

This corpus adopted the rule and enforces it with a script. As of this
writing, 21 skills declare themselves behaviour skills, and 8 have a
displacement table. The other 13 fail the check.#footnote[From
`check_authoring.py`, 16 September 2026. The count changes whenever a table
is added.] That is not a
confession tucked into a chapter about the rule. It is the rule working. Before
the check existed, those thirteen skills looked just as finished as
`statistics` did.

#practice[Build the table for one skill, and count its blocks.][
  Pick a skill whose instructions tell an agent how to behave. Give each section
  one row. In the second column, write what an agent does #emph[without] that
  section. In the third, point to a run where that default fails—or write
  #emph[judgement] and one line saying why no run could show it, or leave it
  empty.

  Count the three blocks. Covered rows need nothing. Judgement rows go in
  the skill's statement of what it cannot do. Each empty third cell is a gap:
  write it down as a check to build, not as a sentence to rewrite.

  Last, read the second column again and mark each default you have actually
  seen an agent do. The unmarked ones are assumptions.
]

The third column asks for a run in which a default visibly fails. Whether the
run itself is capable of failing is the next chapter.
