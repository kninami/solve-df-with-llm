---
id: DFM-1014
type: mitigation
name: Extend file carving tools to search bidirectionally using carving-distance gap estimates
source_refs:
  - DFCite-1008
updated_at: 2026-08-09
status: complete
---

# Extend file carving tools to search bidirectionally using carving-distance gap estimates

## Summary

Modify file carving strategy and tooling to search backward as well as forward from a candidate fragment for a second fragment, using carving-distance gap-size statistics (including their observed clustering around powers of two) to bound and prioritize the search space, rather than assuming all fragments occur in forward disk order.

## Addresses

- [[weaknesses/Existing file carvers ignore out-of-order NTFS file fragmentation]]

## How To Apply

When developing or selecting a file carver for NTFS-formatted evidence, confirm whether it accounts for out-of-order fragmentation; if it does not, treat its reported recovery rate for fragmented files as an upper bound rather than an accurate estimate, since close to half of fragmented files may be missed. Where custom carving is feasible, bound the backward search using the carving-distance metric and its observed power-of-two clustering to keep the search space tractable, and prioritize this investment for file types shown to have high out-of-order rates (bmp, png, raw images, and other formats relevant to the specific investigation).

## References

- [DFCite-1008] van der Meer et al., 2021, "A contemporary investigation of NTFS file fragmentation", FSI: Digital Investigation 38.
