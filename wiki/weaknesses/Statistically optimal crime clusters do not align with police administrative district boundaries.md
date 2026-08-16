---
id: DFW-2088
type: weakness
name: Statistically optimal crime clusters do not align with police administrative district boundaries
description: A k-means crime-cluster partition chosen to maximize a clustering-validity index (such as the Calinski-Harabasz index) produces geographically scattered, statistically well-defined clusters that generally do not correspond to a police force's existing administrative district boundaries, so the clustering result cannot be directly applied to district-level resourcing decisions without further reconciliation.
categories:
  - ASTM_MISINT
mitigation_ids:
  - DFM-2088
source_refs:
  - DFCite-2103
updated_at: 2026-08-16
status: complete
---

# Statistically optimal crime clusters do not align with police administrative district boundaries

## Summary

Selecting a k-means cluster count purely to maximize a statistical clustering-validity index (the Calinski-Harabasz index) produced clusters of high internal statistical quality but a geographic arrangement that, when compared against a jurisdiction's actual police-district boundaries, showed little correspondence: cluster centroids were scattered relative to district centers, and the clusters did not follow district boundary lines. Applying the clustering results directly to decisions such as police-station placement or district boundary redrawing would in practice require relocating stations or redrawing boundaries to match statistically-derived cluster centroids, which the study's own authors note is largely impractical to implement.

## Why It Matters

A decision-maker who is presented with a statistically well-validated crime-cluster map (a high clustering-validity index score) could reasonably but mistakenly assume the clusters are also operationally meaningful for existing administrative structures, when in fact statistical optimality and administrative alignment are independent properties that were shown not to coincide in this analysis. Treating a high validity-index score as a signal of direct operational applicability, without separately checking alignment against the jurisdiction's actual administrative boundaries, risks recommending impractical or low-value resourcing changes.

## Related Mitigations

- [[mitigations/Reconcile statistically optimal crime clusters against administrative boundaries before using them for resourcing decisions]]

## Used By

- [[techniques/Visualize spatial and temporal crime hot-spots using k-means clustering and kernel density estimation]]

## References

- [DFCite-2103] Kowalski, Kusy, and Kocierz, 2023, "The forensic information identification based on machine learning algorithms", FSI: Digital Investigation 47, 301619.
