---
id: DFW-2133
type: weakness
name: Byte-level MMIF modification detection degrades to whole-page reporting when the ISO page is not memory-resident
description: A memory-mapped image file modification-detection technique that relies on the Image Section Object as its memory-resident ground truth cannot identify the exact modified bytes, and falls back to reporting the entire page as modified, whenever the operating system has evicted that ISO page from RAM.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-2134
source_refs:
  - DFCite-2155
updated_at: 2026-08-17
status: complete
---

# Byte-level MMIF modification detection degrades to whole-page reporting when the ISO page is not memory-resident

## Summary

Image Section Object pages are only reliably memory-resident for image files that are actively mapped and accessed by other processes, since Windows evicts infrequently accessed pages under memory pressure. In evaluation, DLLs used by few other processes (e.g., clr.dll, chrome_elf.dll, msedge_elf.dll) had their ISO pages evicted often enough that the resulting loss of ground truth caused every benign modification for those DLLs to be reported as a full unfiltered page rather than the specific patched bytes — the same imprecise result produced by the page-level detection tools the technique was designed to improve upon.

## Why It Matters

When the technique's precision advantage disappears exactly in the cases where an investigator most needs it — a rarely-shared DLL is also a plausible target for an attacker seeking to avoid detection via commonly-instrumented, heavily-shared system libraries — the investigator is left back at manually reviewing up to 4096 bytes per reported page to find the actual malicious modification, with no indication from the tool itself of how much of that page's reported "modification" is a benign difference versus the real injected content.

## Related Mitigations

- [[mitigations/Fall back to on-disk or symbol-server image file copies as ground truth when the ISO page is unavailable]]

## Used By

- [[techniques/Detect memory-mapped image file modifications using Image Section Object byte-level comparison]]

## References

- [DFCite-2155] Block, 2023, "Windows memory forensics: Identification of (malicious) modifications in memory-mapped image files", FSI: Digital Investigation 45.
