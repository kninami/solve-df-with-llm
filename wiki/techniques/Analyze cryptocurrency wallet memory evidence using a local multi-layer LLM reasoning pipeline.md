---
id: LWT-2006
type: technique
name: Analyze cryptocurrency wallet memory evidence using a local multi-layer LLM reasoning pipeline
description: The process of reconstructing cryptocurrency wallet activity (identity, transactions, smart-contract interactions, asset state, network events) from keyword/regex-extracted memory-forensic evidence using a fully local, offline large language model pipeline with progressive baseline, supervisor-review, and retrieval-augmented decision layers to suppress hallucination.
objective_ids:
  - DFO-1001
weakness_ids:
  - LWW-2006
aliases:
  - Tri-Layer RAG-Decider architecture
  - Local hierarchical LLM crypto-wallet memory forensics
source_refs:
  - LWCite-2006
updated_at: 2026-08-14
status: partial
---

# Analyze cryptocurrency wallet memory evidence using a local multi-layer LLM reasoning pipeline

## Summary

Rather than uploading sensitive case memory dumps to a cloud LLM (a confidentiality/data-protection risk) or manually correlating fragmented, noisy memory strings by hand, an investigator dumps volatile memory (e.g. via FTK Imager), extracts wallet-relevant identity/transaction/contract/asset/network fields via keyword and regex search, normalizes them into a structured CSV, and reasons over that CSV using a locally hosted LLM organized into three progressively more rigorous layers: a baseline analyst layer restricted strictly to the provided evidence, a supervisor layer that reviews the baseline's output for hallucinations/inconsistencies and proposes corrections, and a decider layer that integrates supervisor-corrected output with retrieval-augmented domain knowledge (blockchain/wallet-standard reference documents) to produce a final, evidence-grounded, traceable answer.

## Details

LWCite-2006 implements this with LangChain orchestrating a locally hosted LLaMA 3.1-8B model (via Ollama, Q4_K_M quantization, CPU-only) so that no forensic data leaves the investigator's machine. The evidence-processing stage uses WinHex string extraction plus a 120+-keyword, 18-regex, 25-JSON-RPC-mapping rule library (covering identity/wallet, transaction activity, smart-contract interaction, asset/token state, and network/security-event dimensions) to turn a raw memory image into a normalized CSV. The Tri-Layer RAG-Decider architecture retrieves supporting passages from a FAISS vector database of blockchain/wallet reference documents when the decider layer needs domain knowledge beyond the case evidence itself. On a 100-question benchmark, the Tri-Layer system scored an 8.9% higher human-evaluation total than a Single-Layer baseline and came within 0.3% of, and exceeded on reasoning coherence, a commercial cloud model (ChatGPT-4o), while completing full analysis in 3.0-3.5 hours on a standard 32GB, GPU-less investigative laptop.

## Examples

- LWCite-2006's 100-question crypto-wallet forensic benchmark (transaction behavior, wallet/contract operations, gas/transaction anomalies, asset/chain usage, device-record field inference) scored by both a domain expert (six dimensions) and ten automated string/semantic/content-overlap metrics against ChatGPT-4o as reference.

## Related Objectives

- `DFO-1001` Reconstruct events

## Related Weaknesses

- [[weaknesses/A local multi-layer LLM crypto-wallet forensic pipeline has only been validated on simulated single-wallet scenarios]]

## References

- [LWCite-2006] Kao et al., "A local hierarchical LLM framework for privacy-preserving memory forensics of cryptocurrency wallets", IEEE Access, 2026 — source of the Tri-Layer RAG-Decider architecture, evidence-extraction rule library, and dual-track evaluation results.
