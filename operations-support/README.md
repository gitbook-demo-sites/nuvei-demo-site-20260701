---
description: Operational documentation for managing Nuvei payments, risk, reporting, finance, and support after launch.
icon: chart-line
---

# Operations & Support

Payment docs do not end at integration. Merchant operators, finance teams, risk teams, partner teams, and support teams need a reliable place to understand dashboards, reporting, reconciliation, chargebacks, transaction exceptions, and release changes.

<table data-view="cards"><thead><tr><th width="48"></th><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody>
<tr><td><i class="fa-gauge-high"></i></td><td><strong>Control Panel</strong></td><td>Daily workflows for transaction lookup, merchant configuration, reporting, and exception handling.</td><td><a href="control-panel.md">Control Panel</a></td></tr>
<tr><td><i class="fa-shield-halved"></i></td><td><strong>Risk and security</strong></td><td>3DS, fraud controls, chargebacks, credentials, PCI-sensitive guidance, and escalation routing.</td><td><a href="risk-and-security.md">Risk and security</a></td></tr>
<tr><td><i class="fa-scale-balanced"></i></td><td><strong>Reconciliation</strong></td><td>Settlement, reporting, refunds, disputes, balance movement, and finance workflows.</td><td><a href="reconciliation-and-reporting.md">Reconciliation</a></td></tr>
<tr><td><i class="fa-life-ring"></i></td><td><strong>Support playbooks</strong></td><td>Merchant-facing troubleshooting for declined payments, missing webhooks, settlement questions, and go-live blockers.</td><td><a href="support-playbooks.md">Support playbooks</a></td></tr>
</tbody></table>

## Operational ownership model

| Area | Primary reader | What they need from docs |
| --- | --- | --- |
| Transaction monitoring | Support and operations | Searchable transaction states, common exceptions, and escalation steps |
| Risk controls | Risk and compliance | 3DS, fraud rules, chargeback handling, and PCI-sensitive boundaries |
| Settlement and reporting | Finance | Reports, reconciliation timing, refunds, disputes, and payout status |
| Partner enablement | Partner teams | Repeatable onboarding steps, plugin configuration, and launch validation |

{% hint style="success" %}
GitBook angle: Nuvei can keep operational knowledge close to the developer implementation path, so post-launch questions do not fragment across support PDFs, internal wikis, and API-only docs.
{% endhint %}
