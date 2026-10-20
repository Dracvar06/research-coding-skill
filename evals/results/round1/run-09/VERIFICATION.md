# Verification of NOTES.md result

**Verdict: the numbers are correct and reproducible; the wording "cannot be decoded above chance" is stronger than the evidence supports.**

## Checks
| Check | Result | Strength |
|---|---|---|
| Re-run analysis.py | 40/80 = 50.0%, p = 0.544 (NOTES: 0.54) | reproduces |
| Leakage audit | scaler and feature selection are inside the pipeline, refit per fold: no leakage. Contrast: selecting on all data first gives a spurious 85% on the same data | known-answer (negative control) |
| Planted signal (synthetic, 20 voxels shifted by d, same pipeline) | d=0: 48.6%; d=0.5: 59%; d=1.0: 95% | known-answer |
| Seed sensitivity (20x repeated 5-fold, real data) | mean 48.5% (SD 10% per fold); k=100: 51%; k=2000: 47% | consistent with chance |
| Univariate F-tests on real data | min p = 0.0009 over 2000 voxels, about what noise gives | consistent with null |

Not done: independent reimplementation (pipeline is standard sklearn, no custom math; the planted-signal and leakage tests cover it).

## Issues
1. Overstated claim. Power is limited: with 80 trials, a per-voxel effect of d=0.5 over 20 voxels gives only ~59% accuracy, and the binomial test needs at least 48/80 (60%) for p<0.05. Write "no significant decoding (50.0%, p = 0.54); with n=80 the analysis is sensitive only to fairly strong effects", not "cannot be decoded".
2. The printed 50.0% depends on the single CV split; repeated CV gives 48.5%. Report that or a permutation test.
3. The binomial test treats CV predictions as independent trials; a permutation test is safer. This does not change the conclusion (null).
4. Unconfirmed assumption: trials are independent (see ASSUMPTIONS.md).
