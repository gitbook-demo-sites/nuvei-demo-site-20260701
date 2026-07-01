---
description: Hosted checkout path for faster online payment launch.
icon: window-maximize
---

# Payment Page

Payment Page is the right first path for merchants who want a hosted payment experience, a faster implementation, and less payment-field handling in their own frontend.

## Implementation shape

{% stepper %}
{% step %}### Create the payment session
Your backend prepares the transaction, amount, currency, billing details, and return URLs.
{% endstep %}
{% step %}### Redirect or render the hosted experience
The customer completes payment on a Nuvei-managed flow.
{% endstep %}
{% step %}### Handle the result
Listen for return handling and webhook confirmation before fulfilling the order.
{% endstep %}
{% endstepper %}

{% hint style="warning" %}
Always reconcile the final transaction state server-side. Browser redirects can be interrupted.
{% endhint %}
