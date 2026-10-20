# Verification report
**Verdict: NOTES.md result is WRONG. Corrected: amp = 25.8 +/- 9.3 counts/bin, 2.8 sigma (not 3.9 sigma).**

## Bug
analysis.py: counts = (n1+n2)/2, but sigma = sqrt(counts)/2. Var(mean of two Poisson) = (n1+n2)/4 = counts/2,
so sigma = sqrt(counts/2) = sqrt(counts)/sqrt(2). The code's sigma is too small by sqrt(2), so the amplitude
error is too small by sqrt(2) and the significance too large by sqrt(2): 3.9 -> 2.76. Best-fit parameters are unchanged
(a uniform rescaling of sigma does not move the minimum).
Fix: `sigma = np.sqrt(counts / 2)`.

## Checks (verify/check.py)
| Check | Result | Strength |
|---|---|---|
| Original code reproduces NOTES (25.8 +/- 6.6, 3.9) | yes | reproduction only |
| Independent route: fit summed spectrum (Poisson var = sum), halve | 25.81 +/- 9.34, 2.76 sigma | independent of the mean/sigma formula; agrees with corrected |
| Synthetic pull test, 1000 realisations, true amp 25 (similar spectrum) | code sigma: pull std 1.46 (error bars too small, expected 1.41); corrected: 1.04 | known-answer, strong |
| Data dispersion (n1-n2)^2/(n1+n2) | 1.14 ~ Poisson | supports noise model |

The pull mean is about +0.25-0.3 in both cases, which suggests a small positive bias of the fitted amplitude near
the detection threshold. Not investigated further; it is minor against the sigma factor.

## Caveats
- Assumption 5/3 in ASSUMPTIONS.md (floating mu, Wald significance, no look-elsewhere) are unconfirmed. At 2.8 sigma local
  the global significance would be lower still. 2.8 sigma is evidence, not an observation.
- Only one independent implementation (the sum fit) plus the simulation; no separate subagent reimplementations were done (budget).
