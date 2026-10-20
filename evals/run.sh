#!/bin/bash
# Re-run the planted-bug evaluation (9 headless Claude Code sessions).
# Usage: evals/run.sh [workdir]   (needs: claude CLI, python3 with numpy, scipy, scikit-learn)
# Set RUNS to choose runs, e.g. RUNS="yarkovsky:buggy:skill yarkovsky:buggy:base" evals/run.sh
#
# Runs happen in a temp dir OUTSIDE the repo, with opaque run names, and the skill is
# loaded from a plugin dir containing only SKILL.md + references/ + templates/, so the
# runner can't see the README, answer keys or other runs.
set -euo pipefail
REPO=$(cd "$(dirname "$0")/.." && pwd)
W=${1:-$(mktemp -d)}
echo "workdir: $W"
mkdir -p "$W/plugin/rc/.claude-plugin" "$W/plugin/rc/skills/research-coding" "$W/runs" "$W/logs"
echo '{"name":"rc","version":"0.1.0","description":"research coding skill"}' > "$W/plugin/rc/.claude-plugin/plugin.json"
cp -r "$REPO/SKILL.md" "$REPO/references" "$REPO/templates" "$W/plugin/rc/skills/research-coding/"

RUNS=${RUNS:-"evoked:buggy:skill peakfit:buggy:skill decoding:buggy:skill
evoked:buggy:base peakfit:buggy:base decoding:buggy:base
evoked:clean:skill peakfit:clean:skill decoding:clean:skill"}
: > "$W/run-map.txt"; i=0
for spec in $RUNS; do
  i=$((i+1)); id=$(printf "run-%02d" $i); IFS=: read -r t v c <<< "$spec"
  mkdir -p "$W/runs/$id"
  cp "$REPO/evals/tasks/$t/$v/"{analysis.py,NOTES.md} "$W/runs/$id/"
  gen="$REPO/evals/generators/gen_$t.py"
  if [ -f "$gen" ]; then python3 "$gen" "$W/runs/$id/data"; fi
  echo "$id $t $v $c" >> "$W/run-map.txt"
done

run_one() {
  local W=$1 id=$2 cond=$3
  local BASE="Here is my analysis for a paper: NOTES.md describes it and analysis.py is the code. Please check it's correct before I submit."
  local TAIL="Work only inside the current directory. At the end, tell me clearly whether the result in NOTES.md is correct, and if not, what is wrong and what the corrected result is."
  local TOOLS="Read,Write,Edit,Glob,Grep,Agent,Skill,Bash(python3:*),Bash(python:*),Bash(ls:*),Bash(cat:*),Bash(head:*),Bash(mkdir:*),Bash(diff:*),Bash(wc:*),Bash(cp:*)"
  local PROMPT EXTRA=()
  if [ "$cond" = skill ]; then
    PROMPT="Use the research-coding skill (Audit mode). $BASE I'm not available to answer questions during this task: wherever the skill says to ask me, write the question in ASSUMPTIONS.md, make your best assumption, and continue. $TAIL"
    EXTRA=(--plugin-dir "$W/plugin/rc")
  else
    PROMPT="$BASE I'm not available to answer questions during this task: make your best assumptions, write them down, and continue. $TAIL"
  fi
  (cd "$W/runs/$id" && timeout 3600 claude -p "$PROMPT" --permission-mode acceptEdits \
     --allowedTools "$TOOLS" --output-format stream-json --verbose "${EXTRA[@]}" \
     > "$W/logs/$id.jsonl" 2> "$W/logs/$id.err") || true
  echo "$id done"
}
export -f run_one
awk '{print $1, $4}' "$W/run-map.txt" | xargs -P 5 -n 2 bash -c 'run_one "$0" "$1" "$2"' "$W"
echo "Logs in $W/logs; grade against evals/answer-keys.md"
