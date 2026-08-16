---
id: DFT-2125
type: technique
name: Infer a wrist-wear device's evidentiary health data types using a sensor-feature cross-reference table
description: Determine which health-related evidence categories (sleep, heart rate, SpO2, blood pressure, stress, activity) a wrist-wear device from any vendor is capable of producing by cross-referencing its documented sensors and features against a vendor-independent sensor-to-feature reference table, inferring undocumented features from the sensors actually present when a vendor's own manual is incomplete, to guide database extraction and identify potential circumstantial evidence before deep analysis begins.
objective_ids:
  - DFO-1014
weakness_ids:
  - DFW-2134
  - DFW-2135
aliases:
  - WristSense
  - Sensor-Feature Cross-Reference Table (SFCRT)
  - Potential Circumstantial Evidence (PCE) identification
source_refs:
  - DFCite-2156
updated_at: 2026-08-17
status: complete
---

# Infer a wrist-wear device's evidentiary health data types using a sensor-feature cross-reference table

## Summary

Wrist-wear device manuals vary widely in how completely they document a device's health-tracking capabilities, and prior wrist-device forensic research has focused narrowly on individual vendors (e.g. Garmin, Fitbit), leaving the broader multi-vendor market underexplored. A Sensor-Feature Cross-Reference Table (SFCRT) — built from published sensor/feature research and vendor documentation across many devices — records which combinations of sensors are known to support which health features, so that an investigator can look up a specific device's documented sensor list and infer additional plausible features even when the vendor's own manual does not explicitly claim them, arriving at a device-specific list of Potential Circumstantial Evidence (PCE) categories to prioritize during subsequent extraction.

## Details

To generate a device's PCE list, the investigator iterates through each feature in the SFCRT: if the vendor manual explicitly claims the feature, it is added directly; if not, each sensor in the SFCRT known to contribute to that feature is checked against the device's documented sensor list, and the feature is added if a supporting sensor is present. This closes the gap left by vendors such as Apple that list sensors with limited accompanying feature descriptions, letting an investigator still identify plausible evidence categories (e.g., inferring stress monitoring from the presence of heart-rate and temperature sensors even if the vendor manual does not use the term "stress"). The resulting PCE list — sleep, heart rate, blood oxygen, blood pressure, body temperature, activity, and stress data, plus profiling data such as biological markers (age, weight, height), logical markers (paired-device identifiers, stored credentials, Wi-Fi/Bluetooth connections), and location markers (visited routes) — directs a subsequent logical extraction and parsing pass toward the specific SQLite databases most likely to hold case-relevant data, complementing per-vendor extraction techniques such as [[techniques/Extract health, fitness, and location artifacts from a wearable's Android companion application]] by determining what to look for before deep parsing of a specific vendor's database schema begins.

## Examples

- Applied to the Apple Watch Series 9 (whose manual lists sensors like an electrical heart sensor, temperature sensor, and high-G accelerometer but does not explicitly document stress monitoring as a feature), the SFCRT method inferred stress monitoring as plausible PCE from the presence of the heart-rate and temperature sensors, alongside the explicitly documented sleep, heart-rate, activity-tracking, and body-temperature features.
- Applied across five case-study devices from Huawei, Amazfit, Xiaomi, and Samsung, the framework confirmed profiling data (device linkage, biological markers) recoverable from Huawei and Amazfit devices, and PCE recoverable across sleep, heart-rate, SpO2, activity, and stress categories with high step-versus-calorie correlation (0.91-0.98) consistent across all vendors.

## Related Objectives

- `DFO-1014` Find potential digital evidence sources

## Related Weaknesses

- [[weaknesses/Vendor-specific encryption blocks wrist-device profile and health database extraction]]
- [[weaknesses/Consumer wrist-wearable biometric readings are degraded by physiological and environmental factors]]

## References

- [DFCite-2156] Almubairik et al., 2025, "WristSense framework: Exploring the forensic potential of wrist-wear devices through case studies", FSI: Digital Investigation 52.
