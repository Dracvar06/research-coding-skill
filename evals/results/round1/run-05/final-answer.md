**The result in NOTES.md is not correct. The amplitude is right, but the uncertainty is too small, so the significance is overstated.**

**What's wrong:** the error on the combined spectrum is wrong in `analysis.py` (`sigma = np.sqrt(counts) / 2`).
- `counts` is the mean of two detectors, (n1+n2)/2.
- Each detector's count is Poisson, so the variance of the mean is (n1+n2)/4, which is `counts/2`.
- The correct error is therefore `sqrt(counts/2)`, which is `sqrt(counts)/√2`.
- The code divides by 2 instead of √2, so every bin's error is too small by a factor of √2.
- With `absolute_sigma=True`, all the fit uncertainties are then too small by √2.

**Corrected result:** I changed that one line to `np.sqrt(counts / 2)`.

| | NOTES.md | Corrected |
|---|---|---|
| Amplitude | 25.8 counts/bin | 25.8 counts/bin |
| Uncertainty | ± 6.6 | ± 9.3 |
| Significance | 3.9σ | **2.8σ** |

The best-fit values (amplitude, μ ≈ 509.7 keV, width ≈ 3.9 keV) don't change. Only the uncertainties do, and they grow by √2. Replace the NOTES.md sentence with: "We observe a line with amplitude 25.8 ± 9.3 counts/bin, a 2.8σ excess." At 2.8σ it is no longer a 3σ-level excess, so it shouldn't be described as an observation of a line.

**Assumptions:**
- The two detectors are independent, so their Poisson errors add in quadrature.
- Counts are raw, unnormalised integers, as the file header suggests.
- I did not check other choices, such as the fit window, the starting values or the fitted mean (about 509.7 keV rather than 511). I also didn't compute a look-elsewhere correction.

I left `analysis.py` unchanged. The corrected version is saved as `analysis_fixed.py` in the working directory.
