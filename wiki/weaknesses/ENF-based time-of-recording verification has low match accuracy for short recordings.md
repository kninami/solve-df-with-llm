---
id: LWW-2014
type: weakness
name: ENF-based time-of-recording verification has low match accuracy for short recordings
description: Even with the enhanced adaptive STFT segmentation scheme, ENF-based time-of-recording verification achieves well under 100% true-match rates for short recordings (as low as ~54-62% for 2-minute clips), because short ENF patterns are more likely to recur at unrelated times, risking an incorrect verification conclusion for shorter query media.
categories:
  - ASTM_MISINT
mitigation_ids:
  - LWM-2014
source_refs:
  - LWCite-2014
updated_at: 2026-08-14
status: partial
---

# ENF-based time-of-recording verification has low match accuracy for short recordings

## Summary

The source paper's own ENF-WHU benchmark results (Tables 1 and 4) show true time-stamp match rates for 2-minute audio clips ranging from about 53-62% across tested STFT segment sizes and ENF extensions, meaning the correct recording time was identified in fewer than two-thirds of short-clip trials even using the improved segmentation scheme, compared to 85-94% for 6- and 10-minute clips. This is an inherent limitation of the underlying ENF signal, not just the estimation method: short-duration ENF fluctuation patterns are more likely to recur, by chance, at other unrelated times, since the supply/demand discrepancies that shape the ENF pattern are less distinctive over short intervals.

## Why It Matters

If an investigator or expert witness treats an ENF-based time-of-recording result for a short (e.g. under 2-6 minute) recording as reliably confirming or refuting a claimed recording time, without accounting for the substantially elevated false-match/false-non-match risk documented for short clips, they risk drawing an incorrect conclusion about when the recording was actually made - a conclusion that could carry significant weight in legal proceedings (e.g. alibi verification) if presented without this caveat.

## Related Mitigations

- [[mitigations/Prefer longer query recordings and report ENF verification confidence relative to clip length]]

## Used By

- [[techniques/Verify a recording's time using electric network frequency correlation]]

## References

- [LWCite-2014] Yalinkilic and Vatansever, 2024 — Tables 1, 4, 5, and 6 report substantially lower true-decision rates for 2-minute clips than for 6- and 10-minute clips across all tested settings, and the paper's own introduction explains that ENF patterns are less distinctive over shorter time intervals.
