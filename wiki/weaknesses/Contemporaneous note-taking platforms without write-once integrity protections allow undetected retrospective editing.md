---
id: DFW-1131
type: weakness
name: Contemporaneous note-taking platforms without write-once integrity protections allow undetected retrospective editing
description: Note-taking platforms that permit committed entries to be edited or removed after the fact allow a practitioner's examination record to be altered without a visible trace, undermining the audit-trail purpose contemporaneous notes are meant to serve.
categories:
  - ASTM_INAC_ALT
mitigation_ids:
  - DFM-1131
source_refs:
  - DFCite-1128
updated_at: 2026-08-12
status: complete
---

# Contemporaneous note-taking platforms without write-once integrity protections allow undetected retrospective editing

## Summary

An accreditation-body review of digital forensic laboratories raised concerns after discovering contemporaneous-note practices that "do not protect the notes 'in a manner which prevents alteration'." Where a note-taking system (digital or written) allows entries to be edited or removed after they are committed, there is no way to distinguish a genuinely contemporaneous, unaltered record from one that has been retrospectively changed.

## Why It Matters

The evidential value of contemporaneous notes rests on their being an accurate, chronological account created at or near the time of the events they describe; if entries can be silently altered later, that value is undermined regardless of how well-structured the notes otherwise are. This also removes the ability to identify, during a future review, exactly where and when an error in the examination process occurred, since the record of that error could itself have been edited away.

## Related Mitigations

- [[mitigations/Use a write-once, timestamped, per-entry-integrity-checked platform for contemporaneous examination notes]]

## Used By

- [[techniques/Maintain contemporaneous examination notes using a structured noting skeleton]]

## References

- [DFCite-1128] Horsman, 2021, "Contemporaneous notes for digital forensic examinations", FSI: Digital Investigation 37, 301173.
