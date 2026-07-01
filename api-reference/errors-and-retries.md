---
description: Handle validation, decline, network, and retry scenarios.
icon: triangle-exclamation
---

# Errors and Retries

Payment errors are not all the same. Docs should distinguish merchant-fixable configuration issues, customer-actionable declines, retryable network failures, and final failures.

<table><thead><tr><th>Error type</th><th>Merchant action</th><th>Customer message</th></tr></thead><tbody>
<tr><td>Validation</td><td>Fix request payload or checkout mapping.</td><td>Ask for corrected information only if appropriate.</td></tr>
<tr><td>Issuer decline</td><td>Log reason code and offer alternate method.</td><td>Ask customer to try another method.</td></tr>
<tr><td>Network timeout</td><td>Check idempotency and payment state before retrying.</td><td>Show pending or retry-safe state.</td></tr>
</tbody></table>
