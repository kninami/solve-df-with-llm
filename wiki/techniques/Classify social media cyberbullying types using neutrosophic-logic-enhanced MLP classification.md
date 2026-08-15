---
id: DFT-2045
type: technique
name: Classify social media cyberbullying types using neutrosophic-logic-enhanced MLP classification
description: The process of fine-grained-classifying a piece of social media text as a specific cyberbullying subtype (age-, gender-, ethnicity-, religion-, or other-based) by training a one-against-one ensemble of MLP binary classifiers and converting their output probabilities into neutrosophic sets (truth, indeterminacy, falsity membership) to make a final classification decision that explicitly accounts for ambiguous or overlapping category boundaries.
objective_ids:
  - DFO-1003
weakness_ids:
  - DFW-2045
aliases:
  - Neutrosophic cyberbullying fine-grained classification
source_refs:
  - DFCite-2046
updated_at: 2026-08-14
status: partial
---

# Classify social media cyberbullying types using neutrosophic-logic-enhanced MLP classification

## Summary

Cyberbullying-related hate speech recovered from social media during an investigation often needs to be classified not just as "cyberbullying" but by its specific subtype (targeting age, gender, ethnicity, religion, or another characteristic), yet the brief, informal, and context-dependent nature of social media text creates genuinely ambiguous cases that a crisp classifier forces into one category regardless of true uncertainty. An investigator instead uses a one-against-one ensemble of MLP binary classifiers (one per class pair) to capture nuanced pairwise relationships between subtypes, then converts each class's aggregated prediction probability into a three-valued neutrosophic set - how true, how indeterminate, and how false the classification is - rather than a single crisp label, making the model's uncertainty about ambiguous cases explicit rather than hidden.

## Details

DFCite-2046's pipeline: text is cleaned (stripped of emoji, stopwords, punctuation, links, mentions) and vectorized with TF-IDF; a one-against-one MLP ensemble is trained, producing n(n-1)/2 binary decision boundaries for n classes, each classifier predicting the probability of one class over another for a given input; these pairwise probabilities are combined per class to yield an overall class-probability vector; each class's probability is then converted to a neutrosophic set N(P) = (T, I, F) using predefined thresholds - Truth-membership T is set if the probability meets or exceeds a truth threshold, Indeterminacy-membership I is set if the probability falls in an ambiguous middle band, and Falsity-membership F reflects the probability the sample does not belong to that class - and Interval Neutrosophic Sets further represent these as ranges rather than point values, capturing uncertainty more flexibly than a single fuzzy-logic membership degree can. The final classification selects the class whose neutrosophic truth-membership is highest, explicitly informed by how much indeterminacy was present in that decision.

## Examples

- DFCite-2046's evaluation on two Twitter cyberbullying datasets (47,000+ and ~100,000 tweets respectively): 95% and 97% accuracy for the proposed neutrosophic-MLP model, versus 92% for a comparable fuzzy-logic-based classifier and up to a further 3-percentage-point improvement over standalone RF/LR/SVM baselines; data augmentation (synonym replacement, random insertion/deletion) further raised accuracy to 98%.

## Related Objectives

- `DFO-1003` Review content for relevance

## Related Weaknesses

- [[weaknesses/Gender-based cyberbullying classification is consistently the least accurate subtype across all tested methods]]

## References

- [DFCite-2046] Ibrahim et al., "Social media forensics: An adaptive cyberbullying-related hate speech detection approach based on neural networks with uncertainty", IEEE Access, 2024 — source of the one-against-one MLP plus neutrosophic-set classification methodology and evaluation results described above.
