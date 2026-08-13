---
id: DFM-1184
type: mitigation
name: Score unclustered recordings individually as singleton clusters instead of excluding them from speaker identification analysis
source_refs:
  - DFCite-1187
updated_at: 2026-08-12
status: complete
---

# Score unclustered recordings individually as singleton clusters instead of excluding them from speaker identification analysis

## Summary

Rather than silently dropping recordings that HDBSCAN could not assign to any cluster, treat each unclustered recording as its own single-utterance cluster and run it through the same scoring pipeline, accepting a larger candidate list for those specific recordings in exchange for not losing coverage entirely.

## Addresses

- [[weaknesses/HDBSCAN audio clustering excludes unassignable recordings from speaker identification analysis, reducing coverage]]

## How To Apply

After clustering, identify the set of recordings HDBSCAN left unassigned and pass each one through the cluster-scoring pipeline individually rather than discarding it; expect this subset to generate a higher number of raw candidate matches per recording than clustered recordings do (since clustering's variance-reduction benefit does not apply to a single utterance), and prioritize investigator review time accordingly rather than treating the two subsets identically.

## References

- [DFCite-1187] Moura et al., 2024, "Enhancing speaker identification in criminal investigations through clusterization and rank-based scoring", FSI: Digital Investigation 49. Considers interpreting unclustered audio recordings as a single utterance cluster as an alternative to excluding them, while noting the resulting increase in candidate volume.
