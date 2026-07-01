---
description: How Nuvei could move API docs from hand-authored pages to OpenAPI-backed GitBook reference.
icon: diagram-project
---

# OpenAPI Migration Path

GitBook can generate API operation pages from an OpenAPI specification. For Nuvei, that would reduce drift across REST versions, dashboard APIs, payment-method APIs, and partner tools.

## Proposed migration sequence

1. Inventory available OpenAPI or Swagger files.
2. Normalize tags around reader jobs: Payments, Customers, Webhooks, Reporting, Risk, and Settlement.
3. Upload specs to GitBook and generate operation pages.
4. Keep narrative pages for authentication, lifecycle, testing, and migration notes.
5. Add redirects from legacy API docs paths.
