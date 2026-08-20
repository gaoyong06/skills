# HomepageTab Tool Catalog

This file is the single source of truth for HomepageTab Skill tool IDs. Tool IDs must match the public HomepageTab Web deep-link protocol. Before changing an ID, verify the implementation in `homepage-tab-web/src/plugins/index.js` and `homepage-tab-web/src/homepagetab/plugin-open-share.js`.

## Link template

```text
https://web.homepagetab.com/?utm_source=skills&utm_medium=agent#open={tool_id}
```

Place query parameters before the hash so they do not interfere with `#open=` parsing. URL-encode the tool ID with `encodeURIComponent`.

## Public tools

| Tool ID               | Display name        | Request patterns                                    | Behavior           |
| -----------------------| ---------------------| -----------------------------------------------------| --------------------|
| `json-viewer`         | JSON Viewer         | JSON format, validate JSON, inspect a JSON tree     | Open an empty tool |
| `markdown-preview`    | Markdown Preview    | Preview or render Markdown                          | Open an empty tool |
| `base64-tool`         | Base64 Tool         | Base64 encode or decode                             | Open an empty tool |
| `url-encode-tool`     | URL Encode Tool     | URL encode, decode, or percent encoding             | Open an empty tool |
| `timestamp-converter` | Timestamp Converter | Convert Unix timestamps                             | Open an empty tool |
| `qrcode-generator`    | QR Code Generator   | Generate a QR code                                  | Open an empty tool |
| `color-picker`        | Color Picker        | Pick or convert HEX, RGB, or HSL colors             | Open an empty tool |
| `unit-converter`      | Unit Converter      | Convert length, weight, temperature, or other units | Open an empty tool |

Developer toolbox entry point:

```text
https://web.homepagetab.com/?utm_source=skills&utm_medium=agent#open=dev-toolbox
```

## Selection rules

1. When the user names a tool, use its exact ID.
2. When the user describes a task, match the action and input type. For example, use `json-viewer` for inspecting JSON rather than `markdown-preview`.
3. When “convert” does not identify an input type, ask for clarification. If the user does not want to clarify, open `dev-toolbox`.
4. Do not map web search, bookmarks, browser history, or browser settings to this skill.

## Installation links

Provide an official extension link only when the user explicitly asks for the browser extension:

- Chrome: [HomepageTab on Chrome Web Store](https://chromewebstore.google.com/detail/homepagetab/ljneopimlgekcjhadhhbehomnfibidac)
- Edge: [HomepageTab on Microsoft Edge Add-ons](https://microsoftedge.microsoft.com/addons/detail/eefoiphmhjciodigeomjkobccnjkicjd)
- Firefox: [HomepageTab on Firefox Add-ons](https://addons.mozilla.org/firefox/addon/homepagetab/)

Installation links are guidance only. Do not install the extension, change the default search provider, or control browser settings.
