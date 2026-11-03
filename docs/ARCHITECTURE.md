# Renzo-Hacker-Lab Architecture (Draft)

## Current shape

The workspace is one Git repository with distinct project areas. Treating a directory as a system boundary does not yet make it an independently versioned or independently runnable repository.

```text
Operator
   |
   v
AgentDash (cockpit prototype)
   |                         \
   v                          v
ClaudeCode / Agent Runtime   InfoEngine
   \                         /
    \                       /
     v                     v
          BIG_ANIMAL
          /         \
         v           v
    Red Team       Blue Team
         \           /
          v         v
              Labs
```

This is a target relationship map, not a verified call graph. Current code demonstrates project files and prototypes; it does not establish that these systems are connected through stable interfaces or that the workflow runs end to end.

## Responsibilities

- **AgentDash:** operator-facing presentation of events and system state.
- **ClaudeCode / Agent Runtime:** agent lifecycle, event coordination, and runtime workflow.
- **InfoEngine:** knowledge, information processing, and interop.
- **BIG_ANIMAL:** simulation and organism state.
- **Red Team:** authorized testing and recon workflows.
- **Blue Team:** defensive detections and analysis.
- **Labs:** isolated training exercises and learning materials.

Keep BIG_ANIMAL and InfoEngine as separate systems. Integrations should be explicit and should not require either project to be merged into the other.

## Integration direction

The first practical integration should be read-only status and event flow into AgentDash. Define and test an adapter contract before wiring project internals together. Prefer versioned JSON messages and explicit local interfaces; do not make a shared database or direct cross-project file imports the default architecture.

No system should trigger scans, mutate another project's state, or take an operational action implicitly through a dashboard integration. Keep execution opt-in, scoped, and visible to the operator.

## Canonical ownership and cleanup

`big_animal/` is the proposed canonical home for BIG_ANIMAL modules. Root-level `agents/`, `engines/`, `events/`, `organism/`, `simulation/`, and `ui/` overlap by filenames but are not all identical copies. See [Duplicate and naming review](./DUPLICATE_REVIEW.md). Do not remove or move modules until imports, tests, and unique functionality have been mapped.

## Milestones

1. Establish verified standalone commands and smoke tests for the existing project areas.
2. Resolve canonical ownership for overlapping modules and add import/regression tests before any retirement.
3. Document a versioned, minimal status/event contract.
4. Connect AgentDash to one read-only producer at a time and test failure behavior.
5. Add further project integrations only when each side remains useful independently.
