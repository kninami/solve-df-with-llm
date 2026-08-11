---
id: DFW-1093
type: weakness
name: Closed-set source-recording-device recognition cannot identify a device absent from its training set
description: The CNN-BiLSTM/SGMM recognition model operates in a closed-set setting, meaning it can only classify a questioned recording as belonging to one of the specific devices it was trained on; it has no mechanism for correctly identifying, or flagging as unknown, a recording made by a device model that was not part of its training data, and recognition accuracy is further reduced for brands with many similar device models (Xiaomi, Huawei, iPhone in the evaluated dataset).
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1093
source_refs:
  - DFCite-1085
updated_at: 2026-08-10
status: complete
---

# Closed-set source-recording-device recognition cannot identify a device absent from its training set

## Summary

The authors explicitly name this as a direction for future work rather than something the current method addresses: "our future work will place a stronger emphasis on open-set recording device source recognition tasks, addressing real-world scenarios where devices not seen during training must be identified." Separately, the paper's own error analysis found that "incorrect recognition results... are mainly concentrated on the three brands: Xiaomi, Huawei, and iPhone. The primary reason for this is that these three brands have a larger number of models compared to other brands," meaning within-brand model confusion is a distinct, additional accuracy limitation.

## Why It Matters

An investigator using this class of model to attribute a questioned audio recording to a specific device must confirm the actual candidate device (or an identical model) was represented in the model's training set; otherwise the model will still output some classification (forcing the recording into the closest trained class) rather than correctly indicating "not recognized," which risks a confident-looking but wrong attribution being presented as evidence. This risk is compounded for suspect devices from high-model-count brands.

## Related Mitigations

- [[mitigations/Confirm training-set coverage of the candidate device before relying on closed-set recording-device recognition results]]

## Used By

- [[techniques/CNN-BiLSTM structured representation learning of SGMM audio features for source recording device recognition]]

## References

- [DFCite-1085] Zeng et al., 2024, "Audio source recording device recognition based on representation learning of sequential Gaussian mean matrix", FSI: Digital Investigation 48.
