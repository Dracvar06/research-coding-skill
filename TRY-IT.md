# Trying the research-coding skill

This skill makes Claude Code verify research code whose correct output nobody knows. It
writes down its assumptions for you to confirm, tests each step against cases with a
known answer (planted signals, limiting cases, conservation laws, shuffled-label controls),
and ends with a `VERIFICATION.md` report of what was and wasn't checked.

**Honest status:** in our toy tests (`evals/RESULTS.md`), when Claude was *asked to
check* existing code, it found the planted bugs just as well without the skill. What we
haven't tested yet is the case that matters most: Claude *writing* your analysis. That's
what this trial is for.

## 1. Install (2 minutes)

You need [Claude Code](https://claude.com/claude-code). Then:

```bash
git clone -b claude/eager-archimedes-uhj3l6 https://github.com/dracvar06/reseasrch-coding-skill ~/.claude/skills/research-coding
```

(If the clone fails, ask whoever sent you this for access to the repository.)

To check it worked, start `claude` and type `/research-coding`. It should show up as
a skill.

## 2. The test (about 30 minutes)

Pick a **past analysis whose correct result you already know**, ideally one with a
step that's easy to get subtly wrong. Give Claude the data and a description of what
to compute, **but not the result**.

Run it twice, each time in a fresh `claude` session:

- **With the skill:**
  > Use the research-coding skill. Here is my data in `data/` and a description of the
  > analysis in `NOTES.md`. Write the analysis and give me the result.
- **Without the skill:** rename the folder first
  (`mv ~/.claude/skills/research-coding ~/.claude/skills/_off`), then use the same prompt
  without the first sentence. Rename it back afterwards.

Don't hint at the expected answer in either run. Compare both results with the one
you know.

*Optional:* in a third session, ask the skill to check a piece of code you're working
on now ("Use the research-coding skill in Audit mode on `my_analysis.py`").

## 3. What to send back

A few lines are enough:

1. Did each run get the right result? If not, what went wrong?
2. Did the skill run catch anything the plain run missed, or vice versa?
3. Were the questions in `ASSUMPTIONS.md` the right ones, or noise?
4. Was `VERIFICATION.md` worth reading? Would it help with a methods section?
5. Roughly how long each run took, and whether you'd use the skill again.

Please also send the `ASSUMPTIONS.md` and `VERIFICATION.md` files if you're happy to
share them.
