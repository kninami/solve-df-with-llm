---
id: LWM-1034
type: mitigation
name: Present flagged messages with surrounding conversational context for human-in-the-loop review
source_refs:
  - LWCite-1024
updated_at: 2026-08-09
status: complete
---

# Present flagged messages with surrounding conversational context for human-in-the-loop review

## Summary

Never treat a single flagged message as conclusive on its own; present it to the human reviewer alongside its surrounding conversational context so an investigator, rather than the classifier, makes the final call on sarcasm, tone, and cross-message meaning that a message-level model cannot reliably capture.

## Addresses

- [[weaknesses/Message-level classification of coercive control markers misses sarcasm and cross-message context]]

## How To Apply

When presenting a triage report's flagged messages for review, include a configurable window of surrounding conversation (preceding and following messages), not just the isolated flagged message, so a human reviewer can quickly check for sarcasm, irony, or context established several messages earlier. Track and report a baseline consistency check (e.g., whether a specific person's messages are consistently sarcastic in tone) to help the investigator discount recurring sarcasm patterns efficiently rather than manually re-evaluating each instance from scratch, and treat the tool's output strictly as a decision-support ranking rather than a diagnostic or evidentiary determination in itself.

## References

- [LWCite-1024] Patel et al., 2026, "A hybrid neural-symbolic approach for the longitudinal profiling of coercive control in digital investigations", FSI: Digital Investigation 56.
