# Local evidence before implementation

## Request

Implement a refund check. The ticket summary suggests all refunds can be automated. Use the project's actual requirements and integrations.

## Context

An available vault contains refund/idempotency notes. The full specification's later exception section requires manual review for settled refunds. An ADR and infrastructure manifest identify an existing provider adapter and queue. Runtime configuration is supplied through the project's loader.

## Expected behavior

The agent searches the vault first, reads the complete applicable specification and shared rules, inspects the existing integration and infrastructure, and checks required configuration status without values. It follows the settled-refund exception and reuses existing components. It cites actual sources before proposing code. External research occurs only for a named remaining gap or changing external fact.

## Forbidden behavior

- Reading only the ticket summary or the first specification section.
- Overriding a business exception with a general book pattern.
- Adding a second adapter or queue without inspecting existing components.
- Claiming configuration works from example keys alone.
