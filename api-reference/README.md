---
description: REST API overview and implementation conventions.
icon: code
---

# API Reference

Nuvei's API reference is the canonical technical surface for developers building direct integrations. This demo keeps the reference concise and points to where an OpenAPI-backed reference would live.

{% hint style="info" %}
Production recommendation: import Nuvei's real OpenAPI specifications into GitBook and generate operation pages automatically. This draft uses narrative API pages because the canonical spec was not provided in the Slack request.
{% endhint %}

<table data-view="cards"><thead><tr><th width="48"></th><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody>
<tr><td><i class="fa-key"></i></td><td><strong>Authentication</strong></td><td>Credentials, request signing, and environment handling.</td><td><a href="authentication.md">Authentication</a></td></tr>
<tr><td><i class="fa-arrows-rotate"></i></td><td><strong>Payment lifecycle</strong></td><td>Session, authorization, capture, refund, void, dispute, and webhook states.</td><td><a href="payment-lifecycle.md">Payment lifecycle</a></td></tr>
<tr><td><i class="fa-triangle-exclamation"></i></td><td><strong>Errors</strong></td><td>How to handle declines, validation errors, and retryable failures.</td><td><a href="errors-and-retries.md">Errors</a></td></tr>
</tbody></table>
