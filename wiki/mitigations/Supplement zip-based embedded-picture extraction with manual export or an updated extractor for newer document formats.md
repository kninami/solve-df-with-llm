---
id: LWM-2060
type: mitigation
name: Supplement zip-based embedded-picture extraction with manual export or an updated extractor for newer document formats
source_refs:
  - LWCite-2059
updated_at: 2026-08-15
status: complete
---

# Supplement zip-based embedded-picture extraction with manual export or an updated extractor for newer document formats

## Summary

Do not treat a zero- or low-result automated embedded-picture extraction pass over a set of office documents as proof no embedded pictures exist; verify the document's application version and, where it was created with MS Office 2019/365 or another format the extractor does not recognize, manually export or open the document to check for embedded pictures directly, or use an extractor updated for that format's current internal storage layout.

## Addresses

- [[weaknesses/Zip-based embedded-picture extraction misses images in documents saved by newer Microsoft Office versions]]

## How To Apply

Before relying on automated extraction results for a document corpus, sample-check the application version/metadata of a subset of documents that returned no embedded pictures; for documents from a known-affected office suite version, manually inspect the document (e.g., open it in its native application and export embedded media, or unzip and manually walk the archive structure) rather than accepting the automated null result, and track which document formats and versions the extraction tool currently supports so gaps are documented rather than silently missed.

## References

- [LWCite-2059] Gogia & Rughani, 2023, "An ML Based Digital Forensics Software for Triage Analysis Through Face Recognition", JDFSL, Manuscript 1772. Identifies the MS Office 2019/365 embedded-picture storage change as a known extraction gap and flags it as future-work scope.
