---
id: DFT-1033
type: technique
name: Triage chat evidence for linguistic markers using a hybrid regex-BERT model
description: Standardize heterogeneous chat-log exports (WhatsApp, Messenger, SMS, etc.) into a common per-message table, classify each message from a designated person-under-investigation against a fixed taxonomy of psychologically-defined linguistic markers using a hybrid high-precision regex plus high-recall BERT classifier, and aggregate the per-message flags into a quantitative, sorted frequency report to prioritize human review of a large case file.
objective_ids:
  - DFO-1003
weakness_ids:
  - DFW-1034
aliases:
  - Hybrid regex-BERT longitudinal linguistic-marker triage of chat evidence
  - Digital Conversation Analysis Pipeline
  - DCAP
source_refs:
  - DFCite-1024
updated_at: 2026-08-09
status: complete
---

# Triage chat evidence for linguistic markers using a hybrid regex-BERT model

## Summary

Cumulative, longitudinal patterns of abuse in text evidence (such as coercive control) are notoriously difficult for standard keyword search to surface, since the pattern is defined by a repeated, escalating constellation of subtle linguistic markers rather than any single "smoking gun" message. A three-module pipeline first ingests and standardizes raw multi-format chat exports into a clean table, then applies a message-level hybrid classifier combining a small set of high-precision regex patterns (fast, exact matches) with a BERT-based classifier (contextual, high-recall) for each marker trait, and finally aggregates per-message flags into a heatmap-style triage report ranking which markers are most prevalent in the person-under-investigation's messages.

## Details

The regex component checks for unambiguous, high-precision matches first; only when no regex pattern matches does the BERT classifier evaluate the message, with its output accepted only above a tuned confidence threshold, reducing both computational cost and noise from low-confidence neural predictions. The classification taxonomy is intentionally narrowed to a small number of core, clinically-validated trait categories (e.g., a 9-trait subset of DSM-5 diagnostic criteria) rather than a larger academically-derived taxonomy, trading some nuance for computational tractability, output clarity, and direct mapping to criteria investigators and legal professionals already recognize. The final triage report counts and ranks each trait by frequency among the designated person-under-investigation's messages only, letting an investigator immediately filter the underlying analyzed dataset for the exact messages behind any given trait rather than reading the full case file linearly.

## Examples

- Applied to a simulated 8,451-message two-party chat-log case file, the pipeline flagged 812 of 3,982 messages (20.39%) from the person-under-investigation across the ranked trait categories, and isolating the top trait (287 messages) reduced the volume requiring manual review by 92.8% relative to reading the full message set.

## Related Objectives

- `DFO-1003` Review content for relevance

## Related Weaknesses

- [[weaknesses/Message-level classification of coercive control markers misses sarcasm and cross-message context]]

## References

- [DFCite-1024] Patel et al., 2026, "A hybrid neural-symbolic approach for the longitudinal profiling of coercive control in digital investigations", FSI: Digital Investigation 56.
