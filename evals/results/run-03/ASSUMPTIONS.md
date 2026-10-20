# Assumptions (Audit mode; researcher unavailable, so nothing is `confirmed`)
| Assumption | Status |
|---|---|
| Labels 0/1 = A/B, 40 each, rows = trials, columns = voxels | from-code |
| Chance = 50% (balanced classes) | from-code |
| Standardization, k=20 F-test selection, LogReg C=1, 5-fold stratified CV, seed 0 | from-code |
| Intended design: the claim is generalization to unseen trials, so selection/scaling must be fit on training folds only | guessed (question for researcher: is selection meant to be inside CV? Assumed yes, since otherwise accuracy is not an out-of-sample estimate) |
| Binomial test is acceptable on pooled CV predictions (folds are not strictly independent; mildly anticonservative) | guessed |
| Trials are independent (no subject/run/session grouping in the data) | guessed (question: if trials share runs/subjects, CV must be grouped) |
