---
id: DFT-1192
type: technique
name: Determine a ZIP file's creation environment using extra-field structural fingerprints
description: Identify the operating system and application that created or last recompressed a ZIP file by structurally analyzing its local and central-directory extra fields (header ID, timestamp precision, filename encoding, folder-header presence, double-zipping), since different OS/application combinations leave systematically different, reusable structural fingerprints.
objective_ids:
  - DFO-1002
weakness_ids:
  - DFW-1199
aliases:
  - ZIP file fingerprinting for provenance tracking
source_refs:
  - DFCite-1210
updated_at: 2026-08-13
status: complete
---

# Determine a ZIP file's creation environment using extra-field structural fingerprints

## Summary

Every ZIP-compressing application writes a characteristic combination of extra-field header IDs (e.g. `0x000A` NTFS, `0x7875`/`0x5855` Unix UID/GID, `0x7075` UTF-8 path), timestamp precision, filename character encoding, and structural choices such as whether empty-folder headers are created or files are re-compressed on modification ("double zipping"); comparing an unknown ZIP file's extra-field structure against a reference table of these OS/application combinations narrows down, and often uniquely identifies, the environment that created it.

## Details

The technique is implemented as a layered automated classifier: a first algorithm weights reliable, environment-intrinsic characteristics (creating-version byte, extra-field header ID set, data-descriptor presence) most heavily; a second, lower-weight algorithm checks target-file-dependent characteristics (double-zipping, `__MACOSX` folder presence, nanosecond timestamp form, alphabetical file ordering) that can depend on the specific file being compressed rather than purely on the creating environment. Because most applications support adding, deleting, or modifying individual entries in an existing ZIP archive without full recompression, a single archive can end up containing headers from two or more different creating/modifying applications simultaneously, requiring the detailed per-header structural analysis (rather than a single archive-wide check) to correctly attribute provenance. The technique also supports a supplementary decompression-timestamp analysis: which of a decompressed file's modification/access/creation timestamps get set to the decompression time versus preserved from the original compressed value depends on the decompression application and the header ID present, so timestamp interpretation must account for the specific tool used to extract the archive.

## Examples

- Windows: WinRAR, WinZip, 7-zip, Bandizip, and the built-in Compressed Folder feature were each shown to write distinguishable extra-field header ID and timestamp-precision combinations for the same input files.
- macOS/Ubuntu: macOS's `Compress` utility creates a `__MACOSX` folder containing resource-fork metadata that `zip` does not create, and macOS uses NFD UTF-8 encoding for non-ASCII filenames while Windows/Ubuntu use NFC UTF-8, letting the classifier distinguish the creating OS purely from encoding form.
- A field test across three PCs found that a public-computer PC1 had ZIP files bearing a highly varied mix of fingerprints (consistent with importing files created elsewhere), while PC2 and PC3 had more homogeneous, application-specific fingerprint sets consistent with local usage habits — illustrating the technique's use for corroborating or challenging a claimed file origin.

## Related Objectives

- `DFO-1002` Extract data from specific formats

## Related Weaknesses

- [[weaknesses/ZIP extra-field fingerprints become inconsistent when a file is modified or recompressed using different software than created it]]

## References

- [DFCite-1210] Um et al., 2021, "File fingerprinting of the ZIP format for identifying and tracking provenance", FSI: Digital Investigation 39, 301271.
