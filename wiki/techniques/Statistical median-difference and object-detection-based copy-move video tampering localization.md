---
id: DFT-1045
type: technique
name: Statistical median-difference and object-detection-based copy-move video tampering localization
description: Passively detect and localize copy-move object tampering in a video (an object copied from one frame or region and pasted into another) by first computing the normalized pixel-level median difference between consecutive frames to flag which frame ranges show forgery-indicative statistical peaks, then applying a fine-tuned real-time object detector (YOLO V8) to draw a bounding box around the specific tampered object in those frames.
objective_ids:
  - DFO-1019
weakness_ids:
  - DFW-1046
aliases: []
source_refs:
  - DFCite-1036
updated_at: 2026-08-09
status: complete
---

# Statistical median-difference and object-detection-based copy-move video tampering localization

## Summary

Because a video with a static background but an inserted or duplicated moving object breaks the normal temporal redundancy between consecutive frames, a purely statistical, model-free first stage (no training required) can flag suspicious frame ranges without any prior knowledge of what was tampered. A second, learned stage then localizes exactly which object in those flagged frames was copy-moved, giving both a "when" and a "where" answer rather than only a binary forged/pristine classification.

## Details

Each video is decomposed into an ordered frame sequence, and per-pixel absolute differences between consecutive frames are computed and reduced to a single normalized median-difference value per frame; plotting this value against frame number reveals a clear peak or discontinuity at the copy-moved region's frame range, distinct from the comparatively flat baseline of an untampered sequence. A YOLO V8 object detector (an anchor-free, single-stage architecture) is then fine-tuned on labeled forged-object classes to localize and classify the specific object within the flagged range, producing a bounding box and confidence score for the final output.

## Examples

- On the REWIND academic copy-move video forgery dataset (20 sequences, 7 forged object classes, evaluated at multiple compression quality factors), the fine-tuned YOLO V8 achieved mean average precision (mAP50) of 0.99, recall 0.99, and precision 0.99, and the approach separately attained 99.90% accuracy on the larger SYSU-OBJFORG dataset (200 videos, 100 forged scenarios).

## Related Objectives

- `DFO-1019` Detect anti-forensics and other anomalies

## Related Weaknesses

- [[weaknesses/Object-detection-based copy-move localization cannot recognize objects outside its trained class taxonomy]]

## References

- [DFCite-1036] Sandhya and Kashyap, 2024, "A novel method for real-time object-based copy-move tampering localization in videos using fine-tuned YOLO V8", FSI: Digital Investigation 48.
