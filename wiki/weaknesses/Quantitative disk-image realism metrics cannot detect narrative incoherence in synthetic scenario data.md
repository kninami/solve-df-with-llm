---
id: LWW-1041
type: weakness
name: Quantitative disk-image realism metrics cannot detect narrative incoherence in synthetic scenario data
description: A synthetic disk image can score as realistic across every implemented quantitative metric (configuration, longevity, activity, volume) while still containing scenario elements that are internally inconsistent or implausible in a way a human reviewer familiar with the case narrative would immediately recognize, because quantitative metrics do not capture the narrative coherence or investigative-hypothesis plausibility of the underlying story the data is meant to represent.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - LWM-1041
source_refs:
  - LWCite-1031
updated_at: 2026-08-09
status: complete
---

# Quantitative disk-image realism metrics cannot detect narrative incoherence in synthetic scenario data

## Summary

The authors explicitly acknowledge this limitation: "there are challenges to precisely grasping and expressing the notion of relevant evidence... other properties do not inherently lend themselves to quantitative metrics... the complexity of relevant evidence, or the difficulty of interpretation." Someone could artificially improve certain quantitative metrics (e.g., depositing large numbers of random files to raise a Volume metric, or launching arbitrary programs to raise an Activity metric) without making the underlying scenario more coherent or realistic in a narrative sense.

## Why It Matters

A dataset or tool-testing exercise that relies solely on quantitative realism metrics could pass validation while still containing scenarios that would strike a domain expert as implausible or internally contradictory, undermining the dataset's usefulness for training or research purposes that depend on narrative plausibility (e.g., forensic education curricula, or testing an examiner's ability to reconstruct a coherent timeline). Because quantitative metrics are more easily automated and therefore more likely to be relied upon in practice, this gap between "passes the metrics" and "is actually realistic" risks going unnoticed without deliberate qualitative review.

## Related Mitigations

- [[mitigations/Combine quantitative realism metrics with qualitative narrative-coherence review]]

## Used By

- [[techniques/Validate synthetic disk image realism using quantitative metrics]]

## References

- [LWCite-1031] Voigt et al., 2025, "A metrics-based look at disk images: Insights and applications", FSI: Digital Investigation 52.
