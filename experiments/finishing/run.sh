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
# the result an artefact of the harness. The workdir is a throwaway copy.
set -eu

here=$(cd "$(dirname "$0")" && pwd)
id=${1:?usage: run.sh <run-id> [task-file]}
task=${2:-$here/task-A.md}
run=$here/runs/$id
home=$here/runs/.home

[ -e "$run" ] && { echo "$run exists; pick another id" >&2; exit 2; }
mkdir -p "$run"
cp -R "$here/subject" "$run/work"
rm -rf "$run/work/out"

mkdir -p "$home"
cp "$HOME/.hermes/auth.json" "$home/auth.json"
cat > "$home/config.yaml" <<'CFG'
model:
  provider: nous
  base_url: https://inference-api.nousresearch.com/v1
  default: meituan/longcat-2.0:free
  api_mode: chat_completions
CFG

cp "$task" "$run/task.md"
env HERMES_HOME="$home" hermes chat \
    --query-file "$run/task.md" --oneshot --in "$run/work" \
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
} > "$run/meta.txt"
echo "$run"
