from pathlib import Path
from textwrap import dedent

ROOT = Path(__file__).resolve().parent

SPACES = {
    "home": {
        "title": "Home",
        "description": "A branded front door for Nuvei's developer and merchant documentation.",
    },
    "integration-guides": {
        "title": "Integration Guides",
        "description": "Narrative implementation paths for online payments, APMs, plugins, and checkout.",
    },
    "api-reference": {
        "title": "API Reference",
        "description": "REST API overview, authentication, payments lifecycle, errors, and webhooks.",
    },
    "operations-support": {
        "title": "Operations & Support",
        "description": "Control Panel, reporting, risk, reconciliation, partner workflows, and release notes.",
    },
}


def write(path: str, content: str) -> None:
    full = ROOT / path
    full.parent.mkdir(parents=True, exist_ok=True)
    full.write_text(dedent(content).strip() + "\n", encoding="utf-8")


def card(icon: str, title: str, desc: str, href: str) -> str:
    return f'<tr><td><i class="fa-{icon}"></i></td><td><strong>{title}</strong></td><td>{desc}</td><td><a href="{href}">{title}</a></td></tr>'


def yaml(space: str) -> None:
    write(
        f"{space}/.gitbook.yaml",
        """
        root: ./
        structure:
          readme: README.md
          summary: SUMMARY.md
        """,
    )


def summary(space: str, lines: list[str]) -> None:
    write(space + "/SUMMARY.md", "# Table of contents\n\n" + "\n".join(lines))


for name in SPACES:
    yaml(name)

write(
    "README.md",
    """
    # Nuvei demo site

    First-draft GitBook demo content for Nuvei. Each top-level folder is a GitBook space.
    The published demo is built from public Nuvei documentation and marketing pages.
    """,
)
write(".gitignore", ".DS_Store\nThumbs.db\n*.swp\n*.swo\n.idea/\n.vscode/\n")

write(
    "home/README.md",
    """
    ---
    description: "Developer and merchant documentation for Nuvei's global payment infrastructure."
    icon: house
    cover: "https://raw.githubusercontent.com/gitbook-demo-sites/nuvei-demo-site-20260701/main/assets/nuvei-minimal-banner.png?v=07bc08e"
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
    """ + "\n".join(
        [
            card("rocket", "Start integrating", "Pick Payment Page, Web SDK, Simply Connect, server-to-server, or plugins.", "https://app.gitbook.com/s/XSPACE_GUIDES/"),
            card("code", "Build against the API", "Review authentication, payment lifecycle, request patterns, errors, and webhooks.", "https://app.gitbook.com/s/XSPACE_API/"),
            card("chart-line", "Run payment operations", "Use Control Panel, reporting, risk, reconciliation, and finance workflows.", "https://app.gitbook.com/s/XSPACE_OPS/"),
            card("globe", "Go local everywhere", "Map regions, payment methods, APMs, and market readiness in one place.", "market-map.md"),
        ]
    ) + """
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
    """,
)

summary(
    "home",
    [
        "* [Home](README.md)",
        "* [Market and method map](market-map.md)",
        "* [Editorial workflow](editorial-workflow.md)",
        "* [Source notes](source-notes.md)",
    ],
)
write(
    "home/market-map.md",
    """
    ---
    description: Organize local payment methods, markets, and implementation readiness.
    icon: globe
    ---

    # Market and Method Map

    Nuvei's value proposition depends on breadth: global acquiring, local payment methods, APMs, real-time rails, card issuing, payout options, and fraud controls. A strong docs experience should make that breadth navigable without sending each merchant into a long page tree.

    <table data-view="cards"><thead><tr><th width="48"></th><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody>
    <tr><td><i class="fa-credit-card"></i></td><td><strong>Cards and acquiring</strong></td><td>Acceptance, authorization, 3DS, capture, voids, refunds, and disputes.</td><td><a href="https://app.gitbook.com/s/XSPACE_GUIDES/online-payments/server-to-server.md">Cards and acquiring</a></td></tr>
    <tr><td><i class="fa-building-columns"></i></td><td><strong>Bank transfers</strong></td><td>ACH, RTP, FedNow, SEPA, Faster Payments, Interac, and open banking flows.</td><td><a href="https://www.nuvei.com/solutions/bank-transfers">Bank transfers</a></td></tr>
    <tr><td><i class="fa-wallet"></i></td><td><strong>Wallets and APMs</strong></td><td>Apple Pay, Google Pay, PayPal, buy-now-pay-later, QR payments, and local methods.</td><td><a href="https://app.gitbook.com/s/XSPACE_GUIDES/payment-methods/apms.md">Wallets and APMs</a></td></tr>
    <tr><td><i class="fa-shield-halved"></i></td><td><strong>Risk and compliance</strong></td><td>Fraud rules, dynamic 3DS, PCI scope, chargeback tooling, and regional guardrails.</td><td><a href="https://app.gitbook.com/s/XSPACE_OPS/risk-and-security.md">Risk and compliance</a></td></tr>
    </tbody></table>

    ## Reader jobs this page should answer

    * Which payment options are available in my target markets?
    * Which integration path supports the method I need?
    * Which compliance or risk controls are required before launch?
    * Which operational pages should finance and support teams read before go-live?
    """,
)
write(
    "home/editorial-workflow.md",
    """
    ---
    description: How a Nuvei docs team could use GitBook to review, stage, and publish payment documentation.
    icon: pen-nib
    ---

    # Editorial Workflow

    Payment documentation changes often touch product, engineering, legal, compliance, regional operations, and support. GitBook can give those teams one review path while keeping public docs readable.

    {% stepper %}
    {% step %}
    ### Draft in a branch or change request

    Writers update content in Git or GitBook. Product owners can review pages without needing local tooling.
    {% endstep %}

    {% step %}
    ### Route sensitive changes

    Authentication, PCI, risk, and settlement pages can require compliance review before merge.
    {% endstep %}

    {% step %}
    ### Preview with a share link

    Stakeholders test search, AI answers, and navigation before publishing.
    {% endstep %}

    {% step %}
    ### Publish and monitor feedback

    Page feedback and search analytics reveal confusing flows, stale pages, and missing implementation answers.
    {% endstep %}
    {% endstepper %}

    {% hint style="success" %}
    Demo talk track: GitBook does not just make the site prettier. It helps a large payments organization govern who can change docs, how changes are reviewed, and whether readers are finding answers.
    {% endhint %}
    """,
)
write(
    "home/source-notes.md",
    """
    ---
    description: Public source pages used to shape this demo.
    icon: link
    ---

    # Source Notes

    Public source pages used for this draft:

    * [Nuvei documentation portal](https://docs.nuvei.com/documentation/home/)
    * [Nuvei REST 2.0 API introduction](https://docs.nuvei.com/api/v2/main/docs/introduction/)
    * [Nuvei marketing site](https://www.nuvei.com/)
    * [Nuvei developer tools](https://www.nuvei.com/developer-tools)
    * [Web SDK quickstart](https://docs.nuvei.com/documentation/accept-payment/web-sdk/quick-start-for-web-sdk/)
    * [Authentication docs](https://docs.nuvei.com/documentation/features/authentication/)

    This demo intentionally summarizes and reorganizes public themes. A production migration should use Nuvei's canonical docs source, redirects, OpenAPI specifications, and brand assets.
    """,
)

write(
    "integration-guides/README.md",
    """
    ---
    description: Implementation paths for accepting payments with Nuvei.
    icon: rocket
    layout:
      width: default
      tableOfContents:
        visible: true
    ---

    # Integration Guides

    Start with the checkout pattern that matches your product, then move into API behavior, payment methods, testing, and launch readiness.

    <table data-view="cards"><thead><tr><th width="48"></th><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody>
    <tr><td><i class="fa-window-maximize"></i></td><td><strong>Payment Page</strong></td><td>Hosted payment experience for teams that want faster launch and lower PCI scope.</td><td><a href="online-payments/payment-page.md">Payment Page</a></td></tr>
    <tr><td><i class="fa-code"></i></td><td><strong>Web SDK</strong></td><td>Embed a payment form while keeping control over the checkout experience.</td><td><a href="online-payments/web-sdk.md">Web SDK</a></td></tr>
    <tr><td><i class="fa-server"></i></td><td><strong>Server-to-server</strong></td><td>Direct API integration for merchants who need full backend control.</td><td><a href="online-payments/server-to-server.md">Server-to-server</a></td></tr>
    <tr><td><i class="fa-puzzle-piece"></i></td><td><strong>Plugins</strong></td><td>Commerce-platform integrations for Magento, Shopify, SAP, and more.</td><td><a href="plugins/commerce-plugins.md">Plugins</a></td></tr>
    </tbody></table>
    """,
)
summary(
    "integration-guides",
    [
        "* [Overview](README.md)",
        "## Online payments",
        "* [Choose an integration path](online-payments/choose-an-integration-path.md)",
        "* [Payment Page](online-payments/payment-page.md)",
        "* [Web SDK](online-payments/web-sdk.md)",
        "* [Server-to-server](online-payments/server-to-server.md)",
        "## Payment methods",
        "* [Alternative payment methods](payment-methods/apms.md)",
        "* [Apple Pay and Google Pay](payment-methods/wallets.md)",
        "## Plugins",
        "* [Commerce plugins](plugins/commerce-plugins.md)",
        "## Launch",
        "* [Testing and go-live checklist](launch/testing-go-live.md)",
    ],
)
write(
    "integration-guides/online-payments/choose-an-integration-path.md",
    """
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
    """,
)
write(
    "integration-guides/online-payments/payment-page.md",
    """
    ---
    description: Hosted checkout path for faster online payment launch.
    icon: window-maximize
    ---

    # Payment Page

    Payment Page is the right first path for merchants who want a hosted payment experience, a faster implementation, and less payment-field handling in their own frontend.

    ## Implementation shape

    {% stepper %}
    {% step %}### Create the payment session
    Your backend prepares the transaction, amount, currency, billing details, and return URLs.
    {% endstep %}
    {% step %}### Redirect or render the hosted experience
    The customer completes payment on a Nuvei-managed flow.
    {% endstep %}
    {% step %}### Handle the result
    Listen for return handling and webhook confirmation before fulfilling the order.
    {% endstep %}
    {% endstepper %}

    {% hint style="warning" %}
    Always reconcile the final transaction state server-side. Browser redirects can be interrupted.
    {% endhint %}
    """,
)
write(
    "integration-guides/online-payments/web-sdk.md",
    """
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
    """,
)
write(
    "integration-guides/online-payments/server-to-server.md",
    """
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

    See the [API Reference](https://app.gitbook.com/s/XSPACE_API/) for request conventions, authentication, errors, and webhooks.
    """,
)
write(
    "integration-guides/payment-methods/apms.md",
    """
    ---
    description: Add local and alternative payment methods to the checkout.
    icon: wallet
    ---

    # Alternative Payment Methods

    Nuvei's APM surface helps merchants offer the methods customers already trust in each market: bank transfers, wallets, QR payments, buy-now-pay-later, and local schemes.

    ## Documentation pattern

    Each method page should include:

    * Availability by country and currency.
    * Supported integration paths.
    * Required customer fields.
    * Redirect, pending, refund, and dispute behavior.
    * Testing credentials and sandbox caveats.
    """,
)
write(
    "integration-guides/payment-methods/wallets.md",
    """
    ---
    description: Wallet setup patterns for Apple Pay, Google Pay, and similar payment methods.
    icon: mobile-screen-button
    ---

    # Apple Pay and Google Pay

    Wallet documentation should make setup requirements explicit: merchant verification, browser/device support, payment sheet fields, domain registration, and production readiness.

    {% hint style="info" %}
    Demo improvement: use tabs for each wallet so merchants can compare setup steps without reading duplicated paragraphs.
    {% endhint %}
    """,
)
write(
    "integration-guides/plugins/commerce-plugins.md",
    """
    ---
    description: Commerce-platform plugin setup and operational readiness.
    icon: puzzle-piece
    ---

    # Commerce Plugins

    Plugin docs serve a different audience than direct API docs. They should prioritize installation, configuration, payment-method enablement, order-state mapping, refunds, and upgrade notes.

    <table><thead><tr><th>Platform</th><th>Reader job</th><th>GitBook page pattern</th></tr></thead><tbody>
    <tr><td>Magento</td><td>Install and configure checkout</td><td>Stepper + troubleshooting</td></tr>
    <tr><td>Shopify</td><td>Enable Nuvei payment methods</td><td>Checklist + screenshots</td></tr>
    <tr><td>SAP</td><td>Map orders and settlement</td><td>Concept page + reference tables</td></tr>
    </tbody></table>
    """,
)
write(
    "integration-guides/launch/testing-go-live.md",
    """
    ---
    description: Validate a Nuvei integration before switching to live traffic.
    icon: list-check
    ---

    # Testing and Go-live Checklist

    * Confirm merchant credentials and environment URLs.
    * Run successful, declined, pending, refunded, and disputed payment scenarios.
    * Verify 3DS and exemption behavior for target markets.
    * Confirm webhooks are idempotent and signed or otherwise verified.
    * Reconcile dashboard status with backend order state.
    * Prepare support macros for payment failures and pending transactions.
    """,
)

write(
    "api-reference/README.md",
    """
    ---
    description: REST API overview and implementation conventions.
    icon: code
    ---

    # API Reference

    Nuvei's API reference is the canonical technical surface for developers building direct integrations. This demo keeps the reference concise and points to where an OpenAPI-backed reference would live.

    {% hint style="info" %}
    Production recommendation: import Nuvei's real OpenAPI specifications into GitBook and generate operation pages automatically. This draft uses narrative API pages because the canonical spec was not provided in the Slack request.
    {% endhint %}

    <table data-view="cards"><thead><tr><th width="48"></th><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody>
    <tr><td><i class="fa-key"></i></td><td><strong>Authentication</strong></td><td>Credentials, request signing, and environment handling.</td><td><a href="authentication.md">Authentication</a></td></tr>
    <tr><td><i class="fa-arrows-rotate"></i></td><td><strong>Payment lifecycle</strong></td><td>Session, authorization, capture, refund, void, dispute, and webhook states.</td><td><a href="payment-lifecycle.md">Payment lifecycle</a></td></tr>
    <tr><td><i class="fa-triangle-exclamation"></i></td><td><strong>Errors</strong></td><td>How to handle declines, validation errors, and retryable failures.</td><td><a href="errors-and-retries.md">Errors</a></td></tr>
    </tbody></table>
    """,
)
summary(
    "api-reference",
    [
        "* [Overview](README.md)",
        "* [Authentication](authentication.md)",
        "* [Payment lifecycle](payment-lifecycle.md)",
        "* [Requests and responses](requests-and-responses.md)",
        "* [Errors and retries](errors-and-retries.md)",
        "* [Webhooks](webhooks.md)",
        "* [OpenAPI migration path](openapi-migration-path.md)",
    ],
)
write(
    "api-reference/authentication.md",
    """
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
    """,
)
write(
    "api-reference/payment-lifecycle.md",
    """
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
    """,
)
write(
    "api-reference/requests-and-responses.md",
    """
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
    """,
)
write(
    "api-reference/errors-and-retries.md",
    """
    ---
    description: Handle validation, decline, network, and retry scenarios.
    icon: triangle-exclamation
    ---

    # Errors and Retries

    Payment errors are not all the same. Docs should distinguish merchant-fixable configuration issues, customer-actionable declines, retryable network failures, and final failures.

    <table><thead><tr><th>Error type</th><th>Merchant action</th><th>Customer message</th></tr></thead><tbody>
    <tr><td>Validation</td><td>Fix request payload or checkout mapping.</td><td>Ask for corrected information only if appropriate.</td></tr>
    <tr><td>Issuer decline</td><td>Log reason code and offer alternate method.</td><td>Ask customer to try another method.</td></tr>
    <tr><td>Network timeout</td><td>Check idempotency and payment state before retrying.</td><td>Show pending or retry-safe state.</td></tr>
    </tbody></table>
    """,
)
write(
    "api-reference/webhooks.md",
    """
    ---
    description: Webhook delivery, verification, retries, and operational handling.
    icon: webhook
    ---

    # Webhooks

    Webhooks connect Nuvei's payment state to the merchant's order, fulfillment, finance, and support systems.

    {% stepper %}
    {% step %}### Receive the event
    Terminate TLS, parse the event, and capture raw delivery metadata for diagnostics.
    {% endstep %}
    {% step %}### Verify authenticity
    Validate the event using Nuvei's recommended verification method before trusting the payload.
    {% endstep %}
    {% step %}### Process idempotently
    Use event IDs and payment IDs to avoid duplicate fulfillment.
    {% endstep %}
    {% step %}### Reconcile
    Compare webhook state with Control Panel and backend order state.
    {% endstep %}
    {% endstepper %}
    """,
)
write(
    "api-reference/openapi-migration-path.md",
    """
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
    """,
)

write(
    "operations-support/README.md",
    """
    ---
    description: Operational docs for managing payments after launch.
    icon: chart-line
    ---

    # Operations & Support

    Payment docs do not end at integration. Merchant operators, finance teams, risk teams, and support teams need a reliable place to understand dashboards, reporting, reconciliation, and transaction exceptions.

    <table data-view="cards"><thead><tr><th width="48"></th><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody>
    <tr><td><i class="fa-gauge-high"></i></td><td><strong>Control Panel</strong></td><td>Back-office workflows for transaction, finance, risk, and operations teams.</td><td><a href="control-panel.md">Control Panel</a></td></tr>
    <tr><td><i class="fa-shield-halved"></i></td><td><strong>Risk and security</strong></td><td>3DS, chargebacks, fraud controls, credentials, and PCI-sensitive guidance.</td><td><a href="risk-and-security.md">Risk and security</a></td></tr>
    <tr><td><i class="fa-scale-balanced"></i></td><td><strong>Reconciliation</strong></td><td>Settlement, reporting, refunds, disputes, and finance workflows.</td><td><a href="reconciliation-and-reporting.md">Reconciliation</a></td></tr>
    </tbody></table>
    """,
)
summary(
    "operations-support",
    [
        "* [Overview](README.md)",
        "* [Control Panel](control-panel.md)",
        "* [Risk and security](risk-and-security.md)",
        "* [Reconciliation and reporting](reconciliation-and-reporting.md)",
        "* [Partner tools](partner-tools.md)",
        "* [Release notes](release-notes.md)",
        "* [Support playbooks](support-playbooks.md)",
    ],
)
write(
    "operations-support/control-panel.md",
    """
    ---
    description: Back-office workflows for monitoring and managing payment operations.
    icon: gauge-high
    ---

    # Control Panel

    Control Panel documentation should help operators answer: what happened, why did it happen, and what action can I take safely?

    ## Core workflows

    * Search for a transaction.
    * Review authorization, capture, refund, and dispute state.
    * Export reports for finance or reconciliation.
    * Manage risk rules and operational permissions.
    * Escalate issues with the right payment identifiers.
    """,
)
write(
    "operations-support/risk-and-security.md",
    """
    ---
    description: Fraud prevention, authentication controls, credentials, and compliance-sensitive docs.
    icon: shield-halved
    ---

    # Risk and Security

    Risk docs are strongest when they connect technical configuration to business outcomes: higher authorization rates, fewer chargebacks, lower fraud exposure, and clearer compliance review.

    {% hint style="warning" %}
    Sensitive pages can be permissioned or staged in GitBook so legal, compliance, and security teams can review before public release.
    {% endhint %}
    """,
)
write(
    "operations-support/reconciliation-and-reporting.md",
    """
    ---
    description: Reporting, settlement, reconciliation, and finance operations.
    icon: scale-balanced
    ---

    # Reconciliation and Reporting

    Payments teams need operational docs that bridge API events, dashboard states, settlement files, and finance reports.

    <table><thead><tr><th>Question</th><th>Where docs should point</th></tr></thead><tbody>
    <tr><td>Was the payment captured?</td><td>Transaction status and webhook event history.</td></tr>
    <tr><td>Why does the payout not match gross sales?</td><td>Fees, refunds, chargebacks, and settlement timing.</td></tr>
    <tr><td>Which report should finance export?</td><td>Control Panel reporting guide and field definitions.</td></tr>
    </tbody></table>
    """,
)
write(
    "operations-support/partner-tools.md",
    """
    ---
    description: Partner and merchant tools for reporting, configuration, and support.
    icon: handshake
    ---

    # Partner Tools

    Partner-tool docs should be separated from pure developer docs because the readers and jobs differ. Partner users need setup, reporting, access, permissioning, and support workflows.

    ## Useful GitBook pattern

    * Keep "getting started" short.
    * Put role-specific tasks in cards.
    * Add screenshots or Loom embeds for dashboard-heavy tasks.
    * Use page feedback on every operational article to catch stale UI instructions.
    """,
)
write(
    "operations-support/release-notes.md",
    """
    ---
    description: Demo release notes using GitBook's Updates block.
    icon: clock-rotate-left
    layout:
      width: wide
    ---

    # Release Notes

    {% updates format="full" %}
    {% update date="2026-07-01" tags="docs,api" %}
    ## API reference migration draft

    Added a proposed OpenAPI-backed API reference structure with authentication, lifecycle, request handling, errors, webhooks, and migration notes.
    {% endupdate %}

    {% update date="2026-07-01" tags="merchant-ops" %}
    ## Operations space added

    Added Control Panel, risk, reconciliation, partner tools, and support playbooks so post-launch teams have their own docs surface.
    {% endupdate %}
    {% endupdates %}
    """,
)
write(
    "operations-support/support-playbooks.md",
    """
    ---
    description: Support-ready answers for common payment questions.
    icon: headset
    ---

    # Support Playbooks

    Support teams need concise decision trees that connect customer-facing language to transaction evidence.

    ```mermaid
    flowchart TD
      Ticket[Customer payment issue] --> Search[Find transaction]
      Search --> Missing{Transaction found?}
      Missing -->|No| Checkout[Check checkout logs]
      Missing -->|Yes| State{Payment state}
      State --> Pending[Pending: explain timing and monitor webhook]
      State --> Declined[Declined: suggest alternate method]
      State --> Captured[Captured: check fulfillment and settlement]
    ```
    """,
)

print(f"Wrote Nuvei demo content to {ROOT}")
