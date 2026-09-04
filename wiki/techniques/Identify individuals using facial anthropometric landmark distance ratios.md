---
id: LWT-2001
type: technique
name: Identify individuals using facial anthropometric landmark distance ratios
description: The process of comparing two facial images by extracting anthropometric landmark points and computing Euclidean/geodesic distance ratios between them, then classifying the pair as the same or different identity using a trained machine-learning model.
objective_ids:
  - DFO-1008
weakness_ids:
  - LWW-2001
aliases:
  - 2D-3D facial image analysis using MediaPipe landmarks and hyper-parameter-optimized classifiers
  - Digital facial anthropometry
source_refs:
  - LWCite-2001
updated_at: 2026-08-14
status: partial
---

# Identify individuals using facial anthropometric landmark distance ratios

## Summary

An investigator locates a fixed set of anthropometric landmark points on a facial image (e.g. glabella, exocanthion, alare, gnathion), computes Euclidean and/or geodesic distances between selected pairs, and reduces these to distance ratios that are largely pose- and scale-invariant. The ratio vector is then fed into a trained classifier that outputs a same/different identity decision, supporting comparisons such as distinguishing a suspect from a look-alike or identical twin.

## Details

LWCite-2001 implements this using Google's open-source MediaPipe framework to auto-detect 468 3D facial landmarks per 2D image (an upgrade over the classical 17-21-point anthropometric landmark sets, or 68-point dlib/5-point MTCNN detectors, used by earlier forensic facial-comparison work). From the 468 points, 32 named anthropometric distances (e.g. forehead width Ft-Ft, outer canthal width Ex-Ex, nose height N-Sn, mouth breadth Chi-Chi, bigonial breadth Go-Go) are measured both as straight-line Euclidean distances and as curve-following geodesic distances, and expressed as ratios (e.g. intercanthal width to bizygomatic breadth) to normalize for image scale and head pose. These ratio vectors become the feature set for a battery of classifiers (XGBoost, AdaBoost, Random Forest, Naive Bayes, Decision Tree, Logistic Regression, LightGBM, Extra Trees, SVM, Nearest Centroid), each hyperparameter-tuned via grid/random search, to produce a binary "same face" / "different face" decision usable as statistical, courtroom-presentable evidence. This is a narrower, more automatable evolution of the manual digital-anthropometry approach traditionally used by forensic examiners for identical-twin and look-alike discrimination.

## Examples

- LWCite-2001's pipeline: MediaPipe 468-landmark detection -> 32 Euclidean/geodesic anthropometric distances and their ratios -> XGBoost classifier (best result: 78% accuracy, AUC 0.74) on a 600-image self-collected dataset of same-person, different-person, and look-alike/twin pairs.

## Related Objectives

- `DFO-1008` Establish identities

## Related Weaknesses

- [[weaknesses/Facial identification classifiers misattribute identity between look-alikes and identical twins]]

## References

- [LWCite-2001] Sanil et al., "2D-3D facial image analysis for identification of facial features using machine learning algorithms with hyper-parameter optimization for forensics applications", IEEE Access, 2023 — source of the MediaPipe-landmark distance-ratio pipeline and classifier comparison described above.
