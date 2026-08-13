---
id: DFT-1113
type: technique
name: Generate investigative keyword lists and regular expressions using an LLM
description: Prompt a general-purpose LLM to draft a regular expression for a common evidentiary pattern (e.g. credit card numbers, email addresses, vehicle registration plates) or to generate and expand a keyword list for a specific investigative topic (e.g. terms associated with sexual harassment or drug slang), including associated words, common misspellings, and abbreviations, to support keyword-based search preparation.
objective_ids:
  - DFO-1012
weakness_ids:
  - DFW-1118
aliases:
  - LLM-assisted keyword searching
  - ChatGPT regular expression and keyword list generation
source_refs:
  - DFCite-1110
updated_at: 2026-08-12
status: complete
---

# Generate investigative keyword lists and regular expressions using an LLM

## Summary

Preparing an effective keyword search requires anticipating variants, misspellings, abbreviations, and related terminology that a straight keyword match would miss — work that a general-purpose LLM can accelerate by generating an initial regular expression or keyword list from a short natural-language description of the target pattern or topic, which the investigator then reviews and refines.

## Details

For regular expression generation, GPT-4 produced detailed, explained expressions for common entity types (credit card numbers, UK vehicle registration plates, email addresses) and for one custom-described policy-number format, including explicit disclaimers about known coverage gaps (e.g. not validating the Luhn checksum, not covering all RFC 5322-permitted email formats). For keyword list generation, prompting for a topic (e.g. "cannabis") produced not just direct synonyms but associated words and even relevant emoji; prompting with a specific investigative scenario (e.g. sexual harassment reported via message) produced increasingly targeted term sets across follow-up prompts, including terms a victim might use describing being harassed versus terms an alleged harasser might use. Iterative, scenario-specific prompting materially improved the relevance of generated terms compared to a single generic topic prompt.

## Examples

- Prompted with "If I was conducting a digital investigation into sexual harassment generate a list of keywords that could formally be used", GPT-4 produced formal descriptive terms (e.g. "hostile work environment", "catcalling"); a follow-up prompt asking for terms a victim might use produced a distinct, more colloquial term set (e.g. "creepy behaviour", "felt humiliated").

## Related Objectives

- `DFO-1012` Locate potentially relevant content

## Related Weaknesses

- [[weaknesses/LLM-generated regular expressions can be inconsistent with the model's own provided test examples and omit format edge cases]]

## References

- [DFCite-1110] Scanlon et al., 2023, "ChatGPT for digital forensic investigation: The good, the bad, and the unknown", FSI: Digital Investigation 46.
