---
id: LWT-2011
type: technique
name: Identify cryptocurrency wallet mnemonic phrases in text using a TextCNN classifier
description: The process of rapidly locating BIP39 cryptocurrency-wallet mnemonic seed phrases embedded in large volumes of unstructured multilingual forensic text (memos, clipboards, documents) using a trained Text Convolutional Neural Network, instead of comparing every 12-word segment against a static mnemonic word-list.
objective_ids:
  - DFO-1012
weakness_ids:
  - LWW-2011
aliases:
  - TextCNN mnemonic identification
  - NLP-driven mnemonic recognition
source_refs:
  - LWCite-2011
updated_at: 2026-08-14
status: partial
---

# Identify cryptocurrency wallet mnemonic phrases in text using a TextCNN classifier

## Summary

Recovering a cryptocurrency wallet's mnemonic phrase (the 12-24-word seed used to derive its private keys) from files on a seized device is critical for asset seizure, but traditional dictionary/library-matching tools that check every word segment against the 2048-word BIP39 list scale poorly to large data volumes and struggle with non-standard, misspelled, or multilingual mnemonics. An investigator instead trains a Text Convolutional Neural Network (or a comparable RNN/LSTM/BiLSTM model) on labeled mnemonic and non-mnemonic text to classify candidate 12-word segments directly, without exhaustive per-word list lookups.

## Details

LWCite-2011 trains TextCNN (and RNN, LSTM, BiLSTM as comparisons) on a balanced dataset of 110,000 BIP39-generated mnemonics across 11 languages/formats (English, Japanese, Spanish, Simplified/Traditional Chinese, French, Italian, Korean, Czech, Portuguese, and a numeric mnemonic variant) and 110,000 non-mnemonic samples drawn from memos, clipboard text, readme files, articles, and deliberately confusable "extreme case" sentences resembling mnemonics. TextCNN's convolutional filters extract local n-gram-like features from each 12-word sequence's word embeddings, followed by max-pooling and a softmax classifier, giving it strong performance on short, locally-patterned sequences like mnemonics without the higher parameter cost of a Transformer model. On an independent 147,591-sample imbalanced test set (60 real mnemonics amid 147,531 non-mnemonic samples, reflecting realistic forensic scarcity), TextCNN reached 99.9993% accuracy with 0% false-negative rate and just one false positive, while running roughly 40x faster than the traditional mnemonic-library-matching method.

## Examples

- LWCite-2011's benchmark: TextCNN 8.23s execution time and 99.9993% test accuracy vs. the traditional Mnemonic Library Matching Method's 333.30s and 100% (theoretical maximum) accuracy on the same 147,591-sample test set.

## Related Objectives

- `DFO-1012` Locate potentially relevant content

## Related Weaknesses

- [[weaknesses/A TextCNN mnemonic classifier trained on synthetic BIP39 data may miss non-standard mnemonic variants in real evidence]]

## References

- [LWCite-2011] Kao, "Accelerating multilingual cryptocurrency forensics: An NLP-driven approach for efficient mnemonic identification", IEEE Access, 2025 — source of the TextCNN mnemonic-identification model, dataset, and benchmark results described above.
