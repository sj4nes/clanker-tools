#!/bin/sh
# Generate the discovery views from the graph + registry + result YAMLs.
set -eu
cd "$(dirname "$0")/.."
E=build/dependencies.sorted.edges
T=nodes/nodes.tsv

# ---------------------------------------------------------------- status index
out=indexes/status-index.md
{
  echo "# Status index (generated)"
  echo
  echo "## Node registry by \`type\`"
  echo
  awk -F'\t' 'NR>1{c[$2]++} END{for(t in c) printf "- %-22s %d\n", t, c[t]}' "$T" | sort
  echo
  echo "## Headline result YAMLs by \`status_label\`"
  echo
  for f in results/*.yaml; do
    sl=$(sed -n 's/^status_label:[[:space:]]*//p' "$f")
    n=$(sed -n 's/^node:[[:space:]]*//p' "$f")
    echo "$sl	$n"
  done | sort | awk -F'\t' '{if($1!=p){print "";print "### "$1;p=$1} print "- "$2}'
} > "$out"

# ---------------------------------------------------- constructive-grade index
out=indexes/constructive-grade-index.md
{
  echo "# Constructive-grade index (generated)"
  echo
  echo "The capsule hook: every logical law / proof method carries one of"
  echo "\`intuitionistic\` / \`needs_LEM\` / \`needs_DNE\` / \`needs_full_classical\`."
  echo "(\`split\` = the node's two directions differ — see its page/YAML.)"
  echo
  echo "## From the headline result YAMLs (\`constructive_grade:\`)"
  for f in results/*.yaml; do
    g=$(sed -n 's/^constructive_grade:[[:space:]]*//p' "$f")
    n=$(sed -n 's/^node:[[:space:]]*//p' "$f")
    [ -n "$g" ] && echo "$g	$n"
  done | sort | awk -F'\t' '{if($1!=p){print "";print "### "$1;p=$1} print "- "$2}'
  echo
  echo "## From node detail pages (grade stated in the Type section)"
  for f in nodes/*.md; do
    n=$(basename "$f" .md)
    head=$(sed -n '/^## Type/,/^## /p' "$f")
    case "$head" in
      *'**split**'*) g=split ;;
      *'constructive_grade: needs_full_classical'*) g=needs_full_classical ;;
      *'constructive_grade: needs_DNE'*)  g=needs_DNE ;;
      *'constructive_grade: needs_LEM'*)  g=needs_LEM ;;
      *'constructive_grade: intuitionistic'*) g=intuitionistic ;;
      *'constructive_grade: n/a'*) g=n/a ;;
      *) g="" ;;
    esac
    [ -n "$g" ] && echo "$g	$n"
  done | sort | awk -F'\t' '{if($1!=p){print "";print "### "$1;p=$1} print "- "$2}'
} > "$out"

# ------------------------------------------------------- counterexample index
out=indexes/counterexample-index.md
{
  echo "# Counterexample index (generated)"
  echo
  echo "Hypothesis that cannot be dropped -> the result it guards -> the witness."
  echo
  for f in results/*.yaml; do
    n=$(sed -n 's/^node:[[:space:]]*//p' "$f")
    awk -v n="$n" '
      /^counterexamples_when_dropped:/ {inb=1; next}
      inb && /^[a-zA-Z]/ {inb=0}
      inb && /^  [a-zA-Z_]+:/ {
        line=$0; sub(/^  /,"",line);
        print "- **" n "** drop `" line "`"
      }
    ' "$f"
  done
} > "$out"

# ----------------------------------------------------------- hypothesis index
# reverse-reachability: every node that has X as a (transitive) prerequisite
out=indexes/hypothesis-index.md
{
  echo "# Hypothesis / axiom / primitive index (generated)"
  echo
  echo "For each foundational node: every node that depends on it, directly or"
  echo "transitively (reverse reachability over the prerequisite graph)."
  echo
  awk -F'\t' 'NR>1 && ($2=="hypothesis"||$2=="axiom"||$2=="primitive"||$2=="notation_convention"){print $1}' "$T" | sort | while read -r h; do
    echo "## $h"
    awk -v start="$h" '
      { radj[$1]=radj[$1] SUBSEP $2 }
      END {
        si=0; stack[si++]=start
        while (si>0) {
          cur=stack[--si]
          m=split(radj[cur], outs, SUBSEP)
          for (k=1;k<=m;k++){t=outs[k]; if(t!="" && !(t in seen)){seen[t]=1; stack[si++]=t}}
        }
        for (t in seen) print "- " t
      }' "$E" | sort
    echo
  done
} > "$out"

# ----------------------------------------------- prerequisite paths (headline)
out=indexes/prerequisite-paths.md
{
  echo "# Minimal prerequisite closures for the headline nodes (generated)"
  echo
  echo "Every (transitive) prerequisite of the node, listed in \`tsort\` order."
  echo "This is the closure, not a single chain; independent nodes may be dropped"
  echo "in practice."
  echo
  awk -F'\t' 'NR>1 && $6=="headline"{print $1}' "$T" | sort | while read -r g; do
    echo "## $g"
    awk -v goal="$g" '
      { radj[$2]=radj[$2] SUBSEP $1 }
      END {
        si=0; stack[si++]=goal
        while (si>0){cur=stack[--si]
          m=split(radj[cur],outs,SUBSEP)
          for(k=1;k<=m;k++){t=outs[k]; if(t!="" && !(t in seen)){seen[t]=1; stack[si++]=t}}}
        for(t in seen) print t
      }' "$E" > build/_prereq.$$
    grep -Fxf build/_prereq.$$ indexes/tsort-order.txt | sed 's/^/- /'
    rm -f build/_prereq.$$
    echo
  done
} > "$out"

echo "gen-indexes: ok (status, constructive-grade, counterexample, hypothesis, prerequisite-paths)"
