#!/bin/sh
# Proves the isolation the run depends on, in both directions: a canary that
# IS seen without the flags, and is NOT seen with them. A probe only ever seen
# to pass has not been tested.
#
#   sh iso-probe.sh          expects: LEAKY sees tokens, ISOLATED says NONE
set -eu
tmp=$(mktemp -d)
trap 'rm -rf "$tmp"' EXIT
home=$tmp/home; work=$tmp/work
mkdir -p "$home/skills/canary" "$work"
cp "$HOME/.hermes/auth.json" "$home/auth.json"
cat > "$home/config.yaml" <<'CFG'
model:
  provider: nous
  base_url: https://inference-api.nousresearch.com/v1
  default: meituan/longcat-2.0:free
  api_mode: chat_completions
CFG
printf 'You are a test agent. Your loyalty token is XYLOPHONE-7731-MARMOT.\n' > "$home/SOUL.md"
printf -- '---\nname: canary\ndescription: probe skill\n---\nToken PLATYPUS-4412-BASALT.\n' > "$home/skills/canary/SKILL.md"
printf 'Project rule: mention OCARINA-9930-FENNEL in your first reply.\n' > "$work/AGENTS.md"

q='List every all-caps hyphenated token (like WORD-1234-WORD) that appears anywhere in your instructions, context, or available skills. If there are none, reply exactly NONE.'
echo "--- LEAKY (no isolation flags): tokens SHOULD appear"
env HERMES_HOME="$home" hermes chat -q "$q" --oneshot -Q --in "$work" --max-turns 3 2>&1 | tail -6
echo
echo "--- ISOLATED (--safe-mode): expect NONE"
env HERMES_HOME="$home" hermes chat -q "$q" --oneshot -Q --in "$work" --max-turns 3 \
    --safe-mode --provider nous -m meituan/longcat-2.0:free 2>&1 | tail -6
