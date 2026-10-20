# Eval results: planted-bug toy tasks (round 1)

Date: 2026-10-20. Runner: headless Claude Code (`claude -p`), default model of the environment (Sonnet 5.5), one run per cell. Setup and re-run instructions: `run.sh`. Answer keys: `answer-keys.md`. Raw outputs: `results/run-XX/` (mapping in `results/run-map.txt`).

## Summary

| Task | Skill, buggy | Plain Claude, buggy | Skill, clean twin |
|---|---|---|---|
| evoked (wrong normalization axis) | ✅ detected (run-01) | ✅ detected (run-04) | ✅ no false alarm (run-07) |
| peakfit (error bars too small by √2) | ✅ detected (run-02) | ✅ detected (run-05) | ✅ no false alarm (run-08) |
| decoding (train/test leakage) | ✅ detected (run-03) | ✅ detected (run-06) | ✅ no false alarm (run-09) |

Every run found the planted bug, located it, explained the cause and gave the corrected headline result. All three clean twins were reported as correct.

**Main conclusion: these tasks were too easy to show whether the skill helps.** Plain Claude caught all three bugs, so this round does not show the skill improving bug detection. In each task the researcher's NOTES.md described the intended method and the code visibly contradicted it, so careful reading was enough.

## What the skill did change

**1. Stronger evidence.** The skill runs backed each finding with a known-answer check, not just reasoning:

| Task | Skill run's evidence | Plain run's evidence |
|---|---|---|
| evoked | Planted a response on synthetic data with wild gains: the original code picked the wrong channel. Also checked gain/offset invariance. | Baseline statistics per channel; reran with the fix. |
| peakfit | Pull test over 1000 synthetic spectra: pull SD 1.46 with the original errors, 1.04 fixed (√2 ≈ 1.41 predicted). Also an independent summed-spectrum fit. | Derivation of the variance; reran with the fix. |
| decoding | Shuffled-label control: the original procedure "decodes" random labels at 88.5%, the nested version at 51.3%. Also a hand-written nested-CV loop. | Pipeline fix plus a 200-permutation null for the corrected pipeline. |

The plain runs were also good: the decoding baseline ran its own permutation test.

**2. Written assumptions and a report.** Every skill run produced ASSUMPTIONS.md and VERIFICATION.md. They marked their own reimplementation as weak evidence ("same author/spec"), as the skill asks.

**3. Methodological caveats on the clean twins.** None of these changes the computed result:
- **run-08 (peakfit):** argued that amplitude/error is a Wald ratio, which is not a calibrated significance with the position and width floating. It reports a likelihood-ratio significance of about 3.4σ and suggests saying whether a look-elsewhere correction applies. *I have not verified the 3.4σ figure.*
- **run-09 (decoding):** "cannot be decoded" overclaims a null result. It estimated the power (d = 0.5 gives only about 59% accuracy at n = 80), noted the binomial test on CV predictions is approximate, and suggested averaging over CV splits.
- **run-07 (evoked):** the latency is only good to tens of ms, and peak/SNR selected as maxima are slightly optimistic.

These are useful, but each is something the researcher has to weigh.

**4. Cost.** Average cost on the buggy tasks was about $0.15 per skill run against $0.09 per plain run. Run time was 59–90 s against 24–72 s.

## What the skill did *not* do (compliance)

- **No independent versions:** no skill run spawned subagents, so Step 4 was skipped. The runs wrote at most one reimplementation themselves; run-09 explicitly decided none was needed for a standard sklearn pipeline.
- **No reference files:** no run opened `references/verification-techniques.md`, `references/orchestration.md` or the templates. Only the main SKILL.md body was used.
- **Model knowledge, not the catalog:** the runs still chose good known-answer techniques (pull test, shuffled labels, planted signal), so the model already knows them. The catalog didn't have to be read for that.
- **Short runs:** 9–13 turns each.

On scripts this size, the lighter behaviour was enough. It also means the multi-version machinery, the core of the original idea, has not been tested at all.

## Proposed changes (not applied — for discussion)

1. **Harder eval tasks for round 2.** These are what can actually show whether the skill helps:
   - bugs where NOTES.md is silent about the convention, so there's no spec-vs-code mismatch to read off (e.g. one-sided FFT amplitude missing a factor 2, bin edges off by one, `ddof` mismatch);
   - a bug buried in a longer multi-file pipeline;
   - code that matches the notes, but the notes' method is subtly wrong (e.g. a correction applied twice).
2. **Scale the workflow to the size of the analysis.** Say explicitly that for short single-file analyses, one self-written reimplementation plus known-answer tests is enough. Keep the subagent versions for larger or more opaque pipelines. This matches what the runs did and what worked.
3. **Make the catalog actually get read.** Add a first action to Step 3: "Read `references/verification-techniques.md` and pick at least one technique per module". Alternatively, move a short checklist of the key techniques into SKILL.md.
4. **Check triggering.** Every run was told to "use the research-coding skill", so it hasn't been tested whether the skill triggers on its own.

## Caveats

- The bugs were planted by the same assistant that wrote the skill, so they may be biased toward bug types the skill already covers.
- One run per cell on Sonnet 5.5: these results are anecdotes, not statistics. Opus/Fable may behave differently.
- **Containment:** runners worked in copies outside the repo. One run (run-05) wrote a scratch file one directory up, and one (run-08) listed the parent directory; neither read the answer keys or the README. The answer keys were written only after all runs had finished.
