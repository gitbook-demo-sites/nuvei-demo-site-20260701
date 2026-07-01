---
description: Backend-controlled payment flow for advanced integrations.
icon: server
---

# Server-to-server

Server-to-server integrations put the payment lifecycle under backend control. They are best for merchants with mature engineering teams, custom orchestration, and strong operational requirements.

```mermaid
sequenceDiagram
  participant Customer
  participant Merchant
  participant Nuvei
  Customer->>Merchant: Submit checkout
  Merchant->>Nuvei: Create session or payment
  Nuvei-->>Merchant: Return payment response
  Nuvei-->>Merchant: Send webhook update
  Merchant-->>Customer: Confirm order state
```

See the [API Reference](https://app.gitbook.com/s/afWAheAibYE8eCe5yB9X/) for request conventions, authentication, errors, and webhooks.
