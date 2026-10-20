# Verification report — <project name>

Mode: Build / Audit · Date: <date> · Code version: <commit>

## Summary
<2–4 sentences: what was verified, how strongly, and the most important caveat.>

## Headline results and their support
| Result | Supported by | Evidence strength |
|---|---|---|
| <e.g. fitted amplitude A = 3.2 ± 0.4> | <injection–recovery, pull test, 2 independent versions> | strong / moderate / weak |

Evidence strength:
- **strong** — known-answer test(s) on the full path pass (including uncertainties if reported)
- **moderate** — known-answer tests on some modules + invariants; the rest by independent versions
- **weak** — relies only on agreement between versions or on unconfirmed assumptions

## Modules × checks
| Module | Critical | Known-answer | Invariants / metamorphic | Independent versions | Result |
|---|---|---|---|---|---|
| | yes/no | <test name: pass/fail> | | <n versions, agree/disagree> | |

## Disagreements found
| # | Module | Symptom | Hand-computed case | Cause (bug / spec / tolerance) | Resolution |
|---|---|---|---|---|---|

## Modules verified only by agreement (weaker evidence)
- <module> — why no known-answer test was possible

## Remaining assumptions not confirmed by the researcher
- <ASSUMPTIONS.md id> — <assumption> — impact if wrong

## Checks skipped or reduced for cost
- <check> — <what was done instead> — <consequence for confidence>

## Open issues
- <unexplained disagreements, failing checks, anything the researcher should know>

## How to re-run
```
<commands to re-run the tests and the version cross-checks>
```
