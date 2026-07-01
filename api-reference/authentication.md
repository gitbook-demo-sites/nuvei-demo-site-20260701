---
description: Merchant credentials and request authentication.
icon: key
---

# Authentication

Nuvei's public docs describe merchant credentials such as `merchantId`, `merchantSiteId`, and `merchantSecretKey`. A production GitBook page should pair that explanation with exact environment setup, rotation policy, and copy-paste examples.

{% tabs %}
{% tab title="Sandbox" %}
Use sandbox credentials for integration testing, simulated payment outcomes, and webhook validation.
{% endtab %}
{% tab title="Production" %}
Use production credentials only after Nuvei has enabled the merchant account and operational checks are complete.
{% endtab %}
{% endtabs %}

{% hint style="danger" %}
Never expose secret keys in frontend code, browser logs, or public repositories.
{% endhint %}
