---
id: DFM-1075
type: mitigation
name: Visually screen bullet hole shape for ricochet or low-stabilization irregularity before applying length-based trajectory estimation
source_refs:
  - DFCite-1065
updated_at: 2026-08-10
status: complete
---

# Visually screen bullet hole shape for ricochet or low-stabilization irregularity before applying length-based trajectory estimation

## Summary

Before using the bullet-hole-length trajectory estimation tool on a given perforation, visually confirm the hole has a regular shape consistent with a directly-fired, stable bullet impact; exclude irregularly-shaped holes caused by ricochet or low in-flight bullet stabilization from this method.

## Addresses

- [[weaknesses/Bullet-hole-length trajectory estimation cannot be applied to irregular holes from ricocheted or low-stabilization impacts]]

## How To Apply

At the scene, photograph and visually assess each candidate bullet hole for regular versus irregular perimeter shape before measuring hole length for the tool; for holes assessed as irregular (suggestive of ricochet or poor in-flight stabilization), use an alternative trajectory-reconstruction method instead, and apply the tool's standard ±5° uncertainty margin when reporting any accepted estimate.

## References

- [DFCite-1065] Nishshanka et al., 2021, "An android-based field investigation tool to estimate the potential trajectories of perforated AK bullets in 1 mm sheet metal surfaces", FSI: Digital Investigation 38.
