#import "../../preamble.typ": keyterm, headline, practice
#import "../../corpus-facts.typ": corpus-asof, corpus-days, n-commits, n-skills, skill-words

// DRAFT 2026-09-16. Ledger rows: C-I-04..10, C-I-14.

= You have a corpus, and you do not know if it is an asset

#headline[160 runs][
  The ECC Rust test skill was tried 160 times. Its top-line score looked fine.
  Only reading the runs showed it made agents worse.
]

== A skill that looked fine

In September 2026 Dan Luu asked coding agents to implement Zstd in Rust, over
and over, under different testing instructions, and scored each run against a
hidden test suite.#footnote[Dan Luu, "How well do agents use test/verification
techniques?", September 2026, #link("https://danluu.com/agentic-testing/").
// not-a-use: harness—Luu's eval harness, not a verification harness
One task, one harness (codex, GPT-5.6 Sol, medium and xhigh effort), 80 runs per
condition and effort level. The author describes the write-up as quick and
"half-baked", and cautions against strong conclusions from the ordering of
results.] One of the conditions was the Rust testing skill from ECC
(Everything Claude Code), an open-source collection of agent skills that then
had 250,000 GitHub stars.#footnote[#link("https://github.com/affaan-m/ECC"),
formerly `affaan-m/everything-claude-code`; the old name redirects to the same
repository. Its current README does not expand the acronym. Star count as
reported by Luu at the time of the experiment.]

Its score came in almost level with giving the agent no testing instructions at
all. By the number, it was harmless.

The number was misleading. Luu looked at #emph[when] each agent had opened the
skill. The seven runs that never read it scored perfectly, and so did the nine
that read it late and were barely influenced. Among the runs the skill actually
shaped, it scored below average, and "the earlier an agent looked at the skill,
the more its behavior was impacted and the worse the correctness result." Luu's
summary of the whole episode: "superficially, if we just look at the score, ECC
seems ok."

Compare that with your own skills. That one had a quarter of a million
stars, 160 runs, and a careful experimenter—and still needed someone to read
the transcripts before anyone could say it was hurting. Yours have one reviewer, and it is the person who wrote them.

== The pile

// intro: skill-as-document
If you write skills for agents, you probably have a few dozen by now. Each one
went in because it read well, and none has been checked. So you have no way to
tell which of them help, which do nothing, and which, like the ECC skill, make
agents worse.

The natural response is to write another one, for the next thing that went
wrong. The comparable books on the shelf reinforce that. Every one of them
dated to 2026, and by title and subtitle all of them promise to get you
#emph[building] skills—shipping one in a weekend, mastering the standard,
building portable skills.#footnote[From a shelf survey on
15 September 2026; see the comps table. This characterises how the genre
presents itself, not what any one book contains.] Production is the genre's
promise. Evaluation is not in it.

So the pile grows, and each new document inherits the uncertainty of the ones
before it.

== It is not neutral

The tempting belief is that an unevaluated skill is at worst useless—that the
downside of a mediocre document is that it does nothing. The same experiment
measured the opposite.

The official skill for Hegel, a Rust testing library, runs to more than twenty
thousand tokens once its reference file is loaded, and agents re-read it on
many subsequent actions. It raised cost by 26% at medium effort and 41% at
xhigh. Correctness did not improve; it was slightly worse, close enough to be
chance. Luu treats the cost increase as causal and the correctness change as
possibly noise, and so should we.

That gives two costs, and a skill incurs both whether or not it works.

#keyterm[It costs the agent context.] Every run that loads it pays for it,
in tokens, in money, and in whatever else could have been in that context
instead. A skill that does nothing still costs that much.

#keyterm[It stops you watching the problem.] A document that reads well feels like a
problem handled. You stop looking at the behaviour it was written for, because
you wrote something about it. If the document does not work, you have traded a
problem you knew about for one you have stopped watching.

// REWRITE-PASS (drift-check.md §4, ledger C-I-08): "Fifty" is rhetorical, but
// it sits four lines above an as-of count that says 53 and reads as the same
// number. Decide which it is: make it plainly illustrative (a hundred vs five),
// or let it be the corpus figure and generate it with the sentence below.
A corpus compounds both. Fifty skills nobody can evaluate is worse than five,
because the context cost adds up and so does the number of things you have
stopped watching.

== This corpus, as the case

// intro: corpus
This book follows a real corpus rather than a worked example. As of
#corpus-asof it held #n-skills skills, built over #corpus-days days in
#n-commits commits, whose SKILL.md files alone run to roughly #skill-words
words. Every one was written
by a person and an agent working together, and every one is measured against a
written standard, against which the corpus still records 34 open failures at
the time of writing.

The standard did not make the corpus trustworthy by being written down. Part
III reports what happened when it was applied: four audits, in four unrelated
verification tools, each finding checks that had passed for days and could not
have failed. None was found by reading the check. Each was found by breaking something on purpose and
noticing that nothing complained.

// intro: test-writing
One skill from that corpus runs through the rest of the book: `test-writing`,
149 lines, built by planting bugs and confirming the default test missed them
before a word of the skill was written. It is short, it is verified, and it
touches the Luu experiment directly—which, as the next chapter shows, is not
the same as knowing that it works.

== The objection

#emph["Quality in a document like this is a craft judgement. You can't measure
it."]

Some of it is judgement, and this book will say which parts. But the objection
usually carries a stronger claim: that because the #emph[writing] is craft, the
#emph[effect] cannot be checked. Luu's own judgement was good: reading the
skills beforehand, Luu predicted in advance, at 55–65% confidence, that none of the three
public ones would outperform, and that prediction held. But it came with a
confidence no further reading could raise, and the one number everyone
would have looked at said ECC was fine. What settled it was measuring the
effect and then reading the runs. In this corpus, likewise, what found the four
checks that could not fail was breaking things on purpose, not reading them.

#practice[Count what you cannot evaluate.][
  List your skills. Next to each, write one of three words: #emph[checked], if
  you have seen evidence that it changes what an agent does; #emph[unchecked],
  if you have not; #emph[unknown], if you cannot say what checking it would
  even mean.

  The third column is the one this book is about. A skill you cannot say how
  to check is not a skill you have evaluated and found good. Nothing yet
  distinguishes it from the ECC skill, whose headline score also looked
  fine.
]

To move a skill out of that third column, you need to know what it would mean
for it to be wrong—which means knowing what it claims.
