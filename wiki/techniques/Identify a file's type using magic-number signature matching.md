---
id: DFT-1193
type: technique
name: Identify a file's type using magic-number signature matching
description: Determine a file's true type by matching a short, position-sensitive sequence of bytes (its magic number/signature), typically near the start of the file, against a database of known type signatures, independent of and more reliable than the file's extension.
objective_ids:
  - DFO-1002
weakness_ids:
  - DFW-1200
aliases:
  - Magic-number-based file type identification
  - Signature-based file type identification
source_refs:
  - DFCite-1211
updated_at: 2026-08-13
status: complete
---

# Identify a file's type using magic-number signature matching

## Summary

Rather than trusting a file's extension, a magic-number-based tool inspects a database-matched byte sequence within the file's content (e.g. the Unix `file` command's textual magic-file database) to determine its true type, which stays accurate even when the extension has been changed, removed, or was never present, unlike extension-inference tools.

## Details

A comparative benchmark of 10 file-type identification tools (academic and non-academic, including `filetype`, `file-type`, `detect-file-type`, `guess-file-type`, ForENSIque, Fidentify, TrID, EnCase, Autopsy, and Unix `file`) on two datasets (17,500 and 1,000,000 files) via a purpose-built benchmarking platform (G'DIP) found wide accuracy variation, from 34.1% (`guess-file-type`) to 98.1% (Fidentify) on the larger dataset. Magic-number-based tools were, on average, both more accurate and unaffected by extension tampering, while tools that rely partly or wholly on the file extension for identification (`guess-file-type`, EnCase, Autopsy) saw substantial accuracy drops when extensions were removed or renamed. Computation time varied by orders of magnitude between tools (30 seconds to over 4 hours on the 17,500-file dataset) and was found not to correlate with file size, but likely with the size and search algorithm of each tool's signature database.

## Examples

- On the 1,000,000-file dataset, Fidentify (magic-number-based) held steady at 98.1% accuracy whether file extensions were present, removed, or renamed, while `guess-file-type` (extension-reliant) dropped from 96.6% (extensions present) to 38.2% (extensions removed or renamed) — a 58.4-percentage-point collapse.
- Neither Fidentify nor EnCase recognized certain popular but less common extensions (e.g. `7z`, `dpx`) at all, indicating that even accurate magic-number tools require an actively maintained signature database to cover emerging or less common formats.

## Related Objectives

- `DFO-1002` Extract data from specific formats

## Related Weaknesses

- [[weaknesses/Failure to rely on magic-number signatures causes file type identification tools to be defeated by extension tampering]]

## References

- [DFCite-1211] Dubettier et al., 2023, "File type identification tools for digital investigations", FSI: Digital Investigation 46, 301574.
