---
id: DFW-1274
type: weakness
name: X-ray exposure of multi-level flash memory can introduce uncorrectable bit errors
description: Using X-ray radiography or tomography to diagnose or reverse-engineer a component containing multi-level-cell NAND flash memory risks physically altering the stored charge state of memory cells, introducing bit errors that the flash's own error-correction capacity may not be able to fully correct, potentially damaging the very data the investigation aims to recover.
categories:
  - ASTM_INAC_COR
mitigation_ids:
  - DFM-1275
source_refs:
  - DFCite-1302
updated_at: 2026-08-14
status: complete
---

# X-ray exposure of multi-level flash memory can introduce uncorrectable bit errors

## Summary

The underlying study explicitly cautions that "experts should caution about the possibility of introducing uncorrectable bit errors when using x-rays on multilevel flash memories," citing prior published research demonstrating that X-ray exposure can shift the trapped-charge levels multi-level-cell NAND flash uses to represent more than one bit per cell, and that the resulting errors can exceed what the flash controller's built-in error-correcting code is able to fix.

## Why It Matters

An investigator using X-ray diagnostics or tomography to examine a damaged component containing multi-level flash memory faces a direct trade-off: the imaging needed to diagnose the damage and plan a repair can itself introduce new, potentially uncorrectable data errors in the very memory the repair is meant to make readable, and this risk is not visually apparent from the X-ray images themselves — the investigator has no immediate way to know if or how much data corruption occurred until later attempting to read the memory. This is particularly consequential because the technique's advantage (diagnosing a component non-destructively) can be partially undermined if the diagnostic step itself is not actually side-effect-free for this specific memory type.

## Related Mitigations

- [[mitigations/Weigh the diagnostic benefit of X-raying multi-level flash memory against the risk of introducing bit errors]]

## Used By

- [[techniques/Repair a damaged PCB track using 3D X-ray tomography-guided reverse engineering]]

## References

- [DFCite-1302] Heckmann, Souvignet, Sauveron and Naccache, 2021, "Medical Equipment Used for Forensic Data Extraction: A low-cost solution for forensic laboratories not provided with expensive diagnostic or advanced repair equipment", FSI: Digital Investigation 36, 301092.
