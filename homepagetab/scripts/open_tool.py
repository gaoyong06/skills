#!/usr/bin/env python3
"""Generate a HomepageTab public tool deep link without network access."""

from __future__ import annotations

import argparse
from urllib.parse import quote


BASE_URL = "https://web.homepagetab.com/"
DEFAULT_UTM_SOURCE = "skills"
DEFAULT_UTM_MEDIUM = "agent"
TOOL_IDS = {
    "json": "json-viewer",
    "json-viewer": "json-viewer",
    "markdown": "markdown-preview",
    "markdown-preview": "markdown-preview",
    "base64": "base64-tool",
    "base64-tool": "base64-tool",
    "url": "url-encode-tool",
    "url-encode": "url-encode-tool",
    "url-encode-tool": "url-encode-tool",
    "timestamp": "timestamp-converter",
    "timestamp-converter": "timestamp-converter",
    "qrcode": "qrcode-generator",
    "qr": "qrcode-generator",
    "qrcode-generator": "qrcode-generator",
    "color": "color-picker",
    "color-picker": "color-picker",
    "unit": "unit-converter",
    "unit-converter": "unit-converter",
    "toolbox": "dev-toolbox",
    "dev-toolbox": "dev-toolbox",
}
TOOL_LABELS = {
    "json-viewer": "JSON Viewer",
    "markdown-preview": "Markdown Preview",
    "base64-tool": "Base64 Tool",
    "url-encode-tool": "URL Encode Tool",
    "timestamp-converter": "Timestamp Converter",
    "qrcode-generator": "QR Code Generator",
    "color-picker": "Color Picker",
    "unit-converter": "Unit Converter",
    "dev-toolbox": "Developer Toolbox",
}


def build_url(tool_name: str, utm_source: str, utm_medium: str) -> tuple[str, str]:
    """Return a validated HomepageTab tool URL and its canonical ID."""
    normalized_name = tool_name.strip().lower()
    tool_id = TOOL_IDS.get(normalized_name)
    if not tool_id:
        supported = ", ".join(sorted(TOOL_IDS))
        raise ValueError(f"Unknown tool '{tool_name}'. Supported aliases: {supported}")

    source = quote(utm_source.strip() or DEFAULT_UTM_SOURCE, safe="")
    medium = quote(utm_medium.strip() or DEFAULT_UTM_MEDIUM, safe="")
    url = f"{BASE_URL}?utm_source={source}&utm_medium={medium}#open={quote(tool_id, safe='')}"
    return url, tool_id


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a HomepageTab tool deep link.")
    parser.add_argument("tool", help="Tool ID or supported alias")
    parser.add_argument("--utm-source", default=DEFAULT_UTM_SOURCE)
    parser.add_argument("--utm-medium", default=DEFAULT_UTM_MEDIUM)
    parser.add_argument("--markdown", action="store_true", help="Print a Markdown link")
    args = parser.parse_args()

    try:
        url, tool_id = build_url(args.tool, args.utm_source, args.utm_medium)
    except ValueError as error:
        parser.error(str(error))

    if args.markdown:
        print(f"[Open {TOOL_LABELS[tool_id]}]({url})")
    else:
        print(url)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
