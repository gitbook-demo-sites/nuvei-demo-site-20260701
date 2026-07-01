---
description: Validate a Nuvei integration before switching to live traffic.
icon: list-check
---

# Testing and Go-live Checklist

* Confirm merchant credentials and environment URLs.
* Run successful, declined, pending, refunded, and disputed payment scenarios.
* Verify 3DS and exemption behavior for target markets.
* Confirm webhooks are idempotent and signed or otherwise verified.
* Reconcile dashboard status with backend order state.
* Prepare support macros for payment failures and pending transactions.
