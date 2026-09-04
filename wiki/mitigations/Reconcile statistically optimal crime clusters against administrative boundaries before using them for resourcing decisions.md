---
id: LWM-2088
type: mitigation
name: Reconcile statistically optimal crime clusters against administrative boundaries before using them for resourcing decisions
source_refs:
  - LWCite-2103
updated_at: 2026-08-16
status: complete
---

# Reconcile statistically optimal crime clusters against administrative boundaries before using them for resourcing decisions

## Summary

Before using a statistically-optimal crime-cluster map to inform patrol allocation, station placement, or district-boundary decisions, explicitly check the clusters against existing administrative district boundaries and adjust for operational practicality, rather than applying the statistically optimal cluster count and locations directly.

## Addresses

- [[weaknesses/Statistically optimal crime clusters do not align with police administrative district boundaries]]

## How To Apply

Overlay the k-means cluster boundaries and centroids (selected via a validity index such as Calinski-Harabasz) onto a map of existing administrative district boundaries, and manually assess how well they align. Where clusters cross district lines or produce centroids far from any feasible station location, treat the clustering output as a directional signal (which broad areas warrant more attention) rather than a literal resourcing plan, and combine it with the complementary kernel-density-estimation surface -- which some analysts find easier to interpret for identifying specific high-risk sub-areas within a broader region -- to develop a resourcing recommendation that accounts for both statistical concentration and practical operational constraints.

## References

- [LWCite-2103] Kowalski, Kusy, and Kocierz, 2023, "The forensic information identification based on machine learning algorithms", FSI: Digital Investigation 47, 301619.
