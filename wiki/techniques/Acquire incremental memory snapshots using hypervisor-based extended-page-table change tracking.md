---
id: DFT-1194
type: technique
name: Acquire incremental memory snapshots using hypervisor-based extended-page-table change tracking
description: Acquire a full memory snapshot once, then repeatedly acquire only the 4 KiB memory pages that changed since the previous snapshot by using a thin hypervisor's Extended Page Table (EPT) write-permission tracking and TLB shootdown to detect and atomically capture page changes over time, reconstructing a temporal timeline of system RAM activity rather than a single point-in-time image.
objective_ids:
  - DFO-1006
weakness_ids:
  - DFW-1201
aliases:
  - FIMAR
  - Fast Incremental Memory Acquisition and Restoration
source_refs:
  - DFCite-1212
updated_at: 2026-08-13
status: complete
---

# Acquire incremental memory snapshots using hypervisor-based extended-page-table change tracking

## Summary

Conventional memory acquisition tools capture only the current state of RAM at one moment, discarding any evidence of prior activity if the acquisition is late; FIMAR instead uses a thin hypervisor's Extended Page Table permission mechanism to mark pages read-only after each snapshot, catch the subsequent write via an EPT violation VM exit, and transfer only the changed 4 KiB chunks at each interval, building a sequence of atomic snapshots that can be replayed as a memory-activity timeline.

## Details

After the initial full snapshot, the hypervisor deletes write permission on all per-core Extended Page Table entries and invalidates the Translation Lookaside Buffer cache across all logical processors via TLB shootdown, so any subsequent write to a page triggers an EPT violation that is caught before the write completes; the page is then marked (its write permission restored) rather than acquired immediately, so guest OS execution is not stalled for long, and the previously-marked pages are transferred as the next incremental snapshot once a timer interval elapses. A HASH_MODE option computes a 64-bit hash (XXH64) of each marked 4 KiB chunk before and after the interval and skips transferring chunks whose content did not actually change (relevant when a 2 MiB large page has only some of its constituent 4 KiB chunks modified), reducing transfer size at some added hashing cost; a NO_HASH_MODE always transfers every marked page unconditionally. A separate restoration phase reconstructs a standard raw memory image file at any requested timestamp by patching the full snapshot with the chain of incremental snapshots up to that point, which off-the-shelf tools such as Volatility can then analyze without modification. The system was implemented on the open-source BitVisor thin hypervisor and evaluated by reconstructing a timeline of BlueSky ransomware activity exhibiting anti-forensic evasion logic.

## Examples

- Reconstructing a timeline of a BlueSky ransomware sample's execution on a test machine, showing memory-resident artifacts (e.g. transient decrypted code or keys) that existed only briefly between two acquisition intervals and would have been missed by a single-point-in-time memory dump taken either before or after that window.

## Related Objectives

- `DFO-1006` Acquire data

## Related Weaknesses

- [[weaknesses/Hypervisor-based incremental memory acquisition misses paged-out content stored in pagefile.sys]]

## References

- [DFCite-1212] Hirano and Kobayashi, 2023, "FIMAR: Fast incremental memory acquisition and restoration system for temporal-dimension forensic analysis", FSI: Digital Investigation 46, 301603.
