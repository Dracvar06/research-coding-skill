# Assumptions (researcher unavailable; none confirmed — all need your review)
- from-code: labels 0=A, 1=B; 80 trials x 2000 voxels; balanced 40/40; no NaNs, no zero-variance features.
- from-code: scaling + ANOVA top-20 selection + logistic regression (C=1) are all inside the CV pipeline (refit per fold).
- from-code: StratifiedKFold(5, shuffle, seed 0); single split.
- guessed: trials are independent (no repeated subjects/runs/sessions). If trials share a subject, session or run, CV must be grouped (GroupKFold) and the binomial test's independence assumption is questionable. No grouping info is in the data folder.
- guessed: the one-sided binomial test on pooled CV predictions is the intended test (CV predictions are not strictly independent; a permutation test is more defensible).
- guessed: "cannot be decoded" is intended as "no significant evidence", not as evidence of absence.
