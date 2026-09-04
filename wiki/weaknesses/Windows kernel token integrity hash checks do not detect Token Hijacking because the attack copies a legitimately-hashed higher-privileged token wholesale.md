---
id: LWW-2072
type: weakness
name: Windows kernel token integrity hash checks do not detect Token Hijacking because the attack copies a legitimately-hashed higher-privileged token wholesale
description: Windows kernel 6.x+'s SidHash-based token integrity check is designed to detect in-place patching of a process's SID list, but does not detect Token Hijacking, which instead wholesale-copies an entire legitimately-hashed higher-privileged process's SID list and hash into the target token, so the resulting hash check passes as valid.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - LWM-2072
source_refs:
  - LWCite-2076
updated_at: 2026-08-15
status: complete
---

# Windows kernel token integrity hash checks do not detect Token Hijacking because the attack copies a legitimately-hashed higher-privileged token wholesale

## Summary

Windows kernel versions 6.x and later added SidHash/RestrictedSidHash fields to the `_TOKEN` structure specifically as an integrity barricade against direct kernel object manipulation (DKOM) attacks that patch a process's SID list to grant unauthorized privileges. This barricade successfully blocks in-place SID patching, since a modified SID list no longer matches its stored hash. However, the Token Hijacking technique bypasses it entirely: rather than patching individual fields, it copies the complete `UserAndGroupCount`, `UserAndGroups` array, and `SidHash` structure from a legitimately higher-privileged process's token into the target process's token. Because this copied data was never actually tampered with — it is a verbatim, validly-hashed structure from elsewhere — the resulting hash check on the target process passes, and the OS has no built-in mechanism that detects the token content was copied from a different process rather than legitimately assigned.

## Why It Matters

An investigator or automated defense that relies on the OS's own token-integrity hash check (or a memory-forensics plugin that merely re-validates that check) as proof a process's privilege level is legitimate will not detect Token Hijacking, since the hash genuinely is valid for the copied content. This is a completeness gap in privilege-escalation detection: an investigator examining a system for signs of local privilege escalation who checks only hash validity, rather than comparing token content across processes, could miss this specific attack entirely while correctly ruling out simpler SID-patching attacks.

## Related Mitigations

- [[mitigations/Compare a suspect process's full token content against known-legitimate elevated processes rather than trusting the SidHash integrity check alone]]

## Used By

- [[techniques/Detect Windows Token Hijacking privilege escalation by comparing token content against a legitimately elevated process]]

## References

- [LWCite-2076] Korkin, 2021, "Windows Kernel Hijacking Is Not an Option: MemoryRanger Comes to the Rescue Again", JDFSL 16(4). States that the Token Hijacking attack "gains elevated privileges with the correct hash value" by fully copying the static and dynamic parts of a higher-privileged process's token, defeating the SidHash integrity mechanism added in Windows kernel 6.x specifically to prevent this class of attack.
