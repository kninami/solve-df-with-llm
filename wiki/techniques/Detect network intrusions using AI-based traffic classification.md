---
id: DFT-2015
type: technique
name: Detect network intrusions using AI-based traffic classification
description: The process of identifying malicious or anomalous network activity (intrusions, DDoS, botnets, DNS tunneling, and other attacks) by training machine-learning or deep-learning classifiers - signature-based, anomaly-based, or hybrid - on labeled or unsupervised network traffic features drawn from captured packets or flow records.
objective_ids:
  - DFO-1019
weakness_ids:
  - DFW-2015
aliases:
  - AI-based network intrusion detection system (NIDS)
  - AI-based network traffic analysis (NTA)
source_refs:
  - DFCite-2015
updated_at: 2026-08-14
status: partial
---

# Detect network intrusions using AI-based traffic classification

## Summary

Rather than relying solely on manually authored signature libraries, an investigator or defensive system trains an AI model - ranging from classical ML (SVM, decision tree, random forest, k-NN, naive Bayes) through deep learning (1D-CNN, LSTM, RNN, autoencoders) to ensemble/hybrid combinations - on network traffic captured either proactively ("catch it as you can," continuous monitoring) or reactively ("stop, look, and listen," post-detection capture), using features extracted from packet captures (via tools like Wireshark/tcpdump) or flow records (via tools like CICFlowMeter/Argus), to automatically flag intrusions, distributed denial-of-service attacks, botnets, covert DNS tunneling, and other network-based threats across contexts including general enterprise networks, IoT/IIoT networks, cloud environments, and smart-grid infrastructure.

## Details

DFCite-2015 surveys this space across multiple sub-domains: network traffic analysis (e.g. cost-sensitive SVM for imbalanced traffic classification, CNN-LSTM hybrids for mesh-network traffic prediction), intrusion detection systems (e.g. SVM/MLP-based binary and multi-class classifiers on KDD99/NSL-KDD, data-optimized IDS using Isolation Forest sampling with genetic-algorithm feature selection, deep-stacking ensembles combining DT/k-NN/DNN/RF, federated-learning NIDS to address centralized-data privacy concerns), IoT/IIoT-specific detection (semi-supervised Deep-ID using LSTM+CNN with a traffic-attention layer; Deep-IFS combining local gated recurrent units with multi-head attention), DNS tunneling detection (rule-based signature/threshold detection versus model-based ML/DL on features like query length, character distribution, and randomness; 1D-CNN operating directly on raw DNS-packet bytes to avoid manual feature engineering), and smart-grid intrusion detection (graph-neuron lightweight models, multi-agent one-class classifiers for AGC/PMC attack detection, privacy-preserving two-level architectures combining blockchain proof-of-work with variational-autoencoder anomaly detection). Across sub-domains, the common technique pattern is: collect/label traffic, extract or automatically learn discriminative features, train a classifier (often addressing severe class imbalance via resampling, cost-sensitive learning, or synthetic oversampling), and evaluate against benchmark datasets (CICIDS-2017/2018, UNSW-NB15, Bot-IoT, TON_IoT, CIDDS-001, KDD99/NSL-KDD).

## Examples

- DFCite-2015's Table 1 catalog of public network-forensics datasets spanning network-traffic, IoT-traffic, DNS, vehicular (Car-Hacking, VeReMi), VPN, and smart-grid domains, used across the surveyed AI-based detection studies.

## Related Objectives

- `DFO-1019` Detect anti-forensics and other anomalies

## Related Weaknesses

- [[weaknesses/AI-based network intrusion detection suffers high false-positive rates from imbalanced, unverified-representativeness training datasets]]

## References

- [DFCite-2015] Rizvi et al., "Application of artificial intelligence to network forensics: Survey, challenges and future directions", IEEE Access, 2022 — source of the AI-based network forensics technique survey summarized above.
