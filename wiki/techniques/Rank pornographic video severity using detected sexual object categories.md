---
id: DFT-1150
type: technique
name: Rank pornographic video severity using detected sexual object categories
description: After a video is classified and localized as pornographic, run a sexual-object detector (e.g., YOLO) over the flagged segments, map the specific object categories found to a severity scale, and rank segments/videos by combined severity and confidence score, supporting law-enforcement prioritization of pornographic-material caseloads.
objective_ids:
  - DFO-1005
weakness_ids:
  - DFW-1153
aliases:
  - Sexual object detection severity ranking
  - Harmfulness estimation for pornographic video content
source_refs:
  - DFCite-1156
updated_at: 2026-08-12
status: complete
---

# Rank pornographic video severity using detected sexual object categories

## Summary

Rather than treating all detected pornographic content identically, this technique estimates a "harmfulness"/severity level per video segment from the specific sexual objects a detector finds within it, then ranks segments and whole videos by that severity for law-enforcement triage. It addresses a common LEA requirement — being able to prioritize which pornographic material to review first — that binary pornographic/benign classification alone does not support.

## Details

A YOLO-based sexual-object detector is applied to frames within segments already flagged as pornographic by a video-level classifier, producing fine-grained object categories at a finer granularity than prior semantic-component approaches (which used a coarser set of categories on still images only). Each detected object category is mapped to one of four severity levels (1, low severity, through 4, more severe), following the general spirit of scales used elsewhere in adjacent domains (e.g., the COPINE scale for ranking CSAM) but purpose-built for adult pornographic content, where no equivalent standardized severity taxonomy previously existed beyond a coarse "softcore"/"hardcore" split. A segment's final rank combines its assigned severity class with its video-segment classification score, giving investigators an ordered worklist rather than an unordered list of flagged videos.

## Examples

- Applied on top of the APD-VIDEO pornography classifier: sexual objects detected within already-localized pornographic segments were mapped to the four-level severity scale and used to rank segments and videos, providing an automatically-generated prioritization order for review.

## Related Objectives

- `DFO-1005` Prioritize digital evidence sources

## Related Weaknesses

- [[weaknesses/Pornographic content severity ranking relies on a non-standardized, unvalidated severity scale]]

## References

- [DFCite-1156] Borg et al., 2022, "Detecting and ranking pornographic content in videos", FSI: Digital Investigation 42-43.
