# ai-native-sdlc — Memory-first SDLC integrity

A compact, language-neutral skill for coding agents: retrieve project knowledge first, follow approved requirements, reuse existing components, and report real verification evidence.

Version **1.1.0** is an instruction-only product reset, not an SDLC framework. A thin native plugin wrapper distributes the same five Markdown files on Linux/macOS; Windows is out of scope. It adds no engine, custom installer, scaffold, or deployment system. Permissions, hooks, CI, ownership, and human approval remain independent controls. Instructions can improve discipline; they cannot guarantee an agent will obey or make false claims impossible.

## Start here

1. Obtain the authorized clean bundle and install once per client/computer at user scope using the [user guide](docs/USER-GUIDE.md). All local projects reuse that installation.
2. Tell the agent where your vaults, approved specifications, architecture/infrastructure, configuration loader, and verification commands live. The private vault here is **not bundled** with the skill.
3. Explicitly invoke the skill for a task; review its source trail, changes, actual test results, and remaining gaps.

Example task prompt, after installation:

```text
Use ai-native-sdlc to fix this defect. Search our configured vault first,
read the full applicable specification, inspect existing components and
configuration safely, reproduce the failure, and run our real checks.
Report commands, exit codes, test counts, and any unverified work.
```

See [practical use cases](docs/USE-CASES.md) for feature work, defects, suspicious tests, changed requirements, missing policy, credentials, and reviews.

## Portable Linux/macOS installation

Maintainers run `make package` to generate `build/ai-native-sdlc-1.1.0.tar.gz`. Transfer only that artifact to another computer and unpack it in a stable user-owned location. Receivers need neither Python nor Make. Register the extracted clean marketplace with the native client; do not register this private workspace root.

From the extracted `ai-native-sdlc-1.1.0/` directory, choose a client:

```sh
codex plugin marketplace add . &&
codex plugin add ai-native-sdlc@sdlc-local
```

```sh
claude plugin marketplace add . --scope user &&
claude plugin install ai-native-sdlc@sdlc-local --scope user
```

Stop on errors and inspect existing registrations first. Keep the extracted source available: local plugin loading/refreshes may use it directly. See the [guide](docs/USER-GUIDE.md) for activation, updates, supported CLI observations, and project knowledge setup.

## How it works

Each development step/turn starts with focused vault retrieval, full applicable specifications, existing architecture/infrastructure, and secret-safe configuration discovery. Unchanged full readings may be reused after checking for changes. External research follows local discovery for named gaps or changing facts.

The agent should reproduce defects before fixing them when feasible, resist test weakening, verify after the final relevant edit, and distinguish `PASS`, `FAIL`, `BLOCKED`, and `NOT VERIFIED`. A required missing rule, vault, credential, or authority blocks dependent work; it is not permission to invent a result.

Use it with your project's own language and tools. Python and `uv` below are maintainer checks for this repository, **not requirements for using the skill**.

## Contents

- [skills/ai-native-sdlc/](skills/ai-native-sdlc/SKILL.md) — the installable entry point and four focused references.
- `packaging/` and `Makefile` — native catalogs/manifests and a small allowlisted archive build; no installer/runtime.
- [User guide](docs/USER-GUIDE.md) — local setup, activation, memory/configuration, troubleshooting, and migration.
- [Use cases](docs/USE-CASES.md) — illustrative prompts and expected outcomes, not claimed test runs.
- `evals/cases/` — behavioral scenarios for forward-testing the skill with an agent model.
- `tests/` — fast structural and contract checks.
- `docs/v1.1/` — intent, acceptance criteria, plan, and local verification evidence.

Private audit evidence and the read-only knowledge vault stay local. Historical archives are recovery material for the retired framework, not installation packages for this skill. Do not copy the entire workspace into another project or publish those collections.

## Verify as a maintainer

From this repository's root (maintainer checks require Python, Make, and tar):

```sh
python3 -m unittest discover -s tests -t .
uv run --with pyyaml python "${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-creator/scripts/quick_validate.py" skills/ai-native-sdlc
```

The first command checks package boundaries, evaluation-case structure, user-documentation links, and real archive builds including negative cases. GitLab CI uses this command. The second is a local skill-format check requiring `uv` and an installed Codex skill-creator validator; it is not a target-project test runner.

Structural checks do not establish model compliance. See [v1.1 verification](docs/v1.1/VERIFICATION.md) for the four isolated memory-integration trials and their limitations, and [documentation verification](docs/v1.1/DOCUMENTATION-VERIFICATION.md) for this documentation update. Cross-model reliability, compaction recovery, live-provider behavior, and hosted CI remain unverified.

[Distribution verification](docs/v1.1/DISTRIBUTION-VERIFICATION.md) records native validation, isolated Claude user installation across two projects, Codex discovery, payload/privacy checks, and explicit Linux/Codex-install/model-invocation limits.

## Availability and license

Source repository: [eaisdevelopment/skills](https://github.com/eaisdevelopment/skills). Clone the source and build the clean marketplace bundle as described in the [user guide](docs/USER-GUIDE.md). A source checkout is not itself a native marketplace; no downloadable GitHub release is implied.

The package is proprietary. Owner permission is required for use in approved projects and for copying or distribution; see [LICENSE](LICENSE). Preparing public-facing documentation does not change these terms. Release changes are recorded in [CHANGELOG](CHANGELOG.md).
