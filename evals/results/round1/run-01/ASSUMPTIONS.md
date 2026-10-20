# Assumptions (researcher unavailable; questions answered by best guess)

| # | Assumption | Status |
|---|---|---|
| 1 | Z-score is per channel, using that channel's own baseline (samples 0-99), as NOTES.md states | guessed from NOTES.md (code does NOT do this) |
| 2 | Baseline mean/SD pooled over trials and baseline time (vs. per trial). Both tried; same winner, values differ <0.05 z | guessed, immaterial |
| 3 | Window 50-200 ms inclusive = samples 112..150 | from-code, fine |
| 4 | SNR = |peak| / SD over trial average's pre-stimulus samples | from-code |
| 5 | Sign: largest |amplitude|, sign retained | from-code |
| 6 | Axis layout (trials, time, channels), stimulus at sample 100 | from NOTES.md |

Questions I would have asked: is the intended normalization per channel (NOTES.md) or per trial across channels (code)? Assumed per channel.
