---
id: DFW-2099
type: weakness
name: PDF creator-tool classification accuracy is markedly lower for version-level identification than tool-level identification
description: Byte-frequency-and-entropy machine-learning classification of a PDF's creator tool achieves high accuracy (90%+ for the best-performing models) when distinguishing between different tools, but accuracy drops substantially (to roughly 60-85% depending on model) when the same approach is applied to the finer-grained question of distinguishing between different versions of the same tool, in part because far fewer labeled training samples were available per individual tool version than per tool overall.
categories:
  - ASTM_MISINT
mitigation_ids:
  - DFM-2100
source_refs:
  - DFCite-2116
updated_at: 2026-08-16
status: complete
---

# PDF creator-tool classification accuracy is markedly lower for version-level identification than tool-level identification

## Summary

Extending the byte-frequency-and-entropy classification methodology from tool-type identification (90%+ accuracy for the best models) to version-level identification within a single tool (e.g. distinguishing Acrobat PDFMaker 6.1 from 5.0, 7.0, or 6.0) produced markedly lower accuracy across every model tested, generally in the 60-85% range depending on the specific model and tool. The authors attribute this gap partly to a much smaller available sample size for the version-level experiment (2,000 files per version, versus up to 5,000 per tool in the tool-level experiment), limiting the models' ability to learn the finer byte-level distinctions between closely related tool versions.

## Why It Matters

An investigator relying on this classification approach to attribute a document to a *specific version* of a tool -- for instance, to establish whether a document could have been created before or after a particular vulnerability was patched, or before or after a specific feature was introduced -- has meaningfully less confidence in a version-level conclusion than in a tool-level one, and should not treat the two classification tasks as offering comparable reliability. Because the accuracy gap is partly attributed to limited training data rather than a fundamental limit on what byte-level features can distinguish, the achievable accuracy for version-level identification may improve as larger labeled datasets become available, meaning a current accuracy figure should not be treated as a permanent ceiling either.

## Related Mitigations

- [[mitigations/Treat PDF tool-version classification confidence separately from tool-type classification confidence and expand training data where feasible]]

## Used By

- [[techniques/Identify the creator tool of a PDF document using byte-frequency and entropy machine-learning classification]]

## References

- [DFCite-2116] Zia and Adedayo, 2025, "Tool type identification for forensic digital document examination", FSI: Digital Investigation 54, 301972.
