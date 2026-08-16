---
id: DFW-2059
type: weakness
name: Zip-based embedded-picture extraction misses images in documents saved by newer Microsoft Office versions
description: Extracting embedded pictures from office documents by walking the document's Zip archive structure to a fixed, expected media directory fails against documents saved by MS Office 2019 or MS Office 365, which changed how embedded pictures are stored internally, and against image formats outside a tool's supported set.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-2060
source_refs:
  - DFCite-2059
updated_at: 2026-08-15
status: complete
---

# Zip-based embedded-picture extraction misses images in documents saved by newer Microsoft Office versions

## Summary

Zip-based embedded-picture extraction relies on office document formats storing embedded media in a predictable internal Zip directory. The authors explicitly report this assumption breaks for documents created with MS Office 2019 or MS Office 365, which changed how embedded pictures are stored, so extraction against those documents may silently miss embedded images. The same tool's extraction coverage is separately limited to PNG, JPG/JPEG, and GIF picture signatures, so embedded pictures in other image formats are not recovered by header/footer signature carving either.

## Why It Matters

An investigator who runs automated embedded-image extraction over a document corpus and finds no images, or fewer than expected, may incorrectly conclude no relevant pictures exist in those documents, when in fact the pictures are present but stored in a directory structure or format the extractor does not recognize — a completeness gap that is easy to overlook because the tool does not fail loudly, it simply extracts nothing for the affected documents.

## Related Mitigations

- [[mitigations/Supplement zip-based embedded-picture extraction with manual export or an updated extractor for newer document formats]]

## Used By

- [[techniques/Extract embedded picture files from documents and disk images using format-aware carving]]

## References

- [DFCite-2059] Gogia & Rughani, 2023, "An ML Based Digital Forensics Software for Triage Analysis Through Face Recognition", JDFSL, Manuscript 1772. States explicitly that "embedded image extraction may not work with documents created using MS Office 2019 or MS Office 365 due to the change in how embedded pictures are stored" and that the carver only supports PNG, JPG/JPEG, and GIF signatures.
