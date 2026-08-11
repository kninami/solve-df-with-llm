---
id: DFT-1044
type: technique
name: Content-similarity-based reassembly of fragmented structured-text log files
description: Carve and reassemble a fragmented structured-text log file (e.g., a JSON-formatted container log) from unallocated disk space by first identifying candidate data blocks using the format's own structural markers, then resolving ambiguous block-combination choices using a content-similarity model that scores word, sentence, and message-level continuity across a candidate join, rather than relying on structural validity alone.
objective_ids:
  - DFO-1018
weakness_ids:
  - DFW-1045
aliases: []
source_refs:
  - DFCite-1035
updated_at: 2026-08-09
status: complete
---

# Content-similarity-based reassembly of fragmented structured-text log files

## Summary

Log recovery via traditional file-system-metadata methods fails once metadata is lost, while pure signature-based file carving of a text format like JSON produces many structurally valid but semantically wrong block combinations, since a structurally correct join does not guarantee the joined content actually continues meaningfully. This technique divides recovery into identifying data blocks using the target format's own header/content/origin/attributes/timestamp/footer structure, then reassembling fragments using both structural validity and a content-similarity model measuring word, sentence, and message-level continuity to pick the semantically correct combination among multiple structurally valid candidates.

## Details

Data blocks are first classified as structured (containing at least one complete format-conformant item) or unstructured (fragments too small or malformed to identify directly, but locatable via their spatial adjacency to structured blocks). Reassembly proceeds through phases exploiting different redundancy sources — spatial locality of blocks on disk, temporal locality of log lines' timestamps, and content similarity between the format's parsed content fields — validating each candidate join against both a structural discriminator (does the combination match the format's grammar) and a content-similarity threshold (is the combined content smooth, using a Levenshtein-distance-based content-distance metric across neighboring words, sentences, and messages) before accepting it, with conflicting valid combinations resolved by comparative voting across the similarity measures.

## Examples

- On a 27.7GB XFS-formatted test disk image containing json-file Docker container logs, the technique reassembled deleted log lines at a False Acceptance Rate of 0.06% and False Rejection Rate of 3.75% even at the smallest (512-byte) scanning granularity, recovering substantially more log lines than a metadata-dependent tool (WinHex) and a generic structure-only log carver (LL carver), which recovered zero log lines in the absence of file-system metadata.

## Related Objectives

- `DFO-1018` Read data from digital evidence storage formats

## Related Weaknesses

- [[weaknesses/Structured-log carving techniques tied to one log format do not generalize to other logging drivers]]

## References

- [DFCite-1035] Ge et al., 2021, "A novel file carving algorithm for docker container logs recorded by json-file logging driver", FSI: Digital Investigation 39.
