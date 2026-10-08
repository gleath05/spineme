# SpineMe

**Confidence before production. Evidence before confidence.**

A portable, read-only production readiness auditor for AI coding assistants.
Find evidence-backed risks, prioritize blockers, prepare remediation handoffs,
and verify fixes. Default: **full audit + compact output**.

The audit covers backend, frontend, QA, architecture, databases, security,
automation, integrations, infrastructure, CI/CD, observability, performance,
deployment/recovery, documentation, and applicable transaction integrity.

## Download the package for your app

Ready-made ZIPs are in [dist/](../dist/). Pick **one** installation method per host.
Extract to a temporary folder, then follow the included `INSTALL.md`.

| App | Plugin | Direct skill adapter / instructions |
| --- | --- | --- |
| Codex | [Plugin ZIP](../dist/spineme-codex-plugin.zip) | [Adapter ZIP](../dist/spineme-codex-adapter.zip) · [Guide](../adapters/codex/INSTALL.md) |
| Claude Code | [Plugin ZIP](../dist/spineme-claude-code-plugin.zip) | [Adapter ZIP](../dist/spineme-claude-code-adapter.zip) · [Guide](../adapters/claude-code/INSTALL.md) |
| Cursor | [Plugin ZIP](../dist/spineme-cursor-plugin.zip) | [Adapter ZIP](../dist/spineme-cursor-adapter.zip) · [Guide](../adapters/cursor/INSTALL.md) |
| Kiro | Native skill adapter | [Adapter ZIP](../dist/spineme-kiro-adapter.zip) · [Guide](../adapters/kiro/INSTALL.md) |
| Kimi Code | Native skill adapter | [Adapter ZIP](../dist/spineme-kimi-code-adapter.zip) · [Guide](../adapters/kimi-code/INSTALL.md) |
| Grok Build | Native skill adapter | [Adapter ZIP](../dist/spineme-grok-build-adapter.zip) · [Guide](../adapters/grok-build/INSTALL.md) |
| Other chat apps | Prompt attachment | [Chat ZIP](../dist/spineme-chat.zip) · [Guide](../adapters/chat/INSTALL.md) |

These are local installation/development packages, not marketplace listings.
Plugin manifests are included for Codex/Cursor (`plugin.json`) and Claude Code
(`.claude-plugin/plugin.json`). No API keys, hooks, servers, model changes, or
background actions are added. Your existing installed skill need not be replaced
just to try a different host.

## Maintaining the packages

Edit only `skills/spineme/SKILL.md` for shared audit behavior. Edit the relevant
`adapters/<host>/INSTALL.md` or `adapter.json` for host packaging. Then run:

```bash
python3 scripts/build.py
```

Python 3.8+ and its standard library are sufficient. The build overwrites only its
named generated ZIPs and checksum file in `dist/`; it does not install anything.
It checks archive integrity, safe member paths, manifest basics, and exact core
content in every package. Generated ZIPs should not be edited manually.

To publish on GitHub, upload this package's contents, including hidden manifest
folders. SpineMe is MIT licensed; retain the included license. Publish the ZIPs as release assets if useful.
Native marketplace submission is a separate step described in the host guides.

## One skill, different hosts

The core follows the [Agent Skills format](https://agentskills.io/specification):
plain Markdown with `name` and `description` metadata. It has no model vendor,
API, tool-name, or executable dependency. Optional Codex display metadata is kept
separate in `adapters/codex/openai.yaml`.

Native installation depends on the **application hosting the model**. A model
inside a chat app may have very different access from that model in a coding agent.
For apps without native skills, paste or attach the core instructions. This makes
the workflow reusable; it does not guarantee identical behavior across all LLMs.

## Install

Download this repository, then copy `skills/spineme/` into **one** appropriate
skill directory. The result must be `<directory>/spineme/SKILL.md`.

| Host | Example project skill directory | Documentation |
| --- | --- | --- |
| Codex | `.agents/skills/` | [Codex skills](https://learn.chatgpt.com/docs/build-skills#where-codex-loads-local-skills) |
| Claude Code | `.claude/skills/` | [Claude Code skills](https://code.claude.com/docs/en/skills) |
| Cursor | `.cursor/skills/` or `.agents/skills/` | [Cursor skills](https://cursor.com/docs/skills) |
| Kiro | `.kiro/skills/` | [Kiro skills](https://kiro.dev/docs/skills/) |
| Kimi Code CLI | `.kimi-code/skills/` or `.agents/skills/` | [Kimi Code skills](https://www.kimi.com/code/docs/en/kimi-code-cli/customization/skills.html) |
| Grok-based tools / other hosts | Use the host's documented skill loader, or the manual method below | [Grok Build skill guide](https://github.com/xai-org/grok-build/blob/main/crates/codegen/xai-grok-pager/docs/user-guide/08-skills.md) |

Directories above are relative to the project being audited. Consult the linked
host documentation for personal/global installation, invocation, and version limits.
Avoid installing duplicate copies into overlapping discovery directories.

For Codex display metadata, optionally copy `adapters/codex/openai.yaml` into
`agents/openai.yaml` inside the installed `spineme` folder. It is not required
for the portable workflow.

**Manual method, including ordinary Claude, Grok, or Kimi chat:** paste or attach
`skills/spineme/SKILL.md`, supply the relevant source files and logs, then ask:

```text
Follow the attached SpineMe instructions.
Audit only the material I provided, with compact output.
State missing evidence and checks you cannot run.
```

A chat without repository access cannot perform a full repository audit. A chat
without execution tools cannot run your tests. SpineMe must disclose both limits.

## When and how to use it

Use before releases, after risky changes, when inheriting a repository, or when
checking that a fix actually resolves a finding.

```text
Use SpineMe. Perform a full production readiness audit. Use compact output.
```

In Codex you can mention `$spineme`; use the skill selector or invocation supported
by another host. The following are intents, not universal registered commands:

| Intent | Purpose |
| --- | --- |
| `full` | All applicable domains; overall readiness only with sufficient coverage |
| `quick` | Limited risk triage; no overall readiness score |
| `diff` | Changed code and affected flows; specify a comparison base |
| `backend`, `security`, `database`, etc. | One domain |
| `path <directory>` | One directory and relevant dependencies |
| `finding PR-001` | Evidence, confidence, impact, and verification criteria |
| `blockers` / `failures` | Current blockers / failure-scenario analysis |
| `remediation PR-001` | An implementation prompt; does not perform the fix |
| `verify PR-001` / `verify --all` | Recheck one / all supplied findings |

## Scope and output are separate

| Output | What you receive |
| --- | --- |
| **Compact** | Readiness, counts, blockers, important findings, scorecard, gaps, next action |
| **Standard** | Compact plus concise evidence, test results, and important cross-domain risks |
| **Deep** | Complete technical analysis of the requested scope |

Compact shortens the report, not the requested review. Scoped reviews must say
**Overall Production Readiness: NOT ASSESSED**.

```text
Use SpineMe. Audit changes against main. Use compact output.
Use SpineMe. Audit the backend only. Use standard output.
Use SpineMe. Audit path services/payments. Use deep output.
```

Replace paths, base branches, and finding IDs with your actual targets.

## Model guidance without vendor lock-in

Choose the least costly **sufficiently capable** option available to you:

| Profile | Typical work |
| --- | --- |
| **Economy** | Bounded inspection and straightforward verification |
| **Balanced** | Multi-file, cross-service, and nontrivial root-cause analysis |
| **Advanced** | Difficult concurrency, transaction integrity, or high-impact ambiguity |

These profiles describe needs, not fixed rankings of brands. SpineMe uses your
available-model list or your own mapping. If neither is known, it recommends a
capability profile without inventing model names, pricing, or effort settings.

Example preference to include in your request:

```text
Use my current model first if it is sufficient.
Recommend an upgrade only for a concrete unresolved reasoning problem.
Stay within my chosen provider and budget. Do not switch models automatically.
```

For a personal OpenAI setup, you may still supply your Luna/Sol/Astra preference
mapping in your prompt. It is not embedded in the shared skill. Other users can
supply their own choices without editing the audit rules.

Example recommendation (illustrative, not a real finding):

```text
Recommended profile: Balanced
Specific model: Not specified; available models unknown
Required capability: Trace retries and database transactions across services
Upgrade value: MEDIUM
Missing evidence: Concurrent execution test has not been run
```

Model upgrades do not create missing repository access or prove a finding.

## Daily workflow

1. Establish a baseline: **full + compact** with a sufficient low-cost model.
2. During development: **diff or scoped + compact**.
3. Inspect a blocker: **finding PR-001**.
4. Request **remediation PR-001**, then implement in a separate task.
5. Return to SpineMe for **verify PR-001**. Keep IDs and the original evidence.
6. Before release, repeat a full audit and complete outstanding operational checks.

The auditor never edits implementation, deploys, or changes live systems. Safe
builds/tests may generate local artifacts. Read-only instructions are not a security
sandbox; the host controls permissions.

A score never overrides a blocker. Local test success does not prove deployed
behavior, provider integration, backup restore, or device compatibility.

## Validation and publication status

The package has passed local structural validation. Installation guidance is based
on the linked vendor documentation, checked on 2026-10-08. Behavioral testing in
other hosts has not yet been performed; portability is not a cross-model quality
certification. Use the scenarios in [VALIDATION.md](../VALIDATION.md) before claiming
support for a particular host/version/model combination.

SpineMe is MIT licensed. The repository is `gleath05/spineme`; retain the included `LICENSE` in distributions.
