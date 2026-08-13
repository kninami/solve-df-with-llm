---
id: DFT-1174
type: technique
name: Preserve digital evidence integrity using a Merkle-tree-based elastic evidence container
description: Store collected digital evidence items inside a single elastic container that computes a Merkle tree over per-item hashes, so that individual items can be selectively destroyed, encrypted, or compressed as an investigation proceeds while a single Merkle-root value still lets any party verify the integrity of the container and every item's provenance history.
objective_ids:
  - DFO-1010
weakness_ids:
  - DFW-1181
aliases:
  - ECo-Bag
  - Merkle-tree universal digital evidence bag
source_refs:
  - DFCite-1183
updated_at: 2026-08-12
status: complete
---

# Preserve digital evidence integrity using a Merkle-tree-based elastic evidence container

## Summary

Traditional digital evidence bags are typically static, whole-container hash structures that make it awkward to selectively delete privacy-irrelevant items, encrypt sensitive items, or re-triage a case without re-sealing the entire evidence set. An ECo-Bag container instead maintains a Merkle tree of per-item hashes plus a `stateInfo` metadata record of each item's state (normal, deleted, encrypted, compressed) and its full history, so items can be individually updated while the Merkle root still lets any party verify that the container as a whole, and every unmodified item within it, remains untampered.

## Details

Each item in the container has an `itemState` and, when hashed, an `itemHash`; the container-level `stateInfo` JSON file records every item's metadata plus a `history` log of state transitions and a `merkleroot` computed from all item hashes (Algorithm 1: hash the leaves pairwise up the tree, duplicating the last hash if the leaf count is odd). Three update operations are supported per item: Destruction (secure deletion — the item's data is discarded but its prior hash is retained so it still contributes to the Merkle root), Encryption, and Compression; each update increments the container's `state` counter and appends a new `stateInfo` entry (Algorithm 2). A full-mode Verify operation (Algorithm 3) recomputes every item's current hash (decrypting or reading as appropriate) and checks it against the stored Merkle root to detect any tampering; a preview mode instead scans only the recorded `itemHash` values without needing the underlying data, useful for lightweight or partial sharing of the evidence set. Because only the changed item's hash needs recomputation to update the Merkle root, ECo-Bag processes evidence updates and full-container integrity verification substantially faster than legacy whole-image hashing approaches, particularly as item count and multithreading increase. This shares the general goal of tamper-evident, verifiable evidence integrity with [[techniques/Anchor digital evidence integrity and chain of custody on a blockchain]], but computes and verifies its Merkle root locally within the container itself rather than anchoring custody events to an external distributed ledger.

## Examples

- In a comparative runtime test against EnCase and FTK producing an E01 image from two 8 GB USB drives, using a Merkle tree with two threads for integrity verification (Step 3: Verified) took 58 seconds, versus 90-107 seconds for the commercial tools' equivalent verification step, with the advantage widening as thread count and item/data volume increased (tested up to 1 TB / 123,982 files).
- Requesting only a specific user's chat history from a seized messenger-app database can be represented as a secondary outcome stored in the ECo-Bag alongside the original database file (kept in 'normal' state) and the extraction query itself, preserving the original source while still tracking and hash-verifying the derived result.

## Related Objectives

- `DFO-1010` Preserve digital evidence

## Related Weaknesses

- [[weaknesses/Merkle-tree evidence container tamper detection is only as strong as its chosen hash function]]

## References

- [DFCite-1183] Han et al., 2024, "ECo-Bag: An elastic container based on merkle tree as a universal digital evidence bag", FSI: Digital Investigation 49.
