---
description: Match the right Nuvei integration path to your checkout, PCI, and control needs.
icon: route
---

# Choose an Integration Path

{% tabs %}
{% tab title="Fastest launch" %}
Use **Payment Page** when the priority is speed, a hosted checkout page, and reduced frontend complexity.
{% endtab %}
{% tab title="Branded checkout" %}
Use **Web SDK** when the merchant wants a branded checkout but still wants Nuvei to handle sensitive payment fields.
{% endtab %}
{% tab title="Full control" %}
Use **Server-to-server** when payment orchestration happens in the backend and the merchant can support a deeper integration.
{% endtab %}
{% tab title="Commerce platform" %}
Use **Plugins** when the merchant is already on Magento, Shopify, SAP, or another supported platform.
{% endtab %}
{% endtabs %}

```mermaid
flowchart TD
  Start[What checkout control do you need?]
  Start --> Hosted[Hosted checkout]
  Start --> Embedded[Embedded checkout]
  Start --> Backend[Backend-driven API]
  Start --> Platform[Commerce platform]
  Hosted --> PaymentPage[Payment Page]
  Embedded --> WebSDK[Web SDK]
  Backend --> S2S[Server-to-server]
  Platform --> Plugins[Nuvei plugin]
```
