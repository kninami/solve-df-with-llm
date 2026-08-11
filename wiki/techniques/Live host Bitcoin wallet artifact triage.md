---
id: DFT-1028
type: technique
name: Live host Bitcoin wallet artifact triage
description: During the live phase of a premises search, run an automated, low-footprint collection tool against a target Windows host to quickly identify installed Bitcoin wallet applications (via prefetch, registry, and known file locations), then capture wallet-specific artifacts — running-process memory, browser history and cached credentials, filesystem keyword/QR-code search results, and a full RAM dump — before deciding whether cryptocurrency assets need to be secured.
objective_ids:
  - DFO-1006
weakness_ids:
  - DFW-1020
aliases: []
source_refs:
  - DFCite-1020
updated_at: 2026-08-09
status: complete
---


# Live host Bitcoin wallet artifact triage

## Summary

Because wallet applications must hold private keys in memory at some point to sign a transaction, and because encrypted wallet files, cached browser credentials, and recovery-seed-adjacent artifacts are often recoverable well before a full offline forensic image is produced, a purpose-built triage tool run directly on a live target machine during search execution can gather enough evidence within a practicable window (under 2 hours) to inform whether cryptocurrency assets need urgent action, without requiring the examiner's own laptop to have significant compute power.

## Details

The collection tool follows a defined sequence: search prefetch files, known registry keys, and known installation directories to identify installed wallet applications; if found, capture wallet-application-specific artifacts including a process memory dump; if no known application is found, still capture the running process list, browser history, and browser-cached credentials; run a keyword search (constrained to specific file types/locations to remain practicable given read-speed limits) and an image-prefiltered QR-code search for keys/addresses; and finally capture a full RAM dump. All artifacts and passwords harvested (including from cached browser credentials) are added to a candidate password dictionary for later attack stages, and every action taken is logged to support forensic principles around auditability, and file hashes are generated to detect any unintentional changes.

## Examples

- Tested against Electrum (software wallet) and Ledger Live (hardware wallet companion app) on a Windows 10 VM: while each application was running, the collection tool recovered the encrypted wallet file, an encrypted extended private key (Electrum) or extended public key and current balance (Ledger Live), and associated addresses from process memory.

## Related Objectives

- `DFO-1006` Acquire data

## Related Weaknesses

- [[weaknesses/In-memory credential recovery fails once the relevant memory page is overwritten]]

## References

- [DFCite-1020] Holmes and Buchanan, 2023, "A framework for live host-based Bitcoin wallet forensics and triage", FSI: Digital Investigation 44.
