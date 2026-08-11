---
id: DFT-1032
type: technique
name: Clustering-assisted LLM triage of unstructured forensic string-search output
description: Group the noisy plaintext output of a string-search/extraction pass over a raw forensic disk image into thematically coherent clusters using unsupervised k-means clustering on word embeddings, then query each cluster with a large language model to extract and describe forensically relevant information, avoiding both the loss-of-context problem of naive fixed-size chunking and the unmanageable volume of unclustered raw string output.
objective_ids:
  - DFO-1012
weakness_ids:
  - DFW-1033
aliases: []
source_refs:
  - DFCite-1023
updated_at: 2026-08-09
status: complete
---

# Clustering-assisted LLM triage of unstructured forensic string-search output

## Summary

Applying a string-extraction tool to a raw disk image (e.g., from an embedded system such as a vehicle infotainment unit) produces a large volume of noisy, unstructured plaintext with no file-system structure to organize it. K-means clustering on word embeddings of each extracted line groups thematically related strings (e.g., contact records, location names, device identifiers) together, after which a language model is prompted against each cluster's contents — rather than against arbitrary sequential chunks of the raw output — to answer specific investigator questions with the benefit of coherent local context.

## Details

Text lines are embedded (e.g., via a subword-aware embedding model robust to noisy, out-of-vocabulary tokens) and partitioned with k-means, using either an automated silhouette-score search over candidate cluster counts or a manually fixed count when compute/time is constrained. Because a language model has a fixed maximum prompt size, oversized clusters are further split ("reclustered") to fit, using the same embedding-based clustering rather than arbitrary slicing, to avoid breaking apart thematically coherent content. For each (sub-)cluster, the investigator's natural-language question (e.g., "List any phone numbers if present") and the cluster's text are combined into a single model prompt, and the process repeats across all clusters and, optionally, across several different investigator questions.

## Examples

- Applied to a Hyundai vehicle's infotainment disk image, GPT-4 processing of k-means clusters increased recall of contact names by 18% and phone numbers by 3% compared to clustering alone (without the language-model step), and additionally surfaced connected-device and geographical-location data that had been entirely missed during manual analysis.

## Related Objectives

- `DFO-1012` Locate potentially relevant content

## Related Weaknesses

- [[weaknesses/LLM-assisted forensic text triage hallucinates entities not present in the source evidence]]

## References

- [DFCite-1023] Fayyaz et al., 2024, "A hybrid artificial intelligence framework for enhancing digital forensic investigations of infotainment systems", FSI: Digital Investigation 49.
