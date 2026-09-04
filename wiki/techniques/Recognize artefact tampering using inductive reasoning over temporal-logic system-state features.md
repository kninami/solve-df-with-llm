---
id: LWT-1299
type: technique
name: Recognize artefact tampering using inductive reasoning over temporal-logic system-state features
description: Recognize whether a digital artefact has been tampered with — starting with artefact destruction — by formally representing the tampering action in an extended Temporal Logic of Security Actions (S-TLA) model, inductively comparing a generic system's state before and after the action to characterize the observable features that result, and applying a feature-analysis algorithm to a specific case's artefacts to generate a credible, defensible theory about whether tampering occurred, without the impractical state-space search required by prior deductive model-checking approaches.
objective_ids:
  - DFO-1019
weakness_ids:
  - LWW-1309
aliases:
  - Extended S-TLA tampering model with action visibility
source_refs:
  - LWCite-1349
updated_at: 2026-08-15
status: complete
---

# Recognize artefact tampering using inductive reasoning over temporal-logic system-state features

## Summary

When artefact tampering goes unrecognized, it misleads the rest of a digital forensic investigation — a critical concern given legal systems' dependence on evidence authenticity, as illustrated by a Court of Arbitration for Sport hearing where "advanced digital forensics" was needed to uncover tampering meant to undermine the legal process. Prior formal-model approaches to recognizing tampering rely on natural-language tampering descriptions (imprecise and inconsistent across sources — even a narrow concept like "artefact destruction" is described inconsistently as "wiping," "secure disposal," or "dismantling" by different authors) that cannot be applied within formal reasoning frameworks, and on deductive model-checking that requires generating and exhaustively analyzing a system's full state space — considered impractical for real-life cases due to high time complexity and the difficulty of building models faithful to real systems without automation.

## Details

The approach extends the Temporal Logic of Security Actions (S-TLA) language, introducing the property of "action visibility" to formally represent one type of tampering (artefact destruction), which is further characterized into four specific sub-types — replacing ambiguous natural-language descriptions with a precise, model-compatible representation. Rather than deductive model-checking (mathematically proving a specific action occurred by searching a system's state space), the technique applies inductive reasoning — the most common inference mode in actual digital forensics practice, reaching conclusions that are probabilistic, defensible, and ampliative rather than strictly proven — by comparing a generic system's state before and after an artefact-destruction action to characterize the observable features (differences) that result from that class of tampering, independent of any single system's specific implementation. A simple feature-analysis algorithm then applies this characterization to a specific case's artefacts to recognize whether the tampering action has occurred and generate a credible theory of what happened, without needing to construct or search a full state-space model of the actual system under investigation. The knowledge framework this produces is explicitly extended beyond artefact destruction to other tampering types, giving investigators a system-independent means to understand and recognize tampering activity regardless of their technical familiarity with any particular system.

## Examples

- Two brief case studies demonstrate how the inductively-derived features of artefact destruction (comparing pre- and post-tampering system state) can be used with the simple feature-analysis algorithm to recognize whether that specific tampering action occurred in each case.
- Unlike deductive model-checking approaches (such as the Gladyshev and Patel example solved via the NuSMV model checker), which are limited by the model sizes their authors were able to process and rely entirely on human reasoning — with no automation — to construct a model faithful to the real system, this inductive approach proposes generic patterns usable to recognize tampering on any system without first building a system-specific model.

## Related Objectives

- `DFO-1019` Detect anti-forensics and other anomalies

## Related Weaknesses

- [[weaknesses/Feature-based tampering recognition does not weight how strongly a feature indicates tampering versus non-tampering]]

## References

- [LWCite-1349] Neale, Kennedy, and Nuseibeh, 2026, "Reasoning about artefact tampering", FSI: Digital Investigation 58, 302147.
