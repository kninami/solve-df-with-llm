---
id: LWW-1276
type: weakness
name: PLC memory-derived event logs lack creation timestamps, limiting timeline reconstruction
description: Event logs (project downloads, mode changes) recovered by reverse-engineering a PLC's memory dump can be enumerated and correctly sequenced relative to each other, but the vendor does not appear to store an associated creation timestamp for each entry, so an investigator cannot determine exactly when a given recovered event occurred from the memory dump alone.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - LWM-1277
source_refs:
  - LWCite-1304
updated_at: 2026-08-14
status: complete
---

# PLC memory-derived event logs lack creation timestamps, limiting timeline reconstruction

## Summary

The underlying study recovered two forensically important categories of PLC memory-based events — new-project-download events and controller mode-change events (RUN/PROGRAM/TEST) — successfully identifying and ordering all occurrences of both across every test performed, but states plainly: "Although we could not find the log's creation time, the information is still helpful for the forensic investigation." The vendor's controller does not appear to provide any other logging mechanism beyond a non-recoverable diagnostic fault log, so no richer, timestamped logging source is available from the device itself for this controller model.

## Why It Matters

An investigator reconstructing an attack or incident timeline needs to know not just that a mode change or project download occurred, but precisely when, in order to correlate it with other timestamped evidence (network captures, SCADA historian records, physical sensor logs) — without timestamps, the recovered PLC event sequence can establish relative ordering (which event happened before another) but cannot be placed on an absolute timeline or correlated confidently against external time-stamped evidence sources.

## Related Mitigations

- [[mitigations/Corroborate PLC memory-derived event logs with independently timestamped external sources]]

## Used By

- [[techniques/Reverse-engineer a PLC's memory dump to extract control-logic, IO states, and logs using differential analysis]]

## References

- [LWCite-1304] Rais, Awad, Lopez and Ahmed, 2022, "Memory forensic analysis of a programmable logic controller in industrial control systems", DFRWS 2022 EU; FSI: Digital Investigation 40, 301339.
