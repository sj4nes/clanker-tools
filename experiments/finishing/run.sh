#!/bin/sh
# Spawn one naive subject on a fresh copy of the fixture.
#
#   sh run.sh <run-id> [task-file]
#
# Isolation (proved by iso-probe.sh, not assumed): a throwaway HERMES_HOME
# holding only credentials and a pinned model, plus --safe-mode, which sets
# HERMES_IGNORE_USER_CONFIG / HERMES_IGNORE_RULES / HERMES_SAFE_MODE and so
# suppresses SOUL.md, AGENTS.md, memory, preloaded skills, plugins and MCP.
# None of this corpus's skills are installed in Hermes; the 139 that are cannot
# load under --safe-mode.
#
# --yolo is required because single-query mode otherwise blocks command
# execution, which would force every subject down the read-only path and make
# the result an artefact of the harness.
#
# The blast radius of --yolo is then closed by sandbox.sb rather than by asking
# the subject to stay put: the capability probe finished its own task and went
# looking for other copies to fix, and an instruction not to would be a change
# to the prompt -- which is the one thing that must stay identical between the
# arms. The sandbox denies the write; it says nothing to the subject.
set -eu

here=$(cd "$(dirname "$0")" && pwd)
id=${1:?usage: run.sh <run-id> [task-file]}
task=${2:-$here/task-A.md}
run=$here/runs/$id
# A HOME PER SUBJECT, outside the repo and destroyed with the run directory.
# Run 1 was voided because one home was shared: a subject wrote a skill
# describing the fixture -- with the fix in it -- and ten later subjects
# patched that same file. Subjects that can write where the next subject reads
# are not independent subjects.
home=${TMPDIR:-/tmp}/sitegen-homes/$id
# The work copy lives OUTSIDE the repository. The capability probe walked out
# of its own directory, found the sibling master fixture and edited that too;
# a subject reaching the master is not prevented by this, but a subject
# stumbling over it no longer is. score.py reads its reference from HEAD and
# reports any modification of the checked-in fixture, which is the real guard.
work=${TMPDIR:-/tmp}/sitegen-runs/$id

[ -e "$run" ] && { echo "$run exists; pick another id" >&2; exit 2; }
mkdir -p "$run" "$(dirname "$work")"
rm -rf "$work"
cp -R "$here/subject" "$work"
rm -rf "$work/out"
ln -s "$work" "$run/work"

rm -rf "$home"
mkdir -p "$home"
cp "$HOME/.hermes/auth.json" "$home/auth.json"
cat > "$home/config.yaml" <<'CFG'
model:
  provider: nous
  base_url: https://inference-api.nousresearch.com/v1
  default: meituan/longcat-2.0:free
  api_mode: chat_completions
CFG

# Close the fetch channel. --safe-mode stops skills being INJECTED; it does not
# stop a subject fetching one with skill_view, and a fresh home ships thirteen
# bundled categories. An empty read-only directory leaves the tool with nothing
# to return and nowhere to write a new one.
rm -rf "$home/skills"
mkdir -p "$home/skills"
chmod 555 "$home/skills"

cp "$task" "$run/task.md"
sandbox-exec -f "$here/sandbox.sb" \
    -D WORK="$work" -D HHOME="$home" -D TMP="${TMPDIR:-/tmp}" \
    env HERMES_HOME="$home" hermes chat \
    --query-file "$run/task.md" --oneshot --in "$work" \
    --safe-mode --yolo --provider nous -m meituan/longcat-2.0:free \
    --max-turns 40 --run-budget 900 --format stream-json \
    > "$run/events.jsonl" 2> "$run/stderr.txt" || true

{
  echo "run: $id"
  echo "date: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
  echo "model: meituan/longcat-2.0:free (unpinned free tag; no seed)"
  echo "provider: nous"
  echo "hermes: $(hermes --version 2>/dev/null | head -1)"
  echo "task: $(basename "$task")"
  echo "home: per-subject, skills dir emptied and read-only"
} > "$run/meta.txt"
# Leave the home for the manipulation check to inspect, then drop it.
cp -R "$home" "$run/home-after" 2>/dev/null || true
chmod -R u+w "$run/home-after" 2>/dev/null || true
rm -rf "$home"
echo "$run"
