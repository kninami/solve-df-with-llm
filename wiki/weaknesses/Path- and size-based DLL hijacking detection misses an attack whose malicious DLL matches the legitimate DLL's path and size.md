---
id: LWW-1282
type: weakness
name: Path- and size-based DLL hijacking detection misses an attack whose malicious DLL matches the legitimate DLL's path and size
description: Because path/size-consensus-based DLL hijacking detection flags a process only when its loaded module's path or size differs from the majority, an attacker who places a malicious DLL at the exact legitimate path and pads it to the legitimate file size, or who hijacks a DLL loaded in only a single process (leaving no majority to compare against), evades detection entirely, and the detection is limited to 64-bit processes only.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - LWM-1283
source_refs:
  - LWCite-1310
updated_at: 2026-08-15
status: complete
---

# Path- and size-based DLL hijacking detection misses an attack whose malicious DLL matches the legitimate DLL's path and size

## Summary

Path/size-consensus-based DLL hijacking detection assumes a hijacked DLL differs from the legitimate one in its on-disk path, its file size, or both, and assumes enough processes have the legitimate module loaded to establish a reliable majority. Both assumptions can fail: an attacker can match the legitimate path and size, and a DLL loaded in only one process on the system under examination leaves no majority baseline to compare against. The detection is also explicitly scoped to 64-bit processes only.

## Why It Matters

An investigator who treats a clean result from this detection method as confirmation that no DLL hijacking occurred risks a false negative against a competent attacker who deliberately matches the legitimate module's path and size (a straightforward evasion once the detection heuristic is known), or against a hijack of a DLL that is only loaded by the single targeted process. The detection should be understood as a low-cost triage signal for a specific, common hijacking pattern rather than exhaustive proof of the absence of DLL hijacking.

## Related Mitigations

- [[mitigations/Corroborate DLL hijacking detection with hash or signature verification of the loaded module's content]]

## Used By

- [[techniques/Detect DLL hijacking by comparing a loaded module's path and size across memory-dump processes]]

## References

- [LWCite-1310] Fernández-Álvarez and Rodríguez, 2023, "Module extraction and DLL hijacking detection via single or multiple memory dumps", FSI: Digital Investigation 44, 301505.
