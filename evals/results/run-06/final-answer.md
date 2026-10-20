**The result in NOTES.md is not correct. Don't submit it.**

**What's wrong:** `analysis.py` has a feature-selection leak. It standardizes and runs `SelectKBest(f_classif, k=20)` on all 80 trials, using the labels, before cross-validation starts. The 20 voxels are therefore picked with knowledge of the test trials' labels. With 2000 noise-like features and only 80 trials, some voxels will separate the two classes by chance, so cross-validation then scores high on data that carries no real signal.

**Corrected result:** I put the scaler, selection and classifier in one `Pipeline`, so they are re-fit on each training fold only, and re-ran the cross-validation.
- Accuracy is 43.8–51.3% (35–41 of 80 trials) across 5 different CV shuffles. That is chance level.
- The one-sided binomial p-values are 0.46–0.89, so none is significant.
- For comparison, 200 label permutations through the same pipeline gave a mean accuracy of 50.9% and a 95th percentile of 62.5%. Your 85% would be far outside that range if it were real, but the leak-free pipeline never gets near it.
- The data don't show that condition A vs. B can be decoded.

**Assumptions:**
- I kept the other settings the same: 20 voxels, logistic regression with C=1, and 5-fold stratified CV.
- I used the same `random_state=0` for the CV split and tried 4 other seeds as a check.
- I didn't edit `analysis.py` or NOTES.md. I'd fix `analysis.py` by replacing the scaler, selection and classifier with `make_pipeline(StandardScaler(), SelectKBest(f_classif, k=20), LogisticRegression(...))` and passing that to `cross_val_predict`.

My check scripts are in the scratchpad: `/tmp/claude-0/-tmp-claude-0--home-user-f0022ab6-33dd-5702-9526-8ac996d696c5-scratchpad-runs-run-06/f0022ab6-33dd-5702-9526-8ac996d696c5/scratchpad/fix.py`.
