---
id: DFT-1089
type: technique
name: Classify crime scene images for casework triage using Tree-CNN and BoVW-SVM
description: Automatically classify large volumes of crime scene casework images (e.g. drug-offence photographs) into predefined content categories using either a Support Vector Machine classifier over Bag-of-Visual-Words dictionaries built from local image feature descriptors, or a hierarchical deep convolutional neural network (Tree-CNN) that classifies images through a tree of increasingly specific category nodes, to reduce the manual labelling and cataloguing burden on forensic practitioners.
objective_ids:
  - DFO-1012
weakness_ids:
  - DFW-1095
aliases:
  - Hierarchical Tree-CNN and BoVW-SVM crime scene image classification for casework triage
source_refs:
  - DFCite-1087
updated_at: 2026-08-10
status: complete
---

# Classify crime scene images for casework triage using Tree-CNN and BoVW-SVM

## Summary

Forensic laboratories increasingly struggle to manually label and catalogue growing crime scene image databases. Training classifiers directly on real casework images (rather than relying on generic pre-trained models) — either a traditional BoVW-SVM pipeline or a hierarchical Tree-CNN — offers a semi-automated triage capability, letting practitioners review and confirm rather than manually sort every image from scratch.

## Details

Both proof-of-concept models were trained and evaluated on a subset of 60,520 images from a 97,287-image real-world casework database of drug-related offences sourced from the Australian Federal Police illicit drug database, labelled into well-defined categories by AFP personnel. The Tree-CNN model, which classifies images through a hierarchy of parent and child nodes at progressively finer category granularity, was found to outperform the more traditional BoVW-SVM approach and to offer more flexibility for future refinement of category definitions, including for currently unstructured image classes.

## Examples

- The Tree-CNN model's content-based image retrieval component achieved a recall of 70% and a precision of 86% for identifying and matching similar scenes, demonstrating usable performance for surfacing visually related casework images.

## Related Objectives

- `DFO-1012` Locate potentially relevant content

## Related Weaknesses

- [[weaknesses/Hierarchical Tree-CNN crime scene classification confuses visually similar but differently labelled categories]]

## References

- [DFCite-1087] Abraham et al., 2021, "Automatically classifying crime scene images using machine learning methodologies", FSI: Digital Investigation 39.
