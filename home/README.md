---
description: "Developer and merchant documentation for Nuvei's global payment infrastructure."
icon: house
cover: "https://raw.githubusercontent.com/gitbook-demo-sites/nuvei-demo-site-20260701/main/assets/nuvei-minimal-banner.png"
coverY: 0
layout:
  width: wide
  cover:
    visible: true
    size: hero
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: false
  outline:
    visible: false
  pagination:
    visible: true
---

# Nuvei Documentation Hub

The infrastructure for every payment, everywhere.

This first-draft demo reorganizes Nuvei's public documentation into a GitBook experience that is easier to scan, search, review, and adapt by audience. It keeps the familiar pillars from the current docs portal, then adds clearer developer journeys, API patterns, operational guidance, and a visible release surface.

{% hint style="info" %}
Demo assumption: this is a sales-facing first draft, not a full migration. The content mirrors public themes from Nuvei's docs and website, with representative examples that should be replaced by canonical Nuvei source content before production use.
{% endhint %}

## Choose your path

<table data-view="cards"><thead><tr><th width="48"></th><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody>
<tr><td><i class="fa-rocket"></i></td><td><strong>Start integrating</strong></td><td>Pick Payment Page, Web SDK, Simply Connect, server-to-server, or plugins.</td><td><a href="https://app.gitbook.com/s/XeLFuyAuy7wt4ZGIWbb5/">Start integrating</a></td></tr>
<tr><td><i class="fa-code"></i></td><td><strong>Build against the API</strong></td><td>Review authentication, payment lifecycle, request patterns, errors, and webhooks.</td><td><a href="https://app.gitbook.com/s/afWAheAibYE8eCe5yB9X/">Build against the API</a></td></tr>
<tr><td><i class="fa-chart-line"></i></td><td><strong>Run payment operations</strong></td><td>Use Control Panel, reporting, risk, reconciliation, and finance workflows.</td><td><a href="https://app.gitbook.com/s/rUdUhVNVx8fe3XpFqEmR/">Run payment operations</a></td></tr>
<tr><td><i class="fa-globe"></i></td><td><strong>Go local everywhere</strong></td><td>Map regions, payment methods, APMs, and market readiness in one place.</td><td><a href="market-map.md">Go local everywhere</a></td></tr>
</tbody></table>

## Current docs, cleaner shape

The existing Nuvei docs hub presents Online Payments, APMs, Plugins, Partner Tools, Control Panel, and Security as major entry points. This demo keeps those categories but separates the reader jobs:

{% columns %}
{% column %}
**Developers** get a guided path from checkout choice to API implementation.

**Operations teams** get dashboard, reporting, fraud, finance, and reconciliation pages.
{% endcolumn %}
{% column %}
**Partners and merchants** get payment-method, plugin, market, and support readiness pages.

**Editors** get GitBook review flows, AI search, and page feedback.
{% endcolumn %}
{% endcolumns %}

## What GitBook adds

* A single branded hub for docs, API guidance, support workflows, and release notes.
* AI answers over all spaces so merchants can ask implementation and operations questions naturally.
* Git-backed review workflows for technical writers, product, compliance, and regional teams.
* Share-link staging so reps and stakeholders can review a draft before publishing broadly.
