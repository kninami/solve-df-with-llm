---
id: LWW-2050
type: weakness
name: Media signature encoding cannot reliably distinguish between specific AI-based manipulation tools within the same family
description: While media signature encoding reliably clusters media processed by an unknown AI-based inpainting tool together as belonging to the broad "AI-based manipulation" family, it cannot reliably separate which specific AI-based tool within that family (e.g. OPN vs. STTN vs. GM-CNN) produced a given piece of media, even when all three tools are known to the system.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - LWM-2050
source_refs:
  - LWCite-2051
updated_at: 2026-08-14
status: partial
---

# Media signature encoding cannot reliably distinguish between specific AI-based manipulation tools within the same family

## Summary

The source paper's own "Unknown AI-Based Family" experiment (removing OPN, STTN, and GMCNN entirely from training) found that "the average intra-variability of the AI-based family is lower than any other inter-variability in the matrix," confirming the framework correctly identifies AI-based manipulation as a distinct family even when unknown - but the same section states plainly: "the separability among the three instances looks harder... we cannot expect to identify the specific AI-based toolchain, but we are able to find a high compatibility with toolchains of a similar pipeline." The paper's own fully-informed (all classes known) confusion matrix (Figure 7b) independently confirms this: GMCNN, OPN, and STTN show substantial cross-confusion with each other (e.g. GMCNN predicted as OPN in 0.65 of cases) even when the classifier has been trained on all three.

## Why It Matters

An investigator using this framework to determine which specific AI inpainting tool was used to manipulate a piece of media (for example, to link multiple pieces of evidence to the same manipulation software, or to attribute a technique to a specific actor's toolset) should not expect fine-grained tool-level attribution within the AI-based manipulation family; the framework's genuine strength is coarser-grained family-level discrimination (AI-based vs. user-based manipulation) and clustering media that share a similar processing pipeline, not pinpointing the exact tool used.

## Related Mitigations

- [[mitigations/Treat media-signature AI-tool clustering as family-level evidence and use dedicated detectors for specific-tool attribution]]

## Used By

- [[techniques/Cluster media by processing history using open-world media signature encoding]]

## References

- [LWCite-2051] Baracchi et al., 2024 — Section VI.E "Unknown AI-Based Family" and Figure 7b's fully-informed confusion matrix both document poor separability among specific AI-based inpainting tools despite correct family-level clustering.
