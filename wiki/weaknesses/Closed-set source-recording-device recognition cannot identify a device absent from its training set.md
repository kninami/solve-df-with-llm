---
id: LWW-1093
type: weakness
name: Closed-set source-recording-device recognition cannot identify a device absent from its training set
description: The CNN-BiLSTM/SGMM recognition model operates in a closed-set setting, meaning it can only classify a questioned recording as belonging to one of the specific devices it was trained on; it has no mechanism for correctly identifying, or flagging as unknown, a recording made by a device model that was not part of its training data, and recognition accuracy is further reduced for brands with many similar device models (Xiaomi, Huawei, iPhone in the evaluated dataset).
categories:
  - ASTM_INCOMP
mitigation_ids:
  - LWM-1093
source_refs:
  - LWCite-1085
  - LWCite-1103
  - LWCite-2022
updated_at: 2026-08-14
status: complete
---

# Closed-set source-recording-device recognition cannot identify a device absent from its training set

## Summary

The authors explicitly name this as a direction for future work rather than something the current method addresses: "our future work will place a stronger emphasis on open-set recording device source recognition tasks, addressing real-world scenarios where devices not seen during training must be identified." Separately, the paper's own error analysis found that "incorrect recognition results... are mainly concentrated on the three brands: Xiaomi, Huawei, and iPhone. The primary reason for this is that these three brands have a larger number of models compared to other brands," meaning within-brand model confusion is a distinct, additional accuracy limitation.

The same closed-set limitation applies to CAM1D, a multi-signature PCE-trend method for identifying the source camera of seam-carved images [LWCite-1103]: the authors state plainly that "we consider a closed-set problem in which the test photo was taken by one of the cameras under testing," and note that an open-set deployment (where the true source camera may not be among the candidates) would require choosing a minimum decision-score threshold — a design question the paper leaves unresolved.

## Why It Matters

An investigator using this class of model to attribute a questioned audio recording to a specific device must confirm the actual candidate device (or an identical model) was represented in the model's training set; otherwise the model will still output some classification (forcing the recording into the closest trained class) rather than correctly indicating "not recognized," which risks a confident-looking but wrong attribution being presented as evidence. This risk is compounded for suspect devices from high-model-count brands. The same limitation applies to closed-set acoustic-environment classification (LWCite-2022): a CRNN trained on only 3 or 4 fixed environment/device categories has no mechanism to correctly flag a recording made in a genuinely different, untrained environment or with an untrained microphone type as "unknown" rather than forcing it into the nearest trained class.

## Related Mitigations

- [[mitigations/Confirm training-set coverage of the candidate device before relying on closed-set recording-device recognition results]]

## Used By

- [[techniques/Recognize source recording devices using CNN-BiLSTM audio feature learning]]
- [[techniques/Identify a seam-carved image's source camera using multi-signature PCE trend analysis]]
- [[techniques/Classify a recording's acoustic environment and microphone type using CNN-LSTM spectrogram analysis]]

## References

- [LWCite-1085] Zeng et al., 2024, "Audio source recording device recognition based on representation learning of sequential Gaussian mean matrix", FSI: Digital Investigation 48.
- [LWCite-1103] Irshad et al., 2023, "CAMID: An assuasive approach to reveal source camera through inconspicuous evidence", FSI: Digital Investigation 46.
- [LWCite-2022] Qamhan et al., 2021, "Digital audio forensics: Microphone and environment classification using deep learning", IEEE Access 9 — its environment and microphone classifiers are both trained and evaluated as closed-set tasks over a fixed 3-environment/4-microphone taxonomy, with no open-set/unknown-class handling.
