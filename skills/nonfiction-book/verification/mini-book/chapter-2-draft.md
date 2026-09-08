# Chapter 2 — Finding when a line's content changed (DRAFT)

> Draft for revision. Voice is a placeholder to be rewritten by the author.
> Leans on claim-ledger rows C-02, C-03, C-06.

**Hook.** The timeout was five seconds. It should have been fifty milliseconds.
Priya found the line in `client.py` in under a minute — `RETRY_TIMEOUT = 5.0` —
and then spent forty minutes reading every file that imported it, looking for the
place someone had meant to divide by a hundred. The answer was not in the code.
It was in the history, and it took one command to see it.

**Problem.** A bug points you at a line. You need two things: *when* did the line
get its current content, and *why* did whoever changed it think that was right.
The code around the line cannot tell you either. Only the commit that made the
change can, and its message usually does.

**Principle.** History is a graph of snapshots (Chapter 1). "When did this line
change" is the question "which commits, walking back from here, altered this
text". Git has two commands that ask it directly.

**The pickaxe: `git log -S`.** `git log -S'RETRY_TIMEOUT'` lists only the commits
that change how many times `RETRY_TIMEOUT` appears in a file [C-02]. For a
constant that was introduced once and edited once, that is two commits, newest
first. The top one is your answer; `git show` on it gives you the diff and the
message.

One caveat worth learning now: `-S` counts occurrences. If someone changed
`5.0` to `0.05` without touching the name, the count of `RETRY_TIMEOUT` did not
move, and `-S'RETRY_TIMEOUT'` will not show that commit. Search for the part that
actually changed — `git log -S'5.0'` — or use `-G`, which matches a regex against
any changed line.

**The line log: `git log -L`.** When you want the whole life of a line rather
than one token, give `git log` a range and a file:
`git log -L 42,42:client.py` [C-03]. Git shows every commit that touched line 42,
with the diff each time, following the line as its number shifts and as the file
is renamed. It is the closest thing to watching the line evolve.

**Method.** When a bug points at a line: run `git log -L` on that line's range
*before* you read the surrounding code [C-06]. Nine times in ten, the commit
message answers the question the code cannot.

**Pitfalls.** `-L` implies `--patch` and refuses a pathspec; give it exactly one
`start,end:file`. `-S` with a common token (`data`, `value`) returns noise —
pick something distinctive.

**Reader action.** Open your own repo. Pick a line you have wondered about. Run
`git log -S` on a distinctive token in it, then `git log -L` on its range.
Compare what each tells you.

**Transition.** `log -S` and `-L` tell you *when* a line's content changed. They
do not cleanly tell you who owns the line as it stands now, or what it looked
like the instant before it changed. For that, the next chapter turns to `blame`
— and to `blame --reverse`, which finds the moment a line disappeared.
