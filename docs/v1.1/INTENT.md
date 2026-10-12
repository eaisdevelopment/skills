# v1.1 Intent

## Problem

The existing project turned a narrow quality skill into a large SDLC framework. It duplicates native agent controls, costs too much to maintain, and still permits false completion and fake-test bypasses.

## Outcome

Deliver a small, portable Agent Skill that helps an agent execute a repository's existing SDLC honestly. It must prevent unsupported completion claims, resist test gaming, preserve independent human approval, and ground every development step/turn in vault research, full applicable specifications, existing components, and configuration evidence.

## Preserve

- The private evidence corpus in `docs/audit/`.
- The read-only knowledge base in `memory/architect-master-vault/`.
- Focused adversarial examples and evaluations that test dishonest or weak behavior.
- Historical release ZIPs as recovery snapshots.

## Out of scope

The skill will not implement repository scaffolding, CI, deployment, release management, metrics, framework adapters, policy databases, artifact state machines, or replacements for native permissions and hooks.
