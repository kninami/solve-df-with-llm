---
id: LWT-2083
type: technique
name: Recover a document's content from RAM by accounting for its file format and storage-media source
description: When attempting to recover a document's textual content from a memory image, tailor expectations of success to the document's file format (plain text, RTF, DOCX, ODT, or PDF), the storage medium it was opened from (local disk, cloud service, or remote desktop connection), and whether the document was still open or had already been closed at the time of memory capture, since each of these factors independently and substantially affects the proportion of content recoverable.
objective_ids:
  - DFO-1002
  - DFO-1019
weakness_ids:
  - LWW-2086
aliases:
  - Document format, size, and storage media effects on memory forensics
source_refs:
  - LWCite-2101
updated_at: 2026-08-16
status: complete
---

# Recover a document's content from RAM by accounting for its file format and storage-media source

## Summary

The amount of a document's textual content recoverable from a RAM image is not uniform across cases: it varies substantially by the document's file format (because richer formats like DOCX embed content within more complex internal markup that complicates in-memory recovery), by the storage medium the document was opened from (local disk, cloud storage such as Gmail/Google Drive/OneDrive/Dropbox, or a remote desktop connection), and by whether the document was still open in its authoring application or had already been closed when the memory image was captured -- each shown experimentally to independently affect the successfully-recovered content ratio.

## Details

Text-based files (TXT, RTF) recovered most reliably from local storage media (local hard disk and removable USB) in both the opened and closed states, typically in the 80-90% range while opened and remaining comparatively high (though more variable) after closing. Rich-content formats (DOCX, ODT) internally represent content using descriptive markup (e.g. XML), which mingles textual data within language features and complicates in-memory recovery relative to plain text; these formats showed good recovery from local storage while open, but recovery dropped sharply after closing, particularly for cloud-based sources. PDF files, despite their format-preservation reputation, showed comparatively low recovery from local storage but unexpectedly higher recovery from certain cloud sources (Dropbox, Gmail, Google Drive) while open. Across all formats, cloud-based storage media (Gmail, Google Drive, OneDrive, Dropbox) produced substantially more variable and generally lower recovery ratios than local storage, and remote desktop connections produced the worst recovery of any storage medium tested, often near zero, because a remote desktop connection's client-side memory holds comparatively little of the actual document content (most of it residing on the remote host instead). Document file size, by contrast, was found to have minimal effect on the recovered-content ratio once format and storage medium are accounted for -- averaging roughly 40% of content recoverable across sizes when both opened and closed states are combined, but this obscures a sharp difference by state alone: roughly 60% recoverable while the document remains open versus roughly 20% once closed, regardless of file size.

## Examples

- Across six different file sizes tested per format, opened local-hard-disk and removable-USB text files recovered 80-90%+ of content on average, dropping to single-digit percentages for the same files retrieved via a remote desktop connection.
- DOCX files opened from OneDrive or Google Drive recovered 80-90%+ of content, comparable to local storage, while the same files retrieved via Gmail or Dropbox recovered only around 20-25% -- showing that recovery ratio depends on the specific cloud provider, not simply "cloud vs. local" as a binary distinction.
- PDF files showed an unusual pattern relative to the other formats: while opened, Dropbox, Gmail, and Google Drive sources recovered close to 100% of content (the highest of any storage medium tested for PDFs), exceeding even the local hard disk and removable USB results for the same file type.

## Related Objectives

- `DFO-1002` Extract data from specific formats
- `DFO-1019` Detect anti-forensics and other anomalies

## Related Weaknesses

- [[weaknesses/Closing a cloud-opened or remote-desktop-opened document drastically reduces its RAM-recoverable content compared to a local document]]

## References

- [LWCite-2101] Al-Sharif, Al-Senjalawi, and Alzoubi, 2024, "The effects of document's format, size, and storage media on memory forensics", FSI: Digital Investigation 48, 301692.
