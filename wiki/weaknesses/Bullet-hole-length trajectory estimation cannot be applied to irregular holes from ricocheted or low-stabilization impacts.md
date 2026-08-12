---
id: DFW-1075
type: weakness
name: Bullet-hole-length trajectory estimation cannot be applied to irregular holes from ricocheted or low-stabilization impacts
description: The bullet-hole-length-to-incidence-angle correlation the mobile trajectory tool relies on was derived from, and is only valid for, regularly-shaped perforation holes; bullet holes with irregular shapes caused by ricocheted bullets or bullets that were poorly stabilized in flight fall outside the tool's applicable scope and cannot be used with it.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1075
updated_at: 2026-08-10
status: complete
---

# Bullet-hole-length trajectory estimation cannot be applied to irregular holes from ricocheted or low-stabilization impacts

## Summary

The authors state directly that "bullet holes with irregular shapes caused by ricocheted or low stabilized bullets cannot be used with this tool," since the underlying empirical correlation between hole length and incidence angle was established using regular perforation holes from directly-fired, stable bullets on flat sheet metal.

## Why It Matters

A field investigator who applies the tool indiscriminately to any bullet hole on a sheet-metal surface, without first assessing whether the hole shape is regular, risks generating a trajectory estimate that appears numerically precise but is not validly derived for that hole's actual impact conditions — an especially relevant risk at a scene with multiple shots at varied angles, where some holes may be irregular due to ricochet while others are not.

## Related Mitigations

- [[mitigations/Visually screen bullet hole shape for ricochet or low-stabilization irregularity before applying length-based trajectory estimation]]

## Used By

- [[techniques/Estimate bullet trajectory angle from sheet-metal bullet-hole length]]
