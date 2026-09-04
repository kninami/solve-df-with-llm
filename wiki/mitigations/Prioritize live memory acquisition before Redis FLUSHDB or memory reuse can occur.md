---
id: LWM-1015
type: mitigation
name: Prioritize live memory acquisition before Redis FLUSHDB or memory reuse can occur
source_refs:
  - LWCite-1009
updated_at: 2026-08-09
status: complete
---

# Prioritize live memory acquisition before Redis FLUSHDB or memory reuse can occur

## Summary

Because dictEntry-based Redis deleted-record recovery only works while deleted records' memory remains unreclaimed, prioritize acquiring a memory image of a live Redis instance as early as possible in the response, before a suspect can issue a `FLUSHDB`/`FLUSHALL` command or before continued database activity overwrites the freed memory.

## Addresses

- [[weaknesses/Redis deleted-record recovery fails when nofree is disabled or the database is flushed]]

## How To Apply

When a Redis instance is identified as relevant to an investigation (e.g., a compromised server suspected of data tampering), capture a memory image or snapshot as soon as operationally possible rather than waiting, since ordinary continued use of the database will progressively overwrite the memory addresses this technique depends on. Where possible, verify the server's `nofree` configuration; if it has been explicitly set to 1, or if a `FLUSHDB`/`FLUSHALL` is confirmed to have already executed, do not rely on this recovery technique and instead pursue other sources such as the RDB snapshot file, AOF (Append Only File) log, or any available replication/backup copies.

## References

- [LWCite-1009] Chopade and Pachghare, 2021, "A data recovery technique for Redis using internal dictionary structure", FSI: Digital Investigation 38.
