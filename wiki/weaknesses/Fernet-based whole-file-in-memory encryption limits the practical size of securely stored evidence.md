---
id: DFW-2043
type: weakness
name: Fernet-based whole-file-in-memory encryption limits the practical size of securely stored evidence
description: A secure evidence storage pipeline built on the Fernet symmetric-encryption library must load an entire potential-digital-evidence file into memory before it can be encrypted, limiting the practical maximum size of evidence it can securely process to what the system's available memory can hold, unlike streaming-capable encryption approaches.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-2043
source_refs:
  - DFCite-2044
updated_at: 2026-08-14
status: partial
---

# Fernet-based whole-file-in-memory encryption limits the practical size of securely stored evidence

## Summary

The source paper's own performance discussion notes that while the system was demonstrated with a 10GB PDE (completing in 2m24s), "it can cater for file sizes as large as the system's memory, due to the limitations of the Fernet encryption python library," and explicitly states that "this limitation can easily be addressed by file-streaming the information instead" - acknowledging the current design does not stream. Because the design targets small-to-moderate DFR artifacts (not full disk images) this ceiling may be adequate for its intended use case, but it is a real, hard constraint on the evidence sizes the system as built can handle.

## Why It Matters

An organization or investigator who tries to route larger potential digital evidence (e.g. a full memory dump, a large log archive, or a disk image) through this style of secure storage pipeline risks the ingestion or encryption step failing or exhausting available memory, potentially losing evidence or causing a denial-of-service on the storage system, if the deployment's available RAM is not verified against the largest PDE the organization expects to need to store.

## Related Mitigations

- [[mitigations/Switch to streaming encryption or enforce a size ceiling before storing large potential digital evidence]]

## Used By

- [[techniques/Secure potential digital evidence using a proactive encrypted storage pipeline]]

## References

- [DFCite-2044] Singh et al., 2022 — Section V's performance-evaluation discussion explicitly identifies the Fernet-library memory limitation and proposes file-streaming as the fix, noting it falls outside the current study's scope.
