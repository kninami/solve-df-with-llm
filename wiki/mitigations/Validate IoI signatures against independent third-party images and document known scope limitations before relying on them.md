---
id: DFM-1081
type: mitigation
name: Validate IoI signatures against independent third-party images and document known scope limitations before relying on them
source_refs:
  - DFCite-1071
updated_at: 2026-08-10
status: complete
---

# Validate IoI signatures against independent third-party images and document known scope limitations before relying on them

## Summary

Before relying on a community-shared or self-developed Indicator of Inconsistency (IoI) signature in casework, validate it against forensic images independent of the dataset it was originally developed on, and document any known scope limitations discovered during refinement.

## Addresses

- [[weaknesses/IoI signatures developed on a controlled dataset produce false positives against independent third-party forensic images]]

## How To Apply

Run candidate IoI signatures against third-party or previously-unseen images before trusting their output in a new case, tracing any false-positive matches back to their source artifacts to refine the signature's scoping logic (e.g. narrowing an overly broad filename match, or requiring more specific write semantics). Record known scope limitations (such as unhandled multi-profile or multi-provenance cases) alongside the signature in the shared repository so other investigators know its validated boundaries.

## References

- [DFCite-1071] Gunestas et al., 2026, "An indicator of inconsistency framework for detecting contradictory digital artifacts", FSI: Digital Investigation 58.
