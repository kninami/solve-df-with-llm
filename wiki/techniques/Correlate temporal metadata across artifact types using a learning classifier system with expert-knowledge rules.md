---
id: DFT-2081
type: technique
name: Correlate temporal metadata across artifact types using a learning classifier system with expert-knowledge rules
description: Automatically discover and rank which combinations of timestamp-bearing digital artifacts (e.g. file-system MAC times, application log entries, registry key timestamps) tend to co-occur meaningfully around an event of interest, by training a Michigan-style learning classifier system seeded with YARA-inspired expert-knowledge rules on labeled temporal-metadata examples, rather than relying solely on a human analyst's manual timeline correlation.
objective_ids:
  - DFO-1001
weakness_ids:
  - DFW-2083
aliases:
  - Digital Trace Inspector
  - DTI
  - ExSTraCS-based temporal metadata correlation
source_refs:
  - DFCite-2097
updated_at: 2026-08-16
status: complete
---

# Correlate temporal metadata across artifact types using a learning classifier system with expert-knowledge rules

## Summary

Manually correlating timestamps across many different artifact types to reconstruct an event timeline is labor-intensive and scales poorly as the number of candidate artifact sources grows. A learning classifier system (a rule-based evolutionary machine-learning approach, here using the ExSTraCS implementation) trained on labeled examples of which artifact-timestamp combinations are and are not meaningfully related to a target event learns a population of interpretable IF-THEN rules that generalize to new cases, and can be bootstrapped with expert-knowledge rules expressed in a YARA-inspired syntax to encode an analyst's existing domain expectations from the start rather than learning entirely from scratch.

## Details

The Digital Trace Inspector (DTI) tool implements this approach: temporal metadata (timestamps and their source artifact type/field) extracted from a forensic image or artifact set is encoded as feature vectors, and an ExSTraCS learning classifier system is trained on labeled training data indicating which combinations were relevant to a known ground-truth scenario. Domain-expert knowledge can be injected up front as seed rules written in a YARA-inspired syntax (condition-action rule structure familiar to forensic analysts from malware/artifact signature writing), giving the classifier system a head start rather than requiring it to rediscover well-known temporal relationships (e.g. that a file's creation time should not postdate its last-modified time) purely from training examples. Once trained, the resulting rule population can be applied to new, unlabeled temporal metadata to automatically flag artifact combinations likely to be meaningfully correlated with an event of interest, surfacing candidate timeline-relevant relationships for an analyst to review rather than requiring the analyst to manually enumerate every pairwise combination.

## Examples

- The learning classifier system approach was evaluated against a constructed dataset of labeled temporal-metadata examples spanning multiple artifact types, comparing rule populations trained with and without YARA-inspired expert-knowledge seeding.

## Related Objectives

- `DFO-1001` Reconstruct events

## Related Weaknesses

- [[weaknesses/A temporal-metadata learning classifier system's rule quality depends on labeled training data that is costly to construct for new artifact types]]

## References

- [DFCite-2097] "Temporal metadata analysis: A learning classifier system approach", FSI: Digital Investigation 48, 2024.
