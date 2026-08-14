---
id: DFW-2035
type: weakness
name: Geo-location-based attack attribution misattributes VPN- or proxy-obscured traffic origins
description: A forensic framework's geo-tagging module, which enriches events with IP-based geolocation to support spatial attack-chain context and attribution, inherits the underlying IP-to-location mapping service's accuracy limits, producing a measurable misattribution rate for traffic routed through a VPN or proxy that is otherwise robust for direct connections.
categories:
  - ASTM_INAC_AS
mitigation_ids:
  - DFM-2035
source_refs:
  - DFCite-2035
updated_at: 2026-08-14
status: partial
---

# Geo-location-based attack attribution misattributes VPN- or proxy-obscured traffic origins

## Summary

The source paper's own limitations section states that "the geo-tagging module depends on IP-to-location mapping services, whose accuracy degrades for VPN or proxy-obscured traffic (approximately 4% misattribution rate observed in experiments)." A dedicated sensitivity analysis found detection accuracy degrades by 0.4-2.6 percentage points and chain-reconstruction Step Coverage Rate degrades by 0.8-5.2 points as injected misattribution rises from 4% to 20%, with the framework's authors characterizing the real-world 4% baseline level as tolerable but noting "substantial robustness degradation only occurs above 15% misattribution," a threshold that could plausibly be exceeded by a campaign making deliberate, wholesale use of VPNs.

## Why It Matters

An investigator relying on this framework's geo-tagged event data to attribute an attack's true geographic origin, sequence geographically co-located attack stages, or flag a "high-risk geolocation" source (as illustrated in the paper's own healthcare deployment scenario) risks acting on an incorrect location for any traffic routed through a VPN or proxy - a routine anti-forensic/anonymization practice for sophisticated attackers - without independent confirmation that the reported IP geolocation reflects the attacker's actual origin.

## Related Mitigations

- [[mitigations/Corroborate IP-geolocation-based attack attribution with independent network evidence when VPN or proxy use is suspected]]

## Used By

- [[techniques/Reconstruct and explain cyber-attack chains using causal graph neural networks and federated learning]]

## References

- [DFCite-2035] Manivannan and Amalanathan, 2026 — Section IX "Conclusion" states the geo-tagging accuracy limitation directly, and Section VIII.H reports the misattribution sensitivity analysis (Table 10 and accompanying discussion).
