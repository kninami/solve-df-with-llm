---
id: DFT-2070
type: technique
name: Detect Windows Token Hijacking privilege escalation by comparing token content against a legitimately elevated process
description: During Windows kernel memory forensic analysis, detect privilege-escalation malware that copies an entire legitimately-hashed higher-privileged process's `_TOKEN` SID list and integrity hash into a lower-privileged process's token, by comparing a suspect process's full `UserAndGroups` array and `SidHash` content against a known-legitimate elevated process rather than trusting the OS's own SidHash integrity check as proof the token is unmodified.
objective_ids:
  - DFO-1019
weakness_ids:
  - DFW-2072
aliases:
  - Token Hijacking Attack detection
source_refs:
  - DFCite-2076
updated_at: 2026-08-15
status: complete
---

# Detect Windows Token Hijacking privilege escalation by comparing token content against a legitimately elevated process

## Summary

Windows kernel versions 6.x and later added `SidHash`/`RestrictedSidHash` integrity fields to the `_TOKEN` structure specifically to stop direct kernel object manipulation (DKOM) attacks that patch a process's SID list to escalate privileges, since the OS checks these hashes to ensure the SID list has not been tampered with. A newer "Token Hijacking" technique defeats this integrity check not by patching a few SID fields but by wholesale-copying the entire `UserAndGroupCount`, `UserAndGroups` array (including its variable-length SID/attribute entries), and `SidHash` fields from a legitimately higher-privileged process's token — producing a token whose hash is entirely valid because it was never actually tampered with in place, just replaced wholesale. Detecting this requires comparing the suspect process's token content directly against a legitimate elevated process's token, since the hash check alone cannot distinguish a copied-but-valid token from a genuinely-assigned one.

## Details

The attack targets the `_TOKEN` structure pointed to by the `Token` `_EX_FAST_REF` field in a process's `_EPROCESS` structure. Rather than the older "token swapping"/"token stealing" technique (overwriting the `Object` field in `_EPROCESS` to point at an entirely different, already-privileged token — a technique modern antivirus already monitors for) or a direct SID-list patch (blocked by the SidHash integrity check added in Windows kernel 6.x), Token Hijacking copies the full `UserAndGroupCount`, `UserAndGroups` array, and `SidHash` structure fields from a higher-privileged process (e.g., a SYSTEM process) into the target process's own token in place, so the resulting hash check passes because it is recalculated over data that was copied verbatim rather than patched. This is analogous in spirit to two related file-operation attacks the same research describes — Handle Table Hijacking (redirecting a `HANDLE_TABLE_ENTRY`'s `ObjectPointerBits` to point at a different file's `OBJECT_HEADER`) and Hijacking NTFS data structures (copying the content of a `FSRTL_ADVANCED_FCB_HEADER` control-block structure, including `Resource->OwnerEntry.OwnerThread`, from a secret file's structure into the attacker's own) — all three attacks share the same underlying pattern of copying legitimate, validly-hashed or validly-owned kernel structure content into an attacker-controlled structure rather than directly patching a protected field, specifically to evade the narrow, field-level integrity checks Windows kernel security features apply.

## Examples

- A malware process's `_TOKEN` structure whose `UserAndGroups` SID array and `SidHash` exactly match those of the live SYSTEM (PID 4) process's token, despite the malware process having a different `_EPROCESS` and process name, is a strong indicator of Token Hijacking — a discrepancy only visible by directly comparing token content across processes in a memory image, not by checking the malware process's own SidHash validity in isolation.
- For file-handle-based variants, a process's Kernel Handle Table entry whose `ObjectPointerBits` resolves to an `OBJECT_HEADER`/`FILE_OBJECT` inconsistent with the handle's originally-granted access rights, or a `FSRTL_ADVANCED_FCB_HEADER` whose `OwnerEntry.OwnerThread` does not correspond to a thread that legitimately owns that file resource, are the corresponding memory-forensic indicators for Handle Table Hijacking and Hijacking NTFS data structures respectively.

## Related Objectives

- `DFO-1019` Detect anti-forensics and other anomalies

## Related Weaknesses

- [[weaknesses/Windows kernel token integrity hash checks do not detect Token Hijacking because the attack copies a legitimately-hashed higher-privileged token wholesale]]

## References

- [DFCite-2076] Korkin, 2021, "Windows Kernel Hijacking Is Not an Option: MemoryRanger Comes to the Rescue Again", JDFSL 16(4). Source of the Token Hijacking, Handle Table Hijacking, and Hijacking NTFS data structures attack techniques and their underlying kernel data structure details.
