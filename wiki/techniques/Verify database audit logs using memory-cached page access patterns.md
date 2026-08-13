---
id: DFT-1145
type: technique
name: Verify database audit logs using memory-cached page access patterns
description: Detect query activity missing from a DBMS's audit log by comparing the table- and page-level access patterns observed in a trusted memory snapshot's I/O buffer and sort area against the set of operations the audit log claims to have occurred, flagging any observed full table scan or index access that no logged query explains.
objective_ids:
  - DFO-1019
weakness_ids:
  - DFW-1148
aliases:
  - RAM spectroscopy log verification
  - DBMS cache-pattern log validation
source_refs:
  - DFCite-1144
updated_at: 2026-08-12
status: complete
---

# Verify database audit logs using memory-cached page access patterns

## Summary

Query operations produce repeatable, DBMS-independent patterns in process memory: a full table scan caches an entire table (or, for large tables, chunks of it) in the I/O buffer, while an index access caches the traversed B-Tree index pages together with the specific table pages they point to, each page carrying an Object ID (identifying its table) and Page ID recoverable via database page carving. By identifying which tables and pages a memory snapshot's I/O buffer and sort area show were actually accessed and checking whether every observed access pattern is explained by a corresponding entry in the audit log, an investigator can validate the log independently of the DBMS's own logging mechanism — including in the presence of a privileged database administrator who has the ability to disable or bypass audit logging altogether.

## Details

The method defines atomic query operations (full table scan and index access as data-access operations; hash-join/sort-table construction as data-manipulation operations in the sort area) and shows their forensic signatures are consistent across representative heap-table (Oracle) and index-organized-table (MySQL) DBMS architectures. Applied to a workload where an unlogged query (e.g., a `SELECT` executed after disabling audit logging) is interleaved with logged queries, the technique correctly flagged the full-table-scan pattern for the table the hidden query touched as unexplained by any log entry, since no logged operation accounted for it. A key limitation the paper identifies is memory volatility: artifact lifetime in the I/O buffer/sort area depends on the DBMS's page-replacement behavior (typically LRU) and the volume of subsequent query activity, so evidence of a hidden query can itself be overwritten before a forensic snapshot is captured, particularly if the malicious query only touches a small table whose pages are quickly evicted. This method complements the same research group's SVM-based query-type classifier (see [[techniques/Classify database query operations from memory using byte-frequency machine learning]]), which classifies the kind of operation performed rather than validating whether logged and observed activity are consistent.

## Examples

- Detecting a hidden `SELECT * FROM Part` query executed by a database administrator who first disabled Oracle's audit log: the memory snapshot's I/O buffer showed a full-table-scan pattern for the Part table that no entry in the (subsequently re-enabled) audit log explained.

## Related Objectives

- `DFO-1019` Detect anti-forensics and other anomalies

## Related Weaknesses

- [[weaknesses/A privileged database user can disable audit logging without leaving a log-based trace of query activity]]

## References

- [DFCite-1144] Wagner, Nissan and Rasin, 2023, "Database memory forensics: Identifying cache patterns for log verification", FSI: Digital Investigation 45.
