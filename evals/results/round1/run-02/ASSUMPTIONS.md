# Assumptions (Audit mode; researcher unavailable, so nothing is `confirmed`)
| # | Assumption | Status |
|---|---|---|
| 1 | Counts per 2 keV bin in each detector are independent Poisson variables with the same mean | from-code / NOTES |
| 2 | Spectrum = linear background + Gaussian; fit range 441-579 keV; mu starts at 511 | from-code |
| 3 | Significance = amp/sigma_amp (Wald, not a likelihood-ratio test; no look-elsewhere correction, mu is free) | from-code; guessed that this definition is acceptable |
| 4 | Chi-square fit with sigma from observed counts (not model) | from-code |
| 5 | Question for researcher: is the line search at fixed 511 keV or anywhere? The fit lets mu float (fitted 509.7 +/- 1.1) | guessed: reported as-is |
| 6 | Dispersion of (n1-n2)^2/(n1+n2) is 1.14, consistent with Poisson (no extra noise) | checked |
