# ste-check.awk -- advisory Simplified Technical English checker.
#
# Every finding is a CANDIDATE for human review. Nothing here gates by default.
# The tool cannot judge meaning; it flags surface patterns that STE discipline
# tells you to look at. Expect false positives on PASSIVE? and MULTI-ACTION?.
#
# Usage:
#   awk -v max=20 -v hard=25 -v strict=0 -v canon="delete,create" \
#       -f ste-check.awk FILE
#
#   max     procedural sentence length warn threshold, in words   (default 20)
#   hard    descriptive sentence length threshold, in words       (default 25)
#   strict  if "1", exit 1 when any finding is reported           (default 0)
#   canon   comma/space list of your canonical verbs; any OTHER
#           member of that verb's synonym group is flagged as drift
#
# One file per invocation (see run.sh). Skips fenced code blocks, ATX headings,
# table rows, and HTML comments. Strips list markers, inline code, and links
# before checking, so list items ARE checked -- that is where instructions live.

BEGIN {
  if (max  == "") max  = 20
  if (hard == "") hard = 25
  incode = 0
  nfind  = 0

  # Vague verbs: STE says name an observable operation instead.
  split("handle,manage,address,leverage,optimize,facilitate,ensure,process," \
        "utilize,support,maintain,perform,implement,provide,consider,deal," \
        "coordinate,oversee,enable,streamline,robust,seamless,appropriate", V, ",")
  for (i in V) vague[V[i]] = 1

  # Near-synonym groups. 2+ distinct members in one document => drift.
  grp[1] = "check verify validate confirm ensure"
  grp[2] = "delete remove clear purge erase drop"
  grp[3] = "create make generate build produce"
  grp[4] = "start begin commence initiate"
  grp[5] = "get fetch retrieve obtain pull"
  grp[6] = "use utilize employ leverage"
  grp[7] = "stop halt cease terminate"
  grp[8] = "change modify alter update edit"
  ng = 8

  if (canon != "") {
    n = split(canon, C, /[, ]+/)
    for (i = 1; i <= n; i++) if (C[i] != "") canonv[tolower(C[i])] = 1
  }
}

/^[ \t]*```/       { incode = !incode; next }
incode            { next }
/^[ \t]*$/         { flush(); next }
/^[ \t]*#+ /       { next }
/^[ \t]*\|/        { next }
/^[ \t]*<!--/      { next }

{
  line = $0
  sub(/^[ \t]*([-*+]|[0-9]+[.)])[ \t]+/, "", line)   # strip list marker
  gsub(/`[^`]*`/, "CODE", line)                       # inline code -> token
  gsub(/!?\[[^]]*\]\([^)]*\)/, "LINK", line)          # markdown link -> token
  if (buf == "") pstart = FNR
  buf = (buf == "" ? line : buf " " line)
}

END { flush(); report() }

function trim(s) { gsub(/^[ \t]+|[ \t]+$/, "", s); return s }

function flush(   arr, i, n) {
  if (trim(buf) == "") { buf = ""; return }
  n = split_sentences(buf, arr)
  for (i = 1; i <= n; i++) check_sentence(arr[i], pstart)
  buf = ""
}

# Split a paragraph buffer into sentences on . ! ? followed by space or end.
# Deliberately simple: abbreviations ("e.g.", "i.e.", "vs.") can over-split.
function split_sentences(t, out,   i, ch, nxt, prev, cur, ns) {
  gsub(/[ \t]+/, " ", t)
  ns = 0; cur = ""
  for (i = 1; i <= length(t); i++) {
    ch  = substr(t, i, 1)
    cur = cur ch
    if (ch == "." || ch == "!" || ch == "?") {
      nxt  = substr(t, i + 1, 1)
      prev = substr(t, i - 1, 1)
      if ((nxt == " " || nxt == "") && !(prev ~ /[0-9]/ && substr(t, i + 2, 1) ~ /[0-9]/)) {
        if (trim(cur) != "") out[++ns] = trim(cur)
        cur = ""
      }
    }
  }
  if (trim(cur) != "") out[++ns] = trim(cur)
  return ns
}

function check_sentence(s, ln,   low, nw, words, i, w, p, g, gm, m) {
  s = trim(s)
  if (s == "") return
  low = tolower(s)
  nw  = split(s, words, /[ \t]+/)

  # 1. Sentence length.
  if (nw > hard)
    finding(ln, "LENGTH", nw " words (> " hard ", descriptive limit)", s)
  else if (nw > max)
    finding(ln, "LENGTH", nw " words (> " max ", procedural limit)", s)

  # 2. Vague verbs.
  for (i = 1; i <= nw; i++) {
    w = tolower(words[i]); gsub(/[^a-z]/, "", w)
    if (w in vague)
      finding(ln, "VAGUE-VERB", "\"" w "\" -- name a concrete, observable operation", s)
  }

  # 3. Passive voice (low confidence: be-verb + past participle).
  p = " " low " "
  if (match(p, /[^a-z](is|are|was|were|be|been|being)[ ]+[a-z]+(ed|en)[^a-z]/))
    finding(ln, "PASSIVE?", "possible passive voice -- name the actor", s)

  # 4. Multiple actions in one sentence.
  if (nw > 8 && (low ~ /, and |, then | then /))
    finding(ln, "MULTI-ACTION?", "give one instruction per sentence", s)

  # 5. Condition placed after the command.
  if (s ~ /^[A-Z]/ && \
      low ~ /,?[ ]+(if|unless|when|once|after|provided)[ ][^.?!]*[.?!]?[ ]*$/ && \
      low !~ /^(if|unless|when|once|after|provided)[ ]/)
    finding(ln, "CONDITION-LAST", "put the condition before the command it governs", s)

  # 6. Synonym drift -- record which group members appear.
  for (g = 1; g <= ng; g++) {
    m = split(grp[g], gm, " ")
    for (i = 1; i <= m; i++)
      if (p ~ ("[^a-z]" gm[i] "[^a-z]")) {
        seen[g SUBSEP gm[i]] = 1
        if (canon != "" && !(gm[i] in canonv) && any_canon_in_group(g))
          finding(ln, "SYNONYM-DRIFT", \
                  "\"" gm[i] "\" -- a canonical verb for this operation is declared", s)
      }
  }
}

function any_canon_in_group(g,   gm, m, i) {
  m = split(grp[g], gm, " ")
  for (i = 1; i <= m; i++) if (gm[i] in canonv) return 1
  return 0
}

function finding(ln, tag, msg, s) {
  nfind++
  printf "%s:~%d  [%s]  %s\n", FILENAME, ln, tag, msg
  printf "        | %s\n", (length(s) > 100 ? substr(s, 1, 97) "..." : s)
}

function report(   g, gm, m, i, k, members) {
  if (canon == "") {
    for (g = 1; g <= ng; g++) {
      m = split(grp[g], gm, " "); k = 0; members = ""
      for (i = 1; i <= m; i++)
        if ((g SUBSEP gm[i]) in seen) { k++; members = members (members == "" ? "" : ", ") gm[i] }
      if (k >= 2) {
        nfind++
        print FILENAME ":~0  [SYNONYM-DRIFT]  same operation written " k \
              " ways: " members "  -- pick one verb and keep it"
      }
    }
  }
  print ""
  printf "%d finding(s). Advisory only: each line is a candidate for review, not an error.\n", nfind
  if (strict == "1" && nfind > 0) exit 1
}
