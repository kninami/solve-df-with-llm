---
id: DFT-2085
type: technique
name: Visualize spatial and temporal crime hot-spots using k-means clustering and kernel density estimation
description: Given a database of geolocated, timestamped crime records for a jurisdiction, identify when and where specific crime types cluster by grouping incident occurrences by day-of-week and hour-of-day, spatially partitioning incident locations with k-means clustering (selecting cluster count via the Calinski-Harabasz validity index), and generating a continuous risk-density surface with kernel density estimation, to visually and quantitatively support resource-allocation and patrol-planning decisions.
objective_ids:
  - DFO-1009
  - DFO-1004
weakness_ids:
  - DFW-2088
aliases:
  - Crime event spatial-temporal clustering and KDE visualization
source_refs:
  - DFCite-2103
updated_at: 2026-08-16
status: complete
---

# Visualize spatial and temporal crime hot-spots using k-means clustering and kernel density estimation

## Summary

A jurisdiction's crime-incident database records each event's type, location, and timestamp but does not by itself reveal when and where a particular crime type is concentrated. Combining a temporal breakdown (day-of-week and hour-of-day incident counts per crime type) with two complementary spatial-analysis methods -- k-means clustering, which partitions incident locations into discrete geographic groups, and kernel density estimation (KDE), which produces a smooth, continuous probability-density surface -- gives an analyst both a discrete and a continuous view of where a crime type concentrates, supporting decisions such as police-station placement or patrol-priority scheduling.

## Details

Temporal analysis first buckets each crime type's incidents by day of week and by hour of day (using simple counting) to reveal within-week and within-day patterns, such as whether a crime type is more common on weekdays than weekends, or during particular hours. Spatial clustering then applies the k-means algorithm to incident coordinates (using Euclidean distance) for each crime type independently, iteratively testing cluster counts and selecting the value that maximizes the Calinski-Harabasz (CH) index -- a clustering-validity measure based on the ratio of between-cluster to within-cluster variance, where a higher CH index indicates a more well-defined partition -- rather than fixing an arbitrary cluster count in advance. Kernel density estimation separately computes a non-parametric probability-density surface directly from incident coordinates using a chosen kernel function (e.g. the Epanechnikov kernel) and a smoothing parameter, producing a continuous heat-map-style visualization (rather than discrete cluster boundaries) that some analysts find more directly interpretable for identifying the specific highest-risk sub-areas within a broader clustered region.

## Examples

- Applied to seven major crime types recorded by the City of Baltimore, Maryland (larceny, common assault, burglary, larceny in car, aggravated assault, theft of car, robbery-street), temporal analysis found larceny and burglary occurred markedly less often on weekends (attributed to more residents being home, reducing opportunity), while other crime types showed comparatively flat day-of-week distributions; nearly all crime types showed a minimum occurrence rate between 4:00-7:00 a.m. and a rise toward a peak around 20:00-24:00.
- K-means clustering (cluster count selected via CH index, ranging from k=27 for theft of car to k=30 for most other types) showed most crime types produced numerous small, spatially scattered clusters concentrated in the city's central-northern area that did not correspond to police-district boundaries, indicating that clustering purely by CH-index optimality does not automatically yield operationally actionable groupings without further adjustment.
- KDE visualization (Epanechnikov kernel, smoothing parameter h=0.05, chosen as most accurate in prior work by the same authors) showed the large majority of crime types concentrated most heavily in the city center, with aggravated assault showing the least spatial clustering of any type tested (consistent with it being a largely unplanned, emotionally-driven offense rather than one requiring premeditated site selection).

## Related Objectives

- `DFO-1009` Create visualizations
- `DFO-1004` Conduct research

## Related Weaknesses

- [[weaknesses/Statistically optimal crime clusters do not align with police administrative district boundaries]]

## References

- [DFCite-2103] Kowalski, Kusy, and Kocierz, 2023, "The forensic information identification based on machine learning algorithms", FSI: Digital Investigation 47, 301619.
