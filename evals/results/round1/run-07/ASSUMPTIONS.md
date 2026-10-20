# Assumptions (Audit mode; researcher unavailable, so nothing is "confirmed")
| # | Assumption | Status |
|---|---|---|
| 1 | Data axes are (trials, time, channels); 300 samples = 1.2 s at 250 Hz; stimulus at sample 100 (t=0) | from-code, consistent with NOTES |
| 2 | Baseline = samples 0-99; z-score uses the pooled (trials x time) mean and population SD (ddof=0) per channel | from-code |
| 3 | Window 50-200 ms inclusive = samples 113..150 (52-200 ms; sample 112.5 is not a sample) | from-code |
| 4 | "Strongest" = largest |peak| of the trial-averaged z-score; positive/negative both count | from-code |
| 5 | SNR = |peak| / SD of the trial average over t<0 (ddof=0) | from-code |
| 6 | Question for researcher: is comparing channels in baseline-SD (z) units the intended criterion, rather than raw amplitude? Assumed yes, as NOTES says | guessed |
| 7 | No artifact rejection; no NaNs in data (checked); max |z| per channel ~4, no gross outliers | guessed |
