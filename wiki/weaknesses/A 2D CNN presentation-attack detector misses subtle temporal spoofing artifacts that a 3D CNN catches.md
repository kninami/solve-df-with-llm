---
id: LWW-2025
type: weakness
name: A 2D CNN presentation-attack detector misses subtle temporal spoofing artifacts that a 3D CNN catches
description: Because a 2D CNN classifies individual frames independently with no temporal modeling, it exhibits an elevated false-negative rate for presentation attacks whose telltale artifacts (flickering, display-boundary movement, lack of natural micro-movements like blinking) only become apparent across a sequence of frames, meaning some genuine spoofing attempts are misclassified as authentic.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - LWM-2025
source_refs:
  - LWCite-2025
updated_at: 2026-08-14
status: partial
---

# A 2D CNN presentation-attack detector misses subtle temporal spoofing artifacts that a 3D CNN catches

## Summary

The source paper's own results show the 2D CNN's recall dropping to 98% due to a 2% false-negative rate, compared to the 3D CNN's 0% FNR (100% recall) on the same intra-dataset evaluation. The paper explicitly attributes this to the 2D CNN's "inability to model temporal dependencies," noting it showed "reduced effectiveness in detecting subtle or gradual temporal artifacts, such as flickering, display boundary movement, or the lack of natural micro-movements (like blinking), which are hallmarks of digital manipulation," and that this "absence of dedicated temporal modeling led to context fragmentation, frequently resulting in misclassifications of tampered videos."

## Why It Matters

An investigator or system operator who deploys the 2D CNN for its speed and edge-device suitability, without accounting for its measurably weaker recall on subtle, motion-dependent presentation attacks, risks a small but non-zero share of genuine physical spoofing attempts (e.g. a well-executed video replay attack) passing undetected in exactly the scenarios - high-security access points, real-time surveillance triage - where a missed spoof carries the greatest consequence.

## Related Mitigations

- [[mitigations/Reserve the 3D CNN for high-security or forensic-grade presentation-attack detection and use the 2D CNN only for lower-stakes real-time triage]]

## Used By

- [[techniques/Select a 2D or 3D CNN architecture to detect facial presentation attacks based on deployment constraints]]

## References

- [LWCite-2025] Dessouky et al., 2026 — Section IV.C.2 explicitly attributes the 2D CNN's 2% FNR and reduced recall (98%) to its lack of temporal modeling and resulting difficulty detecting flickering, display-boundary movement, and blinking-absence artifacts.
