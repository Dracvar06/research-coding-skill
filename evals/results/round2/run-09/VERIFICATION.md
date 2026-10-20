# VERIFICATION

Headline: da/dt = +0.030 AU/Myr (code prints 0.0302).

| Check | Result | Strength |
|---|---|---|
| Independent analytic: Gauss equation da/dt = 2Tv a²/GM, averaged over mean anomaly (quad, separate script) | 0.03018 AU/Myr, matches 0.0302 | known-answer, strong |
| Null control: T=0 | slope 0.0000 | strong |
| Linearity: T doubled | 0.0603 (2x) | strong |
| Tolerance: rtol 1e-10 vs 1e-12 | 0.0299 vs 0.0302 (1%; fit over only 3e-6 AU change) | numerics OK; rtol 1e-12 fine |
| Unit check of 6.6e-8 AU/yr² vs 1e-11 m/s² | consistent | strong |

No disagreements found. Caveat: the plausibility of the input (see ASSUMPTIONS Q1) is a modelling issue, not a code bug.
Scripts: scratchpad chk.py, conv.py.
