---
id: LWW-1176
type: weakness
name: Failure to systematically enumerate spoliation-trace sources causes deleted-file evidence to be overlooked
description: Without a compiled, systematically-derived list of all OS and application artifacts capable of retaining a deleted file's metadata, investigators checking only the small set of well-known, previously-published sources can miss traces that would have established the file's prior existence, undermining a spoliation claim.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - LWM-1176
source_refs:
  - LWCite-1176
updated_at: 2026-08-12
status: complete
---

# Failure to systematically enumerate spoliation-trace sources causes deleted-file evidence to be overlooked

## Summary

Digital forensic investigations into evidence spoliation have historically relied on investigators' individual experience and knowledge rather than a systematic, comprehensive inventory of artifact sources, and no common professional standard sets what qualifications or checklist an examiner must follow for this task.

## Why It Matters

A single trace of a deleted file's prior existence can be case-determinative in a spoliation claim, so an examiner who checks only well-known sources (e.g. a single Spotlight database) can miss additional independent corroborating traces — such as macOS's Spotlight `parsecd`/`JournalAttr` temp files or an Office application's `ComRPCDB`/`MicrosoftRegistrationDB` databases, which were undocumented prior to systematic study — leading to a weaker or unsupported spoliation claim, or to inconsistent findings between examiners of differing experience levels on the same evidence.

## Related Mitigations

- [[mitigations/Search all OS and application artifacts systematically for spoliation traces using a keyword-driven methodology]]

## Used By

- [[techniques/Reconstruct deleted-file provenance using cross-artifact metadata-remnant correlation]]

## References

- [LWCite-1176] Joun et al., 2023, "Discovering spoliation of evidence through identifying traces on deleted files in macOS", FSI: Digital Investigation 44, 301502.
