---
id: LWW-1148
type: weakness
name: A privileged database user can disable audit logging without leaving a log-based trace of query activity
description: A database administrator (or an attacker who has gained equivalent privileges) can temporarily disable or bypass a DBMS's audit logging, execute a query, and re-enable logging, so the audit log itself contains no record of the query even though the query was necessarily processed in the DBMS's memory.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - LWM-1148
source_refs:
  - LWCite-1144
updated_at: 2026-08-12
status: complete
---

# A privileged database user can disable audit logging without leaving a log-based trace of query activity

## Summary

Every major relational DBMS provides a privileged command to suspend audit logging (e.g., `NOAUDIT SESSION` in Oracle, `audit_log_connection_policy=NONE` in MySQL, `ALTER SERVER AUDIT ... WITH (STATE=OFF)` in SQL Server), and none of these commands prevent the query itself from being processed and cached in memory in the normal way. A privileged user or an attacker who has obtained equivalent access can therefore execute a query — most concerning for read-only `SELECT` retrieval, since prior tamper-evident logging work has focused on detecting modifications from `INSERT`/`UPDATE`/`DELETE` rather than data retrieval — that leaves no entry in the audit log at all, rather than a modified or deleted one.

## Why It Matters

An investigator who treats a DBMS's own audit log as a complete record of query activity may conclude no data was accessed during a suspected breach window, when in fact a privileged account temporarily suspended logging to retrieve sensitive data undetected. Because the memory artifacts left by the query are themselves volatile (subject to being overwritten by subsequent activity or reclaimed by the DBMS's page-replacement policy), this gap can be effectively permanent if a trusted memory snapshot is not captured before the relevant pages are evicted.

## Related Mitigations

- [[mitigations/Cross-check DBMS audit logs against memory-cache access-pattern evidence to detect disabled logging]]

## Used By

- [[techniques/Verify database audit logs using memory-cached page access patterns]]

## References

- [LWCite-1144] Wagner, Nissan and Rasin, 2023, "Database memory forensics: Identifying cache patterns for log verification", FSI: Digital Investigation 45.
