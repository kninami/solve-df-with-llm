---
id: DFM-1025
type: mitigation
name: Supplement missing resource-layer access with externalized artifacts and report the resulting confidence level
source_refs:
  - DFCite-1017
updated_at: 2026-08-09
status: complete
---

# Supplement missing resource-layer access with externalized artifacts and report the resulting confidence level

## Summary

When a cloud service provider does not support VM-internal evidence acquisition (snapshot or live forensics) for a pooled resource, actively seek out externalized artifacts (data an activity produced in storage outside the VM) to support attribution, and explicitly state the resulting confidence tier rather than presenting the attribution as unqualified.

## Addresses

- [[weaknesses/Cross-layer correlation confidence is capped when resource-layer VM-internal artifacts are inaccessible]]

## How To Apply

Identify what externalized artifacts the specific CSP offering does support — persistent storage logs, uploaded/downloaded file records, network flow logs, or externalized profile containers — and combine them with Access- and Control-layer identifier and temporal correlation using the framework in [[techniques/Correlate cross-layer evidence for pooled cloud resources with graded confidence]]. In the investigative report, explicitly state which of the five attribution conditions (user identifier, resource identifier, temporal information, VM-internal artifact, externalized artifact) were and were not met, and the resulting High/Medium/Low confidence tier, so downstream decision-makers understand the attribution's actual evidentiary strength.

## References

- [DFCite-1017] Park et al., 2026, "A forensic investigation framework for desktop-as-a-service in cloud environments", FSI: Digital Investigation 58.
