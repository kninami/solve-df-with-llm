---
id: LWW-2121
type: weakness
name: Messaging-app video-source classifiers confuse apps sharing similar vendor re-encoding pipelines
description: A container-structure-and-metadata-based messaging-app classifier can misattribute a video to the wrong application when two candidate apps are built on similar underlying re-encoding infrastructure (e.g. from the same vendor), since the container/metadata/encoding-parameter fingerprint the classifier relies on can converge for apps that share the same or similar transcoding pipeline despite being distinct products.
categories:
  - ASTM_INAC_AS
mitigation_ids:
  - LWM-2122
source_refs:
  - LWCite-2144
updated_at: 2026-08-16
status: complete
---

# Messaging-app video-source classifiers confuse apps sharing similar vendor re-encoding pipelines

## Summary

The confusion matrix for the best-performing (Extra Trees) classifier, evaluated across 16 IMAs, showed data from the QQ application misclassified as WeChat in 2% of cases -- the only meaningful confusion observed among otherwise near-perfectly-separated classes -- consistent with both applications being products of the same vendor (Tencent) and plausibly sharing similar underlying video re-encoding infrastructure that produces converging container/metadata/encoding-parameter fingerprints.

## Why It Matters

An investigator relying on this classifier's output to attribute a video's transmission history to a specific messaging app risks a wrong conclusion in the small but non-zero proportion of cases involving apps from the same vendor family, and this risk is not necessarily limited to the one confusable pair observed in this study -- other same-vendor or shared-infrastructure app pairs not included in the original 16-app evaluation could plausibly exhibit a similar, currently unmeasured confusion rate. Because the classifier's overall reported accuracy (99.92-99.96%) is dominated by the many easily-distinguished app pairs, this aggregate figure could understate the specific, elevated misattribution risk for same-vendor app pairs specifically.

## Related Mitigations

- [[mitigations/Corroborate a messaging-app video-source classification with independent evidence for known same-vendor confusable app pairs]]

## Used By

- [[techniques/Identify the messaging app that transmitted a video using container structure and metadata machine learning]]

## References

- [LWCite-2144] Yang, Kim, and Park, 2024, "Video source identification using machine learning: A case study of 16 instant messaging applications", FSI: Digital Investigation 50, 301812.
