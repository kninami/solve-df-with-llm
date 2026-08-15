---
id: DFW-1281
type: weakness
name: Combining shared pages from different memory dumps can silently merge inconsistent module content when pages differ
description: Module-aggregation tools that combine pages marked as "shared" across processes or memory dumps assume all shared copies of a given page are content-identical, but in rare cases shared pages at the same offset were observed to differ (due to embedded, process-specific memory addresses), so an aggregated module can silently include a page that does not match the actual on-disk original at that offset.
categories:
  - ASTM_INAC_COR
mitigation_ids:
  - DFM-1282
source_refs:
  - DFCite-1310
updated_at: 2026-08-15
status: complete
---

# Combining shared pages from different memory dumps can silently merge inconsistent module content when pages differ

## Summary

When aggregating a module's pages across processes or memory dumps, a page marked shared is expected to have identical content everywhere it appears, since shared pages are stored only once in physical memory. The developers of Modex/Intermodex found this assumption occasionally breaks: some "shared" pages at the same module offset had small content differences across processes, traced to memory addresses embedded within the page data itself rather than to genuinely different code or resource content.

## Why It Matters

An investigator relying on an aggregated module reconstruction as if it exactly matched the on-disk original risks including a page whose content was silently selected from among several disagreeing candidates, without any flag in the tool's default output indicating that a disagreement occurred at that offset. For evidentiary purposes (e.g. hashing the reconstructed module against a known-good reference, or presenting its content as representative of the loaded code), this ambiguity should be disclosed rather than treated as certain.

## Related Mitigations

- [[mitigations/Manually verify or discard shared pages with inconsistent content before finalizing a combined module extraction]]

## Used By

- [[techniques/Aggregate module pages across single or multiple Windows memory dumps to reconstruct a complete DLL]]

## References

- [DFCite-1310] Fernández-Álvarez and Rodríguez, 2023, "Module extraction and DLL hijacking detection via single or multiple memory dumps", FSI: Digital Investigation 44, 301505.
