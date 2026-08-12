---
id: DFT-1070
type: technique
name: Estimate bullet trajectory angle from sheet-metal bullet-hole length
description: Estimate the angle of incidence of a fired bullet that perforated a thin sheet-metal surface by measuring the length of the resulting bullet hole and applying a pre-established empirical correlation curve (derived from controlled test firings at known angles) between hole length and incident angle, using a purpose-built Android field application that performs the calculation on-site without specialized equipment.
objective_ids:
  - DFO-1001
weakness_ids:
  - DFW-1075
aliases:
  - Bullet-hole-length-based mobile trajectory angle estimation for sheet-metal perforations
  - Bullet Trajectory Plotter
updated_at: 2026-08-10
status: complete
---

# Estimate bullet trajectory angle from sheet-metal bullet-hole length

## Summary

Traditional trajectory-reconstruction methods (such as physical probing) can be impractical or unreliable for very shallow-angle impacts on thin sheet metal, where bullet fragmentation occurs. A prior empirically-derived correlation between the length of a bullet's perforation hole in 1 mm sheet metal and its angle of incidence was packaged into a mobile Android application ("Bullet Trajectory Plotter") so investigators can estimate incidence angles directly in the field by measuring the hole length with a caliper and entering it into the app, without needing specialized equipment or lab access.

## Details

The tool implements the best-fit curve equation relating bullet-hole length to incident angle for standard steel-core 7.62×39 mm AK-pattern ammunition on 1 mm sheet metal, established through controlled test firings. Field testing against a van door (1 mm sheet metal body) fired at multiple known angles found the tool's estimated angles fell within the standard ±5° margin already used in trajectory reconstruction to account for bullet yaw, precession, and nutation, and the tool's accuracy was comparable to the commonly used ellipse method while requiring less specialized measurement.

## Examples

- In a field test firing at nominal angles of 15° to 90° against a van door, the tool's mean estimated angles differed from the actual fired angles by between 0.82° and 3.42° across all tested angles, within the standard ±5° reconstruction tolerance.

## Related Objectives

- `DFO-1001` Reconstruct events

## Related Weaknesses

- [[weaknesses/Bullet-hole-length trajectory estimation cannot be applied to irregular holes from ricocheted or low-stabilization impacts]]
