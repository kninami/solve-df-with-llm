---
id: DFW-2017
type: weakness
name: PaaS cloud database transaction log traces disappear unpredictably with no alternative recovery path
description: In a PaaS cloud SQL database, deleted-row transaction log entries disappear after an unpredictable, undocumented interval following deletion, and because buffer-pool and data-page recovery are structurally blocked by the platform, there is no fallback technique available once the log trace is gone.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-2017
source_refs:
  - DFCite-2017
updated_at: 2026-08-14
status: partial
---

# PaaS cloud database transaction log traces disappear unpredictably with no alternative recovery path

## Summary

The source paper's own experiment found that in Azure SQL Database, transaction log contents accessible via `fn_dblog` "disappeared automatically after a certain period following the deletion event," and that "the experiments did not reveal any deterministic rule governing the duration until log disappearance." Because buffer-pool analysis (`sys.dm_os_buffer_descriptors`) is only usable if the deleted record's Page ID is already known from the transaction log, and data-page analysis (`DBCC PAGE`/`DBCC IND`) is entirely blocked by the platform, once the transaction log trace disappears there is no remaining recovery avenue among the three canonical techniques - a stark contrast to on-premises SQL Server, where log-based and buffer-pool-based recovery both "operated effectively immediately after deletion, and even after some time had elapsed, data page analysis made it possible to identify deleted data."

## Why It Matters

An investigator who does not query the transaction log immediately after learning of a relevant deletion in a PaaS cloud database risks the deleted data becoming permanently unrecoverable through any conventional database-forensic technique, with no reliable time budget to plan around since the log-retention behavior is undocumented and platform-controlled rather than configurable by the investigator or even the database owner.

## Related Mitigations

- [[mitigations/Query the cloud database transaction log immediately and pursue service-level and CSP-cooperation evidence sources in parallel]]

## Used By

- [[techniques/Recover deleted records from a PaaS cloud SQL database using transaction log analysis]]

## References

- [DFCite-2017] Shin and Moon, 2025 — Section V.A and Table 6 report the unpredictable transaction log disappearance behavior and the "Not Applicable" status of buffer-pool and data-page recovery in Azure SQL Database.
