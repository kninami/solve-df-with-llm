---
id: DFT-1015
type: technique
name: Redis dictEntry memory-address diffing for deleted key recovery
description: Periodically capture the linked-list addresses of a Redis database's hash-table dictEntry structures, diff a later capture against an earlier one to identify addresses that dropped out of the live bucket list but remain unfreed in memory, and type-cast those addresses back to dictEntry to recover the deleted key-value pair.
objective_ids:
  - DFO-1018
weakness_ids:
  - DFW-1015
aliases: []
source_refs:
  - DFCite-1009
updated_at: 2026-08-09
status: complete
---

# Redis dictEntry memory-address diffing for deleted key recovery

## Summary

Redis stores every key-value pair as a dynamically allocated `dictEntry` structure referenced from a hash-table bucket array. When Redis's `nofree` deletion option is left at its default (0), deleting a record with `DEL` unlinks its `dictEntry` from the bucket but does not immediately zero or reallocate the underlying memory, so the address and its data can still be read and recovered before being overwritten.

## Details

The technique runs in two algorithmic stages. First, dictEntry addresses for a given Redis database index are read from the live hash table and stored in a circular doubly linked list; this list is periodically compared against the current Bucket List to identify addresses present in the linked-list history but no longer reachable from the live buckets -- these are the addresses of deleted records. Second, each identified address is type-cast back to a `dictEntry` structure, and a data-type-specific iterator (Quicklist, Set, Dict, or Hash Type Iterator, selected per Redis's internal Data Type field) is used to extract the recovered key-value pair, correctly handling all six core Redis data types (string, list, set, sorted set, hash).

## Examples

- Across four experiments with different insert/delete sequencing patterns on a 50k-record movie dataset, average recovery ranged from 98.60% (bulk insert then incremental delete) down to 65.06% (alternating delete-insert-delete sequences), all completing in under one second.

## Related Objectives

- `DFO-1018` Read data from digital evidence storage formats

## Related Weaknesses

- [[weaknesses/Redis deleted-record recovery fails when nofree is disabled or the database is flushed]]

## References

- [DFCite-1009] Chopade and Pachghare, 2021, "A data recovery technique for Redis using internal dictionary structure", FSI: Digital Investigation 38.
