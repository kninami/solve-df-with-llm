---
id: DFT-2078
type: technique
name: Detect deepfakes with pixel-level interpretability using a two-branch content-disentanglement autoencoder
description: Detect a manipulated facial image or video frame while also generating a pixel-level "real-map" and "fake-map" that visually decompose the input into its genuine and forged content, giving an investigator a directly interpretable visual explanation of which specific pixels the model judged forged, rather than only a black-box real/fake classification score.
objective_ids:
  - DFO-1019
  - DFO-1020
weakness_ids:
  - DFW-1265
aliases:
  - TAENet
  - Two-branch Autoencoder Network
source_refs:
  - DFCite-2094
updated_at: 2026-08-16
status: complete
---

# Detect deepfakes with pixel-level interpretability using a two-branch content-disentanglement autoencoder

## Summary

Deep-learning deepfake detectors are typically black boxes that output a classification score without explaining why an image was judged fake or which regions drove the decision, which limits their trustworthiness and traceability as digital evidence. TAENet addresses this by explicitly decoupling an input image's real content from its forged content using a dual-encoder/dual-decoder autoencoder architecture, producing a "real-map" (the genuine content) and a "fake-map" (the forged content) that together reconstruct the original image and visually pinpoint the manipulated region.

## Details

The architecture has three components. Content Feature Disentanglement uses a dual-branch CNN encoder (one branch per content type) to extract separate real-content and fake-content latent features from the input image, with a feature discriminator trained via cross-entropy loss to force the two branches' features to actually be distinguishable from each other rather than converging to similar representations. Content Map Generation then uses a matching dual decoder to reconstruct a real-map and fake-map from those two feature sets respectively, trained with a custom Pixel-level Content Map Generation Loss that constrains a real image's fake-map toward an all-zero map (since a genuine image has no forged content to visualize) and constrains the sum of any image's real-map and fake-map to reconstruct the original input via an L2 reconstruction loss -- directly supervising the model to produce visually meaningful, complementary maps rather than an arbitrary internal representation. Classification then combines an auxiliary classifier (operating on the real-content features, to improve real-map estimation accuracy during training) with a prediction classifier (operating on the forged-content features) to produce the final real/fake decision, so the same features driving the visual explanation also drive the classification result.

## Examples

- Trained separately on each of four FaceForensics++ manipulation subsets (DeepFakes, FaceSwap, Face2Face, NeuralTextures) with a ResNet18 backbone, TAENet matched or exceeded the accuracy of an equivalent plain ResNet18 classifier on three of the four subsets (e.g. 95.99% vs. 95.00% accuracy on FaceSwap) while additionally producing interpretable real-maps and fake-maps, demonstrating that the added interpretability did not come at a meaningful accuracy cost.
- Qualitative visual analysis confirmed the generated fake-maps matched each manipulation method's actual known forged region: Face2Face's fake-map covered nearly the whole face (a full facial-reenactment technique), NeuralTextures' fake-map was concentrated on the mouth area (a technique that only manipulates mouth movement), and FaceSwap/DeepFakes' fake-maps covered most of the facial area consistent with face-swapping.
- An ablation study on the NeuralTextures subset found removing the feature discriminator caused the fake-map's forged-region boundary to become too large and imprecise, and removing the auxiliary classifier caused the real-map's estimated real-content region to visibly deviate from the true real content, confirming each architectural component's specific contribution to interpretability rather than only to raw classification accuracy.
- Cross-dataset generalization testing (train on one dataset, test on FF++/Celeb-DF/DFDC) produced an average AUC just over 75%, which the authors themselves characterize as "not enough for deepfake detection" and identify as a direction for future work.

## Related Objectives

- `DFO-1019` Detect anti-forensics and other anomalies
- `DFO-1020` Document digital forensic activities

## Related Weaknesses

- [[weaknesses/Deepfake detectors trained on one manipulation type generalize poorly to unseen manipulation types]]

## References

- [DFCite-2094] Du, Yu, Li, Chow, Jiang, Zhang, Liang, Li, and Huang, 2024, "TAENet: Two-branch Autoencoder Network for Interpretable Deepfake Detection", FSI: Digital Investigation 50, 301808.
