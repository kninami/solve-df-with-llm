---
id: DFW-1200
type: weakness
name: Failure to rely on magic-number signatures causes file type identification tools to be defeated by extension tampering
description: Some file type identification tools, including established forensic tools, partly or wholly infer a file's type from its extension rather than purely from content-based magic-number signatures, so their accuracy collapses when a suspect renames or removes a file's extension, even though the tool is marketed as a content-based identification solution.
categories:
  - ASTM_MISINT
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1200
source_refs:
  - DFCite-1211
updated_at: 2026-08-13
status: complete
---

# Failure to rely on magic-number signatures causes file type identification tools to be defeated by extension tampering

## Summary

Removing or renaming file extensions across two benchmark datasets left most magic-number-based tools' accuracy essentially unchanged, but caused severe drops for tools with extension-dependent logic: `guess-file-type` fell from 94.8% to 34.1% (a 60.7-percentage-point collapse) on the smaller dataset, and the commercial forensic tool EnCase also showed a smaller but still notable accuracy decrease once extensions were removed — a result the study's authors flagged as surprising precisely because EnCase is a trusted forensic tool.

## Why It Matters

An investigator who selects a file type identification tool based on its stated purpose ("content-based file type identification") rather than verifying its actual internal mechanism may unknowingly be relying on extension inference for at least part of its output, producing systematically wrong type determinations exactly in the scenario — deliberate extension tampering — where correct identification matters most for detecting concealment or exfiltration attempts. This risk is not limited to obviously weak tools; the study found it present even in an established commercial forensic tool, so tool reputation alone is not a reliable proxy for magic-number-only behavior.

## Related Mitigations

- [[mitigations/Combine multiple magic-number-based file type identification tools to raise identification accuracy]]

## Used By

- [[techniques/Identify a file's type using magic-number signature matching]]

## References

- [DFCite-1211] Dubettier et al., 2023, "File type identification tools for digital investigations", FSI: Digital Investigation 46, 301574.
