---
id: DFT-1177
type: technique
name: Narrow speaker identification candidates using clustered rank-adjusted similarity scoring
description: Cluster a large collection of unlabeled audio recordings by presumed common speaker using voice-embedding similarity, then score each cluster against every enrolled individual in a speaker database using a rank-adjusted cosine-similarity function, to narrow a very large pool of candidates down to a short, human-reviewable list for further corroboration.
objective_ids:
  - DFO-1008
weakness_ids:
  - DFW-1184
aliases:
  - Cluster-scoring speaker identification pipeline
source_refs:
  - DFCite-1187
updated_at: 2026-08-12
status: complete
---

# Narrow speaker identification candidates using clustered rank-adjusted similarity scoring

## Summary

Matching every audio recording independently against every individual in a large enrollment database (open-set, text-independent speaker identification) produces an overwhelming number of raw candidate matches, most of them false positives, because voice-embedding similarity alone cannot reliably distinguish a true match from an individual with merely similar vocal characteristics. This technique clusters recordings from the same presumed speaker together and scores whole clusters against the enrollment database using a rank-based adjustment, sharply reducing the number of candidate matches an investigator must manually review.

## Details

The pipeline has five stages. Feature extraction converts each audio recording into a speaker embedding using the ECAPA-TDNN speaker verification model. Scoring computes the cosine similarity between each target recording's embedding and each enrolled individual's embedding. Clusterization groups target-database recordings likely produced by the same person using HDBSCAN over the embeddings, reducing per-recording variability and noise by analyzing a set of same-speaker recordings jointly rather than one at a time. Rank-based adjustment re-weights each raw similarity score by the enrolled individual's relative rank against that same target recording (an adjustment factor controlled by a decay parameter, α), since a high score is only meaningful when that individual scores far above others in the enrollment database rather than merely above an absolute threshold. Cluster scoring then averages the adjusted scores across all recordings in a cluster to produce one final score per (cluster, enrolled individual) pair. The resulting ranked candidate list is deliberately treated as provisional: the paper is explicit that the approach "does not offer unequivocal identifications and necessitates additional supporting information," and that "the occurrence of individuals with similar vocal characteristics is not an uncommon phenomenon," so the candidate list must be consolidated with external corroborating evidence (e.g., photographs, body markings, names) before an investigator treats any candidate as confirmed.

## Examples

- On synthetic Common Voice-derived cell phone datasets, combining clusterization with rank-based score adjustment produced a statistically significant reduction in Equal Error Rate compared to a per-recording cosine-similarity baseline (p = 0.017), while clusterization alone did not show a statistically significant improvement without the rank adjustment.
- Deployed on real prison-system call data (an enrollment database of 69,453 speakers and a target database of over 400,000 utterances from 67 seized cell phones), the approach identified 30 of 86 externally validated candidates while producing roughly 300 candidate cluster-to-individual matches — versus an estimated 300,000 candidate matches and over 200 uninterrupted days of manual review time for the equivalent per-recording baseline approach.

## Related Objectives

- `DFO-1008` Establish identities

## Related Weaknesses

- [[weaknesses/HDBSCAN audio clustering excludes unassignable recordings from speaker identification analysis, reducing coverage]]

## References

- [DFCite-1187] Moura et al., 2024, "Enhancing speaker identification in criminal investigations through clusterization and rank-based scoring", FSI: Digital Investigation 49.
