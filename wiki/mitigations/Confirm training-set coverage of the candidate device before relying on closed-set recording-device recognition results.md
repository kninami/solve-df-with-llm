---
id: DFM-1093
type: mitigation
name: Confirm training-set coverage of the candidate device before relying on closed-set recording-device recognition results
source_refs:
  - DFCite-1085
  - DFCite-1103
updated_at: 2026-08-12
status: complete
---

# Confirm training-set coverage of the candidate device before relying on closed-set recording-device recognition results

## Summary

Before relying on a closed-set recording-device recognition model's classification of a questioned audio file, confirm that the suspected source device (or an identical model) was represented in the model's training set, and apply extra scrutiny to results for brands with many similar device models.

## Addresses

- [[weaknesses/Closed-set source-recording-device recognition cannot identify a device absent from its training set]]

## How To Apply

Check the model's documented training-set device list before treating its classification as meaningful evidence; if the candidate device model is not represented, treat the output as unreliable regardless of its confidence score, since the model has no "unknown device" category and will force a classification into its nearest trained class. Apply added scrutiny and, where feasible, independent corroboration for results involving brands with many closely related models (e.g. Xiaomi, Huawei, iPhone), where within-brand confusion is more likely.

## References

- [DFCite-1085] Zeng et al., 2024, "Audio source recording device recognition based on representation learning of sequential Gaussian mean matrix", FSI: Digital Investigation 48.
- [DFCite-1103] Irshad et al., 2023, "CAMID: An assuasive approach to reveal source camera through inconspicuous evidence", FSI: Digital Investigation 46.
