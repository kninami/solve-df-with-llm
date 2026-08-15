---
id: DFT-2059
type: technique
name: Extract embedded picture files from documents and disk images using format-aware carving
description: Recover picture files embedded inside office documents, PDFs/EPUBs, and raw container formats (disk images, ISO, log, and packet-capture files) by applying the extraction method appropriate to each container's structure, rather than a single generic carving pass.
objective_ids:
  - DFO-1002
weakness_ids:
  - DFW-2059
aliases:
  - SynFO file-in-file extraction
source_refs:
  - DFCite-2059
updated_at: 2026-08-15
status: complete
---

# Extract embedded picture files from documents and disk images using format-aware carving

## Summary

Different container formats store embedded pictures differently, so reliable extraction requires matching the extraction method to the container: raw/opaque formats (DD disk images, ISO, LOG, PCAP) are scanned with classic file-signature header/footer carving, while Zip-based office document formats (PPT/PPTX, DOC/DOCX, XLS/XLSX, ODT/ODP/ODF) are opened as Zip archives and walked for their media directory, and PDF/EPUB documents are parsed with a dedicated reading library. Every extracted candidate is then re-verified against its own magic-byte signature to reject false positives.

## Details

The method builds a per-container-type extraction pipeline: header/footer signature carving locates image byte ranges within otherwise unstructured or opaque files (disk images, logs, packet captures) by matching each supported image format's characteristic start and end byte sequences; Zip extraction exploits the fact that modern office document formats are themselves Zip archives with a predictable internal media directory, so the archive is walked directly rather than carved; and PDF/EPUB extraction relies on a dedicated document-parsing library rather than carving, since those formats do not expose a simple archive or byte-signature structure. Extracted files are always re-checked against magic bytes before being kept, guarding against both carving false positives and archive entries that are not actually valid images. This complements [[techniques/Identify a person of interest across extracted images using automated face recognition matching]] as its upstream extraction step, and is a narrower, format-aware alternative to generic single-signature file carving.

## Examples

- Extracting PNG, JPG/JPEG, and GIF pictures from a forged student-ID document created as a word-processor file, by walking the document's Zip archive structure to its embedded media directory rather than carving the whole document byte-for-byte.
- Header/footer carving picture files directly out of a raw disk image (DD) and a packet capture (PCAP) file using the same magic-byte-based method.

## Related Objectives

- `DFO-1002` Extract data from specific formats

## Related Weaknesses

- [[weaknesses/Zip-based embedded-picture extraction misses images in documents saved by newer Microsoft Office versions]]

## References

- [DFCite-2059] Gogia & Rughani, 2023, "An ML Based Digital Forensics Software for Triage Analysis Through Face Recognition", JDFSL, Manuscript 1772. Source of the per-container-type (header/footer carving vs. Zip extraction vs. PDF/EPUB library reading) embedded-picture extraction methodology.
