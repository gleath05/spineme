# Publishing and maintaining SpineMe

Repository: https://github.com/gleath05/spineme

## Repository installation

Claude Code: send these as two separate prompts:

```text
/plugin marketplace add gleath05/spineme
/plugin install spineme@spineme
```

Codex CLI versions with plugin installation support:

```bash
codex plugin marketplace add gleath05/spineme
codex plugin add spineme@spineme
```

The Claude marketplace points to the plugin at the repository root. The Codex
marketplace points to this repository's `main` branch. Public marketplace directory
approval is separate from installation using these repository catalogs.

## Maintaining a release

1. Edit the canonical skill or host adapters.
2. Run `python3 scripts/build.py` and `python3 scripts/check.py`.
3. Run the cases in `VALIDATION.md` on each host/version/model you claim as tested.
4. Commit source, generated packages, and validation results together.
5. Create a release and attach `dist/` ZIPs when ready.

SpineMe uses the MIT license; include `LICENSE` in every distribution. Cross-host runtime tests and public
marketplace submissions are still pending; do not imply they have passed.
