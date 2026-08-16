---
id: DFM-2101
type: mitigation
name: Periodically update topic-model seed dictionaries with newly observed coded terminology and manually review low-confidence topic clusters
source_refs:
  - DFCite-2117
updated_at: 2026-08-16
status: complete
---

# Periodically update topic-model seed dictionaries with newly observed coded terminology and manually review low-confidence topic clusters

## Summary

Treat a knowledge-guided topic model's seed concept dictionaries as a living resource that must be periodically updated with newly observed coded terminology from casework and open-source intelligence, and manually spot-check low-confidence or unclassified message clusters rather than treating the model's topic assignments as an exhaustive account of relevant content.

## Addresses

- [[weaknesses/Knowledge-guided topic modeling cannot detect novel coded terminology absent from its seed concept dictionaries]]

## How To Apply

Establish a process for capturing newly identified slang or coded terminology encountered during casework (or from external intelligence sources) and feeding it back into the seed concept dictionaries used by the topic-modeling tool, so the model's guidance stays current with evolving evasive language. During review, do not rely solely on the model's topic-flagged clusters; periodically sample messages the model placed in low-confidence, unclassified, or "miscellaneous" clusters, since these are the most likely place novel coded terminology would surface without yet being recognized as a distinct, meaningful topic. Document any newly identified coded terms discovered this way for both the current case and future dictionary updates.

## References

- [DFCite-2117] "Towards a joint semantic analysis in mobile forensics environments", FSI: Digital Investigation 48, 2024.
