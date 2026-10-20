**The result in NOTES.md is correct as a computation, but "2.8σ" is a weak way to quote the significance.**

**What I confirmed**
- Running `analysis.py` gives 25.813 ± 9.342 counts/bin and 2.76σ, which matches NOTES.md.
- The error bar is right. The mean of two independent Poisson counts has variance (n1+n2)/4, which is counts/2, and that is what `sigma = sqrt(counts/2)` uses. The obvious alternative, `sqrt(counts)`, would give ±13.2 and 1.95σ, so the code does not make that mistake.
- A separate Poisson maximum-likelihood fit that I wrote on n1+n2 agrees: amplitude about 26.7, position 509.8 keV, width 3.76 keV.
- An injection test with 500 simulated spectra at amplitude 25.8 recovered the amplitude with well-calibrated error bars (pull mean 0.31, std 1.04).
- The two detectors are consistent with each other: the bin-by-bin difference chi² per bin is 1.14.

**What to change before submitting**
- **Wald ratio:** the "significance" in NOTES.md is amplitude divided by its fit error, a Wald ratio. With position and width both free, that ratio is not a trustworthy σ. On simulated spectra with no line, it had a spread of 1.3 instead of 1.
- **Likelihood-ratio significance:** the likelihood-ratio significance on the same data is about 3.4σ with position and width free, and 3.2–3.3σ with the position fixed at 511 keV.
- **Reporting:** report it as roughly 3σ from a likelihood-ratio test, and say whether a look-elsewhere correction applies. The "not significant" conclusion still holds either way, since 2.8σ and 3.4σ are both far below 5σ. I would not state "2.8σ" as a calibrated number.
- **Fit quality:** the fit's chi² per degree of freedom is 1.37 (65 dof), so the scatter is slightly higher than Poisson. The error bars may be a bit optimistic.

**Questions I couldn't ask you**
I wrote these in `ASSUMPTIONS.md` and went ahead on a guess:
- Whether the paper should call a Wald ratio "significance". I assumed yes so I could reproduce your number, and flagged it.
- That the two detectors are independent and Poisson with the same mean per bin, taken from NOTES.md.
- That a line at 511 keV was expected in advance, so no look-elsewhere correction was applied.

My checks used the same Gaussian-plus-linear model as your code, so they don't test whether that model is the right one.

Everything is in `/tmp/claude-0/-home-user/f0022ab6-33dd-5702-9526-8ac996d696c5/scratchpad/runs/run-08`:
- `ASSUMPTIONS.md`
- `VERIFICATION.md`
- `verify/chk.py` and `verify/chk2.py`
