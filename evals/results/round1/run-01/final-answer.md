**The result in NOTES.md is not correct. Don't submit it as written.**

**What is wrong**
- `analysis.py` lines 12–13 compute the baseline mean and SD with `axis=(1,2)`. That gives one mean and SD per trial, pooled across all 8 channels.
- NOTES.md says each channel is z-scored against its own baseline, so the code doesn't do what the notes describe.
- Your channels have very different gains and offsets: baseline SD runs from about 0.5 to 10, and baseline mean from about −2 to 3.9.
- Pooling across channels leaves those differences in place. Channel 4, with SD about 10 and mean about 3.9, comes out as the biggest "response" only because of its gain and offset.

**Corrected result**
I wrote an independent version with a per-channel baseline in `verify/v2.py`, and tried the baseline per trial and pooled over trials. The two give the same winner and nearly the same numbers:

| | Amplitude | Latency | SNR |
|---|---|---|---|
| Channel 2, baseline pooled over trials | 1.01 z | 124 ms | 7.3 |
| Channel 2, baseline per trial | 1.02 z | 124 ms | 7.4 |

- **Runner-up:** the next strongest channel is channel 1 at −0.33 z, so channel 2 is about 3 times stronger than any other.
- **Channel 4:** it drops to −0.27 z with SNR about 2.2, which is noise level.
- **Fix:** change `axis=(1,2)` to `axis=(0,1)`, which gives a per-channel baseline pooled over trials, or to `axis=1`, which gives it per trial. I did not edit `analysis.py`.

**How I checked it**
- **Planted-signal test (`verify/test_known.py`):** I put a known 120 ms response in channel 2 of synthetic data with wildly different gains and offsets. My version finds channel 2, but the current `analysis.py` picks channel 4.
- **Gain/offset invariance:** my version gives identical results when the data is scaled and shifted (x·3+7), as a correct z-score should. I didn't run `analysis.py` through this check.

**Caveats**
- I couldn't ask you questions, so I assumed the per-channel normalization in NOTES.md is what you intended. That and the other assumptions are in `ASSUMPTIONS.md`. The 50–200 ms window and the SNR definition (peak over the SD of the pre-stimulus average) I took from the code without confirmation.
- The reimplementation is mine, so it isn't a fully independent second opinion. The strongest evidence is the planted-signal test plus the bug being visible directly in the baseline statistics.
- The full write-up is in `VERIFICATION.md`.
