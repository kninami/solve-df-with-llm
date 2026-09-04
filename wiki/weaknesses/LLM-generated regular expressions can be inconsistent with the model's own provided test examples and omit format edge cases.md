---
id: LWW-1118
type: weakness
name: LLM-generated regular expressions can be inconsistent with the model's own provided test examples and omit format edge cases
description: An LLM-generated regular expression can fail to match the very test examples the same model supplied to demonstrate it, and can silently omit valid format variants (such as whitespace-separated digit groups or lowercase top-level domains) that a real-world target string would use, producing false negatives in a keyword or pattern search.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - LWM-1118
source_refs:
  - LWCite-1110
updated_at: 2026-08-12
status: complete
---

# LLM-generated regular expressions can be inconsistent with the model's own provided test examples and omit format edge cases

## Summary

The paper documents two concrete instances. For a credit-card-number regex, when asked for example strings that could be used for testing, "despite the claims 'These numbers should match the regular expression provided in the previous answer', did not match the generated regular expression provided since they contained whitespace" between digit groups. For an email-address regex, the model described it as "a simple regular expression for matching most email addresses" but the expression "fails on simple tests such as 'test@example.com' as it only specified the upper case character set for the top-level domain," meaning it would not have matched a genuine, correctly formatted lowercase email address.

## Why It Matters

An investigator who deploys an LLM-generated regular expression in a real keyword search without independently testing it against representative real-world format variants risks silently missing relevant evidence (a false negative) that a correctly written expression would have matched, with no indication from the search process itself that matches were being missed.

## Related Mitigations

- [[mitigations/Validate LLM-generated regular expressions against representative test cases before deploying them in an investigation]]

## Used By

- [[techniques/Generate investigative keyword lists and regular expressions using an LLM]]

## References

- [LWCite-1110] Scanlon et al., 2023, "ChatGPT for digital forensic investigation: The good, the bad, and the unknown", FSI: Digital Investigation 46.
