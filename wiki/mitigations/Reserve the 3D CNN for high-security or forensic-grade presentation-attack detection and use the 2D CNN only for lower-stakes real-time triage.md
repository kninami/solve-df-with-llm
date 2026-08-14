---
id: DFM-2025
type: mitigation
name: Reserve the 3D CNN for high-security or forensic-grade presentation-attack detection and use the 2D CNN only for lower-stakes real-time triage
source_refs:
  - DFCite-2025
updated_at: 2026-08-14
status: partial
---

# Reserve the 3D CNN for high-security or forensic-grade presentation-attack detection and use the 2D CNN only for lower-stakes real-time triage

## Summary

Do not deploy a 2D CNN presentation-attack detector as the sole safeguard in a context where a missed spoof (false negative) carries serious consequences (post-event forensic verification, high-security access control); reserve the 3D CNN, which achieved zero false negatives in the source study, for those higher-stakes settings, and use the 2D CNN only where its speed/compute advantage matters more than eliminating the last few percent of false negatives.

## Addresses

- [[weaknesses/A 2D CNN presentation-attack detector misses subtle temporal spoofing artifacts that a 3D CNN catches]]

## How To Apply

Follow the source paper's own deployment decision framework: choose the 3D CNN when server/cloud-side compute is available and zero-false-negative detection is required; choose the 2D CNN (or a lightweight ML classifier on handcrafted features) only for edge-device or real-time high-throughput scenarios, and where feasible, route 2D-CNN-flagged "authentic" frames from borderline or high-value cases through a secondary, centralized 3D CNN pass before final acceptance.

## References

- [DFCite-2025] Dessouky et al., 2026 — Section V's "Practical Deployment Guidelines" explicitly recommends the 3D CNN for centralized forensic analysis and high-security environments, and the 2D CNN for real-time, edge-computing surveillance.
