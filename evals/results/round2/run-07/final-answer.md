**The result in NOTES.md is correct.** The asteroid drifts outward at da/dt ≈ +0.030 AU/Myr, and I found nothing to change.

- **Code run:** `analysis.py` gives da/dt = 0.0302 AU/Myr. Over the 100 years, a goes from 1.500000 to 1.500003 AU, so the drift is outward as the notes say.
- **Independent check:** I computed the orbit-averaged drift from first principles, da/dt = 2a²fv/GM, averaged over the orbit. It gives 0.03018 AU/Myr, which matches the code. This is the strongest evidence for the result.
- **Units:** 1e-11 m/s² converts to 6.66e-8 AU/yr². The code uses 6.6e-8, about 1% low, which fits the notes' "≈". Using the exact conversion would give about 0.0305, which still rounds to 0.030 at two significant figures.
- **Integrator tolerance:** My own re-run gives 0.030172 at rtol 1e-12 and 0.030174 at rtol 1e-13, so the result has converged.

**Not completed:** I could not finish the Radau cross-check (too slow here), the zero-acceleration control or the doubled-acceleration test. Only one independent check was run, not several independent versions.

**Question for you:** the notes use a 100-year linear fit of osculating a. I assumed that is what you intend and the result holds, but I couldn't ask you. This and the 6.6e-8 rounding are logged as guesses in `ASSUMPTIONS.md`.

I wrote `ASSUMPTIONS.md` and `VERIFICATION.md` in the working directory.
