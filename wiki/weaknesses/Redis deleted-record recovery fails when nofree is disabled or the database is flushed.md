---
id: LWW-1015
type: weakness
name: Redis deleted-record recovery fails when nofree is disabled or the database is flushed
description: Memory-address-based Redis deleted-record recovery depends on the deleted dictEntry's memory remaining allocated and unreused; it cannot recover records where nofree was set to 1 (freeing memory immediately) or where the deletion was performed via FLUSHDB/FLUSHALL, both of which reclaim or null the underlying memory rather than merely unlinking it.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - LWM-1015
source_refs:
  - LWCite-1009
updated_at: 2026-08-09
status: complete
---

# Redis deleted-record recovery fails when nofree is disabled or the database is flushed

## Summary

Redis's `dictGenericDelete()` function accepts a `nofree` parameter controlling whether a deleted record's memory is freed. With `nofree=0` (the default), `DEL` unlinks a record from the hash table but frees its memory via `zfree()`, replacing what the recovery technique would read with de-allocated (and eventually overwritten) memory. `FLUSHDB` and `FLUSHALL` remove key-value pairs from an entire database or all databases at once, an operation the technique's evaluation found it could not recover from at all, regardless of the `nofree` setting.

## Why It Matters

An investigator applying this recovery technique to a live-acquired or memory-dumped Redis instance needs to know in advance that its effectiveness is contingent on how the suspect's application was configured (default `nofree` behavior) and on which deletion command was actually used. A case involving `FLUSHDB`/`FLUSHALL` -- plausible if a suspect deliberately wiped the database to destroy evidence -- would produce no recoverable data via this method even though the attempt to recover is otherwise well-founded, and the investigator should not assume the technique's reported 65-99% recovery rates generalize to that scenario.

## Related Mitigations

- [[mitigations/Prioritize live memory acquisition before Redis FLUSHDB or memory reuse can occur]]

## Used By

- [[techniques/Recover deleted Redis keys using dictEntry memory-address diffing]]

## References

- [LWCite-1009] Chopade and Pachghare, 2021, "A data recovery technique for Redis using internal dictionary structure", FSI: Digital Investigation 38.
