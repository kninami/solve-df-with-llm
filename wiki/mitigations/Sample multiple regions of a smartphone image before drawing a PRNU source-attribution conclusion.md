---
id: LWM-1314
type: mitigation
name: Sample multiple regions of a smartphone image before drawing a PRNU source-attribution conclusion
source_refs:
  - LWCite-1353
updated_at: 2026-08-15
status: complete
---

# Sample multiple regions of a smartphone image before drawing a PRNU source-attribution conclusion

## Summary

Extract PRNU features from multiple spatial regions of the examined smartphone image, rather than a single arbitrarily-chosen patch, and combine the resulting multi-region evidence before drawing a source-attribution conclusion, so that a low-signal region does not drive the entire result.

## Addresses

- [[weaknesses/PRNU reliability varies unpredictably across regions of a single smartphone image]]

## How To Apply

Apply [[techniques/Identify a smartphone photo's source camera using multi-patch PRNU sampling]] rather than extracting PRNU from a single fixed region or the whole image as one unit. Where the multi-patch machine-learning pipeline is not available, at minimum manually extract and compare PRNU correlation from several distinct regions of the image (avoiding smooth, over-exposed, or under-exposed areas where possible) and report the range of per-region results rather than a single-region figure, flagging cases where regional results disagree substantially as warranting caution in the stated confidence of the source-attribution conclusion.

## References

- [LWCite-1353] Liang, Gao, and Xu, 2025, "Research on smartphone image source identification based on PRNU features collected multivariate sampling strategy", FSI: Digital Investigation 54, 301991.
