---
id: LWM-1181
type: mitigation
name: Select a collision-resistant hash function and consider parallel multi-hash verification for Merkle-tree evidence containers
source_refs:
  - LWCite-1183
updated_at: 2026-08-12
status: complete
---

# Select a collision-resistant hash function and consider parallel multi-hash verification for Merkle-tree evidence containers

## Summary

When building or configuring a Merkle-tree-based evidence container, select a currently robust, collision-resistant hash function for the Merkle tree, and consider computing the tree with multiple independent hash functions in parallel so that a future weakness discovered in one algorithm does not by itself invalidate the container's tamper-evidence guarantee.

## Addresses

- [[weaknesses/Merkle-tree evidence container tamper detection is only as strong as its chosen hash function]]

## How To Apply

Configure the evidence-container tooling to use a modern, well-vetted hash algorithm (avoiding functions with known collision weaknesses) and record which algorithm(s) were used in the container's own metadata; where feasible, compute and store parallel Merkle roots under two independent hash functions so that a container's integrity claim does not rest on a single algorithm's continued strength over the life of a case.

## References

- [LWCite-1183] Han et al., 2024, "ECo-Bag: An elastic container based on merkle tree as a universal digital evidence bag", FSI: Digital Investigation 49. Recommends selecting a robust hash function and potentially employing multiple hash functions in parallel.
