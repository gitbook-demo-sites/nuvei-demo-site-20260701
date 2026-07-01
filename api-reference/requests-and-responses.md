---
description: Request conventions, response handling, and idempotency expectations.
icon: file-code
---

# Requests and Responses

Well-structured API docs should give every endpoint the same predictable pattern:

* What the endpoint does.
* Required credentials and environment.
* Required and optional fields.
* Example request.
* Example success response.
* Example failure response.
* Webhooks or downstream state changes caused by the call.

```json
{
  "amount": 10000,
  "currency": "USD",
  "billingAddress": {
    "country": "US"
  }
}
```
