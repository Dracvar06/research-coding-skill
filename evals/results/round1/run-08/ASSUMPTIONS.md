# Assumptions (Audit mode; researcher unavailable, so none are `confirmed`)

| # | Assumption | Status |
|---|---|---|
| 1 | Counts per 2 keV bin, 441-579 keV, 70 bins; energy = bin centre | from-code |
| 2 | Detectors independent, each Poisson with the same mean per bin (identical detectors, same source and time) | guessed (from NOTES) |
| 3 | Combined spectrum = bin-wise mean; Var(mean) = (n1+n2)/4 = mean/2, so sigma = sqrt(mean/2) | from-code, verified by hand |
| 4 | Model: linear background + Gaussian; mu and width free; amplitude in counts/bin of the *averaged* spectrum | from-code |
| 5 | "Significance" = Wald ratio amp/err (NOTES definition), not a likelihood-ratio or global p-value | from-code; QUESTION for researcher: is a Wald ratio what the paper should call significance? Assumed yes for reproducing the number, and flagged. |
| 6 | Line expected at 511 keV; no look-elsewhere correction | guessed |
| 7 | Sigma taken from observed counts (not from model), no bin has zero counts | from-code |
