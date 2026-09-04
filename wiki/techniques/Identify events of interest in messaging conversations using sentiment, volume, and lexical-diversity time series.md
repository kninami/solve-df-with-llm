---
id: LWT-2074
type: technique
name: Identify events of interest in messaging conversations using sentiment, volume, and lexical-diversity time series
description: Reduce the manual effort of reviewing long-running mobile messaging conversations (SMS, WhatsApp, and similar) by computing per-participant time series of message volume, sentiment polarity, and lexical diversity, smoothing them with moving averages and first-order differencing to reveal daily/weekly trends, and flagging above-average-volume or sharply-changing periods as candidate events of interest for an investigator to review directly.
objective_ids:
  - DFO-1001
  - DFO-1003
weakness_ids:
  - LWW-2076
aliases:
  - Semi-automated text mining for digital forensic conversation triage
source_refs:
  - LWCite-2082
updated_at: 2026-08-16
status: complete
---

# Identify events of interest in messaging conversations using sentiment, volume, and lexical-diversity time series

## Summary

Long-running mobile messaging exchanges between closely related individuals can span years and hundreds of messages a day, making manual sifting through them for investigatively relevant moments impractical. Applying time-series methods (moving averages, first-order differencing) to per-participant message volume, semi-supervised sentiment classification, and lexical-diversity measures produces a timeline that an investigator can drill down into at the specific moments where tone, activity level, or vocabulary breadth changed sharply, rather than reading the full conversation trail.

## Details

Extracted messages are pre-processed to handle SMS/social-media-specific text conventions (abbreviations, acronyms, emoji, limited message length), then three time series are computed per participant: message volume (count per period), sentiment polarity (via a semi-supervised sentiment classifier — pSenti — augmented with a small domain-specific positive/negative lexicon derived from manually annotated seed messages, since general-purpose sentiment models trained on more formal text perform poorly on informal SMS-style text), and lexical diversity (via the Moving Average Type-Token Ratio, MATTR, chosen over simpler type-token ratio measures because it is less sensitive to text length). Each time series is smoothed with a centred moving average at daily (24-hour window) and weekly (168-hour window) granularity, and a first-order-differenced version of the smoothed series is also computed to directly reveal points of large change. Named entity recognition (via a Conditional Random Field model, iteratively bootstrapped with high-confidence Viterbi-tagged sentences) is applied in parallel to extract people, locations, organizations, and commodities mentioned in messages, letting an investigator quickly check whether specific entities relevant to a case appear in the period surrounding a flagged event of interest. An "event of interest" is operationally defined as a subset of messages around an above-average-volume period, an extreme sentiment-polarity value, or a sharp lexical-diversity change — each representing a candidate point where the relationship dynamic or an external event may have affected the conversation.

## Examples

- Applied to two donated long-term conversation datasets (46,304 WhatsApp messages over 482 days between two participants; 38,920 SMS messages over 405 days between two other participants), the framework's moving-average volume plots revealed distinct multi-month periods of elevated or reduced messaging activity per participant, and first-order-difference plots pinpointed the specific days those shifts began.
- The trained sentiment classifier, evaluated on a manually annotated 300-message test set (100 each positive/neutral/negative), achieved an overall F1 score of 0.752 (precision 0.841, recall 0.680), performing best on negative-sentiment messages (F1 0.76) and worst on neutral ones (F1 0.69).

## Related Objectives

- `DFO-1001` Reconstruct events
- `DFO-1003` Review content for relevance

## Related Weaknesses

- [[weaknesses/Sentiment and named-entity models trained for general text misjudge short, informal messaging text]]

## References

- [LWCite-2082] Harris, Jacobson, and Provetti, 2024, "Sentiment and time-series analysis of direct-message conversations", FSI: Digital Investigation 49, 301753.
