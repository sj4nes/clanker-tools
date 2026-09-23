#!/bin/sh
# Structural gate over the skill corpus.  Asserts what prose cannot:
#
#   1. every skills/*/ has a SKILL.md
#   2. every SKILL.md has exactly one `version:` MAJOR.MINOR.PATCH, inside the
#      frontmatter block  (see docs/skill-versioning.md)
#   3. every SKILL.md `name:` matches its directory name
#   4. every .claude/skills entry resolves, and points at ../../skills/<name>
#   5. every skills/*/ is wired into .claude/skills
#   6. every skills/*/ has a CHANGELOG.md whose NEWEST version heading is the
#      version in SKILL.md  (see docs/skill-versioning.md §4)
#   7. the rest of the changelog contract (§3b): a 1.0.0 heading, every later
#      entry opens with its level, and the level is the digit that moved --
#      tools/check-changelogs.py.  Unchecked, those clauses decayed.
#   8. every relative Markdown link resolves, and every `#anchor` names a
#      heading that exists -- tools/check-links.py.  Ten were broken when this
#      clause was added (2026-09-22), eight of them a sibling skill addressed
#      as though skills nested.  No skill's own verification looks at its
#      links, because a link is a claim about the REPOSITORY, not about the
#      skill's subject; only a corpus-wide gate sees them.
#
# Exists because two of these went wrong silently: `math-probability`'s symlink
# dangled for a week (a 131-node capsule that was never loadable), and the
# `version:` field sat at 1.0.0 across a 29-line divergence that included a
# correctness fix.  A field nothing checks is decoration.
set -e
cd "$(dirname "$0")/.."
fail=0
n=0

for d in skills/*/; do
    s=$(basename "$d")
    n=$((n + 1))
    f="$d/SKILL.md"

    if [ ! -f "$f" ]; then
        echo "*** FAIL: $s has no SKILL.md"; fail=$((fail + 1)); continue
    fi

    # exactly one version line
    vc=$(grep -c '^version:' "$f" || true)
    if [ "$vc" -ne 1 ]; then
        echo "*** FAIL: $s has $vc 'version:' lines (want exactly 1)"; fail=$((fail + 1)); continue
    fi

    # semver shape
    v=$(sed -n 's/^version: *//p' "$f")
    if ! printf '%s' "$v" | grep -qE '^[0-9]+\.[0-9]+\.[0-9]+$'; then
        echo "*** FAIL: $s version '$v' is not MAJOR.MINOR.PATCH"; fail=$((fail + 1))
    fi

    # version must sit inside the frontmatter block
    vline=$(grep -n '^version:' "$f" | cut -d: -f1)
    close=$(awk 'NR>1 && /^---$/{print NR; exit}' "$f")
    if [ -z "$close" ] || [ "$vline" -ge "$close" ]; then
        echo "*** FAIL: $s version is outside the frontmatter block"; fail=$((fail + 1))
    fi

    # name must match the directory
    nm=$(sed -n 's/^name: *//p' "$f" | head -1)
    if [ "$nm" != "$s" ]; then
        echo "*** FAIL: $s declares name '$nm'"; fail=$((fail + 1))
    fi

    # changelog present, and its newest entry agrees with `version:`.  A bump
    # with no entry is how a version number goes back to being decoration --
    # the reader can see the number moved and not why.
    cl="$d/CHANGELOG.md"
    if [ ! -f "$cl" ]; then
        echo "*** FAIL: $s has no CHANGELOG.md"; fail=$((fail + 1))
    else
        top=$(sed -n 's/^## \([0-9][0-9]*\.[0-9][0-9]*\.[0-9][0-9]*\).*/\1/p' "$cl" | head -1)
        if [ -z "$top" ]; then
            echo "*** FAIL: $s CHANGELOG.md has no '## MAJOR.MINOR.PATCH' heading"
            fail=$((fail + 1))
        elif [ "$top" != "$v" ]; then
            echo "*** FAIL: $s is version $v but its CHANGELOG.md newest entry is $top"
            fail=$((fail + 1))
        fi
    fi

    # wired in?  Distinguish ABSENT from DANGLING -- a dangling link is the
    # worse failure (it looks wired) and is the one that hid for a week.
    if [ -L ".claude/skills/$s" ] && [ ! -e ".claude/skills/$s" ]; then
        echo "*** FAIL: $s is wired but DANGLING: .claude/skills/$s -> $(readlink ".claude/skills/$s")"
        fail=$((fail + 1))
    elif [ ! -e ".claude/skills/$s" ]; then
        echo "*** FAIL: $s is not wired into .claude/skills (built but not loadable)"
        fail=$((fail + 1))
    fi
done

for l in .claude/skills/*; do
    s=$(basename "$l")
    if [ ! -e "$l" ]; then
        echo "*** FAIL: .claude/skills/$s is a broken symlink -> $(readlink "$l")"
        fail=$((fail + 1)); continue
    fi
    t=$(readlink "$l" 2>/dev/null || true)
    if [ -n "$t" ] && [ "$t" != "../../skills/$s" ]; then
        echo "*** FAIL: .claude/skills/$s points at '$t', want '../../skills/$s'"
        fail=$((fail + 1))
    fi
done

if ! python3 tools/check-changelogs.py; then
    fail=$((fail + 1))
fi

if ! python3 tools/check-links.py; then
    fail=$((fail + 1))
fi

echo
echo "checked $n skills, $(ls .claude/skills | wc -l | tr -d ' ') wired"
if [ "$fail" -eq 0 ]; then
    echo "ALL SKILL CHECKS PASSED"
else
    echo "*** $fail SKILL CHECK(S) FAILED" >&2
    exit 1
fi
