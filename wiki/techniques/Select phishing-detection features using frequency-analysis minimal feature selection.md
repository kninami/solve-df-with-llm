---
id: LWT-2065
type: technique
name: Select phishing-detection features using frequency-analysis minimal feature selection
description: Reduce a large corpus of candidate phishing-detection features (URL and webpage heuristics) to a small, high-relevance minimal feature set by ranking each feature's frequency of occurrence across a confirmed-phishing feature database and retaining only those exceeding an exclusion-limit threshold, before training a classifier — improving classification speed and resource overhead without sacrificing detection accuracy.
objective_ids:
  - DFO-1019
weakness_ids:
  - LWW-2065
aliases:
  - Frequency Feature Assessment Algorithm
source_refs:
  - LWCite-2069
updated_at: 2026-08-15
status: complete
---

# Select phishing-detection features using frequency-analysis minimal feature selection

## Summary

Rather than training a phishing classifier on every candidate feature proposed in the literature (which increases training/testing time, memory overhead, and detection latency without a corresponding accuracy benefit), this technique computes a Frequency Information (FI) score for each candidate feature — the proportion of a confirmed-phishing feature database in which that feature occurs — and keeps only features whose FI exceeds a predefined exclusion-limit threshold, producing a minimal, high-relevance feature list for downstream classifier training.

## Details

The Frequency Feature Assessment Algorithm computes, for every candidate feature `f_i` in a database `DB` of confirmed phishing fingerprints, `FI = f_i / sum(DB)` (the feature's frequency of occurrence across the whole database), then inserts `f_i` into a new high-relevance feature list `x` only if `FI` exceeds the exclusion-limit threshold θ; the resulting list is ranked and the top-relevance features are selected as the final minimal feature set `m`. The feature set is deliberately composed of a fixed ratio (85% URL-based, 15% non-URL/webpage-based) because URL-based features have shown the most consistent discriminative power and lowest response-time overhead in prior anti-phishing literature; features found to be functionally redundant with an already-selected feature (e.g., keyword extraction being redundant with a "missing title" feature, or a "-" character in the URL path being redundant with a URL-length-elongation feature) are explicitly omitted even if individually frequent, to avoid retaining low-marginal-value features. The resulting minimal feature set is then used to train and compare classical ML classifiers (Naive Bayes, Support Vector Machine, Artificial Neural Network, Random Tree, Decision Tree) using standard TP/FP/Precision/Recall/F1/ROC metrics and 10-fold cross-validation.

## Examples

- Applying the algorithm to a 10,000-instance WEKA-formatted phishing dataset (13 features extracted from the UCI phishing repository via a JSoup HTML parser) produced a 13-feature minimal set — Number of Dots, URL Length, @ Symbol, No HTTPS, Domain in Path, HTTPS in Hostname, Path Length, IP Address, Popup Window, Submitting to Email, Missing Title, IFrame Redirection, and Return URL Length — smaller than a comparable prior reduced feature set of 27 features (Karabatak and Mustafa, 2018) while achieving comparable or better classifier accuracy: Random Tree reached 96.1% accuracy with a 0.39% false-positive rate and a 99.7% ROC value, outperforming Decision Tree (78.2%), Artificial Neural Network (74.6%), Support Vector Machine (72.9%), and Naive Bayes (69.9%) on the same reduced feature set.

## Related Objectives

- `DFO-1019` Detect anti-forensics and other anomalies

## Related Weaknesses

- [[weaknesses/Minimal URL-and-webpage-feature phishing classifiers do not generalize to spear-phishing, logo-based, or search-engine-based phishing]]

## References

- [LWCite-2069] Abiodun, Sodiya, Kareem & Oladimeji, 2021, "Performance Assessment of some Phishing predictive models based on Minimal Feature corpus", JDFSL 16(5). Source of the Frequency Feature Assessment Algorithm, the 13-feature minimal set, and the five-classifier comparison.
