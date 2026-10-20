# Verification report

## Headline: line amplitude 25.8 +/- 9.3 counts/bin, 2.8 sigma
Reproduced exactly by `python analysis.py` (25.813 +/- 9.342, 2.76 sigma).

## Checks (scripts in verify/)
| Check | Result | Strength |
|---|---|---|
| Error propagation of the average, by hand: Var((n1+n2)/2) = (n1+n2)/4 = counts/2 | code's sigma = sqrt(counts/2) is correct (sqrt(counts) would give 13.2, 1.95 sigma, wrong) | analytic |
| (n1-n2)^2/(n1+n2) per bin | chi2/dof 1.14 (70 bins), detectors consistent with equal-mean Poisson | data check |
| Independent Poisson max-likelihood fit on n1+n2 (own code, chk2.py) | A = 26.7 (free mu, width), mu 509.8, width 3.76; agrees with curve_fit | independent implementation |
| Injection/recovery MC (500 realizations, A=25.8, mu 510, width 4) | pull mean 0.31, std 1.04: error bar well calibrated | known-answer |
| Null MC (A=0), same fit | pull mean 0.17, std 1.30: amp/err is over-dispersed under the null with free mu and width, so 2.8 is not a Gaussian-calibrated z | known-answer |
| Likelihood-ratio significance (Poisson) | free mu, width: 3.4 sigma; mu fixed at 511: 3.2-3.3 sigma (width 3-5 keV) | independent, differs from Wald |

## Findings
- No bug found: averaging, sigma, model, fit and printed numbers are correct and the 25.8 +/- 9.3 amplitude is right.
- Caveat: the "2.8 sigma" is a Wald ratio. The profile likelihood ratio for the same data is about 3.2-3.4 sigma (local, before any look-elsewhere correction). The Wald ratio is less reliable here because the width is poorly constrained (3.9 +/- 1.6) and the null MC shows pull std 1.3. Both are far below 5 sigma and neither supports a discovery claim, but "2.8 sigma" should not be quoted as a calibrated significance.
- chi2/dof of the fit is 1.37 (65 dof), mild excess scatter; error bars may be slightly optimistic.

## Remaining guessed assumptions
See ASSUMPTIONS.md #2, #5, #6. Independent-version evidence is on the same model, so it is weak support for the model choice itself.
