---
id: DFW-1046
type: weakness
name: Object-detection-based copy-move localization cannot recognize objects outside its trained class taxonomy
description: The object-detection stage of a copy-move video tampering localization system can only draw a bounding box around and classify objects belonging to the fixed set of classes it was trained on; a copy-moved object of a type not present in that training taxonomy will not be recognized or localized, even if the statistical first-stage analysis correctly flags the frame range as suspicious.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1046
source_refs:
  - DFCite-1036
updated_at: 2026-08-09
status: complete
---

# Object-detection-based copy-move localization cannot recognize objects outside its trained class taxonomy

## Summary

The evaluated system's object detector was trained and validated only on seven specific forged-object classes present in its training dataset (ball, cat, car, girl, elephant, duck, TV scene). Because the detection and localization stage relies on supervised object recognition, its accuracy claims (mAP50 of 0.99 and similar) are specific to those trained classes and do not automatically extend to arbitrary objects encountered in real-world evidentiary video.

## Why It Matters

An investigator applying this class of technique to a real case involving a copy-moved object outside the trained taxonomy (for example, a weapon, a specific vehicle model, or a document) would find the statistical median-difference stage still flags the suspicious frame range, but the object-localization stage fails to draw a bounding box around the actual tampered object, or may mislabel it, understating the tool's true forensic coverage for that case. This limitation is not obvious from headline accuracy figures reported against a benchmark dataset covering only the trained classes.

## Related Mitigations

- [[mitigations/Retrain the object-detection model on case-relevant classes or fall back to statistical-only flagging]]

## Used By

- [[techniques/Statistical median-difference and object-detection-based copy-move video tampering localization]]

## References

- [DFCite-1036] Sandhya and Kashyap, 2024, "A novel method for real-time object-based copy-move tampering localization in videos using fine-tuned YOLO V8", FSI: Digital Investigation 48.
