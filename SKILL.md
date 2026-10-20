---
name: research-coding
description: Write or audit research/scientific analysis code whose correct output is unknown (no ground truth to compare against) — numerical simulations, statistical fits and inference, ML or signal-processing pipelines on experimental or observational data. Use when the user is analyzing data for a paper, thesis or experiment, asks to "check my analysis code", "make sure this simulation is right", "reimplement this analysis", or otherwise needs results they cannot verify by eye. Builds known-answer tests, writes independent implementations of critical parts to catch bugs by disagreement, and produces a VERIFICATION.md report. Not for ordinary app/web development where expected behavior is known.
---

# Research coding: correct code when nobody knows the right answer

Research code often produces a number nobody can check. A wrong axis, a missing
factor of 2, or an underestimated error bar produces a plausible-looking result,
and nothing fails. This skill exists to make those bugs visible.

## Core principles (read before every step)

1. **Turn the unknown answer into a known one.** The real data has no ground truth,
   but synthetic data, limiting cases, and invariants do. Most verification effort
   goes here — it is stronger evidence than anything else in this skill.
2. **Disagreement finds bugs; agreement proves little.** Independent LLM-written
   implementations share failure modes (same training, same spec, same blind spots).
   When versions disagree, there is a bug or an ambiguity — always investigate.
   When they agree, record it as *weak* evidence, never as proof.
3. **Protect independence.** Implementers never see each other's code or each
   other's feedback. Never send one "insight" to all versions and have them
   rewrite — that makes them agree for the wrong reason.
4. **Most research bugs are wrong assumptions, not typos.** Units, normalization
   conventions, which axis, biased vs. unbiased estimators, log base, inclusive vs.
   exclusive bins. Write them down and get the researcher to confirm them.
5. **Report honestly.** The final report says which parts are checked against a
   known answer and which rest only on agreement or on unconfirmed assumptions.

## Step 0 — Scope

- Decide the **mode**:
  - **Build**: write new analysis code.
  - **Audit**: the researcher already has code; treat it as "version 1" and
    cross-check it with independent reimplementation(s) plus known-answer tests.
- Identify the **headline result(s)**: the number(s), plot(s) or claim(s) that will
  go into the paper. Everything on the path to them is high priority.
- Identify the field profile(s) — simulation, statistical analysis, ML/signal
  processing — to pick techniques from `references/verification-techniques.md`.

## Step 1 — Assumptions (one review by the researcher)

Create `ASSUMPTIONS.md` in the project from `templates/ASSUMPTIONS.md`. Fill in
every convention the code will depend on: units, coordinate/axis conventions,
normalizations, statistical model and noise model, estimator choices, data
cleaning/cut rules, edge cases (NaN, empty bins, zero variance), random seeds,
and anything you had to guess.

Mark each assumption as `confirmed`, `guessed`, or `from-code` (Audit mode: read
off the existing code). Then **stop and ask the researcher to review it once**.
Do not write analysis code before this review, except quick exploration of the
data format.

After this review, only interrupt the researcher again when an independent-version
disagreement turns out to be a spec ambiguity (Step 5).

## Step 2 — Decompose with explicit interfaces

Split the analysis into modules (typically 3–10). For each module define:
- function signature, input/output **array shapes, dtypes, units**
- what it assumes (link to ASSUMPTIONS.md entries)
- whether it is **critical** (see rule below)

Write these interfaces into a short `INTERFACES.md` (or docstrings in a stub
file). Shared interfaces keep names and shapes consistent across independent
versions — no separate "name-sync" agent is needed. Use a linter/type checker if
the project has one.

**Critical-module rule** (the researcher may override):
- a module is critical if it is on the path to a headline result **and** a bug
  in it would shift that result, **or**
- no known-answer test is possible for it (e.g. no synthetic-data or limiting-case
  check can exercise it).

Non-critical modules: one implementation + known-answer tests.
Critical modules: 2–3 independent implementations + known-answer tests.

## Step 3 — Known-answer tests first

Before (or alongside) implementing, write tests whose expected output is known
**without trusting the code under test**. Pick from
`references/verification-techniques.md`; aim for at least one per module and
at least one end-to-end test. Common choices:

- **Synthetic data with a planted signal** → the pipeline must recover it.
  For uncertainties, repeat over many synthetic realizations and check the pull
  distribution / coverage (error bars are where silent bugs hide).
- **Analytic limits and closed forms** → set a parameter to 0/∞/1 where the answer
  is known.
- **Convergence / manufactured solutions** for numerical solvers.
- **Invariants**: conservation laws, symmetries, units, normalization (sums to 1),
  permutation invariance.
- **Metamorphic relations**: "doubling the input amplitude doubles the fitted
  amplitude", "shifting time by Δ shifts the peak by Δ".
- **Negative controls**: shuffled labels → chance accuracy; pure-noise input →
  no detection.

Write expected values from first principles in the test, never by running the
code and pasting its output.

If a test is too expensive (slow simulation, many realizations), use the cheap
fallback listed in the techniques reference and note it in the report.

## Step 4 — Independent implementations of critical modules

For each critical module, create 2–3 independent versions using subagents
(Agent/Task tool). Follow `references/orchestration.md` exactly — it has the
prompt template and independence rules. In short:

- each implementer receives **only** the module's interface, the relevant
  ASSUMPTIONS.md entries, and a description of the math — never another version's
  code, never the researcher's code in Audit mode, never the tests' expected values
- make the versions **diverse on purpose**: different algorithm (closed-form vs.
  iterative, FFT vs. direct sum), different library (numpy vs. scipy vs. pure
  Python), and different models where available
- each version lives in its own file, e.g. `verify/<module>_v2.py`

In **Audit mode**, the researcher's existing code is version 1; write 1–2 more.

## Step 5 — Differential run and the inspector

Run all versions on: the real data, the synthetic known-answer data, and edge
cases. Compare outputs with a tolerance justified by numerics (state it).

For **every** disagreement, act as the inspector:
1. Shrink it: find the smallest input that still shows the difference.
2. Build a **tiny case you can compute by hand** (2–5 data points) and work out
   the correct answer step by step, independently of all versions.
3. Classify the cause and act:
   - **Bug** in one or more versions → fix that version in place (minimal change).
     Add the tiny case as a regression test.
   - **Spec ambiguity** (versions made different, defensible choices) → ask the
     researcher, update ASSUMPTIONS.md, then align the versions.
   - **Numerical tolerance** (different but both correct within precision) →
     document the expected size of the difference and why.

Do not ask implementers to rewrite from scratch using shared feedback.

Agreement on the real data after this step is still weak evidence — record it
as such.

## Step 6 — Integration

Run an end-to-end known-answer test on the whole pipeline (e.g. inject a signal
into realistic synthetic data, run everything, recover it). Bugs often hide at
module boundaries: unit conversions, shape transposes, off-by-one in bin edges.

## Step 7 — Report

Create `VERIFICATION.md` from `templates/VERIFICATION.md`. It must include:
- the headline results and which checks support each one
- a table of modules × checks (known-answer, invariant, metamorphic, independent
  versions) with pass/fail and evidence strength
- every disagreement found, its cause, and how it was resolved
- remaining `guessed` assumptions
- **modules verified only by agreement** (weaker evidence), clearly flagged
- checks skipped or downgraded for cost, and why

## Stopping rule

Stop only when **all** of these hold:
- every module has at least one passing known-answer test or invariant check
  (or is explicitly flagged in the report as lacking one)
- every disagreement between versions has been explained and resolved
- the end-to-end known-answer test passes
- no assumption on a headline-result path is still `guessed` without being
  flagged in the report

Agreement between versions alone never satisfies the stopping rule.

## Budget guidance (moderate default)

- 1 implementation + tests for non-critical modules
- 2 independent versions for critical modules; 3 only for the module(s) the
  headline result depends on most
- at most ~3 inspector/fix rounds per module; if a disagreement is still
  unexplained, stop and report it instead of looping
