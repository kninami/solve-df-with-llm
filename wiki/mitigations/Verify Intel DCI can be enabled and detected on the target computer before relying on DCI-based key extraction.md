---
id: LWM-1226
type: mitigation
name: Verify Intel DCI can be enabled and detected on the target computer before relying on DCI-based key extraction
source_refs:
  - LWCite-1237
updated_at: 2026-08-13
status: complete
---

# Verify Intel DCI can be enabled and detected on the target computer before relying on DCI-based key extraction

## Summary

After modifying the target's firmware settings, explicitly confirm Intel DCI is detected as enabled (via the Intel System Debugger Target Indicator or CHIPSEC's `common.debugenabled` module) before committing to the reverse-engineering and debugging stages, and have a fallback acquisition plan ready if it is not.

## Addresses

- [[weaknesses/Intel DCI-based BitLocker VMK extraction depends on the target computer's debug interface being enableable]]

## How To Apply

After writing the standard set of DCI-enabling firmware settings, connect the target to a host running Intel System Studio over the USB 3 debug cable and run the Intel System Debugger Target Indicator (or the CHIPSEC `common.debugenabled` check) to confirm the interface is actually detected before investing further effort in the Windows Boot Manager reverse-engineering and live-debugging stages. If DCI cannot be confirmed enabled despite correct firmware modification, treat this as a hard stop for this specific method on this system rather than retrying variations, and fall back to an alternative BitLocker key-recovery approach (e.g. cold-boot, DMA-based, or TPM-sniffing methods) appropriate to the target's hardware generation and configuration, since the underlying cause of DCI-enablement failure (vendor-specific restriction, incomplete firmware coverage) is often not resolvable through further firmware editing alone.

## References

- [LWCite-1237] Bichara de Assumpção, dos Reis, Marcondes, da Silva Eleutério and Vieira, 2023, "Forensic method for decrypting TPM-protected BitLocker volumes using Intel DCI", DFRWS 2023 EU; FSI: Digital Investigation 44, 301514.
