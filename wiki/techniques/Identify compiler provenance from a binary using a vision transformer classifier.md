---
id: LWT-1124
type: technique
name: Identify compiler provenance from a binary using a vision transformer classifier
description: Convert a program binary's raw bytes into an image and classify it with a pre-trained vision-transformer or CNN model to determine its compiler family and optimization level, supporting malware authorship attribution and reverse engineering without handcrafted features.
objective_ids:
  - DFO-1019
weakness_ids:
  - LWW-1128
aliases:
  - Vision-transformer compiler-provenance identification
  - Image-based binary compiler and optimization-level classification
source_refs:
  - LWCite-1124
updated_at: 2026-08-12
status: complete
---

# Identify compiler provenance from a binary using a vision transformer classifier

## Summary

Compiler-provenance identification — determining a binary's compiler family, version, and optimization level — supports function fingerprinting, code-clone detection, and authorship attribution, including understanding the origin of a malware sample. Transforming binaries into images and classifying them with pre-trained computer-vision and vision-transformer models avoids the domain-specific handcrafted feature engineering that earlier syntactic/semantic/structural-feature approaches required.

## Details

Binaries from the BinKit dataset (including Obfuscator-LLVM-obfuscated variants using instruction substitution, bogus control flow, control flow flattening, and combinations thereof) are rendered as images and classified using 8 pre-trained architectures (VGG16, ResNet, GoogleNet, DenseNet, MobileNet, AlexNet) alongside transformer-based models (ViT, Swin Transformer/SViT), focused on the two most common cross-platform compilers, GCC and Clang. Compiler-family identification and optimization-level pairs with clearly different runtime behavior (e.g. O0, no optimization, versus O3, aggressive optimization) reach high accuracy — up to 0.962 for compiler family and 0.945 (pre-trained models) or 0.902 (transformer models) for O0 vs. O3. The approach is architecture-agnostic, requires no handcrafted features or extensive fine-tuning, and is notably resilient to obfuscation: obfuscated-binary accuracy for O0 vs. O3 reached 0.971 using ViT, comparable to deobfuscated performance, in contrast to prior techniques that typically suffer significant accuracy drops on obfuscated code.

## Examples

- ViT achieved 0.962 accuracy identifying compiler family (GCC vs. Clang), and VGG16 achieved 0.945 accuracy (0.942 precision, 0.948 recall) distinguishing O0 from O3 optimization levels on deobfuscated binaries.

## Related Objectives

- `DFO-1019` Detect anti-forensics and other anomalies

## Related Weaknesses

- [[weaknesses/Vision-transformer compiler-provenance classifiers cannot reliably distinguish similarly optimized binaries]]

## References

- [LWCite-1124] Khan et al., 2024, "Compiler-provenance identification in obfuscated binaries using vision transformers", FSI: Digital Investigation 49, 301764.
