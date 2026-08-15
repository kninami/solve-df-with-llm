---
id: DFM-1274
type: mitigation
name: Extend TEE-based IoT memory monitoring to SRAM and add a verified secure-boot mechanism
source_refs:
  - DFCite-1301
updated_at: 2026-08-14
status: complete
---

# Extend TEE-based IoT memory monitoring to SRAM and add a verified secure-boot mechanism

## Summary

Extend a TEE-based IoT anomaly-detection system's memory acquisition to also periodically capture and analyze volatile SRAM, not just flash, and pair its watchdog-triggered reset remediation with a cryptographically verified secure-boot mechanism, so malware operating purely in volatile memory can still be detected and malware cannot simply survive a triggered reset by re-flashing compromised firmware.

## Addresses

- [[weaknesses/TEE-based IoT flash-memory anomaly detection cannot detect malware operating solely in volatile SRAM]]

## How To Apply

Add an SRAM acquisition path alongside the existing flash-memory acquisition module within the TEE, using the same changed-block hashing approach to minimize network overhead, and retrain or extend the anomaly-classification model to incorporate SRAM-derived features so volatile-memory-only compromise is not invisible to the system. Implement a secure-boot chain rooted in the TEE that cryptographically verifies the main firmware's integrity before allowing it to execute after a watchdog-triggered reset, refusing to boot (or re-flashing from a known-good firmware image) if verification fails, so a reset alone cannot be defeated by malware that has modified the device's persistent firmware. Document which memory regions (flash only, flash and SRAM, or other) a given deployment actually monitors, so investigators and defenders relying on the system understand its actual coverage rather than assuming comprehensive memory visibility.

## References

- [DFCite-1301] Waguespack, Smith, Muliri, Vijayakanthan and Ali-Gombe, 2024, "MARS: The first line of defense for IoT incident response", DFRWS 2024 USA; FSI: Digital Investigation 49, 301754.
