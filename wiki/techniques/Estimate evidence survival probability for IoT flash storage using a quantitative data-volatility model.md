---
id: DFT-1297
type: technique
name: Estimate evidence survival probability for IoT flash storage using a quantitative data-volatility model
description: Prioritize evidence-collection effort across a resource-constrained IoT deployment by quantitatively estimating the probability that a given piece of evidence still exists on a device's flash storage at the time of collection, using an analytical data-volatility model calibrated against the target file system's known write/erase behavior, rather than relying on qualitative volatility judgments alone.
objective_ids:
  - DFO-1005
weakness_ids:
  - DFW-1307
aliases:
  - Quantitative IoT flash data volatility model
source_refs:
  - DFCite-1344
updated_at: 2026-08-15
status: complete
---

# Estimate evidence survival probability for IoT flash storage using a quantitative data-volatility model

## Summary

Because IoT investigations must be conducted under limited time, equipment, and personnel, and because the number of potential evidence-holding locations grows with the number and diversity of devices in an IoT deployment, effective triage requires assessing each device's likelihood of holding evidence, the accessibility of its data, and the volatility of that evidence — how quickly it disappears from the system. This work develops an analytical model for quantifying flash-storage data volatility, complementing the largely qualitative volatility literature that predates it, so an investigator can estimate the probability that specific evidence still exists on a device rather than relying on intuition about "high" or "low" volatility.

## Details

The model targets the flash storage component of IoT devices specifically (flash generally has lower volatility than RAM, though other factors — physical destruction, bad-block management, firmware/hardware bugs, and bit-flips from ionizing radiation — are explicitly outside the analysis's scope) and was exemplified using the Coffee File System on Contiki OS, an operating system for constrained IoT devices. Two complementary approaches were used to answer three research questions (how volatility can be analytically calculated, how it can be measured, and how well the two correspond): a theoretical model derived from the known write/erase workings of the target file system, and empirical measurement using the Cooja hardware emulator to generate data on emulated devices while extracting information about write and erase operations during device operation, establishing the actual observed lifetime of written data for comparison against the analytical model's predictions.

## Examples

- Cross-validating the analytical model against Cooja-emulator-derived empirical measurements of Coffee File System write/erase behavior revealed that the theoretical, write/erase-behavior-based approximation model systematically underestimated actual data volatility — meaning evidence on the emulated devices persisted for longer, on average, than the purely analytical model predicted.

## Related Objectives

- `DFO-1005` Prioritize digital evidence sources

## Related Weaknesses

- [[weaknesses/An analytical IoT flash-volatility model based only on known file system write-erase behavior underestimates true evidence volatility]]

## References

- [DFCite-1344] Sandvik, Franke, Abie, and Årnes, 2022, "Quantifying data volatility for IoT forensics with examples from Contiki OS", FSI: Digital Investigation 40, 301343.
