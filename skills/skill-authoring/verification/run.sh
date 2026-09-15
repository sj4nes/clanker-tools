#!/bin/sh
# Verification for `skill-authoring`.
#
# The fixture is the corpus: 50 real skills, not a toy. Two things are checked,
# and the second is the one that makes the first mean anything.
#
#   1. RATCHET. The corpus currently fails the archetype standard in N places.
#      Demanding zero would leave the suite permanently red and teach nothing,
#      so the gate is that the count must not GROW. Remediation lowers the
#      baseline; a new non-conforming skill raises the count and fails.
#   2. MUTATIONS. The checker is broken on purpose, once per gate, and each
#      break must be caught. A conformance number from a checker that cannot
#      fail is the exact defect this corpus keeps finding.
set -e
cd "$(dirname "$0")/../../.."
PY=python3
C=skills/skill-authoring/verification/check_authoring.py
base=$(cat skills/skill-authoring/verification/baseline.txt)
fails=0

echo "=== 1. corpus conformance (ratchet: must not exceed $base) ==="
out=$($PY "$C" 2>&1) && n=0 || n=$(printf '%s\n' "$out" | grep -oE '^\*\*\* [0-9]+ AUTH' | grep -oE '[0-9]+')
printf '%s\n' "$out" | tail -3
if [ "$n" -gt "$base" ]; then
    echo "*** REGRESSION: $n failures, baseline is $base" >&2
    fails=$((fails + 1))
elif [ "$n" -lt "$base" ]; then
    echo "  conformance IMPROVED ($n < $base) -- lower baseline.txt to $n to lock it in"
else
    echo "  at baseline ($n)"
fi
echo

echo "=== 2. the checker must be able to fail ==="
tmp=$(mktemp -d); trap 'rm -rf "$tmp"' EXIT
mkdir -p "$tmp/skills/probe"

# Each mutation writes SKILL.md with a heredoc. An earlier version built the
# body with `printf -- '---\n...'`, which produced an EMPTY file, so every
# mutation reported gate [frontmatter] ("no frontmatter block") and one of them
# looked like a checker bug. The harness was wrong, not the checker.
probe="$tmp/skills/probe/SKILL.md"

expect () {   # expect <name> <gate>
    o=$($PY "$C" "$tmp/skills" 2>&1) && st=0 || st=1
    if [ "$st" -eq 0 ]; then
        echo "  *** SURVIVED: $1"; fails=$((fails + 1))
    elif ! printf '%s\n' "$o" | grep -q "\[$2\]"; then
        echo "  *** WRONG GATE: $1 -- wanted [$2], got:" \
             "$(printf '%s\n' "$o" | grep -oE '\[[a-z-]+\]' | sort -u | tr '\n' ' ')"
        fails=$((fails + 1))
    else
        echo "  caught: $1  ->  [$2]"
    fi
}

cat > "$probe" <<'P'
---
name: probe
description: A probe. NOT real.
version: 1.0.0
author: T
tags: [p]
---
P
expect "undeclared archetype" "frontmatter"

cat > "$probe" <<'P'
---
name: probe
description: A probe. NOT real.
version: 1.0.0
archetype: wishful
author: T
tags: [p]
---
P
expect "unknown archetype" "archetype"

cat > "$probe" <<'P'
---
name: probe
description: A skill that does useful things.
version: 1.0.0
archetype: tool-fact
author: T
tags: [p]
---
P
expect "description with no boundary" "scope"

cat > "$probe" <<'P'
---
name: probe
description: A probe. NOT real.
version: 1.0.0
archetype: behaviour
author: T
tags: [p]
---
P
expect "behaviour skill with no harness" "harness"

cat > "$probe" <<'P'
---
name: probe
description: A probe. NOT real.
version: 1.0.0
archetype: tool-fact
author: T
tags: [p]
---
P
expect "tool-fact with no references/" "payload"

cat > "$probe" <<'P'
---
name: probe
description: A probe. NOT real.
version: 1.0.0
archetype: capsule
author: T
tags: [p]
---
P
expect "capsule with no build/" "capsule"

cat > "$probe" <<'P'
---
name: probe
description: A probe. NOT real.
version: 1.0.0
archetype: meta
author: T
tags: [p]
---
body that names nothing
P
expect "meta naming nothing it drives" "meta"

rm -f "$probe"
expect "directory with no SKILL.md" "frontmatter"

echo
if [ "$fails" -eq 0 ]; then echo "ALL SKILL-AUTHORING CHECKS PASSED"; else
    echo "*** $fails CHECK(S) FAILED" >&2; exit 1; fi
