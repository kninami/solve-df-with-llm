---
id: LWM-2136
type: mitigation
name: Corroborate wrist-wearable biometric readings with cross-sensor or cross-device data before relying on them
source_refs:
  - LWCite-2156
updated_at: 2026-08-17
status: complete
---

# Corroborate wrist-wearable biometric readings with cross-sensor or cross-device data before relying on them

## Summary

Before drawing an investigative conclusion from a wrist-wearable's recorded biometric value (heart rate, sleep stage, SpO2), seek corroborating data from another sensor on the same device, a second paired device, or independent contextual evidence, rather than treating a single consumer-grade sensor reading as an authoritative ground-truth measurement.

## Addresses

- [[weaknesses/Consumer wrist-wearable biometric readings are degraded by physiological and environmental factors]]

## How To Apply

Where available, cross-check a disputed biometric reading against a second data stream from the same device (e.g., activity/step data alongside heart rate) or a companion smartphone health app that may independently log similar metrics, and note in the report any known environmental or physiological factors (documented by the vendor or in the wearable-sensor literature) that could plausibly have affected the specific reading in question. Where the evidentiary stakes are high (e.g., contradicting a suspect's alibi), qualify the conclusion's strength according to the degree of independent corroboration obtained, rather than presenting a single uncorroborated wearable reading as decisive.

## References

- [LWCite-2156] Almubairik et al., 2025, "WristSense framework: Exploring the forensic potential of wrist-wear devices through case studies", FSI: Digital Investigation 52.
