---
id: DFT-1252
type: technique
name: Classify indoor scenes in CSAM triage using self-supervised pretraining
description: Automatically classify the indoor scene context (bedroom, bathroom, child's room, classroom, dressing room, living room, studio, swimming pool) of a suspected child sexual abuse material image using a ResNet-50 model self-supervised-pretrained on combined object-centric and scene-centric imagery before fine-tuning, to group similar imagery and locate identifying environmental cues without needing large volumes of labeled CSAM for training.
objective_ids:
  - DFO-1012
weakness_ids:
  - DFW-1266
aliases:
  - Places8 indoor scene classification
  - Self-supervised CSAI scene classification
source_refs:
  - DFCite-1292
updated_at: 2026-08-14
status: complete
---

# Classify indoor scenes in CSAM triage using self-supervised pretraining

## Summary

Because CSAM is held under strict access and handling restrictions, large labeled CSAM training sets are effectively unobtainable for most researchers; self-supervised learning (SSL) — pretraining a model on abundant unlabeled or weakly-labeled public object- and scene-centric imagery, then fine-tuning only a small final stage on a modest labeled dataset — lets an investigator train a usable indoor-scene classifier for CSAM triage (identifying where abuse imagery was likely captured, e.g. a bedroom vs. a classroom, to group related imagery or locate identifying environmental cues) without requiring large volumes of sensitive material for training.

## Details

The methodology has two stages: a pretext (SSL) stage, where a ResNet-50 backbone is pretrained without labels on a combination of object-centric (ImageNet) and scene-centric (indoor images drawn from Places365 plus synthetic indoor-scene datasets) imagery using a contrastive or redundancy-reduction SSL objective (Barlow Twins performed best among four compared methods: SwAV, SimCLR, Barlow Twins, SupCon); and a downstream fine-tuning stage, where the pretrained backbone is fine-tuned on a small labeled dataset of eight indoor scene classes (a purpose-built "Places8" subset of Places365, selected in consultation with law enforcement partners for relevance to CSAM investigations: bathroom, bedroom, child's room, classroom, dressing room, living room, studio, swimming pool). Sequencing SSL on ImageNet first, then further SSL on scene-centric data, then fine-tuning on the labeled downstream task outperformed skipping either SSL stage, and outperformed a fully supervised ImageNet-pretrained baseline by an average of 2.2 percentage points in balanced accuracy. Critically, the resulting model's benchmark accuracy on public scene-classification data does not predict its accuracy on real CSAM, which must be separately validated under appropriate legal authority and access controls before operational deployment.

## Examples

- The final SSL-pretrained model reached 71.6% balanced accuracy on the held-out Places8 validation set and 77.5% accuracy on a small out-of-distribution test set assembled from Google/Bing images and the Dollar Street dataset, but only 36.7% balanced accuracy when evaluated (by law enforcement partners, under access-controlled conditions) against real CSAM material.
- On real CSAM, per-category accuracy ranged from 94.6% for "bathroom" down to 28% for "child's room" and 20.7% for "living room," with the confusion matrix showing "child's room," "bedroom," and "living room" frequently misclassified as each other or as "dressing room" — a confusion the authors attribute to the near-universal presence of people (specifically children) across all CSAM images, a systematic distributional difference from public scene datasets (which are typically staged, empty-room photography) that the model had not learned to disregard.

## Related Objectives

- `DFO-1012` Locate potentially relevant content

## Related Weaknesses

- [[weaknesses/Scene classifiers trained on public datasets show a large domain gap and degrade sharply on real CSAM]]

## References

- [DFCite-1292] Valois, Macedo, Ribeiro, dos Santos and Avila, 2025, "Leveraging self-supervised learning for scene classification in child sexual abuse imagery", FSI: Digital Investigation 53, 301918.
