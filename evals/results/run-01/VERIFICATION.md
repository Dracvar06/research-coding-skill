# Verification

**Headline (NOTES.md): "Channel 4, 1.17 z at 176 ms, SNR 4.2" is INCORRECT.**

## Bug
analysis.py:12-13 computes `mu`/`sd` with `axis=(1,2)` -> one mean/SD per trial pooled over ALL channels,
not per channel. With channels of very different gain/offset (baseline SD 0.5 ... 10, means -2 ... 3.9)
the z-scoring does not equalise channels, so the high-gain/offset channel 4 (SD ~10, mean 3.9) wins.
Fix: `axis=(0,1)` (per channel, pooled over trials) or `axis=1` (per trial per channel).

## Corrected result (independent reimplementation verify/v2.py, both baseline variants agree)
Channel 2: 1.01 z (pooled) / 1.02 z (per-trial) at 124 ms, SNR 7.3 / 7.4.
Next best: ch1 -0.33 z, ch3/ch0/ch6 ~0.3 z. Channel 4 becomes -0.27 z, SNR 2.2 (noise level).
Channel 2 is far above the rest (3x), so the winner is robust to the baseline-variant choice.

## Checks
| Check | Result |
|---|---|
| Planted-signal test (ch2, 120 ms, random gains/offsets), verify/test_known.py | v2 recovers ch2; **analysis.py picks ch4 (wrong)** |
| Gain/offset invariance (x*3+7) | v2 passes (analysis.py would not) |
| Independent version vs analysis.py on real data | disagree; cause = bug above (evidence: hand-checkable from baseline stats) |

Caveats: v2 was written by me (not fully independent of my reading of the bug); the window/SNR definitions are from-code and unconfirmed. SNR uses a 100-sample noise estimate of the trial average, so values are approximate. Original analysis.py not modified.
