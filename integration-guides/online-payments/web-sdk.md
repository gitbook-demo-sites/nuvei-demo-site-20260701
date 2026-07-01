---
description: Build a branded checkout with Nuvei payment fields.
icon: code
---

# Web SDK

Web SDK gives developers more control over checkout design while keeping payment collection connected to Nuvei's platform.

```javascript
// Illustrative demo snippet only.
const payment = await nuvei.createPayment({
  amount: 10000,
  currency: "USD",
  customer: { email: "customer@example.com" }
});
```

## Good fit

* SaaS or marketplace checkout with strong brand requirements.
* Merchants who need wallet buttons and card fields inside their own flow.
* Teams that want to test UX variants without changing backend payment semantics.
