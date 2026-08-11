---
id: DFW-1054
type: weakness
name: GPU process-usage history is unavailable unless GPU Accounting was proactively enabled
description: NVIDIA's GPU Accounting feature, which tracks per-process GPU usage history (start/end time, live/dead status, PID) in the GpuAccounting NVOC structure, is not enabled by default on closed-source driver installations; if it was never manually enabled before an incident, this valuable process-usage-history artefact simply does not exist in memory to recover, regardless of how thorough the memory acquisition and structure-parsing method used afterward is.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1054
source_refs:
  - DFCite-1044
updated_at: 2026-08-09
status: complete
---

# GPU process-usage history is unavailable unless GPU Accounting was proactively enabled

## Summary

The authors note this directly: "GPU Accounting is not enabled by default for the closed-source modules. Users must enable GPU Accounting with NVIDIA's nvidia-smi tool via the command line." Because this is an opt-in monitoring feature rather than a default logging behavior, a system that never had it explicitly enabled will simply have no GpuAccounting history to recover from memory, no matter how well the acquisition and NVOC-structure-parsing method works.

## Why It Matters

This is a "wasn't turned on before the incident" class of evidence gap: an investigator cannot retroactively enable GPU Accounting after a suspected incident to recover its historical data, since the feature only records data going forward from when it was turned on. Investigators and system administrators need to know about this dependency in advance — as a proactive hardening/logging measure — rather than discovering the gap only after attempting to recover GPU process history from an already-acquired memory image.

## Related Mitigations

- [[mitigations/Proactively enable GPU Accounting before an incident occurs]]

## Used By

- [[techniques/Cross-mapped pointer-chasing recovery of NVIDIA GPU driver structures in memory]]

## References

- [DFCite-1044] Bowen et al., 2024, "A step in a new direction: NVIDIA GPU kernel driver memory forensics", FSI: Digital Investigation 49.
