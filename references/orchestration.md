# Orchestrating independent implementations

How to run the independent-version step (Step 4) and the inspector (Step 5)
without destroying the independence that makes them useful.

## Independence rules

1. **Clean context per implementer.** Launch each version as its own subagent.
   Its prompt contains only: the module interface, the relevant ASSUMPTIONS.md
   entries, the math/method description, and the approach it must use.
2. **Never share** another version's code, the researcher's code (Audit mode),
   test expected values, or the outputs of other versions.
3. **No shared feedback loops.** When the inspector finds a bug, fix the
   affected version in place. Don't broadcast "the insight" to all implementers
   and regenerate — that converts independence into agreement-by-instruction.
4. **Spec changes are the exception.** If a disagreement reveals a spec
   ambiguity and the researcher resolves it, update ASSUMPTIONS.md; then each
   version is updated to the new spec (the spec is shared by design).
5. **Flat orchestration.** The main agent launches all implementers and acts as
   (or launches) the inspector. Don't rely on subagents spawning their own
   subagents.

## Forcing diversity

Correlated mistakes are the main weakness of LLM N-version programming, so make
versions differ along as many axes as practical:

| Axis | Examples |
|---|---|
| Algorithm | closed-form vs. iterative optimizer; FFT vs. direct convolution; analytic Jacobian vs. finite differences; vectorized vs. explicit loops |
| Library | numpy vs. scipy vs. pure Python; statsmodels vs. hand-written likelihood; PyTorch vs. scikit-learn |
| Model | e.g. one version by the main model, one by a different model (`model` parameter on the Agent tool) |
| Formulation | work in log space vs. linear; per-sample vs. batched; different but equivalent parametrization |

Assign an explicit approach to each implementer — don't leave it to chance.
Model routing is for diversity first and cost second; small modules are not
automatically easy (a one-line normalization can carry the headline bug).

## Implementer prompt template

```
You are implementing ONE module of a research analysis, independently.
You will not see any other implementation. Do not search the repository for
other implementations of this module, and do not read files under verify/ or
the existing analysis code.

Module: <name>
Interface (must match exactly):
<signature, input/output shapes, dtypes, units>

Assumptions (from ASSUMPTIONS.md, authoritative):
<relevant entries>

Method description:
<the math / procedure in words and equations>

Required approach for THIS version: <e.g. "pure numpy, closed-form solution,
no scipy.optimize">

Write the implementation to <verify/<module>_vN.py>. Include a docstring that
lists any choice you had to make that the assumptions did not specify — these
are important, do not hide them. Do not write tests and do not run the full
analysis.
```

## Inspector procedure (Step 5)

For each module with ≥2 versions:

1. Run all versions on the same inputs: real data, synthetic known-answer data,
   edge cases. Compare with a stated tolerance (e.g. `rtol=1e-8` for
   deterministic linear algebra, statistical tolerance for stochastic code
   with fixed seeds).
2. For each mismatch:
   - shrink to the smallest failing input
   - construct a 2–5 point case and compute the correct answer **by hand**, step
     by step, in writing, before looking at which version is "closer"
   - classify: **bug** / **spec ambiguity** / **numerical tolerance**
3. Bug → minimal fix to that version, add the tiny case as a regression test.
   Spec ambiguity → ask the researcher (one concise question with the options
   and their consequences), update ASSUMPTIONS.md.
   Tolerance → document the expected magnitude and why.
4. Collect the "choices I had to make" from each version's docstring. Any choice
   that differs between versions is a candidate spec ambiguity even if outputs
   happened to agree on the test data.
5. Limit: ~3 fix rounds per module. If still unexplained, stop and report it as
   an open issue.

Majority vote is **not** a resolution: two versions agreeing against one does not
show the two are right.

## Which version ships?

The production code is one version (in Audit mode, usually the researcher's own,
fixed if needed). The others stay in `verify/` as cross-check tools and can be
re-run when the analysis changes.
