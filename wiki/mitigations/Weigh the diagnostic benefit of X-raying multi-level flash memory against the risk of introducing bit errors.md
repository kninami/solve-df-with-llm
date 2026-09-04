---
id: LWM-1275
type: mitigation
name: Weigh the diagnostic benefit of X-raying multi-level flash memory against the risk of introducing bit errors
source_refs:
  - LWCite-1302
updated_at: 2026-08-14
status: complete
---

# Weigh the diagnostic benefit of X-raying multi-level flash memory against the risk of introducing bit errors

## Summary

Before X-raying a component known or suspected to contain multi-level-cell NAND flash memory, deliberately weigh whether the diagnostic or repair benefit justifies the risk of introducing bit errors, and apply the exposure only if that benefit/risk balance favors it, as recommended directly by the underlying study's authors.

## Addresses

- [[weaknesses/X-ray exposure of multi-level flash memory can introduce uncorrectable bit errors]]

## How To Apply

Where feasible, identify the memory type (SLC, MLC, TLC, QLC NAND) before applying X-ray imaging, since the risk and severity of induced bit errors is understood to vary with cell technology. Minimize total X-ray exposure (dose, duration, and number of imaging passes) to the amount actually needed to achieve the diagnostic or repair goal, rather than applying maximal imaging as a default. Where an alternative non-X-ray diagnostic method (e.g. binocular microscope inspection, 2D X-ray only rather than full 3D tomography) can achieve the same investigative goal with lower or no risk to the memory's data integrity, prefer it. Where X-ray exposure of the memory is unavoidable and the data itself (not just physical repair) is the investigative goal, attempt to acquire and hash the memory's contents before any X-ray exposure occurs, so a subsequent read after X-ray-guided repair can be checked for unexpected changes.

## References

- [LWCite-1302] Heckmann, Souvignet, Sauveron and Naccache, 2021, "Medical Equipment Used for Forensic Data Extraction: A low-cost solution for forensic laboratories not provided with expensive diagnostic or advanced repair equipment", FSI: Digital Investigation 36, 301092.
