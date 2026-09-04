---
id: LWT-1162
type: technique
name: Classify keyword-matched message context as crime-relevant using an LLM majority-vote ensemble
description: Feed each keyword-matched mobile-messenger message, together with a window of surrounding context messages, to multiple large language models with a role-based prompt, and combine their binary crime-relevance judgments by majority vote to distinguish genuine criminal communication from figurative or metaphorical use of the same keyword.
objective_ids:
  - DFO-1003
weakness_ids:
  - LWW-1168
aliases:
  - LLM-driven evidence analysis framework for mobile messenger data
source_refs:
  - LWCite-1173
updated_at: 2026-08-12
status: complete
---

# Classify keyword-matched message context as crime-relevant using an LLM majority-vote ensemble

## Summary

Keyword searching flags a large volume of messages that mention a crime-related term, but most such hits are irrelevant (e.g. "this song is as addictive as drugs"). Prompting several LLMs, each given the target message plus preceding and following context messages, to judge relevance and combining their outputs by majority vote reduces both missed evidence and false alarms compared to relying on any single model.

## Details

The pipeline acquires mobile device data with a forensic tool, exports it to a structured format (e.g. Excel/CSV), keyword-searches for a target term, and extracts each hit together with a fixed window of surrounding messages (40 messages: 20 preceding, 20 following) to preserve context. A role-based prompt ("You are a mobile forensic expert...") with an explicit binary output instruction (1/0) and inclusion criteria is sent to each of several state-of-the-art LLMs (evaluated: GPT-4o, Gemini 1.5, Claude 3.5); the "Sandwich Defense" prompt structure (instruction, input text, reaffirmation of instruction) was needed for at least one model (Gemini) that otherwise lost track of the classification instruction when it directly preceded the message text. The investigator reviews the LLM output and can trigger a re-extraction/re-prompting cycle if the result is unsatisfactory. On a 399-message drug-crime dataset with investigator-labeled ground truth (Cohen's kappa 0.74, substantial agreement), individual models ranged from precision 0.794-1.0 and recall 0.782-0.914; a majority-vote combination across the three models achieved precision 0.944, recall 0.835, and the lowest hallucination rate (0.056) of any single model or the ensemble's components.

## Examples

- On real anonymized drug-crime investigation data (142,214 messages from two cases), the majority-vote ensemble of GPT-4o, Gemini 1.5, and Claude 3.5 achieved an F1 score of 0.886, correctly distinguishing messages like "Let's trade drugs for this price" (relevant) from "This music is as addictive as drugs" (not relevant).

## Related Objectives

- `DFO-1003` Review content for relevance

## Related Weaknesses

- [[weaknesses/Keyword-anchored LLM message triage fails to identify crime-related messages that omit the search keyword]]

## References

- [LWCite-1173] Kim et al., 2025, "Digital forensics in law enforcement: A case study of LLM-driven evidence analysis", FSI: Digital Investigation 54, 301939.
