---
id: DFT-2090
type: technique
name: Track DarkNet market cryptocurrency preference shifts using temporal topic modeling of ClearNet forums
description: Quantify how a DarkNet drug-trading community's cryptocurrency payment preferences shift over time (e.g. from Bitcoin toward privacy-focused coins such as Monero) by applying correlation-explanation temporal topic modeling and sentiment analysis to publicly accessible ClearNet forum discussions (e.g. Reddit) about DarkNet markets, tracking topic prevalence and sentiment trends over multi-year windows rather than relying on a single point-in-time survey.
objective_ids:
  - DFO-1004
  - DFO-1012
weakness_ids:
  - DFW-2093
aliases:
  - CorEx temporal topic modeling for cryptocurrency-preference tracking
source_refs:
  - DFCite-2110
updated_at: 2026-08-16
status: complete
---

# Track DarkNet market cryptocurrency preference shifts using temporal topic modeling of ClearNet forums

## Summary

Understanding how DarkNet drug-market participants' cryptocurrency preferences evolve over time is relevant to assessing the traceability and deterrent effect of blockchain analysis on illicit trade, but this evolution is not directly observable from on-chain data alone. Community-driven ClearNet forums that discuss DarkNet market experiences (e.g. subreddits dedicated to DarkNet markets) provide a public proxy signal: applying temporal topic modeling (CorEx, Correlation Explanation) to track which cryptocurrency-related topics rise or fall in discussion prevalence over time, combined with sentiment analysis (VADER) to gauge community attitude toward each currency, reveals a preference trend that can corroborate or contextualize blockchain-derived transaction-volume evidence.

## Details

Forum posts and comments are collected over a multi-year window and pre-processed (tokenization, stop-word removal) before being fed into a temporal-aware topic modeling pipeline; CorEx identifies latent topics by maximizing the total correlation between words and topics rather than assuming a specific generative document model, and running it across sequential time slices reveals how topic prevalence shifts across the observation window. VADER (Valence Aware Dictionary and sEntiment Reasoner), a lexicon- and rule-based sentiment analysis tool tuned for informal/social-media-style text, is separately applied to posts mentioning each cryptocurrency to track community sentiment (positive, negative, neutral) toward that currency over the same time slices. Combining topic-prevalence and sentiment trends for each cryptocurrency of interest (e.g. Bitcoin, Monero) produces a preference-shift narrative -- for instance, discussion volume and positive sentiment growing around a privacy-focused coin while discussion of a more traceable coin declines -- that can be correlated against independently known events (e.g. law-enforcement blockchain-tracing successes, exchange regulations) to assess whether such events plausibly drove the observed preference shift.

## Examples

- Applied to a multi-year corpus of DarkNet-market-focused subreddit discussions, the technique tracked increasing discussion volume and generally positive sentiment toward Monero alongside declining relative discussion of Bitcoin for illicit drug-trade payment purposes, consistent with growing community awareness of blockchain traceability concerns for Bitcoin.

## Related Objectives

- `DFO-1004` Conduct research
- `DFO-1012` Locate potentially relevant content

## Related Weaknesses

- [[weaknesses/ClearNet forum-derived cryptocurrency preference trends do not directly confirm actual DarkNet marketplace purchasing behavior]]

## References

- [DFCite-2110] "The shift of DarkNet illegal drug trade preferences in cryptocurrency: The question of traceability and deterrence", FSI: Digital Investigation 48, 2024.
