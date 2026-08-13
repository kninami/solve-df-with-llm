---
id: DFW-1120
type: weakness
name: Chip-off removal or restoration handling can catastrophically fracture the target IC before it can be read
description: Imprecise heat control during desoldering, or excessive mechanical pressure during post-removal cleanup (e.g. clamping the IC in a vice against too narrow a base plate), can crack or split a chip-off target chip outright, causing total and irrecoverable loss of the stored data rather than merely altering the device's state.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1120
source_refs:
  - DFCite-1112
updated_at: 2026-08-12
status: complete
---

# Chip-off removal or restoration handling can catastrophically fracture the target IC before it can be read

## Summary

Chip-off's irreversibility is usually discussed in terms of a functionally altered device that forecloses non-destructive re-examination, but a documented case study shows a more severe failure mode: during the restoration stage of "Operation Snappy," an IC was secured in a vice with too narrow a base plate, and as the vice was tightened the IC instantly split into two pieces. Once an IC is cracked or split, data recovery is described as near impossible due to the destruction of its internal nanostructure, ending the case at that stage with no data at all — as opposed to a successful (if irreversible) extraction.

## Why It Matters

Unlike the general irreversibility of chip-off (which still yields data, just forecloses a repeat examination), a catastrophic fracture during removal or restoration destroys the evidence itself. Because low-cost, accessible tooling (general-purpose hot-air guns, improvised base plates and clamps) offers less precise thermal and mechanical control than specialist equipment, this risk is elevated whenever accessible rather than specialist tools are used, particularly during restoration handling where the chip is most fragile.

## Related Mitigations

- [[mitigations/Practice chip-off removal and restoration on a replica device and use standardized fitted fixtures before working the exhibit]]

## Used By

- [[techniques/Extract flash chip contents via chip-off desoldering]]

## References

- [DFCite-1112] Hadgkiss et al., 2022, "Cheap as chips: An accessible chip off acquisition method for ball grid array (BGA) integrated circuits in digital investigations", FSI: Digital Investigation 42-43.
