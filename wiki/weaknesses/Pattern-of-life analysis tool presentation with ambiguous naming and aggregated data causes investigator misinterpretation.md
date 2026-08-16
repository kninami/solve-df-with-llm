---
id: DFW-2098
type: weakness
name: Pattern-of-life analysis tool presentation with ambiguous naming and aggregated data causes investigator misinterpretation
description: A pattern-of-life analysis tool's choices about how to present extracted activity-level data -- ambiguous column/attribute/category naming, insufficient detail or context around a trace, aggregation that obscures individual events behind a summary value, and inconsistent or confusing timestamp ordering -- can cause an investigator to misinterpret otherwise-correctly-extracted data, independent of any data-extraction defect in the tool itself.
categories:
  - ASTM_MISINT
mitigation_ids:
  - DFM-2099
source_refs:
  - DFCite-2115
updated_at: 2026-08-16
status: complete
---

# Pattern-of-life analysis tool presentation with ambiguous naming and aggregated data causes investigator misinterpretation

## Summary

A controlled mock-murder-scenario experiment comparing two pattern-of-life analysis tools (Cellebrite Physical Analyzer and APOLLO) across six experienced digital forensic investigators found the group using the tool with more detailed, granular, less-aggregated data presentation (APOLLO) made substantially fewer errors than the group using the tool whose presentation aggregated more data into summary values and used more ambiguous naming (Cellebrite) -- despite both tools successfully extracting the data needed to answer the case questions, and despite participants having comparable experience levels. Four specific presentation factors were identified as contributing to misinterpretation errors: misleading naming conventions (ambiguous labels such as "connect/disconnect" interpreted inconsistently by different participants), lack of detail and context (relevant data present but insufficiently explained to interpret correctly), data loss by aggregation (individual events combined into summary values, obscuring when specific activity actually started or ended), and misleading presentation of timestamps (inconsistent ordering or unclear linkage between related timestamps).

## Why It Matters

An investigator's conclusions in a pattern-of-life analysis can be materially wrong even when the underlying tool extracted every relevant record correctly, purely because of how that correctly-extracted data was labeled, aggregated, or ordered for presentation -- a source of error that is easy to overlook because it does not manifest as an obvious data-extraction failure. Because misleading naming conventions specifically risk a labelling-effect bias (a well-documented cognitive-psychology phenomenon where a stimulus's applied label skews subsequent interpretation in a consistent direction), this presentation-driven error risk is not random noise but can produce a systematic, directionally-biased pattern of misinterpretation across investigators using the same tool.

## Related Mitigations

- [[mitigations/Use dual-tool peer verification with a differently-designed tool and manually validate ambiguous or aggregated pattern-of-life data]]

## Used By

- (No technique page derived from this source; this weakness documents a comparative-experiment finding about existing commercial tool presentation, per the reuse-first ingestion policy for conceptual/evaluative papers.)

## References

- [DFCite-2115] Andersen, Sunde, and Porter, 2025, "Tool induced biases? Misleading data presentation as a biasing source in digital forensic analysis", FSI: Digital Investigation 52, 301881.
