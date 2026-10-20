# Verification of analysis.py

**Verdict: NOTES.md result (85.0%, p=6e-11) is NOT correct. It is an artifact of data leakage.**

## Bug
analysis.py runs StandardScaler and SelectKBest(f_classif) on all 80 trials and labels *before* cross-validation.
Picking the 20 best of 2000 voxels using the labels, then cross-validating, lets test-fold labels influence the features.

## Evidence
- Original script reproduced: 68/80, p=6.0e-11.
- Selection + scaling inside each training fold (sklearn Pipeline), 5 CV seeds: 35-41/80 (43.8%-51.3%), p=0.46-0.89. Chance level.
- Independent manual nested loop (scipy f_oneway, hand-written scaling), seed 0: 40/80 = 50.0%.
- Negative control (30 label permutations): the original (leaky) procedure gives mean accuracy 88.5% on labels that are pure noise; the nested procedure gives 51.3%.
  So the leaky pipeline "decodes" shuffled labels as well as the real ones.

## Corrected result
Nested-CV accuracy about 50% (range 44-51% over seeds; 40/80 at seed 0), p about 0.5. No evidence that condition is decodable from these data.

## Caveats
Assumptions in ASSUMPTIONS.md are unconfirmed (grouping of trials, binomial test on CV predictions). Evidence strength: the leak is demonstrated by a negative control, not just agreement between versions. Files: verify_leak.py.
