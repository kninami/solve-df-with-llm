---
id: DFW-1124
type: weakness
name: Coffee file system version-ordering by content similarity fails once whole-file changes and intervening sectors are erased
description: Establishing the chronological order of a Coffee file system file's deleted/historical versions by content-similarity diffing only works reliably when successive versions change gradually; where a file's entire content is rewritten between versions rather than incrementally updated, similarity to older versions collapses immediately, so version order cannot be inferred once any intervening versions have been erased from flash.
categories:
  - ASTM_MISINT
mitigation_ids:
  - DFM-1124
source_refs:
  - DFCite-1118
updated_at: 2026-08-12
status: complete
---

# Coffee file system version-ordering by content similarity fails once whole-file changes and intervening sectors are erased

## Summary

Testing three file-modification strategies (a single 1-2 byte value change per version, a gradually changing value, and a whole-file rewrite between every version) found that similarity between the active version and older versions decreased gradually with age only for the gradually-changing file. For the file modified by a small isolated value change and for the file rewritten wholesale each version, similarity to older versions did not decline gradually — it was effectively flat or immediately low — so the content-difference method could not use similarity trends to reconstruct their chronological order once any intervening sector had already been erased.

## Why It Matters

An investigator using content-similarity diffing to reconstruct a Coffee file's version history may get a reliable chronological ordering for one file (whose content happens to change gradually) and an unreliable or unreconstructable ordering for another file on the same device, purely because of how that file's content happened to be modified by the application — a distinction not evident from the recovered file content itself, and one that becomes unrecoverable once the sectors needed to fill the ordering gap have already been erased and reused.

## Related Mitigations

- [[mitigations/Corroborate Coffee file system version ordering with sector-allocation and write-pattern evidence rather than content similarity alone]]

## Used By

- [[techniques/Reconstruct deleted and versioned files from the Coffee file system on Contiki OS IoT devices]]

## References

- [DFCite-1118] Sandvik et al., 2021, "Coffee forensics - Reconstructing data in IoT devices running Contiki OS", FSI: Digital Investigation 37.
