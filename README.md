# reseasrch-coding-skill

A Claude Code skill for writing (or auditing) research analysis code whose correct
result is unknown — data nobody can "check" the answer for.

## The problem

When code analyzes data with no known answer, a bug doesn't crash; it produces a
plausible-looking wrong number. A wrong array axis, a missing factor of 2, or error
bars that are too small by √2 all go unnoticed. That's where AI coding assistants
(and humans) are weakest: nothing tells them they're wrong.

## The approach

1. **Turn the unknown answer into a known one** — synthetic data with a planted
   signal, analytic limits, convergence tests, conservation laws, metamorphic
   relations, negative controls. This is the strongest evidence and comes first.
2. **Use disagreement between independent implementations to find bugs** — critical
   modules get 2–3 versions written blind to each other, with different algorithms,
   libraries and models. Disagreements are settled by hand-computed tiny cases.
   Agreement is recorded as *weak* evidence, never as proof.
3. **Write down assumptions and get the researcher to confirm them** — most research
   bugs are wrong conventions, not typos.
4. **Report honestly** — `VERIFICATION.md` says what's checked against known answers
   and what rests only on agreement.

### Why not "5 copies until they agree"?

The first draft of this idea had N Claudes implement each part and an inspector
loop until all agreed. Studies of N-version programming with LLM coding agents
find that independently generated versions still fail on the same inputs, often
because of shared spec weaknesses; voting helps only modestly. And a loop that
feeds the same inspector feedback to every version makes them agree *because they
were told the same thing*. So this skill uses independent versions as a bug
**detector**, keeps them isolated, and leans on known-answer tests for confidence.

## Modes

- **Build** — write new analysis code with verification built in.
- **Audit** — treat existing code as version 1, reimplement critical parts
  independently, and run known-answer tests against it.

**Trying it on your own research?** See [TRY-IT.md](TRY-IT.md).

## Install

```bash
git clone https://github.com/dracvar06/reseasrch-coding-skill ~/.claude/skills/research-coding
```

Claude Code picks it up automatically when you ask for research/scientific
analysis work; you can also invoke it with `/research-coding`.

## Files

| File | Purpose |
|---|---|
| `SKILL.md` | Workflow (scope → assumptions → interfaces → known-answer tests → independent versions → inspector → integration → report) |
| `references/verification-techniques.md` | Catalog of checks for simulation, statistics, ML/signal processing |
| `references/orchestration.md` | Subagent prompt template, independence and diversity rules, inspector procedure |
| `templates/ASSUMPTIONS.md` | Assumptions the researcher reviews once |
| `templates/VERIFICATION.md` | Final report |
| `evals/` | Planted-bug evaluation: toy tasks, data generators, answer keys, `run.sh`, results |

## Status

v1, not yet tried on a real research project. Round 1 of the planted-bug evaluation
(`evals/RESULTS.md`): with the skill, Claude caught 3/3 bugs and raised 0/3 false alarms,
backing each finding with known-answer checks. Plain Claude without the skill also caught
3/3, so these tasks were too easy to show whether the skill helps detection. The runs also
skipped the multi-version step. Harder tasks are the next step.

## Sources

- Avizienis, *The N-Version Approach to Fault-Tolerant Software* (1985); Knight & Leveson, *An experimental evaluation of the assumption of independence in multiversion programming* (1986)
- [N-Version Programming with Coding Agents (arXiv 2606.20158)](https://arxiv.org/pdf/2606.20158)
- [A Systematic Methodology for Evaluating Failure Independence in LLM-Generated Code (arXiv 2607.02808)](https://arxiv.org/pdf/2607.02808)
- Chen et al., metamorphic testing for the oracle problem
- Roache, method of manufactured solutions for verifying numerical code
