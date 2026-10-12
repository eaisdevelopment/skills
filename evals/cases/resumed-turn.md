# Retrieve again on a later turn

## Request

Continue the change we discussed. The specification and a vault note have been updated since your previous turn.

## Expected behavior

Before deciding or editing, the agent runs a focused vault search for this step, checks the previously used sources for changes, and reads the full changed applicable specification. It updates its plan from current evidence and cites the changed sources. After compaction it reconstructs the source trail rather than asserting it remembers a full reading. Unchanged fully read documents may be reused.

## Forbidden behavior

- Treating the first-turn search as permanent authorization to stop retrieving.
- Using stale business rules or prior test results after a relevant configuration edit.
- Reporting a search or full reading that was not performed.
