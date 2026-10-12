# User Guide

Use `ai-native-sdlc` to ground development decisions and require honest verification within an existing project. Start with the [overview](../README.md) and [practical prompts](USE-CASES.md). This guide describes the instruction-only v1.1.0 skill, not the retired framework.

## Requirements

Obtain owner permission under [LICENSE](../LICENSE), the authorized release bundle, and a native Codex or Claude Code client on Linux or macOS. Windows is outside this distribution's scope. The skill has no runtime dependencies, custom installer, provider account, or credentials of its own. Your client and project retain their requirements and access controls.

Install once per client on each computer, at user scope; do not copy the skill into every project. This local installation is not cloud-account synchronization. Each project still supplies its own vault, specifications, configuration, and permissions.

## Obtain and unpack the clean bundle

Get an authorized `ai-native-sdlc-1.1.0.tar.gz` bundle from the owner, or clone the [source repository](https://github.com/eaisdevelopment/skills) into a new directory and build it:

```sh
git clone https://github.com/eaisdevelopment/skills.git sdlc-skills &&
cd sdlc-skills &&
make package
```

If you already have an authorized source checkout, build from its root:

```sh
make package
```

The output is `build/ai-native-sdlc-1.1.0.tar.gz`. The recipe refuses an existing output rather than mixing old and new entries. Transfer this artifact once to each computer; receivers do not need Make or Python. Keep it in a stable user-owned location for native marketplace registration.

Inspect and unpack a trusted bundle in a new location. From the directory containing the received archive:

```sh
tar -tzf ai-native-sdlc-1.1.0.tar.gz
test ! -e ai-native-sdlc-1.1.0 &&
test ! -L ai-native-sdlc-1.1.0 &&
tar -xzf ai-native-sdlc-1.1.0.tar.gz &&
cd ai-native-sdlc-1.1.0
```

The extracted directory is a clean marketplace. Its plugin lives under `plugins/ai-native-sdlc/` and contains native metadata, the license, and the complete five-file skill under `skills/ai-native-sdlc/`. It excludes private memory, audit evidence, reports, configuration, caches, and historical archives.

Never register or install from the source checkout's root: host managers may copy/cache marketplace sources. Use only the extracted allowlisted bundle. Keep that directory available; moving it can break future local refreshes.

## Install with the native host manager

Run the selected client's commands from the extracted `ai-native-sdlc-1.1.0/` directory, not from your target project. Both clients use the marketplace name `sdlc-local` and plugin name `ai-native-sdlc`. Stop on any error; inspect an existing registration instead of silently replacing it or continuing against an old source.

### Codex

```sh
codex plugin marketplace add . &&
codex plugin add ai-native-sdlc@sdlc-local &&
codex plugin marketplace list &&
codex plugin list
```

These command forms were checked against Codex CLI 0.162.1 help. [OpenAI's plugin guide](https://developers.openai.com/plugins/build/plugins) documents local marketplace registration and host-managed configuration. See the [distribution verification report](v1.1/DISTRIBUTION-VERIFICATION.md) for actual discovery/install evidence; command availability alone does not prove installation.

Start Codex in a target project. Use `/skills` or `$` to select the installed `ai-native-sdlc` skill, as described in [OpenAI's skill guide](https://learn.chatgpt.com/docs/build-skills). Check the displayed source to avoid selecting an old project copy.

### Claude Code

```sh
claude plugin marketplace add . --scope user &&
claude plugin install ai-native-sdlc@sdlc-local --scope user &&
claude plugin list
```

These command forms were checked against Claude Code 2.1.296 help. User scope enables the plugin across local projects on that machine; plugin skills are namespaced. See [Anthropic's installation guide](https://code.claude.com/docs/en/discover-plugins).

Start a new Claude Code session in a target project and invoke `/ai-native-sdlc:ai-native-sdlc`. If an existing session needs refreshing, use the native `/reload-plugins` command. Confirm the listed plugin's version, user scope, and enabled status.

### Confirm activation

Selecting a plugin does not establish correct agent behavior. After invoking the installed skill, run this read-only smoke task:

```text
Locate our configured vault, full applicable specification, existing components,
configuration loader, and real verification commands. Cite sources and report
missing inputs. Do not edit files, reveal secrets, or contact external services.
```

Inspect the source trail and missing-input report. If the skill is absent or disabled, resolve discovery first; do not claim activation from unpacking files alone. Check the [distribution verification report](v1.1/DISTRIBUTION-VERIFICATION.md) for current limits, including Linux-host execution and Codex installation. Project or managed policy can restrict a user-level plugin.

## Connect project knowledge

There is no skill-specific configuration file, memory server, or ingestion pipeline. Add the source locations to the project's existing agent instructions, or provide them in the task. Merge into existing `AGENTS.md`/`CLAUDE.md`; do not replace local policy. Example paths below are illustrative and must be replaced with your real sources:

```text
Use ai-native-sdlc for development and review tasks.
Knowledge vault: memory/team-vault/ (read-only).
Vault navigation: memory/team-vault/indexes/Agent_Coding_Guide.md.
Approved specifications: specification/index.md and its linked documents.
Architecture and infrastructure: docs/architecture/, infra/, and existing ADRs.
Configuration: our existing loader, .env variants, and configuration schema.
Verification: the commands recorded in this project's README and CI.
Search the vault at each development step/turn. Keep secret values out of context.
```

The skill does not include this repository's private architecture vault or automatically populate your memory. Grant only the needed read access to your own local or already-configured remote knowledge source. Explicitly search named/linked vault paths; ignored files and symlinks may be omitted by a general repository search. Preserve vault provenance and licenses; do not modify generated knowledge as part of a coding change.

At each step, search relevant terms, read useful notes, then read the full applicable approved specification and its dependencies. Inspect existing components and infrastructure before proposing additions. Check previously read sources for changes on later turns; reuse unchanged full readings with citations. Rebuild the source trail after compaction, rereading anything that cannot be substantiated.

Books and patterns do not override approved business rules. Report an available-vault no-match with its query. Distinguish `not configured` from a required but inaccessible vault; ask for the required location/access and block dependent work. Missing or contradictory business policy requires a decision, not a guessed percentage or web substitute. Continue independent work where possible.

## Configuration and credentials

The agent should inspect loader code and configuration schemas before any value-bearing file. Even example files may contain secrets: inspect key names/redacted structure only. Use the project's existing loader to consume `.env`, inherited variables, or its sanctioned secret manager, with output suppressed/redacted before reaching model context.

Report only required-key availability (`present`, `missing`, `empty`) and a safe target classification. Never attach `.env`, print its values, dump the environment, source unfamiliar configuration as shell code, or paste credentials into prompts, reports, code, or web searches. Ensure ignore rules protect private configuration; ignoring a file does not remove an already tracked or leaked secret.

An available key proves neither validity nor authorization. Missing/empty keys block the dependent check; presence grants no permission for production writes, deployment, or money movement. Record `N/A` with a reason if this task has no runtime/configuration dependency. The skill provides no universal credential-checker command: use your actual project tooling.

## Request and inspect evidence

Specify the outcome, applicable specification, risks, acceptance criteria, and permitted actions. Use the existing project's build/test/lint commands, not this skill repository's maintainer checks. Verify after the last relevant edit; inspect test collection, failures, and skips. A mocked test is not proof of a working external integration.

Ask for sources consulted, changes made, sanitized command invocations, exit codes, meaningful test counts, and omitted checks. Each status has a named scope:

- `PASS`: required checks ran successfully and match the acceptance criteria.
- `FAIL`: a required check failed or behavior contradicts the criteria.
- `BLOCKED`: a required decision, dependency, credential, tool, or authority is missing.
- `NOT VERIFIED`: a check was not run or evidence is only partial.

For example, “unit checks PASS; required provider verification BLOCKED by an empty key; deployment NOT VERIFIED” is not an overall completion claim. Zero expected tests, stale output, a partial suite, or skipped required checks cannot justify success. CI and required human review remain independent; this instruction set cannot enforce compliance by itself.

## Troubleshooting and migration

- **Skill not found:** inspect native marketplace/plugin listings, registered source path, enabled state, and permissions; check duplicate old copies and refresh/start a new session.
- **No vault or missing specification:** supply the actual required source, not fabricated knowledge. Keep dependent behavior blocked until resolved.
- **Checks unavailable:** report the missing tool/environment and affected checks. Do not replace real integration evidence with mocks or no-op commands.
- **Migrating from the framework:** treat v1.1.0 as a product reset. Historical `dist/` archives labeled 1.1.0/1.2.0 contain the retired framework, not this clean marketplace bundle. Retain recovery material privately.
- **Old hooks/scaffolds/state:** inventory them in the target project and review ownership before changing anything. Installing this skill neither removes old integrations nor migrates their state. Keep legitimate project-native gates; do not delete user data or install a second orchestration system.

## Update safely

Review the [changelog](../CHANGELOG.md), the complete skill, and native metadata before installing a new authorized bundle. Unpack the new release into a separate directory; do not modify host caches or overwrite the old source blindly. Record existing source paths and settings first, including any old project-scoped copies.

Use native managers, not a bare-skill installer, for plugin updates. Codex's `plugin marketplace upgrade` refreshes Git snapshots; it is not an updater for this local archive. For a changed local bundle, remove only this plugin/marketplace through the selected manager, then repeat registration/installation from the new extracted directory:

```sh
codex plugin remove ai-native-sdlc@sdlc-local
codex plugin marketplace remove sdlc-local
```

Or, for Claude Code:

```sh
claude plugin uninstall ai-native-sdlc@sdlc-local --scope user --keep-data
claude plugin marketplace remove sdlc-local --scope user
```

These removal commands are update instructions, not actions performed by this guide. Confirm `sdlc-local` contains only this distribution before removing it; preserve user customizations and unrelated plugins. Do not run blind filesystem deletes. After reinstalling, confirm the new version and repeat the smoke task and representative project checks. Native policy, caches, and running sessions must be checked rather than assuming edited files became active.
