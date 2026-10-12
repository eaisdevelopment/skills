# v1.1 Specification

## Acceptance criteria

- **AC-01 — Existing workflow first:** The skill discovers and uses repository instructions and verification commands instead of installing a parallel framework.
- **AC-02 — Evidence-bound claims:** “Done,” “fixed,” “passing,” and equivalent claims require fresh command evidence from after the last relevant edit.
- **AC-03 — Honest uncertainty:** Missing tools, timeouts, skipped required checks, partial runs, and zero collected tests are reported as `BLOCKED` or `NOT VERIFIED`, never as success.
- **AC-04 — Test integrity:** The skill refuses to delete, skip, weaken, or mock away tests merely to obtain green output.
- **AC-05 — Regression proof:** Bug fixes should demonstrate a failing reproduction before the fix and a passing result afterward when feasible.
- **AC-06 — Independent authority:** The implementing agent does not approve its own work or substitute its judgment for required human/CI approval.
- **AC-07 — Proportional process:** Small changes remain small; risky changes receive stronger planning and verification without mandatory lifecycle artifacts.
- **AC-08 — Mandatory knowledge retrieval:** Every development step/turn performs a focused search of available configured vaults first, cites useful notes, records no-matches, and reports unavailable required vaults honestly. Unchanged full readings may be reused after checking for changes.
- **AC-09 — Compact implementation:** The active skill contains no custom Python engine, installer, generated rule ledger, framework adapters, or vendored project scaffold.
- **AC-10 — Behavioral validation:** Tests exercise decisions and outcomes, not merely exact wording or headings.
- **AC-11 — Stack neutrality:** The distributed skill contains no runtime and assumes no programming language, build system, or test runner.
- **AC-12 — Complete business grounding:** Read the full applicable specification and referenced rules before business research, behavior decisions, or test-oracle design. Missing material rules or contradictions block dependent work.
- **AC-13 — Component reuse:** Inspect applicable architecture, implementation, contracts, schemas, infrastructure, and deployment configuration before proposing new components.
- **AC-14 — Configuration use:** Discover `.env` and other configuration sources, selected environment, and required credential availability. Commands can consume values through existing loaders without exposing values to the model or artifacts. Missing/empty credentials block dependent operations; presence alone grants no authority.
- **AC-15 — Research ordering:** Establish local evidence before internet research or code proposals. External primary documentation may resolve gaps or verify changing facts; neither books nor web results invent missing business requirements.
- **AC-16 — Realistic forward tests:** Exercise local component reuse, resumed-turn retrieval, secret-safe configuration, and missing grounding in isolated workspaces. Distinguish observed agent behavior from structural checks and unrun evals.

## Completion evidence

The implementation is acceptable only after structural validation, focused behavior tests, adversarial dogfooding, and an inspection proving retired runtime code is absent from the active skill.

## Local end-user documentation acceptance

For the 2026-10-09 documentation follow-up:

- An authorized reader can install the complete instruction-only skill locally without a legacy installer, overwrite, assumed remote URL, or bundled private corpus.
- Setup/activation conventions cite current primary host documentation; documentation distinguishes copy validation from actual host activation.
- Project knowledge locations, repeated retrieval, full specifications, component reuse, safe configuration use, and missing-input handling are actionable.
- Use cases provide illustrative prompts and observable outcomes, not fabricated test history or business policy.
- Migration explains the framework reset/version collision and preserves user-owned integrations and evidence.
- Local links resolve, public-facing documents do not link to private collections, and verification/limitations and proprietary terms are explicit. No publication occurs until separately authorized.

## Linux/macOS distribution acceptance

- Default to native user-wide installation once per client/computer, not repeated project copies. Windows is out of scope.
- Keep one canonical five-Markdown-file skill. Add only native metadata and a small standard build recipe; no custom installer, runtime, hooks, MCP, or workflow engine.
- Generate a clean allowlisted marketplace bundle under ignored `build/`. Both registration and installation consume that bundle, never the private workspace root.
- Include both host catalogs, native plugin manifests, exact canonical skill bytes, and the unchanged license. Exclude memory, audit, reports, configuration, caches, historical archives, and symlinks.
- Refuse an existing output archive rather than updating it and retaining stale entries. Missing or symlinked required sources fail safely.
- Validate native metadata, inspect actual payload/cache inventories, and verify user-scope discovery in isolated configuration where supported. Distinguish macOS observations from unexecuted Linux and Codex installation checks.
- Provide portable acquisition/install/update guidance without inventing a GitHub URL or publishing. Keep each project's knowledge/configuration separate from the global skill.
