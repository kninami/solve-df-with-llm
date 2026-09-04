---
id: LWM-1046
type: mitigation
name: Retrain the object-detection model on case-relevant classes or fall back to statistical-only flagging
source_refs:
  - LWCite-1036
updated_at: 2026-08-09
status: complete
---

# Retrain the object-detection model on case-relevant classes or fall back to statistical-only flagging

## Summary

Before relying on the object-detection stage to localize a copy-moved object, confirm the object type is within the model's trained class taxonomy; where it is not, either fine-tune the detector on labeled examples of the case-relevant object class, or fall back to the statistical median-difference stage alone to flag suspicious frame ranges for manual review.

## Addresses

- [[weaknesses/Object-detection-based copy-move localization cannot recognize objects outside its trained class taxonomy]]

## How To Apply

Before applying this technique to case evidence, check whether the object type(s) suspected of being copy-moved fall within the detector's existing trained classes; if a labeled dataset of the relevant object type is available or can be constructed, fine-tune the detector on it following the same training procedure used for the original classes. Where retraining is not feasible in the available time, still run the statistical median-difference stage on its own, since it requires no training and will still flag the suspicious frame range, then manually inspect those frames for the tampered object rather than relying on automated bounding-box localization.

## References

- [LWCite-1036] Sandhya and Kashyap, 2024, "A novel method for real-time object-based copy-move tampering localization in videos using fine-tuned YOLO V8", FSI: Digital Investigation 48.
