#import "../../preamble.typ": keyterm, headline, practice, chref
#import "../../corpus-facts.typ": corpus-asof, n-behaviour, n-capsule, n-meta, n-skills, n-tool-fact

// DRAFT 2026-09-17. Ledger rows: C-II-53..62.

= Author a skill to the standard <ch-author>

#headline[2 of 21][
  Behaviour skills whose history shows the check written before the prose.
  Seventeen arrived in a single commit, including the skill that requires the
  check to come first.
]

== A blank page

Each chapter in this part made one move on a skill that already existed. You
named its default, broke its harness, found its oracle, measured its premise,
and versioned its mistakes. Now there is no skill yet. There is an idea, and a
blank file called `SKILL.md`.

The moves do not change. What is new is that you choose their order. The
corpus has a skill for this,
// intro: skill-authoring
`skill-authoring`, written to make the standard invocable instead of leaving it
in 889 lines of documentation. This chapter follows that skill, and it says
where the evidence disagrees with it.

== First, decide which standard applies

// intro: skill-taxonomy
Not every skill owes every move. A skill that teaches a command-line tool's
quirks has no wrong default to displace. The model simply does not know the
quirks, which is the tool-fact case from #chref(<ch-claim>). Demanding a
displacement table from it produces a table of empty cells, and a reputation
for bureaucracy. So the first move is to declare the skill's #keyterm[archetype]:

#figure({
  set par(justify: false)
  table(
    columns: (auto, 1fr, 1fr),
    align: left,
    stroke: 0.5pt + luma(180),
    inset: 6pt,
    table.header[*Archetype*][*What the agent brings*][*What the skill owes*],
    [behaviour], [A default, and it is wrong.],
      [A harness and a displacement table.],
    [tool-fact], [Nothing. The prior is empty.],
      [Reference material. A table would be meaningless.],
    // not-a-use: knowledge-capsule — the archetype's label, glossed in its own row; Part III treats capsules
    [capsule: a curated body of knowledge], [—],
      [A build and a validation of the knowledge it holds.],
    [meta], [—], [The names of the skills it drives.],
  )},
  caption: [The four archetypes in `skill-authoring`, and what each owes.],
)

Every requirement in this book is conditional on that one field. Before the
field existed, no check could tell which requirements applied, so no check
could enforce any of them. When the field was added to the corpus, the checker's
first run found 35 failures across 29 of the 51 skills the corpus held then. Two of the first
corrections went to the checker itself. Its test for a stated boundary accepted
only the word #emph[NOT], so 12 of its first 25 complaints were about
descriptions that said #emph[excludes] instead. That is #chref(<ch-agent>)'s
lesson on a new instrument: suspect the check first.

// not-a-use: knowledge-capsule — the archetype label again, as counted by the checker
As of #corpus-asof, the corpus's #n-skills skills declare #n-behaviour behaviour, #n-capsule capsule,
#n-tool-fact tool-fact and #n-meta meta, and the checker reports 34 failures across 28 of
them. That number is allowed to fall and not to rise.

The rest of this chapter is about behaviour skills, because they owe the most.

== The order

// intro: authoring-to-the-standard
#keyterm[Authoring to the standard] is making the moves in an order where each
one produces what the next one needs, so that nothing is written before the
thing it has to agree with. For a behaviour skill, the order is this. Each step
names what it produces.

+ *Name the default* (#chref(<ch-default>)). Write the displacement table
  before any prose. Produces the claim: which default, where it visibly fails,
  and which rows are judgement.
+ *Measure the premise* (#chref(<ch-premise>)), if it is cheap to measure.
  Produces evidence that the default is real, or a refutation before you have
  built anything on it. If it is not cheap, record it as unmeasured and go on.
+ *Build the harness and watch it fail* (#chref(<ch-harness>)). Break each guard
  alone. Choose the oracle so that it shares as little as possible with the
  subject (#chref(<ch-oracle>)). Produces the numbers the prose may quote.
+ *Write the prose.* Every number in it comes from the harness. Every judgement
  row becomes a line in what the skill cannot do.
+ *Release at 1.0.0 with a changelog* (#chref(<ch-version>)). From here, a
  correction to what a reader was told is a MAJOR bump.

Throughout, direct the agent doing most of this as #chref(<ch-agent>) describes:
ask it for artifacts that could disagree with you.

One step here is not where `skill-authoring` puts it. The skill numbers
#emph[measure the premise] fifth, after the harness. The corpus's most
expensive lesson argues for moving it up. `role-deck` was built, verified,
released, and revised to 2.0.0 over the first eleven hours of 15 September.
Its founding premise was then fixtured: twelve minutes from the fixture's
commit to the result, and it came back against the claim. The
deck checker survived, and so did the ledger. The reason for the skill did not.

The qualifier #emph[if it is cheap] matters just as much.
`directed-verification`'s behaviour 1 has used up three fixture runs without a
result. A rule that said #emph[no harness until the premise is measured] would
have stopped that skill from being written at all. The standard's own
checklist accepts a premise #emph[measured, or explicitly recorded as
unmeasured]. The second option is honest. Silence is not.

== What the order leaves behind

An order you cannot check is advice, and `skill-authoring` says so about its
own third behaviour. Its verification lists #emph[nothing checks that the
harness preceded the prose] as a gap. It proposes a fix: prove the order from
commit history, the way `claim-fixture` proves that a scorer was committed
before any result.

That fix can be tried now, on the corpus. For each of the 21 behaviour skills,
compare the first commit that touched its harness with the first commit that
touched its `SKILL.md`.

#figure({
  set par(justify: false)
  table(
    columns: (auto, auto, 1fr),
    align: left,
    stroke: 0.5pt + luma(180),
    inset: 6pt,
    table.header[*History shows*][*Skills*][*Which*],
    [harness first], [2], [`test-writing` (two minutes earlier); `role-deck`
      (its checker, as an experiment, two and a half hours earlier)],
    [prose first], [2], [two skills from 6 September, before the standard
      existed; each harness arrived within five minutes],
    [one commit, both], [17], [including `skill-authoring` and
      `directed-verification`],
  )},
  caption: [Harness and prose, by first commit, for every behaviour skill.],
)

The proposed check would be silent on 17 of 21 skills. Silent does not mean
the prose came first. #chref(<ch-agent>) opened with a harness-first failure,
the best size recorded as 54, from a skill whose check and prose share a
commit. The work was done in order. The history cannot show it, because a
commit records what was finished, not the order in which it was written.

So the fix is not a better script. It is a habit that leaves a trace: commit
the harness on its own, before the prose, as `claim-fixture` requires for a
scorer. The check becomes possible only after the habit exists. Four skills in
this corpus left that trace. Seventeen did not, and the standard is one of the
seventeen.

== The standard, held to itself

`skill-authoring` is a behaviour skill, so it owes what it asks for. Its
checker runs the standard over every skill in the corpus and breaks each of its
eight gates alone. Its own table reports 4 covered, 2 judgement and 2 gaps. By
this corpus's measure it is one of the better-evidenced skills.

It had also started to decay in the places nothing checks. When this chapter
was drafted, its verification notes said the corpus failed in 35 places across
29 skills, while the ratchet beside that sentence had moved to 34. More
seriously, its list of what it cannot do cited the Luu experiment as showing
that tutorial-style documents #emph[measured worse than no document at all].
That is the strong version of the result. Part I read the article and found it
weaker: one skill did worse only on the runs it influenced, one did worse
possibly by chance, and one was confounded. The standard's own statement of its
limits quoted a source it had never re-read.

Neither defect changed what the skill tells you to do. Both were #emph[source]
problems, the kind #chref(<ch-oracle>) left open: a restatement made from an
earlier restatement. They are told here because a standard is a skill, and it
goes stale in the same way.

Both are fixed in `skill-authoring` 1.1.0, and so is the order problem from the
previous section: behaviour 3 now tells authors to commit the harness on its
own. The notes no longer restate the failure count at all, because a count in
prose is a clause nothing keeps true. The same overstated citation turned out
to be in `test-writing` and in the documentation both skills copied it from.
It was corrected there too.

== The objection

#emph["This is a lot of process for a Markdown file."]

Some of it is, and the order puts the cheap parts first. A displacement table
is a few rows. `test-writing`'s fixture was committed two minutes before its
prose. The two premise fixtures that refuted `role-deck` took about four
minutes of wall time. The expensive parts are the ones you can defer honestly:
an experiment that will not come out clean, recorded as unmeasured.

What the process cannot give you is a skill that helps. `skill-authoring`
says so plainly. A document can be conformant, verified, honestly versioned,
and still say nothing the model did not already do. Every check in this part
tells you that the skill makes a claim and that the claim could fail. None of
them tells you that the claim was worth making. That judgement stays with the
author, and the standard makes it visible, not correct.

#practice[Author in order, and commit the order.][
  Declare the archetype first. If the skill is not a behaviour skill, find what
  its archetype owes and stop there.

  For a behaviour skill, write the displacement table before any prose. Measure
  the premise if it is cheap. If it is not, write #emph[unmeasured] where a
  reader will see it. Build the harness, watch it fail, and break each guard
  alone. #emph[Commit the harness on its own.] Then write the prose, quoting
  only numbers the harness printed, and release at 1.0.0 with a changelog.

  Then run the standard on the standard. Re-read every source your skill cites
  from the source, not from your own earlier notes. List every sentence in the
  skill and its verification notes that states a count, and find the check
  that keeps each one true. The sentences with no check are where the skill
  will go stale first.
] <pr-author>

That is the standard, one move at a time and then all together. Whether it is
worth anything depends on what it found when it was applied, and that is the
next part.
