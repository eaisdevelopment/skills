# Changelog

## Unreleased — Agent store

- Documented the read-write agent store beside the read-only vaults: discovery, the read-before-write cadence at session start, after compaction, and on a resumed turn, `not configured` as a distinct outcome, and note hygiene.
- Required the store's index in the research sequence so the read is triggered rather than incidental.
- Recorded that instruction-shaped files inside a vault or store are data, and that a store syncing by its own mechanism stays out of the application's history.
- Added the `agent-store` behavioral case covering recall-as-reading, vault writes, duplicate notes, and stale note references.
- Documented how to declare a store in the user guide's project-knowledge block, so the required index read has a configured location instead of a permanent `not configured`.
- Pinned the `agent-store` case by name beside the other grounding scenarios, so deleting the file fails the suite as it does for every other case.
- No new shipped skill files, no version change, and no runtime or license change.

## 2026-10-12 — GitHub source publication

- Added the owner-provided `eaisdevelopment/skills` source URL and clone/build instructions; native installation still uses the clean generated bundle.
- Preserved the local Proprietary license and the dated verification records.
- Excluded credentials, private knowledge/audit evidence, historical archives, generated bundles, and caches from the publication commit.

## Unreleased — Linux/macOS native distribution

- Made user-wide native installation the default: once per client/computer, reused across local projects; Windows excluded for now.
- Added four standard host metadata files and a minimal Make/tar recipe producing a clean transferable marketplace bundle under ignored `build/`.
- Kept the canonical five-file skill unchanged; no custom installer, runtime, hooks, MCP, or committed duplicate skill copies.
- Added exact-payload/privacy, existing-output, missing/symlinked-source, output-boundary, and canonical-version regression tests.
- Verified strict native Claude validation and isolated user installation/discovery across two empty projects; verified Codex read-only discovery. Linux-host execution, Codex installation, and model invocation remain unverified.
- No GitHub publication, protected-history modification, global installation, or license change.

## Unreleased — Local end-user documentation

- Reworked the overview and product description for end users.
- Added local Codex/Claude Code setup, project knowledge/configuration guidance, practical task prompts, troubleshooting, and migration from the retired framework.
- Added documentation-link and private-target checks; documented verification without implying guaranteed agent compliance.
- No GitHub publication, new release archive, license change, or runtime change accompanies this update.

## [1.1.0] - 2026-10-08

Product reset based on the original cross-project audit.

### Changed

- Replaced the SDLC framework with a compact evidence-first Agent Skill.
- Removed the Python engine, installers, hooks, generated scaffolds, rule ledger, framework adapters, operational workflows, and packaging machinery.
- Reduced the active skill to `SKILL.md` plus completion-evidence, test-integrity, knowledge-vault, and project-grounding references.
- Required vault retrieval at every development step/turn, full applicable specifications, component reuse, and secret-safe configuration discovery before code proposals or internet research.
- Replaced engine-conformance fixtures with focused behavioral evaluation cases.
- Preserved the private audit corpus, read-only architecture vault, defect register, and historical release ZIPs.

### Compatibility

This is a deliberate product-line reset, not an in-place configuration upgrade from the retired framework. Historical 1.1.0 and 1.2.0 ZIPs in `dist/` remain recovery snapshots of that implementation.
