# Project Grounding

Use after vault retrieval at each development step. Establish the business requirements, existing components, and configuration before design, implementation, or external research.

## Business specifications

Locate the project's source of truth through its instructions, specification index, feature documents, contracts, and linked requirements. Read the entire applicable specification and referenced business rules before deriving behavior or acceptance tests. For a large specification, read successive sections through the end; do not substitute search snippets or a summary for full reading. Follow dependencies shared with other features.

Extract the applicable actors, authorization, normal/exception flows, state transitions, monetary units and rounding, limits, timing, concurrency, idempotency, and acceptance scenarios. Distinguish approved requirements from historical drafts and proposed changes.

If sources contradict each other or a material rule is unspecified, cite the conflict and block that decision for clarification. Record proposals as proposals. Never fill missing business rules from a book, search result, or existing bug. For work with no business behavior, read the full applicable task/technical specification and state why business specifications are `N/A`.

## Architecture and infrastructure

Trace the current path from entry point to storage/integrations and its tests. Inspect applicable ADRs, component boundaries, API/event contracts, schemas/migrations, dependency manifests, infrastructure definitions, CI/deployment configuration, and operating conventions. Distinguish deployed, local, proposed, and obsolete components.

Verify whether the required service, queue, database, cache, adapter, configuration key, or testing helper already exists before introducing another. An installed dependency or diagram alone does not prove a running capability. Document evidence for reuse and any proposed new component in the project's existing plan or response.

## Configuration and credentials

Locate the project's actual configuration sources: `.env` and environment variants, examples, schemas, documented variable names, CI/secret-manager references, and its existing loader. Determine the selected target environment and required keys for this task. Recheck availability before each configuration-dependent operation.

- Read loader code and configuration schemas first. Inspect examples through key names and redacted structure, treating even example files as potentially sensitive. Broad source searches must exclude value-bearing configuration/secret files.
- An authorized command may consume needed values from `.env` or inherited environment through the project's loader. Inspect only required key names and `present`, `missing`, or `empty` status through a values-suppressed check. Do not output raw values, connection strings, or authentication-bearing URLs.
- Do not attach/include `.env` in model context, run `cat .env`, dump the environment, enable shell tracing, or source an unfamiliar `.env` as executable shell code. Inspect value-dependent facts inside the command and emit only the needed classification, such as `target=test` or `target=production`.
- Keep values out of code, tests, plans, memory, logs, reports, command text, and internet queries. Use inherited variables, files, or the sanctioned secret manager; suppress/redact subprocess output before it reaches the model if it can expose values.
- A present credential does not establish validity, environment safety, or authorization. Confirm the target before connecting. Use the task's existing authority; credentials do not authorize deployment, money movement, or production writes.
- If a required key is missing, empty, or unusable, report the key name and block only the dependent operation. Never fabricate credentials or substitute a fake integration result. If no runtime/configuration is needed, record `N/A` and the reason.

## Evidence before invention

State the local sources and unresolved question before internet research. Consult primary vendor documentation for missing or current technical facts after local discovery; label stale vault advice accordingly. Distinguish established facts, a design proposal, and unresolved business decisions. Keep the source trail in existing work artifacts rather than creating another workflow system.
