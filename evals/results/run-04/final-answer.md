**The result in NOTES.md is wrong.** Channel 4 is not the responding channel. The corrected result is channel 2, at 1.02 z, 124 ms, SNR 7.4.

**The bug** is in `analysis.py`, in the baseline z-scoring:

```python
mu = baseline.mean(axis=(1, 2), keepdims=True)
sd = baseline.std(axis=(1, 2), keepdims=True)
```

Axes 1 and 2 are time and channels. So each trial is normalised by one mean and one SD pooled across all 8 channels. NOTES.md says each channel should be z-scored against its own baseline, because the amplifiers have different gains and offsets.

The data confirm this. The baseline SDs differ widely: channel 4 has SD ≈ 10 and mean ≈ 3.9, while channel 2 has SD ≈ 0.5. Pooling gives these channels almost no normalisation of their own. Channel 4 keeps its large raw variance and offset, so it looks like a big "response" of 1.17 z at 176 ms. Channel 2 is divided by a pooled SD that is far too large for it, so its real response shrinks.

**The fix** is to compute the baseline statistics per channel, with `axis=1` (per trial and channel) or `axis=(0, 1)` (pooled over trials). I ran both:

| Channel | Amplitude (z) | Latency (ms) | SNR |
|---|---|---|---|
| 2 | 1.02 | 124 | 7.4 |
| next strongest (ch 1) | −0.35 | 112 | 2.8 |
| channel 4 after the fix | −0.27 | 172 | 2.2 |

Pooling over trials (`axis=(0, 1)`) gave 1.01 z and SNR 7.3 for channel 2, with the same latency. Channel 2 is the clear winner either way.

**Correct text for the paper:** "Channel 2 shows the strongest evoked response (1.02 z at 124 ms, SNR 7.4)."

**Assumptions:**
- I took the NOTES.md description (per-channel baseline z-scoring) as the intended method.
- I chose per-trial, per-channel normalisation because it is the smallest change to the code.
- I did not edit `analysis.py` or NOTES.md. To apply the fix, change both `axis=(1, 2)` to `axis=1` and update the result line.

I only checked the z-scoring step. I did not review the window or SNR definitions beyond confirming they match the notes.
