---
id: DFM-1306
type: mitigation
name: Tune IoT provenance logging granularity and retention to the device's resource budget
source_refs:
  - DFCite-1340
updated_at: 2026-08-15
status: complete
---

# Tune IoT provenance logging granularity and retention to the device's resource budget

## Summary

Before deploying continuous IoT network provenance collection, measure the target devices' available storage, processing headroom, and (where applicable) battery budget, and tune provenance logging granularity, sampling rate, and retention period to fit within that budget rather than logging at maximum fidelity by default.

## Addresses

- [[weaknesses/IoT network provenance collection imposes growing storage and processing overhead on resource-constrained devices]]

## How To Apply

Before deploying [[techniques/Reconstruct IoT network attacks using PROV-based provenance graph modeling]] in a resource-constrained IoT environment, benchmark the provenance growth rate and processing overhead on representative target hardware, as ProvLink-IoT's own evaluation methodology does, and set logging granularity (which events/interactions generate provenance records) and a retention/rotation policy accordingly. Where full-fidelity, indefinite-retention logging is not feasible, prioritize provenance capture for higher-risk sub-layers or event types identified during a risk assessment, and periodically offload provenance data to less-constrained storage (a gateway device or centralized log server) rather than retaining it indefinitely on the constrained device itself.

## References

- [DFCite-1340] Sadineni, Pilli, and Battula, 2023, "ProvLink-IoT: A novel provenance model for Link-Layer Forensics in IoT networks", FSI: Digital Investigation 46, 301600.
