---
id: LWT-1207
type: technique
name: Carve and reconstruct MSSQL transaction log records from unallocated file-system space
description: Identify Microsoft SQL Server transaction log records (INSERT/DELETE/MODIFY/BEGIN_XACT/COMMIT_XACT) remaining in a file system's unallocated area — after a transaction log backup file was deleted or a log file shrank — using fixed-length record signatures, then reconstruct the originating SQL query and its transaction start/end times.
objective_ids:
  - DFO-1001
weakness_ids:
  - LWW-1218
aliases:
  - MSSQL transaction log unallocated-area record carving
source_refs:
  - LWCite-1229
updated_at: 2026-08-13
status: complete
---

# Carve and reconstruct MSSQL transaction log records from unallocated file-system space

## Summary

MSSQL transaction log records remain undocumented at the binary level, but each log record type has a fixed-length common header with a distinguishing operation identifier and byte-pattern signature, so a deleted transaction log backup file's remnants can be located in a file system's unallocated area by scanning for these signatures and re-parsed into an equivalent query even after the original log file is gone.

## Details

The transaction log file is internally divided into Virtual Log Files (VLFs) made up of 512-byte blocks organized into log blocks, each holding a header, one or more 24-byte-common-area log records, an array of record offsets, and parity-protection bytes. Because deleted transaction log backup files are only marked free rather than wiped, and because their internal record structure survives independent of the file system metadata that once pointed to them, a signature-based scan for the fixed 4-byte operation signatures (e.g. `0x00003E00` for `LOP_INSERT_ROWS`, accounting for parity-bit variants) locates candidate records directly in unallocated space. Query reconstruction then differs by operation: INSERT and DELETE records store the entire affected row directly in `RowLog Contents` and can be reconstructed from the log record alone, while UPDATE (`LOP_MODIFY_ROW`) records only capture the before/after row deltas and require correlating the log record's `Offset in Row` field with the current data file to reconstruct the pre-image. `LOP_BEGIN_XACT`/`LOP_COMMIT_XACT` records sharing the same Transaction ID as a reconstructed record supply the transaction's start and end timestamps. The method does not reconstruct `CREATE`/`DROP TABLE` queries, which are represented by multiple log records within a transaction rather than a single record.

## Examples

- On a self-generated SQL Server 2019 dataset, deleting three transaction log backup files and carving the resulting unallocated area recovered over 95% of the originally inserted 1,000-row batches per file (974/1,000 and 967/1,000 in the second and third backup files respectively).
- On a real SQL Server 2014 production volume in use since 2014, carving a 1.18 TB unallocated area identified 37 million candidate offsets matching log-record signatures; of 50,000 sampled offsets, 2,587 were confirmed as parseable log records and 27 were successfully reconstructed into queries dating from 2020, despite the server having been in continuous use since 2022.
- A comparative validation against the commercial tools ApexSQL Recover and Stellar Log Analyzer for MSSQL Database confirmed identical INSERT/DELETE/UPDATE detection counts (3000/1000/1000) on the self-generated dataset.

## Related Objectives

- `DFO-1001` Reconstruct events

## Related Weaknesses

- [[weaknesses/MSSQL transaction log record carving fails when a record is fragmented across file-system clusters]]

## References

- [LWCite-1229] Choi and Lee, 2023, "Forensic analysis of SQL server transaction log in unallocated area of file system", DFRWS 2023 APAC; FSI: Digital Investigation 46, 301605.
