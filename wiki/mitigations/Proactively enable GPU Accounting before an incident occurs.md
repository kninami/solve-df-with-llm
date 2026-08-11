---
id: DFM-1054
type: mitigation
name: Proactively enable GPU Accounting before an incident occurs
source_refs:
  - DFCite-1044
updated_at: 2026-08-09
status: complete
---

# Proactively enable GPU Accounting before an incident occurs

## Summary

For systems where GPU-related malicious activity is a plausible concern, enable NVIDIA's GPU Accounting feature as a standard system-hardening and logging measure before any incident occurs, since it records only going forward from when it is turned on and cannot be retroactively enabled or reconstructed after the fact.

## Addresses

- [[weaknesses/GPU process-usage history is unavailable unless GPU Accounting was proactively enabled]]

## How To Apply

On systems with NVIDIA GPUs where process-level GPU usage history would be forensically valuable (e.g., systems processing sensitive data, or at elevated risk of GPU-assisted malware), enable GPU Accounting proactively via `nvidia-smi -i \$(GPU_ID) -am ENABLED` as part of standard system logging configuration, rather than only after an incident is suspected. Document this as a specific configuration-hardening recommendation distinct from general logging practices, since it is not part of standard default OS or driver logging behavior and is easy to overlook.

## References

- [DFCite-1044] Bowen et al., 2024, "A step in a new direction: NVIDIA GPU kernel driver memory forensics", FSI: Digital Investigation 49.
