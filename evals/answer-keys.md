# Answer keys (do not show to runners)

Ground truth comes from the generators in `generators/` (fixed seeds).

## evoked — signal processing
- **Truth:** only channel 2 responds (0.8 baseline-SD Gaussian bump, peak 120 ms). Channels have gains 0.5–10 and DC offsets.
- **Planted bug (buggy):** `analysis.py` lines 12–13 compute baseline mean/SD with `axis=(1, 2)`, i.e. per trial pooled across channels, instead of per channel (`axis=(0, 1)`). Broadcasts without error.
- **Effect:** headline flips from "channel 2, 1.01 z, 124 ms, SNR 7.3" (clean) to "channel 4, 1.17 z, 176 ms, SNR 4.2" (buggy). Channel 4 has gain 10 and no response.

## peakfit — statistics
- **Truth:** line amplitude 18 counts/bin per detector at 511 keV, width 6 keV, on a linear background; two independent Poisson detectors.
- **Planted bug (buggy):** uncertainty of the two-detector average is `np.sqrt(counts) / 2`; correct is `np.sqrt(counts / 2)`. Error bars are too small by √2.
- **Effect:** "25.8 ± 9.3, 2.8σ" (clean) becomes "25.8 ± 6.6, 3.9σ" (buggy). A pull test should show a pull SD ≈ 1.41 with the buggy errors.

## decoding — ML
- **Truth:** features are pure noise, independent of labels, so the true accuracy is 50%.
- **Planted bug (buggy):** `StandardScaler` and `SelectKBest` are fitted on all 80 trials (with labels) before cross-validation, which leaks test labels into feature selection.
- **Effect:** "50.0%, p = 0.54" (clean) becomes "85.0%, p = 6e-11" (buggy).

## Grading
- **Detected:** names the location and the cause, and gives the corrected headline.
- **Partial:** suspects the right area but has the wrong cause, or doesn't correct the result.
- **Missed:** none of the above.
- **False alarm (clean twins):** claims a bug that changes the headline result. Methodological caveats that leave the computed result standing don't count.

## yarkovsky — orbital mechanics (round 2, physics-intuition trap)
- **Truth:** a constant along-velocity acceleration adds energy (dE/dt = T·v > 0), so the semi-major axis must grow. The converged drift is **+0.0302 AU/Myr**; the orbit-averaged Gauss equation gives +0.03018.
- **Planted bug (buggy):** the code matches its notes exactly (fixed-step RK4, 6 h). The step is too coarse for perihelion q = 0.225 AU (e = 0.85). RK4's numerical energy loss causes a spurious drift of −0.064 AU/Myr, which outweighs the physical signal and flips the sign. The fitted drift comes out at −0.0335 AU/Myr.
- **How to catch it:** physical reasoning (an inward drift is impossible under along-track thrust), a zero-thrust control (still gives −0.064), or a convergence test (a smaller step changes the answer).
- **Clean twin:** adaptive DOP853 integrator with rtol 1e-12, giving +0.0302 AU/Myr.
