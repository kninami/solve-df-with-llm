---
id: DFM-1283
type: mitigation
name: Corroborate DLL hijacking detection with hash or signature verification of the loaded module's content
source_refs:
  - DFCite-1310
updated_at: 2026-08-15
status: complete
---

# Corroborate DLL hijacking detection with hash or signature verification of the loaded module's content

## Summary

Do not treat a clean result from path/size-consensus DLL hijacking detection as conclusive; independently verify a suspect module's content against a known-good hash or digital signature, and separately review DLLs loaded by only a single process, since both scenarios evade the path/size heuristic.

## Addresses

- [[weaknesses/Path- and size-based DLL hijacking detection misses an attack whose malicious DLL matches the legitimate DLL's path and size]]

## How To Apply

For any module of investigative interest, extract it (using [[techniques/Aggregate module pages across single or multiple Windows memory dumps to reconstruct a complete DLL]] where a single-process copy is incomplete) and compute its cryptographic hash and check its digital signature against a trusted reference copy of the legitimate DLL, rather than relying on path and size alone. Separately flag and manually review any module loaded in only a single process on the system, since the path/size-consensus method cannot establish a majority baseline in that case. Where the target is a 32-bit process, note that the detection method does not apply and rely entirely on hash/signature verification instead.

## References

- [DFCite-1310] Fernández-Álvarez and Rodríguez, 2023, "Module extraction and DLL hijacking detection via single or multiple memory dumps", FSI: Digital Investigation 44, 301505.
