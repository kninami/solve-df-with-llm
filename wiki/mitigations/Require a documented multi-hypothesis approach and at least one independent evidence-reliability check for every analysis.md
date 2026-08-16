---
id: DFM-2081
type: mitigation
name: Require a documented multi-hypothesis approach and at least one independent evidence-reliability check for every analysis
source_refs:
  - DFCite-2093
updated_at: 2026-08-16
status: complete
---

# Require a documented multi-hypothesis approach and at least one independent evidence-reliability check for every analysis

## Summary

Make it a mandatory, documented step of every digital forensic analysis to write down more than one hypothesis about what may have happened -- explicitly including an innocence hypothesis -- before drawing conclusions, and to apply and record at least one independent evidence-reliability check (e.g. metadata examination, hash calculation, cross-checking findings, or [[mitigations/Validate digital forensic tool output against known ground truth rather than relying on dual-tool agreement alone]] rather than dual-tool verification alone), rather than leaving objectivity and reliability safeguards to individual examiners' informal judgment.

## Addresses

- [[weaknesses/Examiners frequently apply no documented technique to safeguard objectivity or evidence reliability during analysis]]

## How To Apply

Build a written-hypothesis requirement into the standard case-report template: before or early in analysis, the examiner records two or more competing explanations for the evidence, including at least one hypothesis consistent with the suspect's innocence, and revisits the list as new evidence emerges rather than settling on a single narrative from the outset. Separately, require and document at least one reliability-checking technique per analysis (metadata examination, hash calculation, cross-checking findings against another data source, or timeline analysis), and where time constraints are cited as a reason for skipping such checks, treat that as a resourcing or scheduling problem to be addressed at an organizational level rather than an acceptable justification for omitting the check. Periodically audit case files for the presence of both elements rather than assuming their use.

## References

- [DFCite-2093] Sunde, Nina, 2022, "Strategies for safeguarding examiner objectivity and evidence reliability during digital forensic investigations", FSI: Digital Investigation 40, 301317.
