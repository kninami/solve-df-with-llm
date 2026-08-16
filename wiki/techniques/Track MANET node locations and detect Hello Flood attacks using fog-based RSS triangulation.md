---
id: DFT-2106
type: technique
name: Track MANET node locations and detect Hello Flood attacks using fog-based RSS triangulation
description: Passively locate and monitor the mobility of nodes in a Mobile Ad-hoc Network (MANET) -- a self-configuring, infrastructure-less wireless network with no central server to log evidence from -- by deploying a Fog Computing server with a three-antenna "Cocktail Fork" receiver that sniffs ordinary communication traffic, measures received signal strength (RSS) from each node, and triangulates each node's position via the inverse square law, additionally flagging a node as a likely Hello Flood attacker when its RSS-based triangulation repeatedly fails to converge to a single consistent location.
objective_ids:
  - DFO-1019
  - DFO-1006
weakness_ids:
  - DFW-2112
aliases:
  - Ad-hoc Forensics Fog
  - AFF
source_refs:
  - DFCite-2132
updated_at: 2026-08-16
status: complete
---

# Track MANET node locations and detect Hello Flood attacks using fog-based RSS triangulation

## Summary

MANETs lack the fixed infrastructure (central servers, consistent logging points) that most digital forensic frameworks assume, since every node behaves independently as both host and router with mobility and topology changing continuously; identifying which node is the source of evidence, and maintaining chain of custody for it, is correspondingly difficult. Ad-hoc Forensics Fog (AFF) addresses this without requiring any change to the network's own communication protocols: a dedicated Fog Computing server passively measures the received signal strength of nodes' existing traffic from three known, fixed antenna locations, and uses the physics of radio signal attenuation (the inverse square law) to triangulate each node's approximate position over time, incidentally also providing a detection signal for Hello Flood attacks.

## Details

The AFF system consists of two node types: the Fog Forensics Server (FFS), a central node mounted on a high-capability "Super Node" providing sufficient power, storage, and bandwidth, and an Associate Node (AN), an ordinary GPS-equipped node that cooperates with the FFS to bootstrap distance calibration. The FFS's "Cocktail Fork" receiver hardware component uses three separately-spaced omnidirectional antennas (each a known, fixed distance apart) to receive an ordinary node's radio signal from three different vantage points simultaneously. During an initialization stage, the FFS sends a "Hello Associate" message to the AN, which replies with its GPS-known coordinates; the FFS uses trigonometry (given its own and the AN's known coordinates) to compute its distance to the AN and measures the received signal strength of the AN's reply, establishing a reference relationship between measured signal power and known distance via the inverse-square-law-derived formula d_n² = d_0² × P_0 / P_n. During collection and examination, the Fork's three antennas each independently measure the signal strength of an ordinary node's traffic; applying the same calibrated distance-power relationship to each of the three measurements yields three candidate distances from the node to each antenna, and a Plotter component draws three circles (one per antenna, radius equal to the computed distance, centered at that antenna's known coordinates) whose geometric intersection determines the node's most probable location. Comparing a node's newly computed location against its previously computed location over successive measurement rounds derives its mobility speed and direction. The technique's Hello Flood attack detection follows directly from this same geometry: a node broadcasting inconsistent transmission power (a hallmark of a Hello Flood attacker attempting to appear as a close neighbor to as many nodes as possible) causes the three plotted circles to fail to intersect at a single consistent point across repeated measurements, and the system tracks how often a given node produces this non-convergence, flagging it as increasingly suspect as the failure count rises.

## Examples

- The framework was validated using a network simulator (OMNeT++), where the viability of the AFF approach for locating simulated ordinary nodes and detecting a simulated Hello Flood attack was demonstrated end to end.
- The system's Registry component logs each observation (target node name, timestamp, and the three antenna-specific signal-strength/distance measurements) centrally at the FFS, giving an investigator a persistent, timestamped location and mobility history for network nodes despite MANETs having no native equivalent logging mechanism of their own.

## Related Objectives

- `DFO-1019` Detect anti-forensics and other anomalies
- `DFO-1006` Acquire data

## Related Weaknesses

- [[weaknesses/RSS-based MANET node triangulation assumes idealized free-space signal propagation, degrading accuracy under real-world conditions]]

## References

- [DFCite-2132] Ragheb, Safwat, and Azer, 2025, "Unearthing the hidden path of MANET's nodes with signal strength measurements: Forensics challenges, survey and a novel approach for data collection, preservation and examination", FSI: Digital Investigation 53, 301916.
