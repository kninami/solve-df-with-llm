---
id: LWM-2011
type: mitigation
name: Periodically retrain and validate the mnemonic classifier against real forensic case text and non-standard mnemonic variants
source_refs:
  - LWCite-2011
updated_at: 2026-08-14
status: partial
---

# Periodically retrain and validate the mnemonic classifier against real forensic case text and non-standard mnemonic variants

## Summary

Before relying on a TextCNN (or similar) mnemonic-identification model as the sole means of locating cryptocurrency wallet mnemonics in a case, validate it against real seized-device text samples containing known non-standard mnemonic forms (misspellings, reordered words, non-BIP39 wallet formats) and periodically retrain it as new variant forms are encountered.

## Addresses

- [[weaknesses/A TextCNN mnemonic classifier trained on synthetic BIP39 data may miss non-standard mnemonic variants in real evidence]]

## How To Apply

Where feasible, supplement the classifier's output with a secondary check against the BIP39 word list for flagged and near-miss candidate segments, and maintain a growing corpus of real, anonymized case-derived mnemonic examples (standard and variant) to periodically retrain the model, rather than relying indefinitely on the original synthetic training set.

## References

- [LWCite-2011] Kao, 2025 — the paper's own future-work discussion recommends larger-scale, more diverse real-world datasets to improve generalizability beyond the synthetic BIP39 training data used in this study.
