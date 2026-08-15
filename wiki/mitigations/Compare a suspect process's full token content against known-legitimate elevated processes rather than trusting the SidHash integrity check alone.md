---
id: DFM-2072
type: mitigation
name: Compare a suspect process's full token content against known-legitimate elevated processes rather than trusting the SidHash integrity check alone
source_refs:
  - DFCite-2076
updated_at: 2026-08-15
status: complete
---

# Compare a suspect process's full token content against known-legitimate elevated processes rather than trusting the SidHash integrity check alone

## Summary

When investigating suspected privilege escalation in a Windows memory image, do not treat a process's valid SidHash as proof its token was never tampered with; instead compare the suspect process's full `_TOKEN` `UserAndGroupCount`/`UserAndGroups`/`SidHash` content directly against known-legitimate elevated processes (e.g., SYSTEM, PID 4) to detect wholesale copying.

## Addresses

- [[weaknesses/Windows kernel token integrity hash checks do not detect Token Hijacking because the attack copies a legitimately-hashed higher-privileged token wholesale]]

## How To Apply

During memory forensic analysis of a system suspected of a local privilege escalation, extract `_TOKEN` structures for all processes (e.g., via Volatility or a similar `_EPROCESS`-walking tool) and specifically compare the SID array and SidHash content of any unexpectedly-privileged process against that of legitimately elevated system processes; a byte-for-byte or near-identical match between a low-privilege process's token content and a high-privilege system process's token content — despite the two being different `_EPROCESS` objects — is a strong indicator of Token Hijacking rather than legitimate privilege assignment. Also check for the related Handle Table Hijacking and NTFS-structure-hijacking indicators (handle-table entries resolving to unexpected object headers; `FSRTL_ADVANCED_FCB_HEADER` ownership fields inconsistent with legitimate access) as related kernel-structure-copying attacks from the same research.

## References

- [DFCite-2076] Korkin, 2021, "Windows Kernel Hijacking Is Not an Option: MemoryRanger Comes to the Rescue Again", JDFSL 16(4). Documents the exact `_TOKEN` fields (UserAndGroupCount, UserAndGroups, SidHash) the Token Hijacking attack copies from a higher-privileged process, which is the same content this mitigation directs an investigator to compare across processes.
