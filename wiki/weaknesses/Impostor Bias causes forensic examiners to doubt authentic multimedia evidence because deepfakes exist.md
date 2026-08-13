---
id: DFW-1238
type: weakness
name: Impostor Bias causes forensic examiners to doubt authentic multimedia evidence because deepfakes exist
description: Awareness that AI-generated deepfake content exists and is increasingly realistic can lead a forensic examiner to distrust the authenticity of genuinely real audio, image, or video evidence on the basis of that general awareness alone, rather than on an objective assessment of the specific content, mirroring how earlier deepfake prevalence has already been shown to erode public trust in authentic media generally.
categories:
  - ASTM_MISINT
mitigation_ids:
  - DFM-1239
source_refs:
  - DFCite-1253
updated_at: 2026-08-13
status: complete
---

# Impostor Bias causes forensic examiners to doubt authentic multimedia evidence because deepfakes exist

## Summary

The authors introduce "Impostor Bias" as a proposed cognitive bias distinct from confirmation bias, anchoring bias, and hindsight bias, previously documented as affecting forensic decision-making: an a priori, systematic tendency to question the authenticity of multimedia content simply because AI-generation tools capable of producing convincing fakes are known to exist, rather than because of any specific indicator found in the content itself. The paper explicitly frames this as a hypothesized bias with no empirical validation yet — it has not been measured in a controlled study of forensic examiners — but grounds it in the same underlying dynamic already documented for public trust in media generally (the "liar's dividend," where the mere possibility of deepfakes lets genuine content be dismissed as fake).

## Why It Matters

If Impostor Bias operates as hypothesized, an examiner could reject or discount genuinely authentic evidence — for example, dismissing a real video recording as a likely deepfake without technical grounds — undermining the objectivity and evidentiary reliability that forensic multimedia examination is expected to provide. Because the bias is described as stemming from a general a priori assumption rather than from the specific evaluated content, it would be difficult for an examiner to self-detect, and its risk is expected by the authors to grow as generative AI output becomes more realistic and more prevalent in casework.

## Related Mitigations

- [[mitigations/Verify suspected-deepfake media using technical detection tools and blind procedures instead of a priori distrust]]

## Used By

This weakness is not specific to any one detection technique's internal mechanism — it is a hypothesized risk in the human judgment step that follows any technical deepfake-authenticity assessment, including [[techniques/Detect deepfakes using frequency-domain analysis]] and [[techniques/Detect deepfakes using face-background noise trace comparison]], whenever an examiner interprets or overrides a tool's output based on a priori distrust of multimedia authenticity in general.

## References

- [DFCite-1253] Casu et al., 2024, "GenAI mirage: The impostor bias and the deepfake detection challenge in the era of artificial illusions", FSI: Digital Investigation 50, 301795.
