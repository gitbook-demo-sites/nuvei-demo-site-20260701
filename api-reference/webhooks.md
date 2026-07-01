---
description: Webhook delivery, verification, retries, and operational handling.
icon: webhook
---

# Webhooks

Webhooks connect Nuvei's payment state to the merchant's order, fulfillment, finance, and support systems.

{% stepper %}
{% step %}### Receive the event
Terminate TLS, parse the event, and capture raw delivery metadata for diagnostics.
{% endstep %}
{% step %}### Verify authenticity
Validate the event using Nuvei's recommended verification method before trusting the payload.
{% endstep %}
{% step %}### Process idempotently
Use event IDs and payment IDs to avoid duplicate fulfillment.
{% endstep %}
{% step %}### Reconcile
Compare webhook state with Control Panel and backend order state.
{% endstep %}
{% endstepper %}
