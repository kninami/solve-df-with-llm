---
id: DFW-1270
type: weakness
name: Metadata-based smartphone file-triage classifiers trained on one case type or platform may not generalize to a different one
description: A file-metadata triage classifier's notion of "interesting" is learned entirely from the specific case type, crime category, and mobile operating system its training data was drawn from, so applying a model trained on one combination (e.g. terrorism cases on Android) to a materially different one (a different crime type, or an iOS device) is not validated by the model's own reported performance figures.
categories:
  - ASTM_MISINT
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1271
source_refs:
  - DFCite-1298
updated_at: 2026-08-14
status: complete
---

# Metadata-based smartphone file-triage classifiers trained on one case type or platform may not generalize to a different one

## Summary

The underlying study deliberately narrowed its scope to Android devices and terrorism-related cases specifically because "the used data has to be similar to real case data" for the resulting model's applicability to hold, and file relevance labels were assigned by forensic examiners based on that specific case type's investigative context — a labeling standard that does not necessarily transfer to a different crime category (e.g. financial fraud or child exploitation, where "interesting" file types, paths, and naming patterns differ substantially) or to a different mobile operating system's file-system conventions.

## Why It Matters

An investigator who applies a metadata-triage classifier trained on one case type or platform to a case outside that training distribution risks the model's published high accuracy and F1-score figures not holding in practice, potentially either missing genuinely relevant files (a false negative that could exclude evidence from review entirely) or flagging so many irrelevant files that the triage benefit is lost — without any indication from the tool itself that it is operating outside its validated scope.

## Related Mitigations

- [[mitigations/Retrain or validate metadata-based file-triage classifiers against the specific case type and platform before relying on them operationally]]

## Used By

- [[techniques/Triage smartphone extraction files by relevance using a metadata classifier]]

## References

- [DFCite-1298] Serhal and Le-Khac, 2021, "Machine learning based approach to analyze file meta data for smart phone file triage", DFRWS 2021 USA; FSI: Digital Investigation 37, 301194.
