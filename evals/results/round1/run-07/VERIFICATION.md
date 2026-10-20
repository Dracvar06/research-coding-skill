# Verification report
**Headline:** "Channel 2, 1.01 z at 124 ms, SNR 7.3" -> **reproduced and judged correct.**

| Check | Result | Strength |
|---|---|---|
| analysis.py rerun | ch2 1.01 z, 124 ms, SNR 7.3 | - |
| Independent reimplementation (per-channel loop, explicit sample indices; /scratchpad/v2.py) | identical amp/latency/SNR for all 8 channels | weak (agreement; same author spec) |
| Metamorphic: per-channel gain/offset change | z-scores unchanged | strong |
| Planted signal (0.8 SD box on ch5 in synthetic data with the same gains/offsets) | ch5 recovered (0.97 z), others at noise level ~0.3 | strong |
| Null (sign-flip of baseline trials, max over 100 samples) | 99.9th pct = 0.57 z; ch2 peak 1.01 and all other channels (<=0.33) fall at or below noise | strong |
| Data inspection | ch2 has a consistent positive deflection ~84-170 ms in nearly every trial (window means mostly >0); no NaNs; no outliers | moderate |

Disagreements between versions: none. Window edge: 50 ms falls between samples (sample 112 = 48 ms excluded, 113 = 52 ms first); 200 ms included; no effect on result.

Caveats for the paper (not errors):
- Other channels' "peaks" (0.17-0.33 z, SNR 1.2-2.6) are noise maxima; only ch2 shows a response. Say so rather than ranking them.
- The 124 ms latency is the maximum of a broad plateau (~85-170 ms), so latency is imprecise (a few tens of ms).
- Peak and SNR are selected maxima, hence slightly optimistic; irrelevant for ch2 given the 7 sigma margin.
- z is in units of single-trial baseline SD, so 1.01 z is not a physical amplitude (ch2 has the smallest raw gain).

Remaining guessed assumptions: #6, #7 in ASSUMPTIONS.md.
