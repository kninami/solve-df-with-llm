---
id: LWT-1271
type: technique
name: Aggregate module pages across single or multiple Windows memory dumps to reconstruct a complete DLL
description: Reconstruct a 64-bit Windows module (DLL or executable) as completely as possible from memory by combining the partial, differently-mapped pages of that same module loaded by multiple processes within one memory dump (intradump extraction) or across multiple memory dumps from the same or similarly-configured machines (interdump extraction), since any single process only maps the subset of a module's pages it actually uses.
objective_ids:
  - DFO-1002
weakness_ids:
  - LWW-1281
aliases:
  - Modex
  - Intermodex
  - Intradump/interdump module extraction
source_refs:
  - LWCite-1310
updated_at: 2026-08-15
status: complete
---

# Aggregate module pages across single or multiple Windows memory dumps to reconstruct a complete DLL

## Summary

A Windows process only maps into its own address space the pages of a shared module (DLL) that it actually accesses, so extracting a module from a single process (the standard approach of tools like Volatility 3's `windows.modules.Modules --dump`) yields an incomplete file. Because multiple processes on the same machine — or the same machine imaged at different points in time, or similarly-configured machines in a managed environment — each map different subsets of a module's pages, combining the pages recovered across all of them reconstructs the module more completely than any single extraction can.

## Details

For a named module, every process that has it loaded is walked and its mapped pages dumped, using the page frame number database's `PrototypePTE` flag (queried via a PTE enumerator) to determine whether each page is shared (identical content across all processes mapping it) or private (process-specific, e.g. after copy-on-write modification). When multiple pages are available at the same module offset, shared pages are preferred over private pages (since shared content best represents the on-disk original), and when several private pages compete, the page most similar to its offset's corresponding shared page — measured via the TLSH similarity-digest algorithm — is chosen. **Intradump extraction (Modex)**, a Volatility 3 plugin, performs this combination within a single memory dump. **Interdump extraction (Intermodex)**, a separate tool built on Modex, extends the same combination logic across multiple memory dumps (from the same machine captured at different times, or from different machines with a similar configuration so that the same module version is being combined); it currently requires the module to be loaded at the same base address, with the same path and size, in every dump combined, which limits its use across machines with different Address Space Layout Randomization (ASLR) outcomes without a page-granularity derelocation step. Empirically, both the number of recoverable pages and completeness increase monotonically as more processes (intradump) or more memory dumps (interdump) are considered.

## Examples

- Combining pages of `ntdll.dll`, `user32.dll`, and `ole32.dll` mapped by four applications (Chrome, Word, Adobe Acrobat Reader, Excel) across five sequential memory dumps recovered substantially more complete modules than extracting from any single process or single dump alone.
- On rare occasions, Modex found "shared" pages at the same offset with slightly different content across processes — later traced to embedded memory addresses within those pages — and was extended to select the most-repeated shared page as a fallback when this anomaly is detected.

## Related Objectives

- `DFO-1002` Extract data from specific formats

## Related Weaknesses

- [[weaknesses/Combining shared pages from different memory dumps can silently merge inconsistent module content when pages differ]]

## References

- [LWCite-1310] Fernández-Álvarez and Rodríguez, 2023, "Module extraction and DLL hijacking detection via single or multiple memory dumps", FSI: Digital Investigation 44, 301505.
