**The result in NOTES.md is not correct.** The 85.0% accuracy (68/80, p = 6e-11) comes from data leakage. Once the leak is fixed, decoding is at chance.

**What's wrong:** `analysis.py` standardizes and selects the 20 best voxels (ANOVA F-test) using all 80 trials and their labels, before cross-validation. With 2000 voxels and only 80 trials, some voxels will separate the labels by chance. Selecting them with the test-fold labels already included makes the cross-validated accuracy look high even on noise.

**How I checked:**
- **Reproduction:** your script gives 68/80 and p = 6.0e-11, as in NOTES.md.
- **Corrected pipeline:** with scaling and selection fitted inside each training fold, five CV seeds gave 35–41 correct out of 80. That is 43.8–51.3%, with p between 0.46 and 0.89.
- **Independent check:** a hand-written nested loop, without sklearn's pipeline, gave 40/80 (50.0%) at seed 0.
- **Shuffled labels:** across 30 random permutations of the labels, your original procedure averaged 88.5% accuracy on pure noise. The nested procedure averaged 51.3%. So your procedure "decodes" random labels better than it decodes the real ones.

**Corrected result:** nested-CV accuracy is about 50% (40/80 at seed 0, 44–51% across seeds), with p about 0.5. These data show no evidence that condition A vs. B can be decoded.

**Assumptions I could not confirm:** I wrote them in ASSUMPTIONS.md, since you weren't available. The main ones:
- **Selection inside CV:** I assumed feature selection is meant to happen inside CV. Otherwise accuracy isn't an out-of-sample estimate.
- **Trial grouping:** I assumed trials are independent. If they share runs or subjects, CV needs to be grouped, which could only lower the accuracy further.
- **Binomial test:** it's applied to pooled CV predictions and is slightly optimistic. This doesn't change the conclusion.

Files are in the working directory:
- ASSUMPTIONS.md
- VERIFICATION.md
- verify_leak.py
