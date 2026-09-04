---
id: LWT-2035
type: technique
name: Reconstruct and explain cyber-attack chains using causal graph neural networks and federated learning
description: The process of detecting an attack, reconstructing its multi-stage progression as a causal graph, and generating a human-interpretable explanation of the model's reasoning, by fusing a Bayesian-network probabilistic attack-chain model with a Temporal Graph Neural Network, applying SHAP/LIME explainability to flagged events, and training collaboratively across institutions via privacy-preserving federated learning.
objective_ids:
  - DFO-1019
weakness_ids:
  - LWW-2035
aliases:
  - GeoForensic-AI
  - Bayesian Network - Temporal Graph Neural Network (BN-TGNN) fusion
source_refs:
  - LWCite-2035
updated_at: 2026-08-14
status: partial
---

# Reconstruct and explain cyber-attack chains using causal graph neural networks and federated learning

## Summary

Traditional forensic detection systems face three compounding problems: monolithic architectures that do not scale to modern IoT/cloud data volumes, opaque deep-learning models that cannot justify their flagged decisions to an investigator, and an inability to pool multi-institution training data without violating data-privacy regulation. An investigator or SOC deploys a layered pipeline instead: a causal-graph attack-chain reconstruction stage (fusing a Bayesian network's probabilistic ordering with a Temporal Graph Neural Network's learned temporal embeddings) identifies the most likely sequence of attacker actions from initial access through impact; an explainability layer (SHAP/LIME) attributes each flagged event to the specific features that drove the model's decision; a transformer-based (DistilBERT) attribution engine maps the reconstructed chain onto MITRE ATT&CK tactics, techniques, and procedures; and a federated-learning layer (FedAvg/DP-FedProx with differential privacy) lets multiple institutions (e.g. hospitals, banks) improve a shared detection model collaboratively without centralizing their raw logs.

## Details

LWCite-2035's seven layers are: Data Layer (trace collection with geo-location tagging); Integrity Layer (SHA-256/Bloom-filter snapshotting for tamper-evident log integrity, supporting chain-of-custody); Reasoning Layer (the causal-graph event-graph builder plus an RNN/Autoencoder-based adversarial tamper detector flagging timestamp manipulation, log injection, and log replay); Explainability Layer (SHAP/LIME); Attribution Layer (DistilBERT TTP classification against MITRE ATT&CK); Privacy Layer (federated forensic intelligence); and Output Layer (forensic report generation with event timelines, attack-path visualization, and SIEM integration). The Bayesian network learns a directed acyclic graph over event nodes via hill-climbing with Bayesian Information Criterion scoring, producing a maximum-a-posteriori attack chain that supplies a soft-label temporal-ordering prior for the TGNN, whose own learned path score is then combined with the BN prior to select the final reconstructed chain - reported as outperforming either component alone on attack-chain reconstruction quality (Path F1 88.2% fused vs. 74.2%/81.3% for BN-only/TGNN-only). Geo-location enrichment (IP geolocation, GPS) is incorporated as an additional 20-dimensional feature contributing measurably to both detection accuracy and chain-reconstruction quality, particularly for sequencing geographically co-located attack stages.

## Examples

- LWCite-2035's simulated healthcare deployment scenario: a ransomware intrusion across a three-hospital federated network is detected and its seven-stage attack chain (Spear Phishing -> Initial Access -> Lateral Movement -> Privilege Escalation -> Credential Dumping -> C2 Communication -> File Encryption, mapped to MITRE ATT&CK tactics T1566/T1021/T1486) is reconstructed and reported in 4.8 minutes total, with a 2.4-second per-event detection latency, while federated learning ensures no raw patient data leaves any individual hospital site.

## Related Objectives

- `DFO-1019` Detect anti-forensics and other anomalies

## Related Weaknesses

- [[weaknesses/Geo-location-based attack attribution misattributes VPN- or proxy-obscured traffic origins]]

## References

- [LWCite-2035] Manivannan and Amalanathan, "GeoForensic-AI: A lightweight and explainable forensic AI framework for modern digital ecosystems", IEEE Access, 2026 — source of the seven-layer architecture, BN-TGNN causal-graph fusion methodology, and healthcare deployment scenario summarized above.
