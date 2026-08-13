---
id: DFW-1184
type: weakness
name: HDBSCAN audio clustering excludes unassignable recordings from speaker identification analysis, reducing coverage
description: The HDBSCAN clustering step used to group same-speaker recordings leaves some recordings unassigned to any cluster, and those unclustered recordings are excluded from the cluster-scoring pipeline entirely, so any true match they contain is missed.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1184
source_refs:
  - DFCite-1187
updated_at: 2026-08-12
status: complete
---

# HDBSCAN audio clustering excludes unassignable recordings from speaker identification analysis, reducing coverage

## Summary

The authors name this as "the main limitation" of their approach: "its limited scope in the number of analyzed utterances. In the clustering process, certain utterances could not be assigned to any cluster, posing a challenge with low coverage." Because the cluster-scoring pipeline only scores recordings that HDBSCAN successfully groups into a cluster, any recording HDBSCAN leaves unclustered — for reasons such as poor audio quality, insufficient similarity to other recordings from the same speaker, or genuine outlier status — is silently dropped from consideration rather than being flagged for separate review.

## Why It Matters

An investigator relying on this technique's candidate output should not assume that every recording in the target database has been checked against the enrollment database; recordings HDBSCAN cannot cluster receive no score against any enrolled individual at all, meaning a true match contained in an unclustered recording will not appear on the candidate list regardless of how distinctive that recording's voice pattern is.

## Related Mitigations

- [[mitigations/Score unclustered recordings individually as singleton clusters instead of excluding them from speaker identification analysis]]

## Used By

- [[techniques/Narrow speaker identification candidates using clustered rank-adjusted similarity scoring]]

## References

- [DFCite-1187] Moura et al., 2024, "Enhancing speaker identification in criminal investigations through clusterization and rank-based scoring", FSI: Digital Investigation 49. States the main limitation as unclustered utterances being excluded from analysis, "posing a challenge with low coverage."
