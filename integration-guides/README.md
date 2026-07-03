---
description: Implementation paths for launching Nuvei payment experiences across methods, markets, and business models.
icon: rocket
layout:
  width: default
  tableOfContents:
    visible: true
---

# Integration Guides

Start with the checkout pattern that matches your product, then move into payment methods, regional readiness, risk controls, testing, and launch operations.

{% hint style="success" %}
Strong demo story: Nuvei does not need one flat developer portal. It needs guided paths for different merchant maturity levels: hosted checkout for speed, SDKs for branded control, direct API for platform depth, and plugins for commerce teams that need packaged adoption.
{% endhint %}

<table data-view="cards"><thead><tr><th width="48"></th><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody>
<tr><td><i class="fa-window-maximize"></i></td><td><strong>Payment Page</strong></td><td>Hosted checkout for faster launch, lighter PCI scope, and a familiar conversion path.</td><td><a href="online-payments/payment-page.md">Payment Page</a></td></tr>
<tr><td><i class="fa-code"></i></td><td><strong>Web SDK</strong></td><td>Embed payments in a branded checkout while keeping sensitive payment collection controlled.</td><td><a href="online-payments/web-sdk.md">Web SDK</a></td></tr>
<tr><td><i class="fa-server"></i></td><td><strong>Server-to-server</strong></td><td>Direct API integration for platforms, marketplaces, subscriptions, and merchants that need backend orchestration.</td><td><a href="online-payments/server-to-server.md">Server-to-server</a></td></tr>
<tr><td><i class="fa-puzzle-piece"></i></td><td><strong>Commerce plugins</strong></td><td>Packaged integrations for commerce platforms where speed and repeatability matter most.</td><td><a href="plugins/commerce-plugins.md">Plugins</a></td></tr>
</tbody></table>

## Launch sequence

{% stepper %}
{% step %}
### Choose the commerce model

Identify whether the merchant needs a hosted checkout, embedded checkout, direct API integration, plugin, payout flow, or multi-method global rollout.
{% endstep %}

{% step %}
### Map methods and markets

Document cards, APMs, wallets, bank transfers, local acquiring, currency support, and regional controls before implementation starts.
{% endstep %}

{% step %}
### Build and validate the flow

Connect authentication, payment creation, customer redirects, webhook handling, retries, idempotency, and test cases.
{% endstep %}

{% step %}
### Prepare operations

Route finance, support, and risk teams to Control Panel, reconciliation, reporting, chargebacks, and release notes before go-live.
{% endstep %}
{% endstepper %}
