# Decoding condition A vs. B from voxel patterns

80 trials (40 per condition), 2000 voxel features per trial (`data/features.npy`,
labels in `data/labels.npy`).

Pipeline: standardize features, keep the 20 most informative voxels (ANOVA F-test), and
classify with logistic regression using 5-fold stratified cross-validation. Accuracy is
tested against chance (50%) with a one-sided binomial test.

## Result for the paper
Condition can be decoded well above chance: 85.0% accuracy (68/80), p = 6e-11.
Run: `python analysis.py`
