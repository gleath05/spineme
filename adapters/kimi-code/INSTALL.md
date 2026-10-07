# SpineMe for kimi-code

## Skill adapter (no plugin manager required)

1. Extract `spineme-kimi-code-adapter.zip` into a temporary folder. Enable hidden-file
   display if your file browser hides dot-prefixed folders.
2. Copy its `.kimi-code/skills/spineme` folder into `.kimi-code/skills/spineme` in the project
   you want to audit. Create the parent folders if necessary. Compare existing
   SpineMe files before replacing them; preserve unrelated files and settings.
3. Start a fresh host session in that project and confirm SpineMe is discovered.
4. Invoke `/skill:spineme` and request a full audit with compact output.

The archive's `INSTALL.md` is for you; it does not need to go into the project.
The source adapter recipe builds the correct folder layout; no installer runs
and no app settings change automatically.

[Host documentation](https://www.kimi.com/code/docs/en/kimi-code-cli/customization/skills.html). Paths are project-relative. Personal/global and
remote/cloud installations may differ. Documentation checked 2026-10-08.

## Packaging choice

This package uses the host's native skill directory. It does not claim a separate
plugin-manager integration. For ordinary chat instead of this coding host, use
`spineme-chat.zip` and provide the source files yourself.

## Model choices and verification

The host's selected model runs the audit. The core's Economy/Balanced/Advanced
profiles remain vendor-neutral; provide your own available-model mapping if desired.
This adapter sets no model and cannot switch one.

Check discovery, read-only behavior, scope limits, evidence accuracy, and verification
against a small disposable project before relying on it. Packaging has been checked
locally; this host's runtime loading and audit behavior have not been tested here.
