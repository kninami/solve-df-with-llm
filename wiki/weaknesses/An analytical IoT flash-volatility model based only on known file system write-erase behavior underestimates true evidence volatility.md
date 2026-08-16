---
id: DFW-1307
type: weakness
name: An analytical IoT flash-volatility model based only on known file system write-erase behavior underestimates true evidence volatility
description: A theoretical data-volatility model derived purely from a file system's documented or reverse-engineered write/erase behavior systematically underestimates real-world data volatility on flash-based IoT storage compared to empirically measured behavior, meaning the model's evidence-survival-probability estimates are optimistic relative to reality.
categories:
  - ASTM_MISINT
mitigation_ids:
  - DFM-1309
source_refs:
  - DFCite-1344
updated_at: 2026-08-15
status: complete
---

# An analytical IoT flash-volatility model based only on known file system write-erase behavior underestimates true evidence volatility

## Summary

Cross-validating the theoretical Coffee-File-System volatility model against Cooja-emulator-derived empirical measurements found that "an approximated model based on the known workings of the file system underestimated the volatility" — that is, the purely analytical approach predicted data would disappear (or become overwritten/erased) faster than it actually did in the empirically observed, emulated system behavior.

## Why It Matters

An investigator relying solely on the analytical model's evidence-survival-probability estimate to make a triage/prioritization decision risks either under-prioritizing a device whose evidence has actually persisted longer than the model predicts (potentially deprioritizing collection from a device that, in fact, still holds recoverable evidence), or — more favorably but still misleadingly — being pleasantly surprised that evidence remains recoverable past the model's predicted window. Either way, treating the analytical model's estimate as precisely calibrated rather than a conservative approximation risks systematic errors in prioritization decisions made under the very time pressure the model was designed to help manage.

## Related Mitigations

- [[mitigations/Calibrate an analytical IoT volatility model against empirical measurements for the specific target file system before relying on it for triage]]

## Used By

- [[techniques/Estimate evidence survival probability for IoT flash storage using a quantitative data-volatility model]]

## References

- [DFCite-1344] Sandvik, Franke, Abie, and Årnes, 2022, "Quantifying data volatility for IoT forensics with examples from Contiki OS", FSI: Digital Investigation 40, 301343.
