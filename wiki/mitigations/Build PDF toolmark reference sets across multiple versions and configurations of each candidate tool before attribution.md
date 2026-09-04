---
id: LWM-1292
type: mitigation
name: Build PDF toolmark reference sets across multiple versions and configurations of each candidate tool before attribution
source_refs:
  - LWCite-1322
updated_at: 2026-08-15
status: complete
---

# Build PDF toolmark reference sets across multiple versions and configurations of each candidate tool before attribution

## Summary

When attributing a questioned PDF document to a candidate creating tool via structural toolmarks, build the reference toolmark set from documents generated across multiple versions and plausible configuration options of that tool, rather than a single default installation, and report attribution as narrowing the set of plausible tools rather than as a unique match.

## Addresses

- [[weaknesses/PDF toolmark-based tool attribution can misclassify documents from the same tool under different configurations]]

## How To Apply

Before applying [[techniques/Attribute a PDF document to its creating tool using consistent structural toolmarks]] to attribute a questioned document, generate reference documents from the candidate tool across its known versions and any configuration options relevant to the case (installed plugins, output settings, target PDF version) rather than relying on a single reference sample. Where the specific version/configuration of the suspect's tool at the time the questioned document was created cannot be established, disclose this uncertainty and frame the toolmark match as excluding implausible tools and narrowing the candidate set, not as a unique, conclusive identification of the creating tool.

## References

- [LWCite-1322] Olivier, 2026, "On the classification of questioned PDF documents — Attributing PDF documents to the tools that created them", FSI: Digital Investigation 57, 302104.
