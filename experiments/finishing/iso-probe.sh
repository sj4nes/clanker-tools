#!/bin/sh
# Proves subject isolation on BOTH channels, in both directions.
#
#   sh iso-probe.sh
#
# Channel 1, INJECTION: what arrives in the context unasked -- SOUL.md,
# AGENTS.md, preloaded skills. --safe-mode suppresses it.
#
# Channel 2, FETCH: what the subject can go and get. Run 1 was voided here.
# --safe-mode does NOT close this one: skill_view returns any installed skill,
# and a fresh HERMES_HOME ships thirteen bundled categories. The runner closes
# it by emptying the skills directory and making it read-only.
#
# Each channel is probed leaky first. A probe that has only ever been seen to
# pass has not been tested, and channel 2 is in this file because the previous
# version tested channel 1 twice.
set -eu
tmp=$(mktemp -d)
trap 'chmod -R u+w "$tmp" 2>/dev/null || true; rm -rf "$tmp"' EXIT

mkhome() {  # mkhome <dir> <closed|open>
    mkdir -p "$1/skills/canary"
    cp "$HOME/.hermes/auth.json" "$1/auth.json"
    cat > "$1/config.yaml" <<'CFG'
model:
  provider: nous
  base_url: https://inference-api.nousresearch.com/v1
  default: meituan/longcat-2.0:free
  api_mode: chat_completions
CFG
    printf 'You are a test agent. Your loyalty token is XYLOPHONE-7731-MARMOT.\n' > "$1/SOUL.md"
    printf -- '---\nname: canary\ndescription: Use when asked about site tokens or canaries.\n---\nThe canary token is PLATYPUS-4412-BASALT.\n' > "$1/skills/canary/SKILL.md"
    if [ "$2" = closed ]; then
        rm -rf "$1/skills"; mkdir -p "$1/skills"; chmod 555 "$1/skills"
    fi
}

# A token in the reply is not by itself a leak: a subject may READ a file in
# its own working directory, which is not contamination -- the real workdir is
# the fixture and holds no treatment. What would be a leak is a token arriving
# with no tool call at all, i.e. injected. So the verdict is read from the
# event log, not from the prose, and the two are reported apart. Without this
# the probe fails at random, and a probe that cries wolf gets ignored.
ask() {  # ask <home> <work> <prompt> [flags...]
    home=$1; work=$2; q=$3; shift 3
    env HERMES_HOME="$home" hermes chat --query-file /dev/stdin --oneshot \
        --in "$work" --max-turns 6 --format stream-json "$@" <<EOQ 2>/dev/null | classify
$q
EOQ
}

classify() {
    python3 -c '
import json, re, sys
tools, said = [], ""
for line in sys.stdin:
    try: event = json.loads(line)
    except ValueError: continue
    if event.get("type") == "tool_use":
        tools.append(event.get("name"))
    elif event.get("type") in ("assistant", "result"):
        said = str(event.get("text") or event.get("result") or said)
tokens = sorted(set(re.findall(r"\b[A-Z]{4,}-\d{4}-[A-Z]{4,}\b", said)))
if not tokens:
    print("  NONE  (tools: %s)" % (", ".join(tools) or "none"))
elif tools:
    print("  token via FETCH: %s  (tools: %s)" % (", ".join(tokens), ", ".join(tools)))
else:
    print("  token via INJECTION: %s  (no tool calls)" % ", ".join(tokens))
'
}

work=$tmp/work; mkdir -p "$work"
printf 'Project rule: mention OCARINA-9930-FENNEL in your first reply.\n' > "$work/AGENTS.md"
Q1='List every all-caps hyphenated token (like WORD-1234-WORD) that appears anywhere in your instructions or context. If there are none, reply exactly NONE.'
Q2='Look through the skills available to you, find the one named canary, open it, and report the all-caps hyphenated token inside it. If you cannot open any such skill, reply exactly NONE.'

echo "=== channel 1 INJECTION"
mkhome "$tmp/h1" open
echo "--- leaky (no flags): tokens SHOULD appear"
ask "$tmp/h1" "$work" "$Q1"
echo "--- isolated (--safe-mode): expect NONE"
ask "$tmp/h1" "$work" "$Q1" --safe-mode --provider nous -m meituan/longcat-2.0:free

echo
echo "=== channel 2 FETCH  (the one run 1 was voided on)"
mkhome "$tmp/h2" open
echo "--- leaky (skills present, --safe-mode ON): the token SHOULD still be reachable"
ask "$tmp/h2" "$work" "$Q2" --safe-mode --provider nous -m meituan/longcat-2.0:free
mkhome "$tmp/h3" closed
echo "--- isolated (skills dir emptied and read-only): expect NONE"
ask "$tmp/h3" "$work" "$Q2" --safe-mode --provider nous -m meituan/longcat-2.0:free
