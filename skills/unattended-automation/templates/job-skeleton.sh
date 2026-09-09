#!/bin/sh
# Reference skeleton for an unattended job. POSIX sh. Adapt, do not run as-is.
#
# Wires in: strict mode, structured logging, input validation, kill switch,
# single-instance lock, dry-run, bounded retry with backoff, per-call timeout,
# postcondition check, SIGTERM trap, checkpoint, meaningful exit codes.
#
# Exit codes: 0 ok | 1 failure | 2 bad input | 3 skipped | 4 reconcile needed
#             | 5 dependency down | 75 transient (retry whole job later)

set -eu

# ---- configuration (from environment; validated below) --------------------
: "${TARGET_DIR:?TARGET_DIR is required}"
: "${RETENTION_DAYS:?RETENTION_DAYS is required}"
DRY_RUN="${DRY_RUN:-0}"
MAX_ITEMS="${MAX_ITEMS:-1000}"
LOCK_DIR="${LOCK_DIR:-/var/lock/$(basename "$0").lock}"
KILL_SWITCH="${KILL_SWITCH:-/etc/automation/PAUSED}"
CHECKPOINT="${CHECKPOINT:-/var/lib/automation/$(basename "$0").ckpt}"
AUDIT_LOG="${AUDIT_LOG:-/var/log/automation/$(basename "$0").jsonl}"
CALL_TIMEOUT="${CALL_TIMEOUT:-20}"
RUN_ID="$(date -u +%Y%m%dT%H%M%SZ)-$$"

# ---- structured logging --------------------------------------------------
log() { # log EVENT_TYPE KEY=VAL ...
  et="$1"; shift
  printf '{"ts":"%s","run_id":"%s","event_type":"%s"' \
    "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$RUN_ID" "$et"
  for kv in "$@"; do printf ',"%s":"%s"' "${kv%%=*}" "${kv#*=}"; done
  printf '}\n'
} >> "$AUDIT_LOG"

die() { log error "reason=$2"; echo "$2" >&2; exit "$1"; }

# ---- cleanup / signal handling -----------------------------------------
STOP_REQUESTED=0
cleanup() { rmdir "$LOCK_DIR" 2>/dev/null || true; }
on_term() { STOP_REQUESTED=1; log stop_requested signal=TERM; }
trap cleanup EXIT
trap on_term TERM INT

# ---- 1. validate inputs -----------------------------------------------
case "$RETENTION_DAYS" in
  ''|*[!0-9]*) die 2 "RETENTION_DAYS must be a positive integer" ;;
esac
[ "$RETENTION_DAYS" -ge 1 ] && [ "$RETENTION_DAYS" -le 3650 ] \
  || die 2 "RETENTION_DAYS out of range 1..3650"
[ -d "$TARGET_DIR" ] || die 2 "TARGET_DIR does not exist: $TARGET_DIR"
# empty target often means a failed mount -> refuse
[ -n "$(ls -A "$TARGET_DIR" 2>/dev/null)" ] || die 2 "TARGET_DIR is empty (mount failure?)"

# ---- 2. guards: kill switch, lock, limits ----------------------------
[ -e "$KILL_SWITCH" ] && { log skipped reason=kill_switch; exit 3; }
if ! mkdir "$LOCK_DIR" 2>/dev/null; then
  log skipped reason=locked; exit 3          # overrun policy: skip
fi

# ---- 3. plan (compute changes, make none) ---------------------------
PLAN="$(mktemp)"; trap 'rm -f "$PLAN"; cleanup' EXIT
find "$TARGET_DIR" -type f -mtime "+$RETENTION_DAYS" > "$PLAN" || true
COUNT="$(wc -l < "$PLAN" | tr -d ' ')"
log plan planned="$COUNT" dry_run="$DRY_RUN"
[ "$COUNT" -le "$MAX_ITEMS" ] || die 4 "plan of $COUNT exceeds MAX_ITEMS=$MAX_ITEMS"
[ "$DRY_RUN" = "1" ] && { log done outcome=dry_run planned="$COUNT"; exit 0; }

# ---- 4. execute one unit at a time, with retry + checkpoint --------
TRASH="$TARGET_DIR/.trash/$RUN_ID"; mkdir -p "$TRASH"
DONE=0
: > "$CHECKPOINT"
while IFS= read -r f; do
  [ "$STOP_REQUESTED" = "1" ] && { log stopped processed="$DONE"; exit 0; }
  attempt=1
  while :; do
    if timeout "$CALL_TIMEOUT" mv "$f" "$TRASH/" 2>/dev/null; then
      DONE=$((DONE + 1)); echo "$f" >> "$CHECKPOINT"; break
    fi
    # already moved (e.g. retry after partial failure)? treat as done
    [ ! -e "$f" ] && { DONE=$((DONE + 1)); echo "$f" >> "$CHECKPOINT"; break; }
    if [ "$attempt" -ge 3 ]; then die 5 "mv failed after retries: $f"; fi
    sleep "$(awk "BEGIN{srand();print 2^$attempt*(0.5+rand()/2)}")"
    attempt=$((attempt + 1))
  done
done < "$PLAN"

# ---- 5. verify postcondition --------------------------------------
REMAIN="$(find "$TARGET_DIR" -type f -mtime "+$RETENTION_DAYS" \
           -not -path "$TARGET_DIR/.trash/*" | wc -l | tr -d ' ')"
[ "$REMAIN" -eq 0 ] || die 4 "postcondition failed: $REMAIN stale files remain"

# ---- 6. audit + heartbeat ----------------------------------------
log done outcome=success planned="$COUNT" moved="$DONE" trash="$TRASH"
# ping the dead-man's switch here, e.g.:
#   timeout 10 curl -fsS "$HEARTBEAT_URL" >/dev/null || true
exit 0
