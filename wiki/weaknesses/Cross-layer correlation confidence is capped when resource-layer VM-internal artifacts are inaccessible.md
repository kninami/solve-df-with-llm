---
id: DFW-1025
type: weakness
name: Cross-layer correlation confidence is capped when resource-layer VM-internal artifacts are inaccessible
description: In pooled cloud VM allocations where the cloud service provider does not support disk snapshot or live-forensic access to a shared virtual machine, cross-layer user-activity attribution cannot reach the framework's High-confidence tier, regardless of how completely the remaining layers (access, control) are collected, because the underlying evidence type required for High confidence is structurally unavailable.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1025
source_refs:
  - DFCite-1017
updated_at: 2026-08-09
status: complete
---

# Cross-layer correlation confidence is capped when resource-layer VM-internal artifacts are inaccessible

## Summary

Whether a VM-internal user activity artifact (as opposed to only an externalized one) is obtainable depends on the cloud service provider's offering and policy for the specific service in question, not on investigator effort or methodology quality. In the AWS WorkSpaces case study, neither VM disk snapshot acquisition nor live forensics was supported for the pooled, non-persistent allocation used, structurally limiting the Resource Layer evidence to externalized S3 persistent-storage artifacts.

## Why It Matters

An investigator working within a CSP's access constraints may correctly execute every step of the cross-layer correlation methodology and still be unable to attribute a specific activity to a specific user at High confidence, purely because of platform limitations outside their control. Presenting a Medium-confidence attribution as though it were High confidence (or failing to explain why confidence is capped) risks overstating the strength of the evidentiary conclusion, particularly relevant where such attribution may inform legal action against a specific individual.

## Related Mitigations

- [[mitigations/Supplement missing resource-layer access with externalized artifacts and report the resulting confidence level]]

## Used By

- [[techniques/Confidence-graded cross-layer evidence correlation for pooled cloud resources]]

## References

- [DFCite-1017] Park et al., 2026, "A forensic investigation framework for desktop-as-a-service in cloud environments", FSI: Digital Investigation 58.
