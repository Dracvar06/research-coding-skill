# Decoding condition A vs. B from voxel patterns

80 trials (40 per condition), 2000 voxel features per trial (`data/features.npy`,
labels in `data/labels.npy`).

Pipeline: standardize features, keep the 20 most informative voxels (ANOVA F-test), and
classify with logistic regression using 5-fold stratified cross-validation. Accuracy is
tested against chance (50%) with a one-sided binomial test.

## Result for the paper
Condition cannot be decoded above chance: 50.0% accuracy (40/80), p = 0.54.
Run: `python analysis.py`
