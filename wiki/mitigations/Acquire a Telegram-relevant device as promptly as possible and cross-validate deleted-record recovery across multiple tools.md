---
id: LWM-1316
type: mitigation
name: Acquire a Telegram-relevant device as promptly as possible and cross-validate deleted-record recovery across multiple tools
source_refs:
  - LWCite-1354
updated_at: 2026-08-15
status: complete
---

# Acquire a Telegram-relevant device as promptly as possible and cross-validate deleted-record recovery across multiple tools

## Summary

Prioritize prompt acquisition of a device known or suspected to hold relevant Telegram deleted content to minimize the elapsed-time and further-app-interaction factors that degrade recoverability, and run more than one forensic tool against the acquired database/WAL files, since different tools were found to produce diverging results on identical data.

## Addresses

- [[weaknesses/Telegram deleted-message recoverability depends unpredictably on elapsed time, device power state, and app interaction]]

## How To Apply

When Telegram deleted content is relevant to a case, prioritize prompt seizure and acquisition of the device to minimize elapsed time and further app usage, and where feasible acquire the device in as close to its current power/connectivity state as possible rather than allowing it to reboot or reconnect before acquisition, since Telegram's WAL file (which can hold the most recently deleted content) is time- and checkpoint-sensitive. Apply [[techniques/Recover deleted SQLite records]] using more than one current forensic tool against the acquired Telegram database and WAL files, and reconcile any differences in reported results between tools, documenting which tool(s) recovered which specific records so the basis for the reported findings is transparent and reproducible.

## References

- [LWCite-1354] Vasilaras, Dosis, Kotsis, and Rizomiliotis, 2022, "Retrieving deleted records from Telegram", FSI: Digital Investigation 43, 301447.
