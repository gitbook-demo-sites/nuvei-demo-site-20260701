import json
import os
import subprocess
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ORG_ID = "7N6Uef1YNS68eBZgQRzB"
SITE_ID = "site_lK9LH"
REPO_URL = "https://github.com/gitbook-demo-sites/nuvei-demo-site-20260701.git"
BASE = "https://api.gitbook.com/v1"

SPACES = [
    {
        "key": "HOME",
        "sentinel": "XSPACE_HOME",
        "folder": "home",
        "title": "Home",
        "emoji": "1f3e0",
        "icon": "house",
        "path": "home",
        "description": "Branded front door, market map, editorial workflow, and source notes.",
    },
    {
        "key": "GUIDES",
        "sentinel": "XSPACE_GUIDES",
        "folder": "integration-guides",
        "title": "Integration Guides",
        "emoji": "1f680",
        "icon": "rocket",
        "path": "integration-guides",
        "description": "Online payments, payment methods, plugins, and go-live readiness.",
    },
    {
        "key": "API",
        "sentinel": "XSPACE_API",
        "folder": "api-reference",
        "title": "API Reference",
        "emoji": "1f4bb",
        "icon": "code",
        "path": "api-reference",
        "description": "Authentication, payment lifecycle, errors, webhooks, and OpenAPI migration path.",
    },
    {
        "key": "OPS",
        "sentinel": "XSPACE_OPS",
        "folder": "operations-support",
        "title": "Operations & Support",
        "emoji": "1f4c8",
        "icon": "chart-line",
        "path": "operations-support",
        "description": "Control Panel, risk, reconciliation, partner tools, support, and release notes.",
    },
]


def api(method: str, path: str, body=None, expected=(200, 201, 204)):
    token = os.environ["GITBOOK_TOKEN"]
    data = None if body is None else json.dumps(body).encode()
    req = urllib.request.Request(
        BASE + path,
        data=data,
        method=method,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            text = resp.read().decode()
            payload = json.loads(text) if text else None
            if resp.status not in expected:
                raise RuntimeError(f"{method} {path} returned {resp.status}: {text}")
            return resp.status, payload
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode()
        raise RuntimeError(f"{method} {path} returned {exc.code}: {detail}") from exc


def replace_sentinels(space_ids):
    replacements = {item["sentinel"]: space_ids[item["key"]] for item in SPACES}
    for path in ROOT.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        original = text
        for old, new in replacements.items():
            text = text.replace(old, new)
        if text != original:
            path.write_text(text, encoding="utf-8")


def git_commit_push(message: str):
    subprocess.run(["git", "add", "."], cwd=ROOT, check=True)
    diff = subprocess.run(["git", "diff", "--cached", "--quiet"], cwd=ROOT)
    if diff.returncode == 0:
        return
    subprocess.run(["git", "commit", "-m", message], cwd=ROOT, check=True)
    subprocess.run(["git", "push"], cwd=ROOT, check=True)


def main():
    created = {
        "org": ORG_ID,
        "site": SITE_ID,
        "spaces": {},
        "sections": {},
        "site_spaces": {},
    }

    api(
        "PATCH",
        f"/orgs/{ORG_ID}/sites/{SITE_ID}",
        {"title": "Nuvei Documentation Hub", "visibility": "share-link", "basename": "nuvei-documentation-hub"},
    )

    for item in SPACES:
        _, space = api(
            "POST",
            f"/orgs/{ORG_ID}/spaces",
            {"title": item["title"], "emoji": item["emoji"], "empty": True, "editMode": "live"},
        )
        space_id = space["id"]
        created["spaces"][item["key"]] = space_id

        _, section = api(
            "POST",
            f"/orgs/{ORG_ID}/sites/{SITE_ID}/sections",
            {"spaceId": space_id, "title": item["title"], "icon": item["icon"], "draft": False},
        )
        section_id = section["id"]
        created["sections"][item["key"]] = section_id
        site_space_id = section["siteSpaces"][0]["id"]
        created["site_spaces"][item["key"]] = site_space_id
        api(
            "PATCH",
            f"/orgs/{ORG_ID}/sites/{SITE_ID}/sections/{section_id}",
            {"path": item["path"], "description": item["description"], "draft": False, "defaultSiteSpace": site_space_id},
        )

    api(
        "PATCH",
        f"/orgs/{ORG_ID}/sites/{SITE_ID}",
        {
            "defaultSiteSection": created["sections"]["HOME"],
            "defaultSiteSpace": created["site_spaces"]["HOME"],
        },
    )

    replace_sentinels(created["spaces"])
    (ROOT / "gitbook-created.json").write_text(json.dumps(created, indent=2) + "\n", encoding="utf-8")
    git_commit_push("Resolve Nuvei GitBook space links")

    import_results = {}
    for item in SPACES:
        space_id = created["spaces"][item["key"]]
        status, _ = api(
            "POST",
            f"/spaces/{space_id}/git/import",
            {
                "url": REPO_URL,
                "ref": "refs/heads/main",
                "repoProjectDirectory": item["folder"],
                "repoTreeURL": "https://github.com/gitbook-demo-sites/nuvei-demo-site-20260701/tree/main",
                "repoCommitURL": "https://github.com/gitbook-demo-sites/nuvei-demo-site-20260701/commit",
                "force": True,
                "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            },
            expected=(204,),
        )
        import_results[item["key"]] = {"status": status, "space": space_id, "folder": item["folder"]}

    (ROOT / "gitbook-import-results.json").write_text(json.dumps(import_results, indent=2) + "\n", encoding="utf-8")
    time.sleep(25)

    customization = {
        "title": "Nuvei Documentation Hub",
        "localizedTitle": {},
        "internationalization": {"locale": "en"},
        "styling": {
            "theme": "clean",
            "primaryColor": {"light": "#160850", "dark": "#0C98D4"},
            "infoColor": {"light": "#0C98D4", "dark": "#0C98D4"},
            "successColor": {"light": "#00B67A", "dark": "#00B67A"},
            "warningColor": {"light": "#E31B48", "dark": "#E31B48"},
            "dangerColor": {"light": "#CA013F", "dark": "#E40046"},
            "tint": {"color": {"light": "#FAF9F8", "dark": "#160850"}},
            "corners": "straight",
            "depth": "flat",
            "links": "accent",
            "font": "Inter",
            "monospaceFont": "IBMPlexMono",
            "icons": "regular",
            "background": "plain",
            "sidebar": {"background": "filled", "list": "line"},
            "codeTheme": {
                "default": {"light": "default-light", "dark": "default-dark"},
                "openapi": {"light": "default-light", "dark": "default-dark"},
            },
            "search": "prominent",
        },
        "favicon": {
            "icon": {
                "light": "https://cdn.prod.website-files.com/69bbe852f53519cb6c89312c/69dcf0eac485075180e47ef4_favicon.jpg",
                "dark": "https://cdn.prod.website-files.com/69bbe852f53519cb6c89312c/69dcf1638e16eb08e4669e3d_favicon-dark.jpg",
            }
        },
        "header": {
            "preset": "default",
            "logo": {
                "light": "https://cdn.prod.website-files.com/69bbe852f53519cb6c89312c/69dcf0eac485075180e47ef4_favicon.jpg",
                "dark": "https://cdn.prod.website-files.com/69bbe852f53519cb6c89312c/69dcf1638e16eb08e4669e3d_favicon-dark.jpg",
            },
            "links": [
                {"title": "Nuvei", "to": {"kind": "url", "url": "https://www.nuvei.com/"}, "style": "link", "links": [], "localizedTitle": {}},
                {"title": "Current docs", "to": {"kind": "url", "url": "https://docs.nuvei.com/documentation/home/"}, "style": "link", "links": [], "localizedTitle": {}},
                {"title": "API docs", "to": {"kind": "url", "url": "https://docs.nuvei.com/api/v2/main/docs/introduction/"}, "style": "button-secondary", "links": [], "localizedTitle": {}},
            ],
        },
        "footer": {
            "logo": {
                "light": "https://cdn.prod.website-files.com/69bbe852f53519cb6c89312c/69dcf0eac485075180e47ef4_favicon.jpg",
                "dark": "https://cdn.prod.website-files.com/69bbe852f53519cb6c89312c/69dcf1638e16eb08e4669e3d_favicon-dark.jpg",
            },
            "groups": [
                {
                    "title": "Demo paths",
                    "localizedTitle": {},
                    "links": [
                        {"title": "Start integrating", "to": {"kind": "space", "space": created["spaces"]["GUIDES"]}, "localizedTitle": {}},
                        {"title": "API reference", "to": {"kind": "space", "space": created["spaces"]["API"]}, "localizedTitle": {}},
                        {"title": "Operations", "to": {"kind": "space", "space": created["spaces"]["OPS"]}, "localizedTitle": {}},
                    ],
                },
                {
                    "title": "Sources",
                    "localizedTitle": {},
                    "links": [
                        {"title": "Source repo", "to": {"kind": "url", "url": "https://github.com/gitbook-demo-sites/nuvei-demo-site-20260701"}, "localizedTitle": {}},
                        {"title": "Nuvei website", "to": {"kind": "url", "url": "https://www.nuvei.com/"}, "localizedTitle": {}},
                    ],
                },
            ],
            "copyright": "Nuvei Documentation Hub demo - built for review in GitBook.",
        },
        "themes": {"default": "light", "toggeable": True},
        "pdf": {"enabled": True},
        "feedback": {"enabled": True},
        "ai": {
            "mode": "assistant",
            "suggestions": [
                "Which Nuvei integration path should I choose?",
                "How do webhooks affect fulfillment?",
                "Where do I find APM setup guidance?",
                "How should finance reconcile transactions?",
                "What should be migrated to OpenAPI?",
            ],
        },
        "advancedCustomization": {"enabled": True},
        "trademark": {"enabled": True},
        "externalLinks": {"target": "self"},
        "pagination": {"enabled": True},
        "pageActions": {"externalAI": True, "markdown": True, "mcp": True, "items": ["assistant", "markdown", "external-ai", "mcp", "pdf"]},
        "git": {"showEditLink": False},
        "privacyPolicy": {"url": "https://www.nuvei.com/privacy-policy"},
        "socialPreview": {"url": "https://cdn.prod.website-files.com/69bbe852f53519cb6c89312c/69e6815b9bf945343178b129_OG-image.jpg"},
        "socialAccounts": [],
        "insights": {"trackingCookie": True},
    }

    _, customized = api("PUT", f"/orgs/{ORG_ID}/sites/{SITE_ID}/customization", customization)
    (ROOT / "gitbook-customization-result.json").write_text(json.dumps(customized, indent=2) + "\n", encoding="utf-8")

    publish_status, publish = api("POST", f"/orgs/{ORG_ID}/sites/{SITE_ID}/publish")
    share_status, share = api(
        "POST",
        f"/orgs/{ORG_ID}/sites/{SITE_ID}/share-links",
        {"name": "Nuvei demo review"},
    )
    final = {
        "publish_status": publish_status,
        "publish": publish,
        "share_status": share_status,
        "share": share,
        "published_url": share["urls"]["published"],
        "app_url": publish["urls"]["app"],
        "preview_url": publish["urls"]["preview"],
    }
    (ROOT / "gitbook-publish-share.json").write_text(json.dumps(final, indent=2) + "\n", encoding="utf-8")
    git_commit_push("Add Nuvei GitBook publish artifacts")
    print(json.dumps(final, indent=2))


if __name__ == "__main__":
    main()
