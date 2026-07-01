---
description: Understand payment states from creation through settlement and post-payment actions.
icon: arrows-rotate
---

# Payment Lifecycle

```mermaid
stateDiagram-v2
  [*] --> Created
  Created --> Authorized
  Created --> Declined
  Authorized --> Captured
  Authorized --> Voided
  Captured --> Refunded
  Captured --> Disputed
  Declined --> [*]
  Voided --> [*]
  Refunded --> [*]
  Disputed --> [*]
```

## Implementation rule

Treat webhooks and server-side status checks as authoritative. Frontend states improve UX, but they should not be the only signal used for fulfillment or support.
