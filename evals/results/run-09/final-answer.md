The numbers in NOTES.md are correct, but "Condition cannot be decoded above chance" claims more than the data supports. I'd reword it before you submit.

**What I checked**
- **Reproduction:** `python analysis.py` gives 40/80 = 50.0% and p = 0.544, matching NOTES.md.
- **Leakage:** there is none. Scaling and the top-20 voxel selection sit inside the cross-validation pipeline and are refit on each training fold. For contrast, selecting voxels on all the data first gives a spurious 85% on this same data. Your pipeline avoids that.
- **Planted signal:** I added a shift to 20 voxels in synthetic noise and ran the same pipeline. With no shift it gave 48.6%. A modest shift (d = 0.5) gave only 59%, and a strong one (d = 1.0) gave 95%.
- **Seed sensitivity:** across 20 repeats of the 5-fold split, the real data averages 48.5%. Using 100 voxels gives 51% and using all 2000 gives 47%, so it is consistent with chance.
- **Univariate tests:** the smallest p-value across 2000 voxels is 0.0009, about what pure noise gives.
- **Not done:** I didn't write an independent reimplementation, because the pipeline is standard sklearn with no custom math. The leakage and planted-signal tests cover it instead.

**What to fix in the wording**
1. **Absence claim:** the result shows no significant decoding, not that decoding is impossible. With 80 trials, a modest effect (d = 0.5) reaches only about 59%, and you need at least 48/80 correct (60%) to get p < 0.05. Suggested text: "No significant decoding (50.0%, 40/80, p = 0.54); with n = 80 the analysis is sensitive only to fairly strong effects."
2. **Single split:** the 50.0% comes from one cross-validation split with seed 0. Repeating the split gives about 48.5%, so consider reporting that figure instead.
3. **Binomial test:** it treats the pooled cross-validated predictions as independent trials, which they are not strictly. A permutation test is safer. It won't change the conclusion here.

I couldn't ask questions, so I recorded my assumptions in `ASSUMPTIONS.md`. The main one for you to confirm is that trials are independent. If they share a subject, session or run, cross-validation needs to be grouped, and the result could change.

Files are in `/tmp/claude-0/-home-user/f0022ab6-33dd-5702-9526-8ac996d696c5/scratchpad/runs/run-09`:
- ASSUMPTIONS.md
- VERIFICATION.md
