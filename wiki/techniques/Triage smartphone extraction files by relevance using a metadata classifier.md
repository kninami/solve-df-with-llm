---
id: LWT-1258
type: technique
name: Triage smartphone extraction files by relevance using a metadata classifier
description: Rank a smartphone forensic extraction's files as "Interesting" or "Not Interesting" using a machine learning classifier trained on engineered file-metadata features (file type, size, path depth and structure, filename character composition, EXIF presence, and delta between file-modified and device-apprehended dates) rather than on the files' actual content, letting an examiner focus review effort on the small fraction of files likely to matter.
objective_ids:
  - DFO-1003
weakness_ids:
  - LWW-1270
aliases:
  - ML-based smartphone file metadata triage
source_refs:
  - LWCite-1298
updated_at: 2026-08-14
status: complete
---

# Triage smartphone extraction files by relevance using a metadata classifier

## Summary

A typical smartphone forensic extraction contains vastly more uninteresting operating-system and application files than case-relevant ones (in one real-case dataset, only 6% of nearly two million extracted files were of interest), so manually reviewing every file is both slow and an inefficient use of skilled examiner time; training a classifier on file metadata alone — rather than requiring content inspection or hardcoded file-hash/keyword templates — lets a triage tool flag likely-relevant files automatically, filling the gap left by classical block-hash/regex triage (which requires known templates) and prior device-level ML triage approaches (which classify a whole device, not individual files).

## Details

Files are logically extracted and logged with a forensic tool (e.g. XRY), then twelve base metadata features are engineered per file: general features (file type/extension, file size, delta between apprehension date and file-modified date, presence of EXIF data, and X/Y resolution for photos), filename-related features (character count and the percentage of numeric and underscore characters in the name), and path-related features (whether the path itself contains numbers, path depth, and number of periods in the path). File type and file path are additionally vectorized via a bag-of-words CountVectorizer to capture categorical distinctions (e.g. distinguishing a WhatsApp-path file from a Telegram-path file). Recursive Feature Elimination with cross-validation is used to prune the resulting larger feature space (up to 187 features after vectorization) back down to the subset that maximizes F1-score, and several classifier families (Naive Bayes, SVM, k-nearest-neighbors, decision tree, random forest, and a multi-layer-perceptron neural network) are trained and compared via 10-fold cross-validation with hyperparameter tuning via grid search, using F1-score (rather than raw accuracy, which is misleading on this heavily class-imbalanced problem) as the primary comparison metric.

## Examples

- Trained and evaluated on metadata from nearly 2 million files extracted from 12 Android devices linked to real terrorism cases (6% labeled "Interesting" by forensic experts), a Random Forest classifier achieved the best overall performance (F1-score 0.9861, precision 0.9841, recall 0.9881, accuracy 0.9983), correctly identifying 98.81% of files of interest on average while executing in under 20 minutes for the full 10-fold cross-validation.
- Naive Bayes achieved the highest raw recall (99.32%) but the lowest precision (78.91%) and F1-score (0.8795) of all six classifiers tested, meaning it caught nearly every interesting file but also flagged roughly 21% of uninteresting files as interesting — illustrating that recall alone is an incomplete metric for a triage tool intended to reduce, not merely re-order, an examiner's review workload.

## Related Objectives

- `DFO-1003` Review content for relevance

## Related Weaknesses

- [[weaknesses/Metadata-based smartphone file-triage classifiers trained on one case type or platform may not generalize to a different one]]

## References

- [LWCite-1298] Serhal and Le-Khac, 2021, "Machine learning based approach to analyze file meta data for smart phone file triage", DFRWS 2021 USA; FSI: Digital Investigation 37, 301194.
