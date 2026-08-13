---
id: DFM-1118
type: mitigation
name: Validate LLM-generated regular expressions against representative test cases before deploying them in an investigation
source_refs:
  - DFCite-1110
updated_at: 2026-08-12
status: complete
---

# Validate LLM-generated regular expressions against representative test cases before deploying them in an investigation

## Summary

Before using an LLM-generated regular expression in an actual search, independently construct a set of representative positive and negative test strings — including plausible real-world format variants such as whitespace, mixed case, and locale differences — and confirm the expression matches and excludes them correctly, rather than trusting the model's own claims or provided examples.

## Addresses

- [[weaknesses/LLM-generated regular expressions can be inconsistent with the model's own provided test examples and omit format edge cases]]

## How To Apply

Build a small independent test set covering the target pattern's known real-world variants (e.g. digit groupings with and without separators, mixed-case domains, alternate regional formats) and run the generated regular expression against it directly, rather than relying on the LLM's own self-reported test cases or assurances that it is correct. Where the expression fails on any representative case, iterate with the model or hand-correct the pattern, and document any known, accepted coverage gaps (such as checksum validation the expression does not perform) before deploying it in a live search.

## References

- [DFCite-1110] Scanlon et al., 2023, "ChatGPT for digital forensic investigation: The good, the bad, and the unknown", FSI: Digital Investigation 46.
