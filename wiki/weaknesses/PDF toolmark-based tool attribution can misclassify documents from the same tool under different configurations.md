---
id: DFW-1291
type: weakness
name: PDF toolmark-based tool attribution can misclassify documents from the same tool under different configurations
description: Because a PDF-creation tool's structural toolmarks can depend on how the tool is configured (options, settings, or version) rather than being fixed purely by the tool's identity, documents genuinely created by the same tool under different configurations can present differing toolmarks, and documents from different tools that happen to share default configuration choices can present matching ones, undermining a one-to-one mapping between toolmark and tool.
categories:
  - ASTM_INAC_AS
mitigation_ids:
  - DFM-1292
source_refs:
  - DFCite-1322
updated_at: 2026-08-15
status: complete
---

# PDF toolmark-based tool attribution can misclassify documents from the same tool under different configurations

## Summary

The underlying research explicitly identifies "toolmarks may depend on tool configuration" as one of its core findings. A toolmark reflects a specific tool *as configured*, not the tool's identity alone, so two documents produced by literally the same software installation but with different user-selected options, plugin sets, or version updates can present structurally different toolmark feature vectors.

## Why It Matters

An investigator using toolmark-based classification to attribute a questioned document to a suspect's known tool risks a false exclusion if the suspect's tool was configured differently when creating the questioned document than when the reference samples were generated, or a false inclusion if an innocent party's differently-configured tool happens to produce a matching toolmark vector by coincidence. Toolmark-based attribution should therefore narrow the set of plausible creating tools rather than being treated as a unique, conclusive identification, consistent with how the source research frames its own goal (excluding implausible tools rather than proving a single positive match).

## Related Mitigations

- [[mitigations/Build PDF toolmark reference sets across multiple versions and configurations of each candidate tool before attribution]]

## Used By

- [[techniques/Attribute a PDF document to its creating tool using consistent structural toolmarks]]

## References

- [DFCite-1322] Olivier, 2026, "On the classification of questioned PDF documents — Attributing PDF documents to the tools that created them", FSI: Digital Investigation 57, 302104.
