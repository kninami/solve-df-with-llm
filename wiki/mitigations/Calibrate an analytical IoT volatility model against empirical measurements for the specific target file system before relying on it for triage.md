---
id: LWM-1309
type: mitigation
name: Calibrate an analytical IoT volatility model against empirical measurements for the specific target file system before relying on it for triage
source_refs:
  - LWCite-1344
updated_at: 2026-08-15
status: complete
---

# Calibrate an analytical IoT volatility model against empirical measurements for the specific target file system before relying on it for triage

## Summary

Before using an analytical, write/erase-behavior-derived volatility model to make triage or prioritization decisions, cross-validate its predictions against empirically measured data-survival behavior on representative hardware (or an emulator) for the specific target file system, and apply a conservative correction factor reflecting the model's documented tendency to underestimate volatility, or treat its predicted survival window as a conservative lower bound rather than a precise estimate.

## Addresses

- [[weaknesses/An analytical IoT flash-volatility model based only on known file system write-erase behavior underestimates true evidence volatility]]

## How To Apply

Where feasible, before relying on [[techniques/Estimate evidence survival probability for IoT flash storage using a quantitative data-volatility model]] for a specific IoT device/file-system combination in a triage decision, run a comparable empirical validation (e.g. using a hardware emulator or a representative test device) to measure actual write/erase behavior and data lifetime, and compare against the analytical model's prediction. Where empirical validation is not feasible in the time available, treat the analytical model's predicted evidence-survival window as a conservative lower bound (evidence may persist longer than predicted, not less), and avoid deprioritizing a device based solely on the analytical model suggesting a short survival window without other supporting information.

## References

- [LWCite-1344] Sandvik, Franke, Abie, and Årnes, 2022, "Quantifying data volatility for IoT forensics with examples from Contiki OS", FSI: Digital Investigation 40, 301343.
