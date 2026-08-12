---
id: DFT-1037
type: technique
name: Classify photo capture timeslots using defective-pixel patterns
description: Estimate which time period a digital photograph was captured in by training multi-class classifiers on the local-neighbourhood variation behaviour of candidate defective pixel locations within a specific camera's images over time, since a sensor's defective pixels accumulate and evolve gradually and independently of EXIF metadata, which can be altered.
objective_ids:
  - DFO-1001
weakness_ids:
  - DFW-1038
aliases:
  - Defective-pixel-based picture acquisition timeslot classification
source_refs:
  - DFCite-1028
updated_at: 2026-08-09
status: complete
---

# Classify photo capture timeslots using defective-pixel patterns

## Summary

Camera image sensors accumulate defective pixels (hot, dead, and partially stuck pixels) over their operational lifetime, and this accumulation is constant and independent of external conditions, unlike ordinary pixel values. A three-stage system extracts candidate defective-pixel locations using two proposed local-variation features (first- and second-order), trains a multi-class classifier per pixel location to predict which of several known timeslots an image was taken in, then combines many individually-trained pixel-location classifiers and image blocks via majority voting to reach a final, more robust timeslot prediction.

## Details

For each candidate pixel location within a fixed-size, non-overlapping image block, first-order local variation (LV1: absolute deviation of the center pixel from its window average) and second-order local variation (LV2: RMS deviation) are computed per color channel and used as classifier training features, since regions containing a genuine defective pixel exhibit distinctively higher-than-usual local variation. The K best-performing pixel-location classifiers (by validation accuracy) are retained, then retrained using "virtual sub-classes" that halve each actual timeslot into two finer-grained classes before reconstruction back to the actual timeslot, which improved accuracy by forcing the underlying classifiers to solve a more discriminating problem. Finally, predictions from multiple non-overlapping image blocks (found optimal at 45 blocks) are combined via a second majority-voting step to produce the final timeslot classification for a query image.

## Examples

- On the NTIF dataset (10 digital cameras, 41,684 images across 94 weeks), the KNN-based system with local variation features, virtual sub-classes, and 45-block fusion achieved 88-93% accuracy predicting which of five ~8-week timeslots an image was captured in, outperforming a prior state-of-the-art correlation-coefficient-based competing technique by 30-49 percentage points across all ten cameras.

## Related Objectives

- `DFO-1001` Reconstruct events

## Related Weaknesses

- [[weaknesses/Defective-pixel timeslot classification requires prior training images from the specific camera]]

## References

- [DFCite-1028] Ahmed et al., 2021, "A machine learning-based approach for picture acquisition timeslot prediction using defective pixels", FSI: Digital Investigation 39.
