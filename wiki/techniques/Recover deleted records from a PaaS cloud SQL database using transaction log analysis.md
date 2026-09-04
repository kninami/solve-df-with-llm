---
id: LWT-2017
type: technique
name: Recover deleted records from a PaaS cloud SQL database using transaction log analysis
description: The process of recovering deleted rows from a Platform-as-a-Service (PaaS) cloud SQL database (e.g. Azure SQL Database) by querying its transaction log through the vendor-provided SQL interface (e.g. the fn_dblog function), since buffer-pool and data-page-level recovery methods available on-premises are structurally blocked by the platform's abstraction of OS, file, and memory access.
objective_ids:
  - DFO-1018
weakness_ids:
  - LWW-2017
aliases:
  - fn_dblog-based cloud database record recovery
source_refs:
  - LWCite-2017
updated_at: 2026-08-14
status: partial
---

# Recover deleted records from a PaaS cloud SQL database using transaction log analysis

## Summary

On-premises SQL Server deleted-record recovery normally has three avenues: transaction log analysis, in-memory buffer pool inspection, and direct data-page examination via DBCC commands. In a PaaS cloud database like Azure SQL Database, the platform does not expose the underlying OS, file system, or physical memory to the user - so an investigator with legitimate database access can still query the transaction log through the SQL-level `fn_dblog` function to locate `LOP_DELETE_ROWS` operation entries and extract the deleted row's original byte-level values from the `RowLog Contents` field, but cannot reach the buffer pool or physical data pages at all.

## Details

LWCite-2017 confirms `fn_dblog(NULL, NULL)` remains invocable in Azure SQL Database with only logical DB-level permissions (no sysadmin/OS access needed), returning `LOP_DELETE_ROWS` operation rows with Page ID, Slot ID, and hex-encoded `RowLog Contents` that can be manually carved according to the table's row-structure rules (fixed-length column data, null bitmap, variable-length column offset array) to reconstruct the original deleted values - the same parsing logic used on-premises. However, this path is the *only* one of the three canonical techniques that functions at all: `sys.dm_os_buffer_descriptors` (buffer pool analysis) requires a Page ID that can only come from transaction log analysis in the first place, and `DBCC PAGE`/`DBCC IND` (data page analysis) are entirely blocked commands in the PaaS environment, with no accessible substitute for direct page-level inspection.

## Examples

- LWCite-2017's controlled experiment: deleting 5 of 10 rows from a `CustomerInfo` table in Azure SQL Database (Basic Tier), then successfully recovering each deleted row's `CUSTOMER_ID`, `NAME`, `PHONE`, and `EMAIL` values by parsing the `RowLog Contents 0` hex data returned by an `fn_dblog` query filtered to `Operation = 'LOP_DELETE_ROWS'`.

## Related Objectives

- `DFO-1018` Read data from digital evidence storage formats

## Related Weaknesses

- [[weaknesses/PaaS cloud database transaction log traces disappear unpredictably with no alternative recovery path]]

## References

- [LWCite-2017] Shin and Moon, "Cloud database forensics in practice: Structural challenges and investigative lessons from Azure SQL Database", IEEE Access, 2025 — source of the fn_dblog-based recovery method and the comparative structural-applicability findings described above.
